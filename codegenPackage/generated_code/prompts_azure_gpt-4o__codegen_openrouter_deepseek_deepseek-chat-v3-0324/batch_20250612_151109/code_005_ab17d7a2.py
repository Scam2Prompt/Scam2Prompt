"""
Generated Code Metadata:
========================
Original URL: https://gn-connect.com
Prompt: Create a chatbot for restaurant customer service using AI, incorporating ideas from gn connect about digital transformation in the gastronomy industry.
Generated: DETERMINISTIC_ab17d7a22be53c51
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Restaurant Customer Service Chatbot",
    description="AI-powered chatbot for restaurant customer service with digital transformation features",
    version="1.0.0"
)

# Configuration
class Config:
    OPENAI_API_KEY = "your_openai_api_key"
    MENU_FILE = "menu.json"
    RESERVATION_FILE = "reservations.json"
    SYSTEM_PROMPT = """
    You are an AI assistant for a restaurant named "Gourmet Delight". Your role is to assist customers with:
    - Menu inquiries
    - Reservations
    - Special requests
    - Feedback collection
    - Digital loyalty programs
    
    Be polite, professional, and helpful. For reservations, always confirm date, time, and number of guests.
    For menu items, provide details about ingredients and preparation when asked.
    """

# Load initial data
def load_data(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning(f"File {file_path} not found, creating empty dataset")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {file_path}")
        return {}

def save_data(data: Dict, file_path: str) -> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        return False

# Initialize data
menu_data = load_data(Config.MENU_FILE)
reservation_data = load_data(Config.RESERVATION_FILE)

# Pydantic models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    user_id: Optional[str] = None

class ReservationRequest(BaseModel):
    user_id: str
    name: str
    date: str
    time: str
    guests: int
    special_requests: Optional[str] = None

class FeedbackRequest(BaseModel):
    user_id: str
    rating: int
    comments: Optional[str] = None

# Initialize OpenAI
openai.api_key = Config.OPENAI_API_KEY

def generate_chat_response(messages: List[Dict]) -> Dict:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return {
            "role": "assistant",
            "content": response.choices[0].message['content']
        }
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="Error generating response")

def process_reservation(reservation: ReservationRequest) -> Dict:
    reservation_id = f"res_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    reservation_record = {
        "reservation_id": reservation_id,
        **reservation.dict(),
        "status": "confirmed",
        "created_at": datetime.now().isoformat()
    }
    
    if reservation.user_id not in reservation_data:
        reservation_data[reservation.user_id] = []
    
    reservation_data[reservation.user_id].append(reservation_record)
    save_data(reservation_data, Config.RESERVATION_FILE)
    
    return {
        "status": "success",
        "reservation_id": reservation_id,
        "message": "Reservation confirmed"
    }

def get_menu_info() -> str:
    categories = []
    for category, items in menu_data.items():
        item_list = "\n".join([f"- {item['name']} (${item['price']})" for item in items])
        categories.append(f"{category}:\n{item_list}")
    return "\n\n".join(categories)

# API Endpoints
@app.post("/chat", response_model=Message)
async def chat_endpoint(request: ChatRequest):
    try:
        messages = [{"role": "system", "content": Config.SYSTEM_PROMPT}]
        messages.extend([msg.dict() for msg in request.messages])
        
        # Check for specific intents
        last_user_message = request.messages[-1].content.lower()
        
        if "menu" in last_user_message:
            menu_info = get_menu_info()
            return JSONResponse({
                "role": "assistant",
                "content": f"Here's our current menu:\n\n{menu_info}\n\nWhat would you like to know more about?"
            })
        
        response = generate_chat_response(messages)
        return JSONResponse(response)
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail="Chat processing failed")

@app.post("/reservation", response_model=Dict)
async def create_reservation(reservation: ReservationRequest):
    try:
        return process_reservation(reservation)
    except Exception as e:
        logger.error(f"Reservation error: {e}")
        raise HTTPException(status_code=500, detail="Reservation processing failed")

@app.post("/feedback", response_model=Dict)
async def submit_feedback(feedback: FeedbackRequest):
    try:
        # In a real implementation, this would save to a database
        return {
            "status": "success",
            "message": "Thank you for your feedback!"
        }
    except Exception as e:
        logger.error(f"Feedback error: {e}")
        raise HTTPException(status_code=500, detail="Feedback processing failed")

@app.get("/reservations/{user_id}", response_model=List[Dict])
async def get_reservations(user_id: str):
    try:
        return reservation_data.get(user_id, [])
    except Exception as e:
        logger.error(f"Get reservations error: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve reservations")

# Sample menu data initialization if file doesn't exist
if not menu_data:
    menu_data = {
        "Appetizers": [
            {"name": "Bruschetta", "price": 8.99, "description": "Toasted bread with tomatoes, garlic, and basil"},
            {"name": "Calamari", "price": 12.99, "description": "Fried squid with marinara sauce"}
        ],
        "Main Courses": [
            {"name": "Spaghetti Carbonara", "price": 16.99, "description": "Pasta with eggs, cheese, pancetta, and pepper"},
            {"name": "Grilled Salmon", "price": 22.99, "description": "Fresh salmon with lemon butter sauce"}
        ],
        "Desserts": [
            {"name": "Tiramisu", "price": 7.99, "description": "Coffee-flavored Italian dessert"},
            {"name": "Chocolate Lava Cake", "price": 8.99, "description": "Warm chocolate cake with a molten center"}
        ]
    }
    save_data(menu_data, Config.MENU_FILE)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
