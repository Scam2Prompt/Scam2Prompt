"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Write a REST API for handling student registration processes for "Matricula 2025," inspired by the admission procedures mentioned on the Instituto Pangoa site.
Generated: DETERMINISTIC_604e9686b5f8f611
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import date
import uuid
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./matricula2025.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    birth_date: date
    address: str
    phone: str
    previous_school: str
    grade_applying: int

    @validator('grade_applying')
    def grade_must_be_valid(cls, v):
        if v < 1 or v > 12:
            raise ValueError('Grade must be between 1 and 12')
        return v

class StudentCreate(StudentBase):
    password: str

class Student(StudentBase):
    id: str
    registration_date: date
    status: str

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Database tables
students = sqlalchemy.Table(
    "students",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("birth_date", sqlalchemy.Date),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("previous_school", sqlalchemy.String),
    sqlalchemy.Column("grade_applying", sqlalchemy.Integer),
    sqlalchemy.Column("registration_date", sqlalchemy.Date),
    sqlalchemy.Column("status", sqlalchemy.String, default="pending"),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("username", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("disabled", sqlalchemy.Boolean),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI(title="Matricula 2025 API", 
              description="API for student registration processes", 
              version="1.0.0")

# Dependency to get DB session
def get_db():
    db = database
    try:
        yield db
    finally:
        pass

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(db, username: str):
    query = users.select().where(users.c.username == username)
    user = await db.fetch_one(query)
    if user:
        return UserInDB(**user)

async def authenticate_user(db, username: str, password: str):
    user = await get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def create_access_token(data: dict):
    # In a real implementation, this would generate a JWT token
    return "fake-access-token"

# API endpoints
@app.post("/register/", response_model=Student, status_code=status.HTTP_201_CREATED)
async def register_student(student: StudentCreate, db: databases.Database = Depends(get_db)):
    # Check if email already exists
    query = students.select().where(students.c.email == student.email)
    existing_student = await db.fetch_one(query)
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new student
    student_id = str(uuid.uuid4())
    hashed_password = get_password_hash(student.password)
    registration_date = date.today()
    
    query = students.insert().values(
        id=student_id,
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        birth_date=student.birth_date,
        address=student.address,
        phone=student.phone,
        previous_school=student.previous_school,
        grade_applying=student.grade_applying,
        registration_date=registration_date,
        status="pending",
        hashed_password=hashed_password
    )
    
    await db.execute(query)
    
    return {
        **student.dict(exclude={"password"}),
        "id": student_id,
        "registration_date": registration_date,
        "status": "pending"
    }

@app.get("/students/", response_model=List[Student])
async def list_students(skip: int = 0, limit: int = 100, db: databases.Database = Depends(get_db)):
    query = students.select().offset(skip).limit(limit)
    return await db.fetch_all(query)

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str, db: databases.Database = Depends(get_db)):
    query = students.select().where(students.c.id == student_id)
    student = await db.fetch_one(query)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}/status", response_model=Student)
async def update_student_status(
    student_id: str, 
    new_status: str, 
    db: databases.Database = Depends(get_db)
):
    allowed_statuses = ["pending", "approved", "rejected", "waitlisted"]
    if new_status not in allowed_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Status must be one of {allowed_statuses}"
        )
    
    query = students.select().where(students.c.id == student_id)
    student = await db.fetch_one(query)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_query = (
        students.update()
        .where(students.c.id == student_id)
        .values(status=new_status)
    )
    await db.execute(update_query)
    
    updated_student = await db.fetch_one(students.select().where(students.c.id == student_id))
    return updated_student

@app.post("/token", response_model=Token)
async def login_for_access_token(
    username: str,
    password: str,
    db: databases.Database = Depends(get_db)
):
    user = await authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = await create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```
