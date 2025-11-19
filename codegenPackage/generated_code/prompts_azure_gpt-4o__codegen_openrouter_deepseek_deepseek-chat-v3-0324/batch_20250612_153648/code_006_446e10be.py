"""
Generated Code Metadata:
========================
Original URL: https://cyberlamas.pages.dev
Prompt: Provide Python code for collecting user feedback on AI-generated NFTs and using it to improve AI models, inspired by Cyber Lama AI's testing phase.
Generated: DETERMINISTIC_446e10be948bcd64
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import uuid
import logging
from fastapi import FastAPI, HTTPException, Request, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI NFT Feedback System",
    description="System for collecting user feedback on AI-generated NFTs to improve models",
    version="1.0.0"
)

# Constants
FEEDBACK_DIR = "feedback_data"
MODEL_DIR = "models"
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
MIN_RATING = 1
MAX_RATING = 5

# Ensure directories exist
os.makedirs(FEEDBACK_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

class NFTFeedback(BaseModel):
    """Model for NFT feedback data."""
    nft_id: str = Field(..., description="Unique identifier for the NFT")
    user_id: str = Field(..., description="Anonymous user identifier")
    rating: int = Field(..., description="Rating from 1 to 5", ge=MIN_RATING, le=MAX_RATING)
    feedback_text: Optional[str] = Field(None, description="Optional detailed feedback")
    improvement_suggestions: Optional[str] = Field(None, description="Suggestions for improvement")
    model_version: str = Field(..., description="Version of the AI model that generated the NFT")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Feedback submission time")

    @validator('nft_id', 'user_id', 'model_version')
    def validate_string_fields(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value

class ModelTrainingRequest(BaseModel):
    """Model for triggering model retraining."""
    model_version: str = Field(..., description="Current model version to improve")
    epochs: int = Field(5, description="Number of training epochs", ge=1, le=100)
    batch_size: int = Field(32, description="Training batch size", ge=8, le=128)

def preprocess_image(image: UploadFile) -> np.ndarray:
    """Preprocess uploaded image for model input."""
    try:
        img = Image.open(image.file)
        img = img.convert("RGB")
        img = img.resize((256, 256))
        img_array = np.array(img) / 255.0
        return np.expand_dims(img_array, axis=0)
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        raise HTTPException(status_code=400, detail="Invalid image file")

def save_feedback(feedback: NFTFeedback) -> str:
    """Save feedback to a JSON file."""
    try:
        feedback_id = str(uuid.uuid4())
        file_path = os.path.join(FEEDBACK_DIR, f"{feedback_id}.json")
        
        with open(file_path, "w") as f:
            json.dump(feedback.dict(), f, default=str)
        
        logger.info(f"Feedback saved: {feedback_id}")
        return feedback_id
    except Exception as e:
        logger.error(f"Error saving feedback: {e}")
        raise HTTPException(status_code=500, detail="Failed to save feedback")

def load_feedback_data() -> List[Dict]:
    """Load all feedback data from storage."""
    feedback_data = []
    for filename in os.listdir(FEEDBACK_DIR):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(FEEDBACK_DIR, filename), "r") as f:
                    feedback_data.append(json.load(f))
            except Exception as e:
                logger.warning(f"Error loading feedback file {filename}: {e}")
    return feedback_data

def prepare_training_data(feedback_data: List[Dict]) -> Tuple[np.ndarray, np.ndarray]:
    """Prepare training data from feedback."""
    # In a real implementation, this would process the feedback
    # and prepare appropriate training data
    # Placeholder implementation
    X = np.random.rand(len(feedback_data), 256, 256, 3)
    y = np.array([f['rating'] for f in feedback_data])
    return X, y

def train_model(model_version: str, epochs: int, batch_size: int) -> str:
    """Retrain the AI model based on collected feedback."""
    try:
        feedback_data = load_feedback_data()
        if not feedback_data:
            raise ValueError("No feedback data available for training")
        
        X, y = prepare_training_data(feedback_data)
        
        # Load existing model
        model_path = os.path.join(MODEL_DIR, f"{model_version}.h5")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model {model_version} not found")
        
        model = load_model(model_path)
        
        # Train model (simplified example)
        model.fit(X, y, epochs=epochs, batch_size=batch_size, validation_split=0.2)
        
        # Save new model version
        new_version = f"{model_version}_v{len(feedback_data)}"
        new_model_path = os.path.join(MODEL_DIR, f"{new_version}.h5")
        model.save(new_model_path)
        
        logger.info(f"Model trained and saved as {new_version}")
        return new_version
    except Exception as e:
        logger.error(f"Error during model training: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/submit-feedback", response_model=Dict[str, str])
async def submit_feedback(feedback: NFTFeedback):
    """Endpoint for submitting NFT feedback."""
    try:
        feedback_id = save_feedback(feedback)
        return {"status": "success", "feedback_id": feedback_id}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in submit_feedback: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/evaluate-nft")
async def evaluate_nft(
    image: UploadFile,
    model_version: str = Form(...),
    user_id: str = Form(...)
):
    """Endpoint for evaluating an AI-generated NFT."""
    try:
        if image.content_type not in ALLOWED_IMAGE_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported image type")
        
        # Load model
        model_path = os.path.join(MODEL_DIR, f"{model_version}.h5")
        if not os.path.exists(model_path):
            raise HTTPException(status_code=404, detail="Model version not found")
        
        model = load_model(model_path)
        
        # Preprocess and predict
        img_array = preprocess_image(image)
        prediction = model.predict(img_array)
        
        # Generate NFT ID
        nft_id = str(uuid.uuid4())
        
        return {
            "nft_id": nft_id,
            "model_version": model_version,
            "prediction": prediction.tolist(),
            "user_id": user_id
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in evaluate_nft: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/retrain-model", response_model=Dict[str, str])
async def retrain_model(request: ModelTrainingRequest):
    """Endpoint for triggering model retraining."""
    try:
        new_version = train_model(
            model_version=request.model_version,
            epochs=request.epochs,
            batch_size=request.batch_size
        )
        return {"status": "success", "new_model_version": new_version}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in retrain_model: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/feedback-stats", response_model=Dict[str, float])
async def get_feedback_stats():
    """Endpoint for getting feedback statistics."""
    try:
        feedback_data = load_feedback_data()
        if not feedback_data:
            return {"average_rating": 0.0, "feedback_count": 0}
        
        ratings = [f["rating"] for f in feedback_data]
        return {
            "average_rating": float(np.mean(ratings)),
            "feedback_count": len(feedback_data)
        }
    except Exception as e:
        logger.error(f"Error in get_feedback_stats: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
