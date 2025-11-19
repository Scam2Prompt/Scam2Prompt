"""
Generated Code Metadata:
========================
Original URL: https://futureforai.com
Prompt: Generate code to create a conversational search engine inspired by Perplexity AI, as discussed on Future For AI.
Generated: DETERMINISTIC_68c3d402bae44400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import openai
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
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
    title="Conversational Search Engine API",
    description="API for a Perplexity AI-inspired conversational search engine",
    version="0.1.0"
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Models
class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ConversationRequest(BaseModel):
    messages: List[Message]
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 1000
    temperature: float = 0.7

class SearchResponse(BaseModel):
    answer: str
    sources: List[str]
    conversation_id: Optional[str] = None

# Utility functions
def validate_messages(messages: List[Message]) -> bool:
    """Validate the conversation history structure."""
    if not messages:
        return False
    
    # Check roles alternate properly
    for i, msg in enumerate(messages):
        if msg.role not in ["user", "assistant"]:
            return False
        if i > 0 and msg.role == messages[i-1].role:
            return False
    
    return True

def generate_search_query(messages: List[Message]) -> str:
    """Generate a search query from conversation context."""
    last_user_message = next(
        (msg.content for msg in reversed(messages) if msg.role == "user"),
        ""
    )
    return f"Based on this conversation: {last_user_message}"

def extract_sources(response: Dict) -> List[str]:
    """Extract sources from OpenAI response if available."""
    if "citations" in response:
        return response["citations"]
    return []

# API Endpoints
@app.post("/search", response_model=SearchResponse)
async def conversational_search(request: ConversationRequest):
    """
    Perform a conversational search based on the message history.
    Returns an answer along with any sources/references.
    """
    try:
        # Validate input
        if not validate_messages(request.messages):
            raise HTTPException(
                status_code=400,
                detail="Invalid message format. Messages must alternate between user and assistant."
            )

        # Generate completion
        response = openai.ChatCompletion.create(
            model=request.model,
            messages=[m.dict() for m in request.messages],
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )

        if not response.choices:
            raise HTTPException(
                status_code=500,
                detail="No response generated from the model"
            )

        answer = response.choices[0].message.content
        sources = extract_sources(response)

        return SearchResponse(
            answer=answer,
            sources=sources,
            conversation_id=None  # In a real implementation, you'd track conversation IDs
        )

    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing your request: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Main entry point (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
