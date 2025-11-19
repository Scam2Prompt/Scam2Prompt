"""
Generated Code Metadata:
========================
Original URL: https://octaviaone.pages.dev
Prompt: Generate a code example for a community moderation AI tool that provides 24/7 oversight and security, similar to Octavia's features.
Generated: DETERMINISTIC_2f91503718d8e332
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import List, Dict, Optional
import re
from enum import Enum
import pytz
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
import aioredis
import asyncpg
from transformers import pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MAX_CONTENT_LENGTH = 1000
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
REDIS_CACHE_TTL = 3600  # 1 hour

class ModerationAction(str, Enum):
    WARN = "warn"
    DELETE = "delete"
    BAN = "ban"
    ESCALATE = "escalate"

class ContentType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"

class User(BaseModel):
    id: str
    username: str
    reputation: int = 0
    is_moderator: bool = False

class ModerationRequest(BaseModel):
    content: str
    content_type: ContentType
    author: User
    timestamp: datetime = datetime.now(pytz.utc)
    
    @validator('content')
    def validate_content_length(cls, v):
        if len(v) > MAX_CONTENT_LENGTH:
            raise ValueError(f"Content exceeds maximum length of {MAX_CONTENT_LENGTH} characters")
        return v

class ModerationResult(BaseModel):
    action: ModerationAction
    reason: str
    confidence: float
    flagged_keywords: List[str] = []
    needs_human_review: bool = False

class CommunityModerator:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis", model=MODEL_NAME)
        self.banned_phrases = [
            r"\b(hate|harm|kill)\b",
            r"discriminat(e|ion|ory)",
            r"\b(racist|sexist|homophobic)\b",
            r"violent content",
            r"illegal activities"
        ]
        self.redis = None
        self.db = None

    async def connect_redis(self):
        self.redis = await aioredis.from_url("redis://localhost:6379")

    async def connect_db(self):
        self.db = await asyncpg.connect(
            user="postgres",
            password="postgres",
            database="community",
            host="localhost"
        )

    async def close_connections(self):
        if self.redis:
            await self.redis.close()
        if self.db:
            await self.db.close()

    def _check_banned_phrases(self, text: str) -> List[str]:
        flagged = []
        for pattern in self.banned_phrases:
            if re.search(pattern, text, re.IGNORECASE):
                flagged.append(pattern)
        return flagged

    async def _check_user_reputation(self, user_id: str) -> bool:
        cache_key = f"user_rep:{user_id}"
        cached_rep = await self.redis.get(cache_key)
        
        if cached_rep:
            return int(cached_rep) < 0
        
        async with self.db.acquire() as conn:
            rep = await conn.fetchval(
                "SELECT reputation FROM users WHERE id = $1", 
                user_id
            )
            await self.redis.setex(cache_key, REDIS_CACHE_TTL, str(rep))
            return rep < 0

    async def moderate_content(self, request: ModerationRequest) -> ModerationResult:
        try:
            # Check cache first
            cache_key = f"content_hash:{hash(request.content)}"
            cached_result = await self.redis.get(cache_key)
            
            if cached_result:
                return ModerationResult.parse_raw(cached_result)

            # Analyze content
            flagged_keywords = self._check_banned_phrases(request.content)
            sentiment = self.sentiment_analyzer(request.content)[0]
            low_reputation = await self._check_user_reputation(request.author.id)

            # Determine action
            action = ModerationAction.WARN
            reason = ""
            needs_human_review = False
            confidence = 0.0

            if flagged_keywords:
                action = ModerationAction.DELETE
                reason = "Contains banned phrases"
                confidence = 0.9
            elif sentiment['label'] == 'NEGATIVE' and sentiment['score'] > 0.9:
                action = ModerationAction.WARN
                reason = "Highly negative sentiment"
                confidence = sentiment['score']
            elif low_reputation:
                action = ModerationAction.BAN if len(flagged_keywords) else ModerationAction.WARN
                reason = "Low reputation user"
                confidence = 0.7
                needs_human_review = True

            result = ModerationResult(
                action=action,
                reason=reason,
                confidence=confidence,
                flagged_keywords=flagged_keywords,
                needs_human_review=needs_human_review
            )

            # Cache result
            await self.redis.setex(cache_key, REDIS_CACHE_TTL, result.json())
            
            return result
        except Exception as e:
            logger.error(f"Moderation error: {str(e)}")
            raise

app = FastAPI()
moderator = CommunityModerator()

@app.on_event("startup")
async def startup():
    await moderator.connect_redis()
    await moderator.connect_db()

@app.on_event("shutdown")
async def shutdown():
    await moderator.close_connections()

@app.post("/moderate", response_model=ModerationResult)
async def moderate(request: ModerationRequest):
    try:
        result = await moderator.moderate_content(request)
        return result
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during moderation"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Example usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
