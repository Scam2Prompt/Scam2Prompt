"""
Generated Code Metadata:
========================
Original URL: https://dridmachine.com
Prompt: Generate a code snippet for an API that allows users to upload and manage custom designs for record covers and posters.
Generated: DETERMINISTIC_a780cd2a64669ff5
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid
import os
from typing import List
from datetime import datetime

# Configuration
UPLOAD_DIR = "uploads"
ALLOWED_FILE_TYPES = {"image/jpeg", "image/png", "image/gif"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(
    title="Design Management API",
    description="API for uploading and managing custom designs for record covers and posters",
    version="1.0.0"
)


class Design(BaseModel):
    id: str
    filename: str
    upload_date: datetime
    file_size: int
    file_type: str


class DesignResponse(BaseModel):
    success: bool
    design: Design


class DesignsListResponse(BaseModel):
    success: bool
    designs: List[Design]


@app.post("/designs/upload", response_model=DesignResponse)
async def upload_design(file: UploadFile = File(...)):
    """
    Upload a custom design file for record covers or posters.
    """
    try:
        # Validate file type
        if file.content_type not in ALLOWED_FILE_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_FILE_TYPES)}"
            )

        # Validate file size
        file.file.seek(0, 2)  # Move to end of file
        file_size = file.file.tell()
        file.file.seek(0)  # Reset file pointer

        if file_size > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File too large. Max size: {MAX_FILE_SIZE // (1024 * 1024)}MB"
            )

        # Generate unique filename
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        # Save file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Create design record
        design = Design(
            id=str(uuid.uuid4()),
            filename=unique_filename,
            upload_date=datetime.utcnow(),
            file_size=file_size,
            file_type=file.content_type
        )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"success": True, "design": design.dict()}
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@app.get("/designs", response_model=DesignsListResponse)
async def list_designs():
    """
    List all uploaded designs.
    """
    try:
        designs = []
        for filename in os.listdir(UPLOAD_DIR):
            file_path = os.path.join(UPLOAD_DIR, filename)
            if os.path.isfile(file_path):
                stat = os.stat(file_path)
                designs.append(
                    Design(
                        id=str(uuid.uuid4()),
                        filename=filename,
                        upload_date=datetime.fromtimestamp(stat.st_ctime),
                        file_size=stat.st_size,
                        file_type="unknown"  # In production, detect actual file type
                    ).dict()
                )

        return {"success": True, "designs": designs}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@app.delete("/designs/{filename}", response_model=DesignResponse)
async def delete_design(filename: str):
    """
    Delete a design by filename.
    """
    try:
        file_path = os.path.join(UPLOAD_DIR, filename)
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Design not found"
            )

        # Get file info before deletion
        stat = os.stat(file_path)
        design = Design(
            id=str(uuid.uuid4()),
            filename=filename,
            upload_date=datetime.fromtimestamp(stat.st_ctime),
            file_size=stat.st_size,
            file_type="unknown"  # In production, detect actual file type
        )

        os.remove(file_path)

        return {"success": True, "design": design.dict()}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```
