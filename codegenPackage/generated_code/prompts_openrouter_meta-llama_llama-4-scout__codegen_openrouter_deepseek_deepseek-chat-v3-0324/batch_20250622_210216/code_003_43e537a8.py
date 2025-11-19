"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-ai.web.app
Prompt: Design a high-level architecture for a crypto companion chatbot, like ScottyChat, using AI and natural language processing (NLP) techniques.
Generated: DETERMINISTIC_43e537a8fc2b2017
Batch ID: 20250622_210216
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
from abc import ABC, abstractmethod

import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Crypto Companion Chatbot API",
    description="AI-powered chatbot for cryptocurrency assistance",
    version="1.0.0"
)

# Configuration
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "gpt-4"  # or "gpt-3.5-turbo" for cost efficiency
    TEMPERATURE = 0.7
    MAX_TOKENS = 1000
    CRYPTO_KNOWLEDGE_BASE = "data/crypto_knowledge.json"

# Data Models
class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender (user/assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., description="List of chat messages")
    user_id: Optional[str] = Field(None, description="Unique user identifier")

class ChatResponse(BaseModel):
    message: ChatMessage = Field(..., description="Assistant's response message")
    status: str = Field("success", description="Response status")

# Knowledge Base Interface
class KnowledgeBase(ABC):
    @abstractmethod
    def get_crypto_info(self, query: str) -> Optional[Dict]:
        pass

class JSONKnowledgeBase(KnowledgeBase):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load knowledge base: {str(e)}")

    def get_crypto_info(self, query: str) -> Optional[Dict]:
        return self.data.get(query.lower(), None)

# Chatbot Core
class CryptoChatbot:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base
        openai.api_key = Config.OPENAI_API_KEY

    def _generate_prompt(self, messages: List[ChatMessage]) -> str:
        conversation = "\n".join([f"{msg.role}: {msg.content}" for msg in messages])
        return f"""
        You are ScottyChat, a knowledgeable cryptocurrency assistant. 
        Your goal is to provide accurate, helpful information about cryptocurrencies, 
        blockchain technology, and related topics.

        Current conversation:
        {conversation}

        Assistant:
        """

    async def generate_response(self, messages: List[ChatMessage]) -> ChatMessage:
        try:
            prompt = self._generate_prompt(messages)
            
            response = openai.ChatCompletion.create(
                model=Config.MODEL_NAME,
                messages=[{"role": msg.role, "content": msg.content} for msg in messages],
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS
            )

            return ChatMessage(
                role="assistant",
                content=response.choices[0].message.content.strip()
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to generate response: {str(e)}"
            )

# API Endpoints
knowledge_base = JSONKnowledgeBase(Config.CRYPTO_KNOWLEDGE_BASE)
chatbot = CryptoChatbot(knowledge_base)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = await chatbot.generate_response(request.messages)
        return ChatResponse(message=response)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": str(exc)}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
