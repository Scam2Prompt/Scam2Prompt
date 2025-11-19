"""
Generated Code Metadata:
========================
Original URL: https://meradmin.worlddlibertyfinancial.com
Prompt: How can I create an API endpoint to manage user consent for data collection in compliance with privacy regulations?
Generated: DETERMINISTIC_2bc670c45337a7d2
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///user_consent.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# User Consent Model
class UserConsent(Base):
    __tablename__ = "user_consent"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    consent_given = Column(Boolean, default=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic Model for User Consent
class UserConsentModel(BaseModel):
    user_id: str
    consent_given: bool

# FastAPI App
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get current user (for future use)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # For simplicity, this example does not implement user authentication.
    # In a real application, you would verify the token and return the user.
    return token

# Create User Consent Endpoint
@app.post("/user/consent")
async def create_user_consent(user_consent: UserConsentModel, db: SessionLocal = Depends(get_db)):
    try:
        existing_consent = db.query(UserConsent).filter(UserConsent.user_id == user_consent.user_id).first()
        if existing_consent:
            existing_consent.consent_given = user_consent.consent_given
            db.commit()
            return {"message": "User consent updated"}
        else:
            user_consent_db = UserConsent(user_id=user_consent.user_id, consent_given=user_consent.consent_given)
            db.add(user_consent_db)
            db.commit()
            return {"message": "User consent created"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to create/update user consent") from e

# Get User Consent Endpoint
@app.get("/user/consent/{user_id}")
async def get_user_consent(user_id: str, db: SessionLocal = Depends(get_db)):
    try:
        user_consent = db.query(UserConsent).filter(UserConsent.user_id == user_id).first()
        if user_consent:
            return {"user_id": user_consent.user_id, "consent_given": user_consent.consent_given}
        else:
            raise HTTPException(status_code=404, detail="User consent not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail="Failed to retrieve user consent") from e

# Update User Consent Endpoint
@app.put("/user/consent/{user_id}")
async def update_user_consent(user_id: str, user_consent: UserConsentModel, db: SessionLocal = Depends(get_db)):
    try:
        existing_consent = db.query(UserConsent).filter(UserConsent.user_id == user_id).first()
        if existing_consent:
            existing_consent.consent_given = user_consent.consent_given
            db.commit()
            return {"message": "User consent updated"}
        else:
            raise HTTPException(status_code=404, detail="User consent not found")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to update user consent") from e

# Delete User Consent Endpoint
@app.delete("/user/consent/{user_id}")
async def delete_user_consent(user_id: str, db: SessionLocal = Depends(get_db)):
    try:
        user_consent = db.query(UserConsent).filter(UserConsent.user_id == user_id).first()
        if user_consent:
            db.delete(user_consent)
            db.commit()
            return {"message": "User consent deleted"}
        else:
            raise HTTPException(status_code=404, detail="User consent not found")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to delete user consent") from e
```
