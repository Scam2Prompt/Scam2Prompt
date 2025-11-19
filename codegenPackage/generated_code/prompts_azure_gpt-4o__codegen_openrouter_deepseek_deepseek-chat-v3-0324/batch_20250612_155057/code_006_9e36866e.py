"""
Generated Code Metadata:
========================
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Suggest tools or frameworks to build a data liquidity pool for personal data portability, inspired by the Vana Network.
Generated: DETERMINISTIC_9e36866ea559b424
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_liquidity_pool.py
import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import hashlib
import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

# Constants
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data_pool.db")
SECRET_KEY = os.getenv("SECRET_KEY", Fernet.generate_key().decode())
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", Fernet.generate_key().decode())

# Database setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Encryption setup
fernet = Fernet(ENCRYPTION_KEY)

class DataType(str, Enum):
    PROFILE = "profile"
    BEHAVIORAL = "behavioral"
    TRANSACTIONAL = "transactional"
    SENSOR = "sensor"
    OTHER = "other"

@dataclass
class DataEntry:
    id: str
    owner_id: str
    data_type: DataType
    encrypted_data: str
    created_at: datetime
    updated_at: datetime
    is_shared: bool = False
    shared_with: List[str] = None

class DataShareRequest(BaseModel):
    data_id: str
    recipient_id: str
    expiration: Optional[datetime] = None

class DataUploadRequest(BaseModel):
    data_type: DataType
    raw_data: Dict
    is_shared: bool = False

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    public_key = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class DataRecord(Base):
    __tablename__ = "data_records"
    id = Column(String, primary_key=True, index=True)
    owner_id = Column(String, index=True)
    data_type = Column(String)
    encrypted_data = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_shared = Column(Boolean, default=False)
    shared_with = Column(JSON, default=[])

class ShareRecord(Base):
    __tablename__ = "share_records"
    id = Column(String, primary_key=True, index=True)
    data_id = Column(String, index=True)
    owner_id = Column(String, index=True)
    recipient_id = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expiration = Column(DateTime, nullable=True)

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Data Liquidity Pool API",
    description="API for personal data portability inspired by Vana Network",
    version="0.1.0"
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )

def encrypt_data(data: Dict) -> str:
    json_data = json.dumps(data)
    return fernet.encrypt(json_data.encode()).decode()

def decrypt_data(encrypted_data: str) -> Dict:
    decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
    return json.loads(decrypted_data)

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user():
    db = SessionLocal()
    user_id = str(uuid.uuid4())
    public_key = hashlib.sha256(user_id.encode()).hexdigest()
    
    user = User(id=user_id, public_key=public_key)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    
    return {"user_id": user_id, "public_key": public_key}

@app.post("/data/upload/", status_code=status.HTTP_201_CREATED)
async def upload_data(data_request: DataUploadRequest, owner_id: str):
    db = SessionLocal()
    
    # Verify user exists
    user = db.query(User).filter(User.id == owner_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create data record
    data_id = str(uuid.uuid4())
    encrypted_data = encrypt_data(data_request.raw_data)
    
    data_record = DataRecord(
        id=data_id,
        owner_id=owner_id,
        data_type=data_request.data_type.value,
        encrypted_data=encrypted_data,
        is_shared=data_request.is_shared
    )
    
    db.add(data_record)
    db.commit()
    db.refresh(data_record)
    db.close()
    
    return {"data_id": data_id, "status": "uploaded"}

@app.post("/data/share/", status_code=status.HTTP_200_OK)
async def share_data(share_request: DataShareRequest, owner_id: str):
    db = SessionLocal()
    
    # Verify owner and data exist
    owner = db.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    data_record = db.query(DataRecord).filter(DataRecord.id == share_request.data_id).first()
    if not data_record:
        raise HTTPException(status_code=404, detail="Data not found")
    
    if data_record.owner_id != owner_id:
        raise HTTPException(status_code=403, detail="Not authorized to share this data")
    
    # Verify recipient exists
    recipient = db.query(User).filter(User.id == share_request.recipient_id).first()
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    
    # Update data record
    if share_request.recipient_id not in data_record.shared_with:
        data_record.shared_with.append(share_request.recipient_id)
        data_record.is_shared = True
    
    # Create share record
    share_record = ShareRecord(
        id=str(uuid.uuid4()),
        data_id=share_request.data_id,
        owner_id=owner_id,
        recipient_id=share_request.recipient_id,
        expiration=share_request.expiration
    )
    
    db.add(share_record)
    db.commit()
    db.refresh(share_record)
    db.close()
    
    return {"status": "shared", "share_id": share_record.id}

@app.get("/data/{data_id}", response_model=Dict)
async def get_data(data_id: str, user_id: str):
    db = SessionLocal()
    
    data_record = db.query(DataRecord).filter(DataRecord.id == data_id).first()
    if not data_record:
        raise HTTPException(status_code=404, detail="Data not found")
    
    # Check access rights
    if data_record.owner_id != user_id and user_id not in data_record.shared_with:
        raise HTTPException(status_code=403, detail="Not authorized to access this data")
    
    decrypted_data = decrypt_data(data_record.encrypted_data)
    db.close()
    
    return {
        "data_id": data_id,
        "owner_id": data_record.owner_id,
        "data_type": data_record.data_type,
        "data": decrypted_data,
        "created_at": data_record.created_at,
        "updated_at": data_record.updated_at
    }

@app.get("/user/data/", response_model=List[Dict])
async def list_user_data(user_id: str):
    db = SessionLocal()
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    data_records = db.query(DataRecord).filter(DataRecord.owner_id == user_id).all()
    result = []
    
    for record in data_records:
        result.append({
            "data_id": record.id,
            "data_type": record.data_type,
            "is_shared": record.is_shared,
            "shared_with": record.shared_with,
            "created_at": record.created_at,
            "updated_at": record.updated_at
        })
    
    db.close()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
