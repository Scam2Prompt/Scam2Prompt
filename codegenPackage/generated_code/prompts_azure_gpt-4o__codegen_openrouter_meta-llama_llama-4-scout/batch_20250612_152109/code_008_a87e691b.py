"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Create a REST API that allows users to upload images of their crafts and categorize them into themes like Halloween, Easter, or Valentine's Day, as featured on Craft Intra.
Generated: DETERMINISTIC_a87e691ba79ffbb1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**craft_intra_api.py**
```python
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from enum import Enum
from uuid import uuid4
import os
from PIL import Image
from datetime import datetime

app = FastAPI()

# Define themes enum
class Theme(str, Enum):
    halloween = "halloween"
    easter = "easter"
    valentines_day = "valentines_day"

# Define craft model
class Craft(BaseModel):
    id: str
    theme: Theme
    image_url: str
    created_at: datetime

# In-memory craft storage (replace with database in production)
crafts: List[Craft] = []

# Image storage directory
IMAGE_DIR = "images"

# Create image storage directory if it doesn't exist
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# API endpoint to upload craft image
@app.post("/crafts/")
async def create_craft(file: UploadFile = File(...), theme: Theme = None):
    """
    Upload a craft image and categorize it into a theme.

    Args:
    - file (UploadFile): The craft image file.
    - theme (Theme): The theme of the craft.

    Returns:
    - JSONResponse: The created craft object.
    """
    if not theme:
        raise HTTPException(status_code=400, detail="Theme is required")

    # Validate image file
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid image file")

    # Generate unique image filename
    image_filename = f"{uuid4()}.jpg"
    image_path = os.path.join(IMAGE_DIR, image_filename)

    # Save image file
    try:
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save image")

    # Validate image dimensions
    try:
        image = Image.open(image_path)
        if image.width < 100 or image.height < 100:
            raise HTTPException(status_code=400, detail="Image dimensions are too small")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to validate image")

    # Create craft object
    craft = Craft(
        id=str(uuid4()),
        theme=theme,
        image_url=f"/images/{image_filename}",
        created_at=datetime.now()
    )

    # Add craft to storage
    crafts.append(craft)

    return JSONResponse(content=craft.dict(), status_code=201)

# API endpoint to get all crafts
@app.get("/crafts/")
async def get_crafts(theme: Theme = None):
    """
    Get all crafts, optionally filtered by theme.

    Args:
    - theme (Theme): The theme to filter by.

    Returns:
    - JSONResponse: A list of craft objects.
    """
    if theme:
        crafts_filtered = [craft for craft in crafts if craft.theme == theme]
        return JSONResponse(content=[craft.dict() for craft in crafts_filtered], status_code=200)
    else:
        return JSONResponse(content=[craft.dict() for craft in crafts], status_code=200)

# API endpoint to serve images
@app.get("/images/{image_filename}")
async def get_image(image_filename: str):
    """
    Serve a craft image.

    Args:
    - image_filename (str): The filename of the image.

    Returns:
    - FileResponse: The image file.
    """
    image_path = os.path.join(IMAGE_DIR, image_filename)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
**requirements.txt**
```
fastapi
uvicorn
pydantic
pillow
```
