"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Develop a feature for tracking school toppers and maintaining a gallery section, as described in Him Saral's School Toppers & Gallery module.
Generated: DETERMINISTIC_0ef23af58ce25c75
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_toppers_gallery.py

import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, validator
from PIL import Image
import shutil

app = FastAPI(title="School Toppers & Gallery Module")

# Configuration
UPLOAD_FOLDER = "uploads"
TOPPERS_FILE = "data/toppers.json"
GALLERY_FILE = "data/gallery.json"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
THUMBNAIL_SIZE = (200, 200)

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(TOPPERS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(GALLERY_FILE), exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class Topper(BaseModel):
    id: str
    name: str
    year: int
    percentage: float
    achievements: str
    photo_url: Optional[str] = None

    @validator('percentage')
    def validate_percentage(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Percentage must be between 0 and 100')
        return v

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if not 1900 <= v <= current_year:
            raise ValueError(f'Year must be between 1900 and {current_year}')
        return v

class GalleryItem(BaseModel):
    id: str
    title: str
    description: str
    date: str
    image_url: str
    tags: List[str] = []

def load_data(file_path: str, default: List) -> List:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def save_data(file_path: str, data: List) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_thumbnail(image_path: str, thumbnail_path: str) -> None:
    with Image.open(image_path) as img:
        img.thumbnail(THUMBNAIL_SIZE)
        img.save(thumbnail_path)

@app.get("/toppers", response_model=List[Topper])
def get_toppers(year: Optional[int] = None):
    toppers = load_data(TOPPERS_FILE, [])
    if year:
        return [topper for topper in toppers if topper['year'] == year]
    return toppers

@app.post("/toppers", response_model=Topper)
def add_topper(topper: Topper):
    toppers = load_data(TOPPERS_FILE, [])
    if any(t['id'] == topper.id for t in toppers):
        raise HTTPException(status_code=400, detail="Topper with this ID already exists")
    toppers.append(topper.dict())
    save_data(TOPPERS_FILE, toppers)
    return topper

@app.post("/toppers/upload-photo")
async def upload_topper_photo(file: UploadFile = File(...), topper_id: str = Form(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    toppers = load_data(TOPPERS_FILE, [])
    topper = next((t for t in toppers if t['id'] == topper_id), None)
    if not topper:
        raise HTTPException(status_code=404, detail="Topper not found")
    
    filename = f"topper_{topper_id}.{file.filename.rsplit('.', 1)[1].lower()}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    thumbnail_path = os.path.join(UPLOAD_FOLDER, f"thumb_{filename}")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        generate_thumbnail(file_path, thumbnail_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    topper['photo_url'] = f"/static/{filename}"
    save_data(TOPPERS_FILE, toppers)
    
    return {"message": "Photo uploaded successfully", "photo_url": topper['photo_url']}

@app.get("/gallery", response_model=List[GalleryItem])
def get_gallery_items(tag: Optional[str] = None):
    gallery = load_data(GALLERY_FILE, [])
    if tag:
        return [item for item in gallery if tag in item['tags']]
    return gallery

@app.post("/gallery", response_model=GalleryItem)
def add_gallery_item(item: GalleryItem):
    gallery = load_data(GALLERY_FILE, [])
    if any(i['id'] == item.id for i in gallery):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    gallery.append(item.dict())
    save_data(GALLERY_FILE, gallery)
    return item

@app.post("/gallery/upload-image")
async def upload_gallery_image(file: UploadFile = File(...), item_id: str = Form(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    gallery = load_data(GALLERY_FILE, [])
    item = next((i for i in gallery if i['id'] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Gallery item not found")
    
    filename = f"gallery_{item_id}.{file.filename.rsplit('.', 1)[1].lower()}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    thumbnail_path = os.path.join(UPLOAD_FOLDER, f"thumb_{filename}")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        generate_thumbnail(file_path, thumbnail_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    item['image_url'] = f"/static/{filename}"
    save_data(GALLERY_FILE, gallery)
    
    return {"message": "Image uploaded successfully", "image_url": item['image_url']}

@app.get("/static/{filename}")
async def serve_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
