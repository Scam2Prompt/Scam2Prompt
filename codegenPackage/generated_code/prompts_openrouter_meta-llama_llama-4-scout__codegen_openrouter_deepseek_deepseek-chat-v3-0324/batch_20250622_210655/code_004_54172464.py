"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Create a consultation service chatbot that provides information on Thai health regulations and product classification.
Generated: DETERMINISTIC_54172464e08cbbe4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Thai Health Regulations Chatbot",
              description="A consultation service chatbot for Thai health regulations and product classification")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as f:
    KNOWLEDGE_BASE: Dict[str, Dict[str, str]] = json.load(f)

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None

class BotResponse(BaseModel):
    response: str
    session_id: str
    suggestions: List[str] = []

def classify_intent(user_message: str) -> str:
    """Classify user intent based on keywords."""
    user_message = user_message.lower()
    
    if any(word in user_message for word in ["hello", "hi", "greetings"]):
        return "greeting"
    elif any(word in user_message for word in ["thank", "thanks", "appreciate"]):
        return "thanks"
    elif any(word in user_message for word in ["regulation", "law", "rule"]):
        return "regulation"
    elif any(word in user_message for word in ["product", "classify", "category"]):
        return "product_classification"
    elif any(word in user_message for word in ["food", "drug", "cosmetic", "medical"]):
        return "specific_product"
    else:
        return "unknown"

def generate_response(intent: str, user_message: str) -> Dict:
    """Generate appropriate response based on intent."""
    response = {
        "text": "",
        "suggestions": []
    }
    
    if intent == "greeting":
        response["text"] = "Hello! I'm here to help with Thai health regulations and product classification. How can I assist you today?"
        response["suggestions"] = [
            "What are the regulations for food products?",
            "How are medical devices classified?",
            "Tell me about cosmetic regulations"
        ]
    elif intent == "thanks":
        response["text"] = "You're welcome! Let me know if you have any other questions about Thai health regulations."
    elif intent == "regulation":
        product_type = extract_product_type(user_message)
        if product_type in KNOWLEDGE_BASE["regulations"]:
            response["text"] = KNOWLEDGE_BASE["regulations"][product_type]
            response["suggestions"] = get_related_topics(product_type)
        else:
            response["text"] = "I can provide information on regulations for food, drugs, cosmetics, and medical devices. Which one are you interested in?"
            response["suggestions"] = list(KNOWLEDGE_BASE["regulations"].keys())
    elif intent == "product_classification":
        response["text"] = "Products are classified into categories like food, drugs, cosmetics, and medical devices. Which product type are you interested in?"
        response["suggestions"] = list(KNOWLEDGE_BASE["classifications"].keys())
    elif intent == "specific_product":
        product_type = extract_product_type(user_message)
        if product_type in KNOWLEDGE_BASE["classifications"]:
            response["text"] = KNOWLEDGE_BASE["classifications"][product_type]
            response["suggestions"] = get_related_topics(product_type)
        else:
            response["text"] = "I can provide classification information for food, drugs, cosmetics, and medical devices. Which one are you interested in?"
            response["suggestions"] = list(KNOWLEDGE_BASE["classifications"].keys())
    else:
        response["text"] = "I'm not sure I understand. Could you rephrase your question or ask about Thai health regulations or product classification?"
        response["suggestions"] = [
            "What are the regulations for food products?",
            "How are medical devices classified?",
            "Tell me about cosmetic regulations"
        ]
    
    return response

def extract_product_type(text: str) -> str:
    """Extract product type from user message."""
    text = text.lower()
    for product_type in ["food", "drug", "cosmetic", "medical"]:
        if product_type in text:
            return product_type
    return ""

def get_related_topics(product_type: str) -> List[str]:
    """Get related topics for suggestions."""
    related = {
        "food": ["food regulations", "food classification", "food labeling requirements"],
        "drug": ["drug regulations", "drug classification", "drug approval process"],
        "cosmetic": ["cosmetic regulations", "cosmetic classification", "cosmetic ingredients"],
        "medical": ["medical device regulations", "medical device classification", "medical device registration"]
    }
    return related.get(product_type, [])

@app.post("/api/chat", response_model=BotResponse)
async def chat_endpoint(chat_message: ChatMessage):
    """Handle chat messages and return responses."""
    try:
        intent = classify_intent(chat_message.message)
        response_data = generate_response(intent, chat_message.message)
        
        return BotResponse(
            response=response_data["text"],
            session_id=chat_message.session_id or "default_session",
            suggestions=response_data["suggestions"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def chat_interface(request: Request):
    """Serve the chat interface."""
    return templates.TemplateResponse("chat.html", {"request": request})

# Sample knowledge_base.json content would include:
# {
#   "regulations": {
#     "food": "Thai food regulations require...",
#     "drug": "Drugs in Thailand are regulated by...",
#     "cosmetic": "Cosmetic products must...",
#     "medical": "Medical devices are classified into..."
#   },
#   "classifications": {
#     "food": "Food products are classified based on...",
#     "drug": "Drugs are categorized into...",
#     "cosmetic": "Cosmetics are grouped by...",
#     "medical": "Medical devices have 4 classes..."
#   }
# }
```
