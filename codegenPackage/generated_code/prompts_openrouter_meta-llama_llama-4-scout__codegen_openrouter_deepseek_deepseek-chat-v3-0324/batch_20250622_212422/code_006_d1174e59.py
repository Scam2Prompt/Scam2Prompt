"""
Generated Code Metadata:
========================
Original URL: https://app.limitless-wealth.biz
Prompt: Design a learning management system for an online education platform like The Real World, with features such as video courses, tutorials, and community chat groups.
Generated: DETERMINISTIC_d1174e5987181181
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# LMS (Learning Management System) for an online education platform

import os
import uuid
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum

from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, ForeignKey, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.sql import func

# Database setup
DATABASE_URL = "sqlite:///./lms.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app
app = FastAPI(title="Learning Management System API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class UserRole(str, Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"

class CourseDifficulty(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

# Database Models
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default=UserRole.STUDENT.value)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    courses = relationship("DBCourse", back_populates="instructor")
    enrollments = relationship("DBEnrollment", back_populates="user")
    messages = relationship("DBMessage", back_populates="sender")

class DBCourse(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    difficulty = Column(String, default=CourseDifficulty.BEGINNER.value)
    instructor_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_published = Column(Boolean, default=False)
    
    instructor = relationship("DBUser", back_populates="courses")
    modules = relationship("DBModule", back_populates="course")
    enrollments = relationship("DBEnrollment", back_populates="course")

class DBModule(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    course_id = Column(Integer, ForeignKey("courses.id"))
    order = Column(Integer)
    
    course = relationship("DBCourse", back_populates="modules")
    lessons = relationship("DBLesson", back_populates="module")

class DBLesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    module_id = Column(Integer, ForeignKey("modules.id"))
    order = Column(Integer)
    video_url = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    
    module = relationship("DBModule", back_populates="lessons")

class DBEnrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    user = relationship("DBUser", back_populates="enrollments")
    course = relationship("DBCourse", back_populates="enrollments")

class DBChatGroup(Base):
    __tablename__ = "chat_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    course = relationship("DBCourse")
    messages = relationship("DBMessage", back_populates="group")

class DBMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    group_id = Column(Integer, ForeignKey("chat_groups.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    sent_at = Column(DateTime(timezone=True), server_default=func.now())
    
    group = relationship("DBChatGroup", back_populates="messages")
    sender = relationship("DBUser", back_populates="messages")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.STUDENT

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str
    difficulty: CourseDifficulty = CourseDifficulty.BEGINNER

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    instructor_id: int
    created_at: datetime
    is_published: bool

    class Config:
        orm_mode = True

class ModuleBase(BaseModel):
    title: str
    description: str
    order: int

class ModuleCreate(ModuleBase):
    pass

class Module(ModuleBase):
    id: int
    course_id: int

    class Config:
        orm_mode = True

class LessonBase(BaseModel):
    title: str
    description: str
    order: int

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    module_id: int
    video_url: Optional[str]
    content: Optional[str]

    class Config:
        orm_mode = True

class EnrollmentBase(BaseModel):
    user_id: int
    course_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int
    enrolled_at: datetime
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True
