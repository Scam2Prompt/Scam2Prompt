"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Suggest an API for managing digital art portfolios, considering the focus on artistic expression and development at Ânima.
Generated: DETERMINISTIC_a2afdf2e4238fa06
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Digital Art Portfolio API for Ânima

```python
from fastapi import FastAPI, HTTPException, UploadFile, Form, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import os
from PIL import Image
import shutil
import mimetypes

app = FastAPI(
    title="Ânima Digital Art Portfolio API",
    description="API for managing digital art portfolios with focus on artistic expression",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configuration
MEDIA_DIR = "media"
PORTFOLIO_THUMBNAIL_SIZE = (300, 300)
SUPPORTED_MEDIA_TYPES = ["image/jpeg", "image/png", "image/gif", "video/mp4"]

# Ensure media directory exists
os.makedirs(MEDIA_DIR, exist_ok=True)

# Models
class Artist(BaseModel):
    id: str
    name: str
    email: EmailStr
    bio: Optional[str] = None
    joined_date: datetime

class Artwork(BaseModel):
    id: str
    artist_id: str
    title: str
    description: Optional[str] = None
    media_url: str
    thumbnail_url: str
    creation_date: datetime
    tags: List[str] = []
    is_featured: bool = False
    dimensions: Optional[str] = None

class Portfolio(BaseModel):
    artist_id: str
    artworks: List[Artwork] = []
    showcase: List[Artwork] = []
    style_description: Optional[str] = None

class Comment(BaseModel):
    id: str
    artwork_id: str
    author_id: str
    content: str
    created_at: datetime

# Database Mock (in production, replace with real database)
db = {
    "artists": {},
    "artworks": {},
    "portfolios": {},
    "comments": {}
}

# Utility Functions
def generate_id():
    return str(uuid.uuid4())

def save_media_file(file: UploadFile) -> str:
    try:
        # Validate media type
        if file.content_type not in SUPPORTED_MEDIA_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported media type")
        
        # Generate unique filename
        file_ext = mimetypes.guess_extension(file.content_type)
        if not file_ext:
            file_ext = os.path.splitext(file.filename)[1]
        filename = f"{generate_id()}{file_ext}"
        file_path = os.path.join(MEDIA_DIR, filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        return filename
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save media: {str(e)}")

def create_thumbnail(media_path: str) -> str:
    try:
        # Only create thumbnails for images
        if not media_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return media_path
            
        # Generate thumbnail filename
        thumbnail_path = f"{os.path.splitext(media_path)[0]}_thumb.jpg"
        full_thumb_path = os.path.join(MEDIA_DIR, thumbnail_path)
        
        # Create thumbnail
        with Image.open(os.path.join(MEDIA_DIR, media_path)) as img:
            img.thumbnail(PORTFOLIO_THUMBNAIL_SIZE)
            img.save(full_thumb_path, "JPEG")
            
        return thumbnail_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create thumbnail: {str(e)}")

# Authentication
async def get_current_artist(token: str = Depends(oauth2_scheme)):
    # In production, implement proper token validation
    artist = db["artists"].get(token)
    if not artist:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return artist

# Endpoints
@app.post("/artists/register", response_model=Artist)
async def register_artist(name: str = Form(...), email: EmailStr = Form(...), bio: Optional[str] = Form(None)):
    artist_id = generate_id()
    new_artist = Artist(
        id=artist_id,
        name=name,
        email=email,
        bio=bio,
        joined_date=datetime.utcnow()
    )
    db["artists"][artist_id] = new_artist
    db["portfolios"][artist_id] = Portfolio(artist_id=artist_id)
    return new_artist

@app.get("/artists/{artist_id}", response_model=Artist)
async def get_artist(artist_id: str):
    if artist_id not in db["artists"]:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db["artists"][artist_id]

@app.post("/artworks", response_model=Artwork)
async def create_artwork(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    file: UploadFile = Form(...),
    tags: List[str] = Form([]),
    dimensions: Optional[str] = Form(None),
    artist: Artist = Depends(get_current_artist)
):
    try:
        media_filename = save_media_file(file)
        thumbnail_filename = create_thumbnail(media_filename)
        
        artwork_id = generate_id()
        new_artwork = Artwork(
            id=artwork_id,
            artist_id=artist.id,
            title=title,
            description=description,
            media_url=f"/media/{media_filename}",
            thumbnail_url=f"/media/{thumbnail_filename}",
            creation_date=datetime.utcnow(),
            tags=tags,
            dimensions=dimensions
        )
        
        db["artworks"][artwork_id] = new_artwork
        db["portfolios"][artist.id].artworks.append(new_artwork)
        
        return new_artwork
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/artworks/{artwork_id}", response_model=Artwork)
async def get_artwork(artwork_id: str):
    if artwork_id not in db["artworks"]:
        raise HTTPException(status_code=404, detail="Artwork not found")
    return db["artworks"][artwork_id]

@app.get("/artists/{artist_id}/portfolio", response_model=Portfolio)
async def get_portfolio(artist_id: str):
    if artist_id not in db["portfolios"]:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db["portfolios"][artist_id]

@app.put("/portfolios/showcase", response_model=Portfolio)
async def update_showcase(
    artwork_ids: List[str],
    artist: Artist = Depends(get_current_artist)
):
    portfolio = db["portfolios"].get(artist.id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    new_showcase = []
    for artwork_id in artwork_ids:
        if artwork_id not in db["artworks"] or db["artworks"][artwork_id].artist_id != artist.id:
            raise HTTPException(status_code=400, detail="Invalid artwork in showcase")
        new_showcase.append(db["artworks"][artwork_id])
    
    portfolio.showcase = new_showcase
    return portfolio

@app.post("/artworks/{artwork_id}/comments", response_model=Comment)
async def add_comment(
    artwork_id: str,
    content: str = Form(...),
    artist: Artist = Depends(get_current_artist)
):
    if artwork_id not in db["artworks"]:
        raise HTTPException(status_code=404, detail="Artwork not found")
    
    comment_id = generate_id()
    new_comment = Comment(
        id=comment_id,
        artwork_id=artwork_id,
        author_id=artist.id,
        content=content,
        created_at=datetime.utcnow()
    )
    
    db["comments"][comment_id] = new_comment
    return new_comment

@app.get("/artworks/{artwork_id}/comments", response_model=List[Comment])
async def get_comments(artwork_id: str):
    if artwork_id not in db["artworks"]:
        raise HTTPException(status_code=404, detail="Artwork not found")
    
    return [comment for comment in db["comments"].values() if comment.artwork_id == artwork_id]

# Media serving
@app.get("/media/{filename}")
async def serve_media(filename: str):
    file_path = os.path.join(MEDIA_DIR, filename)
    if not os.path.exists(file_path):
