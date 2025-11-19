"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Generate code for an API that allows users to interact with AI-generated art, using Refik Anadol's Sphere LA Times project as a reference.
Generated: DETERMINISTIC_2f850de0ae0efc6c
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
import os
from datetime import datetime
import logging
from PIL import Image
import io
import base64
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Art Generation API",
    description="API for interacting with AI-generated art inspired by Refik Anadol's Sphere LA Times project",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ArtGenerationRequest(BaseModel):
    prompt: str
    style: Optional[str] = "abstract"
    resolution: Optional[str] = "1024x1024"
    iterations: Optional[int] = 100

class ArtPiece(BaseModel):
    id: str
    prompt: str
    style: str
    resolution: str
    created_at: str
    image_url: Optional[str] = None
    image_base64: Optional[str] = None

class GalleryResponse(BaseModel):
    pieces: List[ArtPiece]
    count: int

# Configuration
ART_STORAGE_DIR = "art_storage"
os.makedirs(ART_STORAGE_DIR, exist_ok=True)

# Load AI model (placeholder - replace with actual model loading)
try:
    # In a real implementation, this would load your trained AI model
    # model = load_model('path/to/your/model.h5')
    logger.info("AI model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load AI model: {e}")
    raise

# Utility functions
def generate_art_image(prompt: str, style: str, resolution: str) -> str:
    """
    Generate art image using AI model (placeholder implementation)
    In a real implementation, this would use the loaded model
    """
    try:
        # Placeholder: Generate a random image
        width, height = map(int, resolution.split('x'))
        random_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        img = Image.fromarray(random_image)
        
        # Save to file
        art_id = str(uuid.uuid4())
        filename = f"{art_id}.png"
        filepath = os.path.join(ART_STORAGE_DIR, filename)
        img.save(filepath)
        
        return art_id
    except Exception as e:
        logger.error(f"Error generating art: {e}")
        raise

def get_image_base64(art_id: str) -> str:
    """Convert image to base64 string"""
    try:
        filepath = os.path.join(ART_STORAGE_DIR, f"{art_id}.png")
        with open(filepath, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        logger.error(f"Error converting image to base64: {e}")
        raise

# API Endpoints
@app.post("/generate", response_model=ArtPiece)
async def generate_art(request: ArtGenerationRequest):
    """Generate AI art based on prompt and style"""
    try:
        logger.info(f"Generating art with prompt: {request.prompt}")
        
        art_id = generate_art_image(
            prompt=request.prompt,
            style=request.style,
            resolution=request.resolution
        )
        
        created_at = datetime.utcnow().isoformat()
        
        return ArtPiece(
            id=art_id,
            prompt=request.prompt,
            style=request.style,
            resolution=request.resolution,
            created_at=created_at,
            image_url=f"/art/{art_id}",
            image_base64=get_image_base64(art_id)
        )
    except Exception as e:
        logger.error(f"Error in generate_art: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/art/{art_id}", response_model=ArtPiece)
async def get_art(art_id: str):
    """Retrieve generated art by ID"""
    try:
        filepath = os.path.join(ART_STORAGE_DIR, f"{art_id}.png")
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="Art piece not found")
        
        created_at = datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
        
        return ArtPiece(
            id=art_id,
            prompt="Unknown",  # In a real implementation, store metadata
            style="Unknown",
            resolution="Unknown",
            created_at=created_at,
            image_url=f"/art/{art_id}",
            image_base64=get_image_base64(art_id)
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in get_art: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gallery", response_model=GalleryResponse)
async def get_gallery(limit: int = 10, offset: int = 0):
    """Get a list of all generated art pieces"""
    try:
        art_files = [f for f in os.listdir(ART_STORAGE_DIR) if f.endswith('.png')]
        art_files = art_files[offset:offset+limit]
        
        pieces = []
        for art_file in art_files:
            art_id = art_file.split('.')[0]
            filepath = os.path.join(ART_STORAGE_DIR, art_file)
            created_at = datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
            
            pieces.append(ArtPiece(
                id=art_id,
                prompt="Unknown",
                style="Unknown",
                resolution="Unknown",
                created_at=created_at,
                image_url=f"/art/{art_id}"
            ))
        
        return GalleryResponse(
            pieces=pieces,
            count=len(pieces)
        )
    except Exception as e:
        logger.error(f"Error in get_gallery: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-style")
async def upload_style(
    file: UploadFile = File(...),
    style_name: str = Form(...),
    description: Optional[str] = Form(None)
):
    """Upload a new style for AI art generation"""
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise HTTPException(status_code=400, detail="Only image files are allowed")
        
        # Process and save the style image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # In a real implementation, you would process the style image
        # and potentially train or update your model
        
        return {"message": "Style uploaded successfully", "style_name": style_name}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in upload_style: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
```
