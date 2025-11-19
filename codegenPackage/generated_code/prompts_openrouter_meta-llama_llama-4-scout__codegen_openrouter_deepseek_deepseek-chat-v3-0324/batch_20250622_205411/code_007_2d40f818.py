"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Develop a chatbot that provides guidance on vibrational catalysis and holographic architecture, using the website's content as a knowledge base.
Generated: DETERMINISTIC_2d40f8187f58ee35
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Vibrational Catalysis & Holographic Architecture Chatbot")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Load knowledge base
KNOWLEDGE_BASE_PATH = "knowledge_base.json"

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str

def load_knowledge_base() -> Dict:
    """Load the knowledge base from JSON file."""
    try:
        with open(KNOWLEDGE_BASE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Knowledge base not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid knowledge base format")

def get_context_from_knowledge_base(query: str) -> str:
    """Retrieve relevant context from knowledge base."""
    knowledge_base = load_knowledge_base()
    # Simple keyword matching - could be enhanced with vector search
    context = []
    for topic, content in knowledge_base.items():
        if query.lower() in topic.lower() or any(q in content.lower() for q in query.lower().split()):
            context.append(f"{topic}: {content}")
    return "\n\n".join(context) if context else "No specific information found in knowledge base."

def generate_chat_response(prompt: str, context: str, conversation_id: str) -> ChatResponse:
    """Generate response using OpenAI API with context."""
    try:
        system_message = (
            "You are an expert assistant specializing in vibrational catalysis "
            "and holographic architecture. Provide detailed, accurate responses "
            "based on the provided context. If unsure, say you don't know."
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return ChatResponse(
            response=response.choices[0].message.content,
            conversation_id=conversation_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the chat interface."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    """Handle chat requests."""
    if not chat_request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    context = get_context_from_knowledge_base(chat_request.message)
    conversation_id = chat_request.conversation_id or "default_conversation"
    
    return generate_chat_response(
        prompt=chat_request.message,
        context=context,
        conversation_id=conversation_id
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
