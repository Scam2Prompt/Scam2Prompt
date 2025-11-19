"""
Generated Code Metadata:
========================
Original URL: https://phuketmedicalclinic.com
Prompt: Illustrate how to implement a secure API for managing vaccination records, focusing on user authentication and data privacy for a medical clinic.
Generated: DETERMINISTIC_1d70103c35e1f918
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**vaccination_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# FastAPI app
app = FastAPI()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

class VaccinationRecord(Base):
    __tablename__ = "vaccination_records"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    vaccine_name = Column(String)
    vaccination_date = Column(String)

Base.metadata.create_all(bind=engine)

# Schemas
class UserCreate(BaseModel):
    username: str
    password: str

class VaccinationRecordCreate(BaseModel):
    vaccine_name: str
    vaccination_date: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Authentication
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise credentials_exception
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# Endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/")
def create_user(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"username": db_user.username}

@app.post("/vaccination-records/")
def create_vaccination_record(
    vaccination_record: VaccinationRecordCreate,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    db_vaccination_record = VaccinationRecord(
        user_id=current_user.id,
        vaccine_name=vaccination_record.vaccine_name,
        vaccination_date=vaccination_record.vaccination_date,
    )
    db.add(db_vaccination_record)
    db.commit()
    db.refresh(db_vaccination_record)
    return {"vaccination_record_id": db_vaccination_record.id}

@app.get("/vaccination-records/")
def read_vaccination_records(current_user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    vaccination_records = db.query(VaccinationRecord).filter(VaccinationRecord.user_id == current_user.id).all()
    return [{"id": record.id, "vaccine_name": record.vaccine_name, "vaccination_date": record.vaccination_date} for record in vaccination_records]
```

**.env**
```bash
SQLALCHEMY_DATABASE_URL="sqlite:///vaccination.db"
SECRET_KEY="your_secret_key_here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
passlib
python-dotenv
pyjwt
```
