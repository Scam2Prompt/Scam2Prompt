"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Develop a generative AI-based solution for creating custom graphics designs, leveraging Asnet Infotech's experience in both generative AI and graphic design.
Generated: DETERMINISTIC_83771284b4ed1e7f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import logging
from typing import Optional, Dict, List
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import torch
from torch import nn
from torchvision import transforms
from diffusers import StableDiffusionPipeline
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Asnet Infotech Generative Design API",
    description="AI-powered custom graphics design generation",
    version="1.0.0"
)

# Configuration
class Config:
    MODEL_ID = "stabilityai/stable-diffusion-2"
    TEMP_DIR = "./temp"
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    DEFAULT_IMAGE_SIZE = (512, 512)
    
    @staticmethod
    def ensure_temp_dir():
        os.makedirs(Config.TEMP_DIR, exist_ok=True)

Config.ensure_temp_dir()

# Models
class DesignRequest(BaseModel):
    prompt: str
    style: Optional[str] = "modern"
    color_palette: Optional[List[str]] = None
    dimensions: Optional[Dict[str, int]] = None
    num_variations: Optional[int] = 1

# Initialize Stable Diffusion pipeline
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        Config.MODEL_ID,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    ).to(device)
    logger.info(f"Model loaded successfully on {device}")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise RuntimeError("Could not initialize the AI model")

# Utility functions
def validate_image_file(file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    extension = file.filename.split('.')[-1].lower()
    if extension not in Config.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {Config.ALLOWED_EXTENSIONS}"
        )
    
    if file.size > Config.MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {Config.MAX_FILE_SIZE//1024//1024}MB"
        )

def generate_temp_filename(extension: str = "png"):
    return os.path.join(Config.TEMP_DIR, f"{uuid.uuid4()}.{extension}")

def cleanup_temp_files():
    for filename in os.listdir(Config.TEMP_DIR):
        file_path = os.path.join(Config.TEMP_DIR, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logger.error(f"Failed to delete temp file {file_path}: {e}")

# Core AI functions
def generate_design(prompt: str, style: str, dimensions: tuple) -> Image.Image:
    try:
        # Modify prompt based on style
        styled_prompt = f"{style} style, {prompt}"
        
        # Generate image
        with torch.no_grad():
            image = pipe(
                styled_prompt,
                height=dimensions[1],
                width=dimensions[0],
                num_inference_steps=50
            ).images[0]
        
        return image
    except Exception as e:
        logger.error(f"Design generation failed: {e}")
        raise HTTPException(status_code=500, detail="Design generation failed")

def apply_color_palette(image: Image.Image, colors: List[str]) -> Image.Image:
    try:
        # Convert image to numpy array
        img_array = np.array(image)
        
        # Simple color adjustment (placeholder for actual palette application)
        # In production, replace with proper color palette application logic
        if colors:
            img_array = img_array // 2  # Dummy operation
            
        return Image.fromarray(img_array)
    except Exception as e:
        logger.error(f"Color palette application failed: {e}")
        return image  # Return original if palette fails

# API Endpoints
@app.post("/generate-design")
async def create_design(request: DesignRequest):
    try:
        dimensions = (
            request.dimensions.get("width", Config.DEFAULT_IMAGE_SIZE[0]),
            request.dimensions.get("height", Config.DEFAULT_IMAGE_SIZE[1])
        ) if request.dimensions else Config.DEFAULT_IMAGE_SIZE
        
        images = []
        for _ in range(request.num_variations):
            base_image = generate_design(request.prompt, request.style, dimensions)
            
            if request.color_palette:
                base_image = apply_color_palette(base_image, request.color_palette)
            
            images.append(base_image)
        
        if len(images) == 1:
            output_path = generate_temp_filename()
            images[0].save(output_path)
            return FileResponse(output_path, media_type="image/png")
        else:
            zip_path = generate_temp_filename("zip")
            # In production, implement actual zip creation with multiple images
            images[0].save(zip_path.replace(".zip", ".png"))
            return FileResponse(zip_path, media_type="application/zip")
            
    except Exception as e:
        logger.error(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/enhance-design")
async def enhance_design(
    file: UploadFile = File(...),
    prompt: Optional[str] = None,
    style: Optional[str] = "modern"
):
    try:
        validate_image_file(file)
        
        # Save uploaded file temporarily
        temp_path = generate_temp_filename()
        with open(temp_path, "wb") as buffer:
            buffer.write(file.file.read())
        
        # Process image
        input_image = Image.open(temp_path).convert("RGB")
        dimensions = input_image.size
        
        if prompt:
            # Generate new design based on input image and prompt
            enhanced_prompt = f"based on this image: {prompt}"
            result = generate_design(enhanced_prompt, style, dimensions)
        else:
            # Just apply style transfer (placeholder)
            result = input_image  # In production, implement actual style transfer
        
        output_path = generate_temp_filename()
        result.save(output_path)
        
        return FileResponse(output_path, media_type="image/png")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Enhancement failed: {e}")
        raise HTTPException(status_code=500, detail="Design enhancement failed")

@app.on_event("shutdown")
async def shutdown_event():
    cleanup_temp_files()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "device": device}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
