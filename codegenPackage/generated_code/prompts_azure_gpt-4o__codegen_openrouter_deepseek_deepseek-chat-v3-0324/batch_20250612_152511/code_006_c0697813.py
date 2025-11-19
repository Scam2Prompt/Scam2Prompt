"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Develop a chatbot prototype for nonprofit organizations in emerging economies to assist with digital-first fundraising, inspired by Emerging Gifts' approach.
Generated: DETERMINISTIC_c0697813a6a591e1
Batch ID: 20250612_152511
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
    title="Nonprofit Fundraising Chatbot",
    description="AI assistant for digital-first fundraising in emerging economies",
    version="0.1.0"
)

# Configuration
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-3.5-turbo"
    TEMPERATURE = 0.7
    MAX_TOKENS = 500
    SYSTEM_PROMPT = """
    You are a helpful fundraising assistant for nonprofit organizations in emerging economies. 
    Your goal is to help organizations with digital-first fundraising strategies, donor engagement, 
    and campaign optimization. Be supportive, culturally aware, and provide practical advice 
    suitable for resource-constrained environments.
    """

# Validate configuration
if not Config.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Initialize OpenAI client
openai.api_key = Config.OPENAI_API_KEY

# Data models
class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender (user/assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., description="List of chat messages")
    organization_context: Optional[Dict[str, str]] = Field(
        None,
        description="Context about the nonprofit organization"
    )

class ChatResponse(BaseModel):
    message: ChatMessage = Field(..., description="Assistant's response message")
    suggestions: List[str] = Field(..., description="Suggested follow-up questions")

# Error handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."}
    )

# Helper functions
def generate_suggestions() -> List[str]:
    """Generate suggested follow-up questions"""
    return [
        "How can I improve my online donation page?",
        "What are low-cost digital fundraising ideas?",
        "How do I engage first-time donors?",
        "What metrics should I track for my campaign?"
    ]

def build_prompt(messages: List[ChatMessage], context: Optional[Dict[str, str]]) -> List[Dict[str, str]]:
    """Build the conversation prompt for the AI model"""
    prompt = [{"role": "system", "content": Config.SYSTEM_PROMPT}]
    
    if context:
        org_info = "\n".join(f"{k}: {v}" for k, v in context.items())
        prompt.append({
            "role": "system",
            "content": f"Organization context:\n{org_info}"
        })
    
    prompt.extend([{"role": msg.role, "content": msg.content} for msg in messages])
    return prompt

# API endpoints
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main chat endpoint that handles conversations with the fundraising assistant.
    """
    try:
        prompt = build_prompt(request.messages, request.organization_context)
        
        response = openai.ChatCompletion.create(
            model=Config.OPENAI_MODEL,
            messages=prompt,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS
        )
        
        assistant_message = response.choices[0].message.content
        
        return ChatResponse(
            message=ChatMessage(
                role="assistant",
                content=assistant_message
            ),
            suggestions=generate_suggestions()
        )
        
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail="Service temporarily unavailable. Please try again later."
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
