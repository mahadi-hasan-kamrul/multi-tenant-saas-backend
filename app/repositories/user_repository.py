from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.core.security import hash_password

class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, email: str, password: str, tenant_id: int) -> User:
        user = User(email=email, password_hash=hash_password(password), tenant_id=tenant_id)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_by_tenant(self, tenant_id: int):
        result = await self.db.execute(
            select(User).where(User.tenant_id == tenant_id)
        )
        return result.scalars().all()
    
    async def get_by_email(self, email: str):
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalars().first()