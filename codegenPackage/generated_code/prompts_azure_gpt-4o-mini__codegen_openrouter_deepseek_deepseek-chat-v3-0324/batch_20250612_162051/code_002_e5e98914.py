"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Create a REST API for managing Agile courses that includes endpoints for user enrollment and course completion tracking, similar to the services provided by CrestAgile.
Generated: DETERMINISTIC_e5e9891436a89b6d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Annotated

# Initialize FastAPI app
app = FastAPI(
    title="Agile Course Management API",
    description="A REST API for managing Agile courses, user enrollment, and course completion tracking.",
    version="1.0.0",
)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # In production, use a proper secret key and keep it secure
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in-memory for this example)
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False
    hashed_password: str

class UserInDB(User):
    pass

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Course(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    duration_hours: int
    price: float
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

class Enrollment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    course_id: UUID
    enrollment_date: datetime = Field(default_factory=datetime.now)
    completion_status: str = "enrolled"  # enrolled, in_progress, completed
    completion_date: Optional[datetime] = None

# In-memory databases
db_users = {}
db_courses = {}
db_enrollments = {}

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    for user_id, user in db.items():
        if user.username == username:
            return user
    return None

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(db_users, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(db_users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    if get_user(db_users, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    db_users[str(db_user.id)] = db_user
    return db_user

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

# Course endpoints
@app.post("/courses/", response_model=Course)
async def create_course(course: Course, current_user: Annotated[User, Depends(get_current_active_user)]):
    course_id = str(course.id)
    db_courses[course_id] = course
    return course

@app.get("/courses/", response_model=List[Course])
async def read_courses(skip: int = 0, limit: int = 10):
    return list(db_courses.values())[skip : skip + limit]

@app.get("/courses/{course_id}", response_model=Course)
async def read_course(course_id: str):
    if course_id not in db_courses:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_courses[course_id]

@app.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: str, course: Course, current_user: Annotated[User, Depends(get_current_active_user)]):
    if course_id not in db_courses:
        raise HTTPException(status_code=404, detail="Course not found")
    db_courses[course_id] = course
    return course

@app.delete("/courses/{course_id}")
async def delete_course(course_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    if course_id not in db_courses:
        raise HTTPException(status_code=404, detail="Course not found")
    del db_courses[course_id]
    return {"message": "Course deleted successfully"}

# Enrollment endpoints
@app.post("/enrollments/", response_model=Enrollment)
async def create_enrollment(enrollment: Enrollment, current_user: Annotated[User, Depends(get_current_active_user)]):
    # Check if user exists
    if str(enrollment.user_id) not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if course exists
    if str(enrollment.course_id) not in db_courses:
        raise HTTPException(status_code=404, detail="Course not found")
    
    enrollment_id = str(enrollment.id)
    db_enrollments[enrollment_id] = enrollment
    return enrollment

@app.get("/enrollments/", response_model=List[Enrollment])
async def read_enrollments(skip: int = 0, limit: int = 10):
    return list(db_enrollments.values())[skip : skip + limit]

@app.get("/enrollments/{enrollment_id}", response_model=Enrollment)
async def read_enrollment(enrollment_id: str):
    if enrollment_id not in db_enrollments:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return db_enrollments[enrollment_id]

@app.put("/enrollments/{enrollment_id}", response_model=Enrollment)
async def update_enrollment(enrollment_id: str, enrollment: Enrollment, current_user: Annotated[User, Depends(get_current_active_user)]):
    if enrollment_id not in db_enrollments:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    db_enrollments[enrollment_id] = enrollment
    return enrollment

@app.patch("/enrollments/{enrollment_id}/complete")
async def mark_enrollment_complete(enrollment_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    if enrollment_id not in db_enrollments:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    enrollment = db_enrollments[enrollment_id]
    enrollment.completion_status = "completed"
    enrollment.completion_date = datetime.now()
