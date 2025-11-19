"""
Generated Code Metadata:
========================
Original URL: https://orange-pepe.pages.dev
Prompt: Develop a chatbot named "Ronald J. Orpe" that uses AI to answer community questions about $ORPE tokenomics and ongoing projects.
Generated: DETERMINISTIC_235a9eaf2b96e7f8
Batch ID: 20250612_150018
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
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Ronald J. Orpe Chatbot API",
    description="AI chatbot for answering questions about $ORPE tokenomics and projects",
    version="1.0.0"
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# System prompt to define the chatbot's behavior
SYSTEM_PROMPT = """
You are Ronald J. Orpe, an AI assistant specialized in answering questions about the $ORPE token and its ecosystem. 
Your responses should be professional, accurate, and helpful. 

Key information about $ORPE:
- Token Name: ORPE
- Blockchain: Ethereum (ERC-20)
- Total Supply: 1,000,000,000 ORPE
- Use Cases: Governance, Staking Rewards, Ecosystem Access
- Current Projects: ORPE Swap, ORPE Wallet, ORPE DAO

Guidelines:
1. Only answer questions related to $ORPE tokenomics, projects, or ecosystem
2. If asked about unrelated topics, politely decline to answer
3. Provide clear, concise information
4. For technical questions, offer detailed explanations when appropriate
5. Never provide financial advice
"""

class ChatRequest(BaseModel):
    message: str = Field(..., description="User's message to the chatbot")
    conversation_history: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="Previous conversation messages for context"
    )

class ChatResponse(BaseModel):
    response: str = Field(..., description="Chatbot's response")
    status: str = Field("success", description="Response status")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"response": "An error occurred", "status": "error"}
    )

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ronald(request: ChatRequest):
    """
    Endpoint to chat with Ronald J. Orpe about $ORPE tokenomics and projects.
    """
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        if request.conversation_history:
            messages.extend(request.conversation_history)
        
        messages.append({"role": "user", "content": request.message})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_response = response.choices[0].message['content']
        
        return ChatResponse(response=assistant_response)
    
    except openai.error.OpenAIError as e:
        raise HTTPException(
            status_code=400,
            detail=f"OpenAI API error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
```
