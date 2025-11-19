"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Write Python code to create an AI avatar system that uses visual cards to capture subconscious emotional preferences, similar to the initial avatar creation process described on blur.today.
Generated: DETERMINISTIC_80b5d59ac2dcc758
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
from pathlib import Path
import uuid
from PIL import Image
import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# Configuration
class Config:
    STATIC_DIR = "static"
    UPLOAD_DIR = "uploads"
    AVATAR_DIR = "avatars"
    CARD_DIR = "cards"
    MAX_IMAGE_SIZE = (800, 800)
    COLOR_CLUSTERS = 5
    MAX_CARDS = 20
    SESSION_EXPIRY = 3600  # 1 hour in seconds

# Data Models
@dataclass
class EmotionCard:
    id: str
    image_path: str
    dominant_colors: List[List[int]]
    emotion_tags: List[str]

@dataclass
class UserSession:
    session_id: str
    selected_cards: List[EmotionCard]
    created_at: float
    avatar_path: Optional[str] = None

# Initialize directories
def init_directories():
    Path(Config.STATIC_DIR).mkdir(exist_ok=True)
    Path(Config.UPLOAD_DIR).mkdir(exist_ok=True)
    Path(Config.AVATAR_DIR).mkdir(exist_ok=True)
    Path(Config.CARD_DIR).mkdir(exist_ok=True)

# Helper functions
def generate_id() -> str:
    return str(uuid.uuid4())

def get_dominant_colors(image_path: str, k: int = Config.COLOR_CLUSTERS) -> List[List[int]]:
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_.astype(int)
    return colors.tolist()

def resize_image(image_path: str, max_size: tuple = Config.MAX_IMAGE_SIZE):
    with Image.open(image_path) as img:
        img.thumbnail(max_size)
        img.save(image_path)

def save_uploaded_file(file: UploadFile) -> str:
    file_ext = os.path.splitext(file.filename)[1]
    file_name = f"{generate_id()}{file_ext}"
    file_path = os.path.join(Config.UPLOAD_DIR, file_name)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    resize_image(file_path)
    return file_path

def generate_avatar(selected_cards: List[EmotionCard]) -> str:
    # Simple avatar generation by blending dominant colors
    colors = []
    for card in selected_cards:
        colors.extend(card.dominant_colors)
    
    if not colors:
        raise ValueError("No colors available for avatar generation")
    
    # Create a simple gradient avatar
    avatar = np.zeros((300, 300, 3), dtype=np.uint8)
    for i, color in enumerate(colors[:3]):
        start = i * 100
        end = (i + 1) * 100
        avatar[:, start:end] = color
    
    avatar_path = os.path.join(Config.AVATAR_DIR, f"{generate_id()}.png")
    cv2.imwrite(avatar_path, cv2.cvtColor(avatar, cv2.COLOR_RGB2BGR))
    return avatar_path

# Initialize app and directories
app = FastAPI(title="AI Avatar System")
app.mount("/static", StaticFiles(directory=Config.STATIC_DIR), name="static")
init_directories()

# In-memory storage (replace with database in production)
sessions: Dict[str, UserSession] = {}
emotion_cards: List[EmotionCard] = []

# Load initial emotion cards
def load_emotion_cards():
    card_images = [
        "nature.jpg", "abstract.jpg", "city.jpg", 
        "ocean.jpg", "forest.jpg", "space.jpg"
    ]
    
    for img_name in card_images:
        img_path = os.path.join(Config.CARD_DIR, img_name)
        if os.path.exists(img_path):
            colors = get_dominant_colors(img_path)
            card = EmotionCard(
                id=generate_id(),
                image_path=img_path,
                dominant_colors=colors,
                emotion_tags=["calm", "peaceful"]  # Example tags
            )
            emotion_cards.append(card)

load_emotion_cards()

# API Endpoints
@app.post("/api/session/create")
async def create_session():
    session_id = generate_id()
    session = UserSession(
        session_id=session_id,
        selected_cards=[],
        created_at=float(os.time())
    )
    sessions[session_id] = session
    return {"session_id": session_id}

@app.get("/api/cards")
async def get_cards(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Return a random subset of cards
    random.shuffle(emotion_cards)
    return emotion_cards[:Config.MAX_CARDS]

@app.post("/api/cards/select")
async def select_card(session_id: str, card_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    card = next((c for c in emotion_cards if c.id == card_id), None)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    sessions[session_id].selected_cards.append(card)
    return {"status": "success"}

@app.post("/api/avatar/generate")
async def generate_avatar_endpoint(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    if not session.selected_cards:
        raise HTTPException(status_code=400, detail="No cards selected")
    
    try:
        avatar_path = generate_avatar(session.selected_cards)
        session.avatar_path = avatar_path
        return {"avatar_url": f"/static/{os.path.basename(avatar_path)}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload/card")
async def upload_card(file: UploadFile = File(...)):
    try:
        file_path = save_uploaded_file(file)
        colors = get_dominant_colors(file_path)
        
        card = EmotionCard(
            id=generate_id(),
            image_path=file_path,
            dominant_colors=colors,
            emotion_tags=["custom"]  # Can be extended with emotion detection
        )
        emotion_cards.append(card)
        return {"card_id": card.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
