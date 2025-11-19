"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Write code to implement an "Avatar Casting Call" feature that allows users to submit their avatars for potential inclusion in comics or media, as described on the Parallel platform.
Generated: DETERMINISTIC_40c6d305aa525d29
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, validator
from uuid import uuid4
import aiofiles

# Initialize FastAPI app
app = FastAPI(
    title="Avatar Casting Call API",
    description="API for submitting avatars for potential inclusion in comics or media",
    version="1.0.0"
)

# Configuration
AVATAR_UPLOAD_DIR = "uploads/avatars"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_FILE_TYPES = ["image/jpeg", "image/png", "image/gif"]
os.makedirs(AVATAR_UPLOAD_DIR, exist_ok=True)

# Data Models
class AvatarSubmission(BaseModel):
    """Model for avatar submission data"""
    user_id: str
    name: str
    email: EmailStr
    avatar_name: str
    description: str
    social_media: Optional[str] = None
    terms_accepted: bool
    
    @validator('terms_accepted')
    def validate_terms(cls, v):
        if not v:
            raise ValueError("You must accept the terms and conditions")
        return v

class SubmissionResponse(BaseModel):
    """Response model for successful submission"""
    submission_id: str
    message: str
    timestamp: datetime

# Helper Functions
async def save_uploaded_file(file: UploadFile, submission_id: str) -> str:
    """Save uploaded file to disk and return the file path"""
    file_ext = os.path.splitext(file.filename)[1]
    file_name = f"{submission_id}{file_ext}"
    file_path = os.path.join(AVATAR_UPLOAD_DIR, file_name)
    
    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(8192):  # 8KB chunks
            await f.write(chunk)
    
    return file_path

def validate_file(file: UploadFile):
    """Validate the uploaded file"""
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File type not supported. Allowed types: {', '.join(ALLOWED_FILE_TYPES)}"
        )
    
    file.file.seek(0, 2)  # Seek to end of file
    file_size = file.file.tell()
    file.file.seek(0)  # Reset file pointer
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size: {MAX_FILE_SIZE//(1024*1024)}MB"
        )

# API Endpoints
@app.post("/submit-avatar", response_model=SubmissionResponse)
async def submit_avatar(
    name: str = Form(...),
    email: EmailStr = Form(...),
    avatar_name: str = Form(...),
    description: str = Form(...),
    social_media: Optional[str] = Form(None),
    terms_accepted: bool = Form(...),
    avatar_file: UploadFile = File(...)
):
    """
    Submit an avatar for casting call consideration.
    
    Args:
        name: User's full name
        email: User's email address
        avatar_name: Name of the avatar
        description: Description of the avatar
        social_media: Optional social media link
        terms_accepted: Must be True to accept terms
        avatar_file: Image file of the avatar
    
    Returns:
        SubmissionResponse with submission details
    """
    try:
        # Validate file
        validate_file(avatar_file)
        
        # Generate submission ID
        submission_id = str(uuid4())
        
        # Save avatar file
        await save_uploaded_file(avatar_file, submission_id)
        
        # Create submission record (in a real app, this would be saved to a database)
        submission = AvatarSubmission(
            user_id=submission_id,
            name=name,
            email=email,
            avatar_name=avatar_name,
            description=description,
            social_media=social_media,
            terms_accepted=terms_accepted
        )
        
        # Return success response
        return SubmissionResponse(
            submission_id=submission_id,
            message="Avatar submitted successfully!",
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/submissions", response_model=List[AvatarSubmission])
async def list_submissions():
    """
    List all avatar submissions (stub implementation).
    In a real application, this would query a database.
    """
    # This is a stub - in production you would query a database
    return []

# Error Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.exception_handler(500)
async def internal_server_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error"}
    )

# Health Check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
