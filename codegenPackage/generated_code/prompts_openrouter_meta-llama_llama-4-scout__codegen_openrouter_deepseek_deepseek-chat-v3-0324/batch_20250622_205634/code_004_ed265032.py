"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Create a cryptocurrency support chatbot using natural language processing (NLP) techniques, considering Arcler Desk's cryptocurrency support solutions.
Generated: DETERMINISTIC_ed265032955646c6
Batch ID: 20250622_205634
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
import numpy as np
from typing import Dict, List, Optional
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Load spaCy model for NLP processing
nlp = spacy.load("en_core_web_md")

# Initialize FastAPI app
app = FastAPI(
    title="Cryptocurrency Support Chatbot",
    description="A chatbot providing support for cryptocurrency-related queries using NLP techniques.",
    version="1.0.0"
)

# Configuration
class Config:
    CRYPTO_API_URL = "https://api.coingecko.com/api/v3"
    SUPPORT_KB_FILE = "support_knowledge_base.json"
    SIMILARITY_THRESHOLD = 0.7

# Data models
class UserQuery(BaseModel):
    text: str

class BotResponse(BaseModel):
    response: str
    confidence: float
    suggested_actions: Optional[List[str]] = None

# Knowledge base loader
class KnowledgeBase:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.knowledge_base = self._load_knowledge_base()
        self._train_vectorizer()

    def _load_knowledge_base(self) -> Dict:
        try:
            with open(Config.SUPPORT_KB_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Knowledge base file {Config.SUPPORT_KB_FILE} not found")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON format in {Config.SUPPORT_KB_FILE}")

    def _train_vectorizer(self):
        all_questions = [item['question'] for item in self.knowledge_base['intents']]
        self.vectorizer.fit(all_questions)

    def get_response(self, query: str) -> Dict:
        query_vec = self.vectorizer.transform([query])
        questions = [item['question'] for item in self.knowledge_base['intents']]
        question_vecs = self.vectorizer.transform(questions)
        
        similarities = cosine_similarity(query_vec, question_vecs)
        max_index = np.argmax(similarities)
        max_similarity = similarities[0, max_index]
        
        if max_similarity < Config.SIMILARITY_THRESHOLD:
            return {
                "response": "I'm sorry, I don't understand your question. Could you rephrase it?",
                "confidence": max_similarity,
                "suggested_actions": ["Contact support", "Browse help center"]
            }
        
        best_match = self.knowledge_base['intents'][max_index]
        return {
            "response": best_match['answer'],
            "confidence": max_similarity,
            "suggested_actions": best_match.get('actions', [])
        }

# Crypto price fetcher
class CryptoPriceFetcher:
    @staticmethod
    def get_price(crypto_id: str) -> Optional[float]:
        try:
            response = requests.get(
                f"{Config.CRYPTO_API_URL}/simple/price",
                params={
                    'ids': crypto_id,
                    'vs_currencies': 'usd'
                }
            )
            response.raise_for_status()
            data = response.json()
            return data.get(crypto_id, {}).get('usd')
        except requests.RequestException:
            return None

# Chatbot service
class ChatbotService:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.price_fetcher = CryptoPriceFetcher()

    def process_query(self, query_text: str) -> BotResponse:
        # Extract entities using spaCy
        doc = nlp(query_text)
        
        # Check for cryptocurrency price queries
        crypto_entities = [ent.text.lower() for ent in doc.ents if ent.label_ == "CRYPTO"]
        if crypto_entities and any(word in query_text.lower() for word in ['price', 'value', 'worth']):
            crypto_id = crypto_entities[0]
            price = self.price_fetcher.get_price(crypto_id)
            if price:
                return BotResponse(
                    response=f"The current price of {crypto_id} is ${price:.2f} USD.",
                    confidence=1.0,
                    suggested_actions=[f"View {crypto_id} chart", "Compare prices"]
                )
        
        # Fall back to knowledge base
        kb_response = self.kb.get_response(query_text)
        return BotResponse(
            response=kb_response['response'],
            confidence=kb_response['confidence'],
            suggested_actions=kb_response['suggested_actions']
        )

# API endpoints
@app.post("/query", response_model=BotResponse)
async def handle_query(query: UserQuery):
    try:
        chatbot = ChatbotService()
        return chatbot.process_query(query.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
