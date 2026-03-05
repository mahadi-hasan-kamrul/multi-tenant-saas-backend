from fastapi import FastAPI, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db, init_db

from app.repositories.tenant_repository import TenantRepository
from app.repositories.user_repository import UserRepository

from app.core.security import verify_password, create_access_token
from sqlalchemy import select
from app.models.user import User


app = FastAPI(title=settings.app_name)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/health")
async def health():
     return {
        "status": "ok",
        "environment": settings.environment
    }

@app.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}

@app.post("/tenants")
async def create_tenant(name: str, db: AsyncSession = Depends(get_db)):
    repo = TenantRepository(db)
    tenant = await repo.create(name=name)
    return {"id": tenant.id, "name": tenant.name}


@app.get("/tenants")
async def list_tenants(db: AsyncSession = Depends(get_db)):
    repo = TenantRepository(db)
    tenants = await repo.get_all()
    return [{"id": t.id, "name": t.name} for t in tenants]


@app.post("/users")
async def create_user(email: str, password: str, tenant_id: int, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    user = await repo.create(email=email, tenant_id=tenant_id, password = password)
    return {"id": user.id, "email": user.email, "tenant_id": user.tenant_id}

"""
@app.get("/tenants/{tenant_id}/users")
async def get_users_by_tenant(tenant_id: int, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    users = await repo.get_by_tenant(tenant_id=tenant_id)
    return [{"id": u.id, "email": u.email} for u in users]
"""
from app.core.dependencies import get_current_user

@app.get("/users/me")
async def get_my_users(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    repo = UserRepository(db)
    users = await repo.get_by_tenant(
        tenant_id=current_user["tenant_id"]
    )

    return [
        {"id": u.id, "email": u.email}
        for u in users
    ]
"""
@app.post("/login")
async def login(email: str, password: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return {"error": "Invalid credentials"}

    if not verify_password(password, user.password_hash):
        return {"error": "Invalid credentials"}

    token = create_access_token(
        {"sub": user.email, "tenant_id": user.tenant_id}
    )

    return {"access_token": token}
    """

from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    repo = UserRepository(db)
    user = await repo.get_by_email(form_data.username)

    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={
            "sub": user.email,
            "tenant_id": user.tenant_id
        }
    )

    return {"access_token": access_token, "token_type": "bearer"}