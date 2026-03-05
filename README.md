Multi-Tenant SaaS Authentication API

Backend authentication system implementing JWT authentication with tenant isolation using FastAPI.

This project demonstrates how a backend service can support multiple tenants (organizations) where each tenant's users and data are logically separated while using a single backend service.

The system includes:

User registration

Login with JWT

Protected routes

Tenant-aware authentication

Tech Stack

Python

FastAPI

Poetry (dependency management)

JWT Authentication

OAuth2 Password Flow

Pydantic

Uvicorn

Key Backend Concepts Implemented

This project focuses on backend architecture patterns, including:

Multi-Tenant Architecture

Each user belongs to a tenant (tenant_id).
JWT tokens include the tenant identifier to enforce tenant-level access control.

JWT Authentication

Secure authentication using signed tokens.

Token payload contains:

{
  "sub": "user_email",
  "tenant_id": 2,
  "exp": timestamp
}
OAuth2 Password Flow

Authentication follows the OAuth2 password flow implemented through FastAPI's security utilities.

Protected Routes

Endpoints require a valid JWT token.

Example protected endpoint:

GET /users/me

Returns the authenticated user based on the JWT.

Project Structure
app/
 ├── main.py
 ├── auth.py
 ├── models.py
 ├── schemas.py
 ├── database.py
 └── dependencies.py

main.py → FastAPI application entrypoint

auth.py → authentication and token logic

models.py → database models

schemas.py → request/response validation

database.py → database connection

dependencies.py → authentication dependencies

Installation

Clone the repository

git clone https://github.com/yourusername/project-name.git
cd project-name

Install dependencies using Poetry

poetry install

Activate the environment

poetry shell
Environment Variables

Create a .env file based on .env.example.

Example:

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./app.db
Run the Application

Start the server:

uvicorn app.main:app --reload

Server will run at:

http://127.0.0.1:8000
API Documentation

Interactive API docs are available at:

http://127.0.0.1:8000/docs

Swagger UI allows testing:

/login

/users/me

Example Authentication Flow
Login
POST /login

Request body:

username: main@gmail.com
password: 123456

Response:

{
  "access_token": "...",
  "token_type": "bearer"
}
Access Protected Route
GET /users/me
Authorization: Bearer <token>
Purpose of the Project

This project was built to demonstrate understanding of:

Backend authentication architecture

Multi-tenant system design

JWT based security

API design using FastAPI

Possible Future Improvements

Role Based Access Control (RBAC)

Tenant specific databases

Refresh tokens

Production ready configuration

Docker deployment

Author

Mahadi