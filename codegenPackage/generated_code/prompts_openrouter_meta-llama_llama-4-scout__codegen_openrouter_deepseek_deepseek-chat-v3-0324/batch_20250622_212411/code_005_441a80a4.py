"""
Generated Code Metadata:
========================
Original URL: https://phanytom.com
Prompt: "Create a custom software solution for a financial institution to manage user access to sensitive data and applications in a cloud environment."
Generated: DETERMINISTIC_441a80a45adb700e
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import jwt
from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from pydantic import BaseModel, ValidationError
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from starlette.middleware.cors import CORSMiddleware

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./financial_access.db")

# Database setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True)
    roles = relationship("UserRole", back_populates="user")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    permissions = relationship("Permission", back_populates="role")

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))
    user = relationship("User", back_populates="roles")
    role = relationship("Role")

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="permissions")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    sensitive = Column(Boolean, default=False)

class DataAccess(Base):
    __tablename__ = "data_access"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    application_id = Column(Integer, ForeignKey("applications.id"))
    granted_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    disabled: bool
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleInDB(RoleBase):
    id: int

    class Config:
        orm_mode = True

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    role_id: int

class PermissionInDB(PermissionBase):
    id: int

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    name: str
    description: Optional[str] = None
    sensitive: bool = False

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationInDB(ApplicationBase):
    id: int

    class Config:
        orm_mode = True

class DataAccessBase(BaseModel):
    user_id: int
    application_id: int
    expires_at: Optional[datetime] = None

class DataAccessCreate(DataAccessBase):
    pass

class DataAccessInDB(DataAccessBase):
    id: int
    granted_at: datetime

    class Config:
        orm_mode = True

# Utils
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")),
    db: Session = Depends(get_db)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (jwt.PyJWTError, ValidationError):
        raise credentials_exception
    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user

async def get_current_active_user(
    current_user: UserInDB = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def check_permission(db: Session, user: User, permission_name: str):
    for user_role in user.roles:
        for permission in user_role.role.permissions:
            if permission.name == permission_name:
                return True
    return False

# Initialize database
def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Create admin role if not exists
        admin_role = db.query(Role).filter(Role.name == "admin").first()
        if not admin_role:
            admin_role = Role(name="admin", description="Administrator with full access")
            db.add(admin_role)
            db.commit()
            db.refresh(admin_role)
            
            # Add admin permissions
            permissions = [
                Permission(name="users:read", description="Read users", role_id=admin_role.id),
                Permission(name="users:write", description="Create/update users", role_id=admin_role.id),
                Permission(name="roles:read", description="Read roles", role_id=admin_role.id),
                Permission(name="roles:write", description="Create/update roles", role_id=admin_role.id),
                Permission(name="data:access", description="Access sensitive data", role_id=admin_role.id),
                Permission(name="applications:manage", description="Manage applications", role_id=admin_role.id),
            ]
            db.bulk_save_objects(permissions)
            db.commit()
