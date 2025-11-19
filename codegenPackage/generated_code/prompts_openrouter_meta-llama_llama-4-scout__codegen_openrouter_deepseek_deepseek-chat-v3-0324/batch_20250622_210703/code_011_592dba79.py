"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Develop a chatbot to provide information about the services and programs offered by جمعية التنمية الأهلية بتبوك, using a natural language processing (NLP) library.
Generated: DETERMINISTIC_592dba7900c57ad6
Batch ID: 20250622_210703
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
import spacy
from spacy.matcher import PhraseMatcher
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize FastAPI app
app = FastAPI(
    title="Tabuk Community Development Association Chatbot",
    description="A chatbot to provide information about services and programs offered by جمعية التنمية الأهلية بتبوك",
    version="1.0.0"
)

# Knowledge base containing information about services and programs
KNOWLEDGE_BASE = {
    "education": {
        "description": "We offer educational programs including literacy classes, vocational training, and scholarship opportunities.",
        "contact": "education@tabuk-cda.org"
    },
    "health": {
        "description": "Our health services include free medical checkups, awareness campaigns, and mobile clinics.",
        "contact": "health@tabuk-cda.org"
    },
    "social": {
        "description": "Social programs include family counseling, youth development initiatives, and community events.",
        "contact": "social@tabuk-cda.org"
    },
    "employment": {
        "description": "Employment services include job training, career counseling, and job placement assistance.",
        "contact": "employment@tabuk-cda.org"
    },
    "general": {
        "description": "جمعية التنمية الأهلية بتبوك is a community development association offering various programs in education, health, social services, and employment.",
        "contact": "info@tabuk-cda.org"
    }
}

# Initialize phrase matcher
matcher = PhraseMatcher(nlp.vocab)
phrases = ["education", "health", "social", "employment", "help", "programs", "services"]
patterns = [nlp(text) for text in phrases]
matcher.add("SERVICES", patterns)

class ChatRequest(BaseModel):
    message: str
    language: str = "en"

class ChatResponse(BaseModel):
    response: str
    relevant_service: Optional[str] = None
    contact: Optional[str] = None

def process_message(message: str) -> Dict:
    """
    Process user message and return appropriate response.
    """
    doc = nlp(message.lower())
    matches = matcher(doc)
    
    found_services = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        found_services.add(span.text)
    
    # Determine the most relevant service
    if not found_services:
        return {
            "response": KNOWLEDGE_BASE["general"]["description"],
            "relevant_service": "general",
            "contact": KNOWLEDGE_BASE["general"]["contact"]
        }
    
    # Prioritize services based on order in KNOWLEDGE_BASE
    for service in KNOWLEDGE_BASE:
        if service in found_services:
            return {
                "response": KNOWLEDGE_BASE[service]["description"],
                "relevant_service": service,
                "contact": KNOWLEDGE_BASE[service]["contact"]
            }
    
    # Fallback response
    return {
        "response": "I couldn't find specific information about your query. Please contact info@tabuk-cda.org for more assistance.",
        "relevant_service": None,
        "contact": "info@tabuk-cda.org"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main endpoint for chatbot interactions.
    """
    try:
        response_data = process_message(request.message)
        return ChatResponse(**response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler for the API.
    """
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred while processing your request."}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
