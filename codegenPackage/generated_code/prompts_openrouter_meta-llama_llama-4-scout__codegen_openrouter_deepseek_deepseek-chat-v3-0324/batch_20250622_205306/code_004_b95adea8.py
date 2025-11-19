"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Create a chatbot that provides franchise consulting services, using the knowledge and expertise of Franchise Teacher's team.
Generated: DETERMINISTIC_b95adea8fccb1590
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import os
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Franchise Consulting Chatbot",
    description="AI-powered chatbot providing franchise consulting services",
    version="1.0.0"
)

# Configuration
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-4"
    MAX_TOKENS = 1500
    TEMPERATURE = 0.7
    SYSTEM_PROMPT = """
    You are FranchiseGPT, an AI assistant providing expert franchise consulting services 
    based on the knowledge and expertise of Franchise Teacher's team. Your responses 
    should be professional, informative, and tailored to help clients make informed 
    franchise decisions. Focus on areas like franchise selection, investment analysis, 
    legal considerations, operations, and growth strategies. Always be clear about 
    what you know and what might require consultation with human experts.
    """

# Pydantic models
class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender (user/assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., description="List of chat messages")
    session_id: Optional[str] = Field(None, description="Session ID for continuity")

class ChatResponse(BaseModel):
    response: str = Field(..., description="Assistant's response")
    session_id: Optional[str] = Field(None, description="Session ID for continuity")

# Initialize OpenAI client
openai.api_key = Config.OPENAI_API_KEY

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Franchise Consulting Chatbot Service")
    if not Config.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not set")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred. Please try again later."}
    )

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main endpoint for franchise consulting chat.
    Processes user messages and returns AI responses.
    """
    try:
        if not request.messages:
            raise HTTPException(status_code=400, detail="No messages provided")
        
        # Prepare messages for OpenAI API
        messages = [{"role": "system", "content": Config.SYSTEM_PROMPT}]
        for msg in request.messages:
            messages.append({"role": msg.role, "content": msg.content})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model=Config.OPENAI_MODEL,
            messages=messages,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS
        )
        
        assistant_response = response.choices[0].message.content
        
        return ChatResponse(
            response=assistant_response,
            session_id=request.session_id
        )
        
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing your request with the AI service")
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
