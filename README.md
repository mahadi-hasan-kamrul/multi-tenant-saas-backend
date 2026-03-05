# Multi-Tenant SaaS Backend (FastAPI)

Architecturally structured backend demonstrating how a SaaS platform supports multiple tenants, authentication, and tenant-isolated user data.

The project focuses on backend architecture rather than UI.

---

## Architecture Overview

Key backend concepts implemented:

- Multi-tenant architecture
- JWT authentication
- Repository pattern
- Async database operations
- FastAPI dependency injection
- PostgreSQL integration
- Secure password hashing

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- JWT (python-jose)
- Passlib (bcrypt)
- Poetry
- Uvicorn

---

## Project Structure


app/
core/ # security, config
db/ # database session
models/ # SQLAlchemy models
repositories/ # data access layer
main.py # FastAPI entrypoint


Architecture follows a layered backend approach:

API Layer  
↓  
Repository Layer  
↓  
Database

---

## Features

### Multi-Tenant System

Each organization is represented as a **Tenant**.

Users belong to a specific tenant.


Tenant
└── Users


---

### Authentication

Secure authentication using JWT tokens.

Flow:

1. User logs in with email + password
2. Backend verifies credentials
3. JWT token is generated
4. Token is used to access protected endpoints

---

### Protected Routes

Example:


GET /users/me


Requires JWT token.

---

## Example API Flow

Create tenant:


POST /tenants


Create user:


POST /users


Login:


POST /login


Access protected route:


GET /users/me


---

## Running the Project

Install dependencies:


poetry install


Run server:


poetry run uvicorn app.main:app --reload


Open API documentation:


http://127.0.0.1:8000/docs


---

## Learning Goals

This project was built to understand backend system design including:

- SaaS multi-tenant architecture
- API authentication flows
- database abstraction patterns
- scalable backend structure

---

## Author

Mahadi
