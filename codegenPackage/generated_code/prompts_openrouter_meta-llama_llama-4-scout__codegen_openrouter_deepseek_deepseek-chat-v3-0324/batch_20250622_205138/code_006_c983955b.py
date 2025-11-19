"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Design a RESTful API for managing 3D CAD models, including uploading, sharing, and annotating, based on cadvio's functionality.
Generated: DETERMINISTIC_c983955bf6e242c5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CAD Model Management API
This module provides RESTful endpoints for managing 3D CAD models,
including upload, sharing, and annotation functionality.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import os
from pathlib import Path

app = FastAPI(
    title="CAD Model Management API",
    description="API for managing 3D CAD models with upload, share, and annotation features",
    version="1.0.0"
)

# Security setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (would typically be ORM models in production)
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True

class CADModel(BaseModel):
    id: str
    name: str
    file_path: str
    file_type: str
    file_size: int
    owner_id: str
    created_at: datetime
    updated_at: datetime
    is_public: bool = False

class ModelShare(BaseModel):
    id: str
    model_id: str
    shared_with_user_id: str
    permission_level: str  # "view", "edit", "admin"
    shared_by: str
    shared_at: datetime

class Annotation(BaseModel):
    id: str
    model_id: str
    author_id: str
    content: str
    position: List[float]  # [x, y, z]
    created_at: datetime
    updated_at: datetime

# Config
MODEL_STORAGE_PATH = Path("models")
ALLOWED_FILE_TYPES = [".stl", ".obj", ".step", ".iges"]
MAX_FILE_SIZE_MB = 50

# Ensure storage directory exists
MODEL_STORAGE_PATH.mkdir(exist_ok=True)

# Helper functions
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In production, this would validate the token and return user
    # Mock implementation for demo purposes
    return User(id="user1", username="testuser", email="user@example.com", hashed_password="")

def validate_file(file: UploadFile):
    file_extension = Path(file.filename).suffix.lower()
    if file_extension not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_FILE_TYPES)}"
        )
    
    if file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File size exceeds maximum allowed size of {MAX_FILE_SIZE_MB}MB"
        )

# API Endpoints
@app.post("/models/upload", response_model=CADModel, status_code=status.HTTP_201_CREATED)
async def upload_model(
    file: UploadFile = File(...),
    is_public: bool = False,
    current_user: User = Depends(get_current_user)
):
    """
    Upload a new CAD model.
    """
    validate_file(file)
    
    model_id = str(uuid.uuid4())
    file_extension = Path(file.filename).suffix.lower()
    file_name = f"{model_id}{file_extension}"
    file_path = MODEL_STORAGE_PATH / file_name
    
    try:
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error saving file: {str(e)}"
        )
    
    model = CADModel(
        id=model_id,
        name=file.filename,
        file_path=str(file_path),
        file_type=file_extension,
        file_size=file.size,
        owner_id=current_user.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_public=is_public
    )
    
    # In production, would save to database here
    return model

@app.get("/models", response_model=List[CADModel])
async def list_models(
    current_user: User = Depends(get_current_user),
    public_only: bool = False
):
    """
    List all CAD models accessible to the current user.
    """
    # Mock implementation - in production would query database
    mock_models = [
        CADModel(
            id="model1",
            name="Example Model",
            file_path="/path/to/model1.stl",
            file_type=".stl",
            file_size=1024,
            owner_id=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            is_public=True
        )
    ]
    return mock_models

@app.get("/models/{model_id}", response_model=CADModel)
async def get_model(
    model_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Get details of a specific CAD model.
    """
    # Mock implementation - in production would query database
    # and check permissions
    return CADModel(
        id=model_id,
        name="Example Model",
        file_path="/path/to/model1.stl",
        file_type=".stl",
        file_size=1024,
        owner_id=current_user.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_public=True
    )

@app.post("/models/{model_id}/share", response_model=ModelShare)
async def share_model(
    model_id: str,
    shared_with_user_id: str,
    permission_level: str,
    current_user: User = Depends(get_current_user)
):
    """
    Share a CAD model with another user.
    """
    if permission_level not in ["view", "edit", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid permission level"
        )
    
    # In production, would verify model exists and user has permission to share
    
    share = ModelShare(
        id=str(uuid.uuid4()),
        model_id=model_id,
        shared_with_user_id=shared_with_user_id,
        permission_level=permission_level,
        shared_by=current_user.id,
        shared_at=datetime.utcnow()
    )
    
    return share

@app.post("/models/{model_id}/annotations", response_model=Annotation)
async def create_annotation(
    model_id: str,
    content: str,
    position: List[float],
    current_user: User = Depends(get_current_user)
):
    """
    Create an annotation on a CAD model.
    """
    if len(position) != 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Position must be an array of 3 coordinates [x, y, z]"
        )
    
    annotation = Annotation(
        id=str(uuid.uuid4()),
        model_id=model_id,
        author_id=current_user.id,
        content=content,
        position=position,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    return annotation

@app.get("/models/{model_id}/annotations", response_model=List[Annotation])
async def get_annotations(
    model_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Get all annotations for a CAD model.
    """
    # Mock implementation
    return [
        Annotation(
            id="anno1",
            model_id=model_id,
            author_id=current_user.id,
            content="Example annotation",
            position=[0.0, 0.0, 0.0],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
    ]

@app.delete("/models/{model_id}")
async def delete_model(
    model_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Delete a CAD model.
    """
    # In production, would verify ownership/permissions
    # and delete from storage and database
    return {"message": "Model deleted successfully"}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred"}
    )
```
