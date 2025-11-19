"""
Generated Code Metadata:
========================
Original URL: https://bafybeiggfg7harzlrxx3ccklh6kjolvxmejdxtqnqqtcadvfp5c5zzddbu.ipfs.dweb.link
Prompt: Generate code for deploying an AI bot like "Emma" from MyShell Labs that uses Stable Diffusion for image generation in a creator-focused application.
Generated: DETERMINISTIC_d885cc975d7d8cc5
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import io
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="MyShell AI Creator Platform",
    description="API for AI-powered creator tools with Stable Diffusion integration",
    version="1.0.0"
)

# Configuration
class Config:
    def __init__(self):
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.safety_checker = True
        self.max_image_size = (1024, 1024)
        self.default_steps = 50
        self.default_guidance_scale = 7.5

config = Config()

# Load model
try:
    pipe = StableDiffusionPipeline.from_pretrained(
        config.model_id,
        torch_dtype=torch.float16 if config.device == "cuda" else torch.float32,
        safety_checker=None if not config.safety_checker else None
    )
    pipe = pipe.to(config.device)
    logger.info(f"Model loaded successfully on device: {config.device}")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise RuntimeError("Model initialization failed")

# Request models
class TextToImageRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    steps: Optional[int] = config.default_steps
    guidance_scale: Optional[float] = config.default_guidance_scale
    width: Optional[int] = 512
    height: Optional[int] = 512
    seed: Optional[int] = None

class ImageEditRequest(BaseModel):
    prompt: str
    init_image: UploadFile = File(...)
    strength: Optional[float] = 0.8
    steps: Optional[int] = config.default_steps
    guidance_scale: Optional[float] = config.default_guidance_scale
    seed: Optional[int] = None

# Utility functions
def validate_image_size(width: int, height: int) -> bool:
    max_w, max_h = config.max_image_size
    return width <= max_w and height <= max_h and width > 0 and height > 0

def generate_seed_if_none(seed: Optional[int]) -> int:
    return seed if seed is not None else torch.randint(0, 2**32 - 1, (1,)).item()

def process_image(image: Image.Image) -> Image.Image:
    return image.resize((image.width, image.height))  # Placeholder for actual processing

# API endpoints
@app.post("/generate-image")
async def generate_image(request: TextToImageRequest):
    """Generate image from text prompt using Stable Diffusion"""
    try:
        if not validate_image_size(request.width, request.height):
            raise HTTPException(
                status_code=400,
                detail=f"Image dimensions must be <= {config.max_image_size}"
            )

        generator = torch.Generator(device=config.device).manual_seed(
            generate_seed_if_none(request.seed)
        )

        with torch.autocast(config.device):
            image = pipe(
                prompt=request.prompt,
                negative_prompt=request.negative_prompt,
                num_inference_steps=request.steps,
                guidance_scale=request.guidance_scale,
                width=request.width,
                height=request.height,
                generator=generator
            ).images[0]

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        logger.error(f"Image generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/edit-image")
async def edit_image(
    prompt: str = Form(...),
    init_image: UploadFile = File(...),
    strength: float = Form(0.8),
    steps: int = Form(config.default_steps),
    guidance_scale: float = Form(config.default_guidance_scale),
    seed: Optional[int] = Form(None)
):
    """Edit an existing image using Stable Diffusion img2img"""
    try:
        if strength <= 0 or strength >= 1:
            raise HTTPException(
                status_code=400,
                detail="Strength must be between 0 and 1"
            )

        # Read and validate input image
        input_image = Image.open(init_image.file)
        if input_image.mode != "RGB":
            input_image = input_image.convert("RGB")

        generator = torch.Generator(device=config.device).manual_seed(
            generate_seed_if_none(seed)
        )

        with torch.autocast(config.device):
            image = pipe(
                prompt=prompt,
                image=input_image,
                strength=strength,
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                generator=generator
            ).images[0]

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        logger.error(f"Image editing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "device": config.device}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
