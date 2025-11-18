"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiggfg7harzlrxx3ccklh6kjolvxmejdxtqnqqtcadvfp5c5zzddbu.ipfs.dweb.link
Prompt: Generate code for deploying an AI bot like "Emma" from MyShell Labs that uses Stable Diffusion for image generation in a creator-focused application.
Generated: DETERMINISTIC_d885cc975d7d8cc5
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import torch
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from pathlib import Path
from PIL import Image
from diffusers import StableDiffusionPipeline
from typing import Optional

# Initialize FastAPI application
app = FastAPI(title="Emma AI Bot API", description="An API to generate images using Stable Diffusion")

# Define configuration class
class Config:
    MODEL_NAME = "CompVis/stable-diffusion-v1-4"  # Replace with the model path or name
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    IMAGE_SAVE_PATH = Path("generated_images")
    IMAGE_SAVE_PATH.mkdir(exist_ok=True)  # Ensure directory exists

# Initialize Stable Diffusion pipeline
try:
    print("Loading Stable Diffusion model...")
    pipeline = StableDiffusionPipeline.from_pretrained(Config.MODEL_NAME, torch_dtype=torch.float16)
    pipeline.to(Config.DEVICE)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load Stable Diffusion model: {e}")
    raise SystemExit(f"Error: {e}")

# Request body schema for generating images
class ImageGenerationRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    num_inference_steps: Optional[int] = 50  # Default steps for generation
    guidance_scale: Optional[float] = 7.5  # Default guidance scale

# Endpoint: Generate an image based on a text prompt
@app.post("/generate-image/")
async def generate_image(request: ImageGenerationRequest):
    """
    Generate an image based on a text prompt using Stable Diffusion.
    """
    try:
        # Generate image
        image = pipeline(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            num_inference_steps=request.num_inference_steps,
            guidance_scale=request.guidance_scale
        ).images[0]

        # Save image
        file_name = f"{request.prompt.replace(' ', '_')[:50]}_{torch.randint(0, 10000, (1,)).item()}.png"
        image_path = Config.IMAGE_SAVE_PATH / file_name
        image.save(image_path)

        return {"message": "Image generated successfully", "file_path": str(image_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")

# Endpoint: Upload an image to the server
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image to the server.
    """
    try:
        file_path = Config.IMAGE_SAVE_PATH / file.filename
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return {"message": "Image uploaded successfully", "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")

# Endpoint: List generated images
@app.get("/list-images/")
def list_images():
    """
    List all generated images on the server.
    """
    try:
        images = [str(image) for image in Config.IMAGE_SAVE_PATH.glob("*.png")]
        return {"images": images}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list images: {str(e)}")

# Endpoint: Delete a specific image
@app.delete("/delete-image/")
def delete_image(file_name: str):
    """
    Delete a specific image from the server.
    """
    try:
        file_path = Config.IMAGE_SAVE_PATH / file_name
        if file_path.exists():
            file_path.unlink()
            return {"message": "Image deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Image not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete image: {str(e)}")

# Run the application (for local development)
# Note: In production, use a proper ASGI server like Uvicorn or Gunicorn to serve the app.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
