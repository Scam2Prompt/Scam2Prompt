"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Recommend a framework for building a secure backend system for handling high-volume transactions in cryptocurrency, tailored for platforms like BaxBet.
Generated: DETERMINISTIC_ff31ff8f92ff470e
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

The following code demonstrates how to use the Python framework **FastAPI** for building a secure backend system to handle high-volume cryptocurrency transactions. FastAPI is chosen due to its performance, security features, and scalability. The example includes secure endpoints, rate limiting, input validation, and logging.

```python
# main.py
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, Field
from typing import Dict
import logging
import time
from redis import Redis
from functools import lru_cache
from dotenv import dotenv_values
import hashlib

# Load configuration from .env file
config = dotenv_values(".env")

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize Redis for rate limiting
redis_client = Redis(host="localhost", port=6379, decode_responses=True)

# FastAPI instance
app = FastAPI(title="Crypto Transaction Backend", version="1.0.0")

# API Key for authentication
API_KEY_NAME = "X-API-KEY"
API_KEY = config["API_KEY"]
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Error messages
ERROR_RATE_LIMIT = "Rate limit exceeded. Please try again later."
ERROR_INVALID_API_KEY = "Invalid API key."

# Transaction model for input validation
class Transaction(BaseModel):
    sender: str = Field(..., regex=r"^[a-zA-Z0-9]{42}$", description="Sender's wallet address (42 characters alphanumeric)")
    receiver: str = Field(..., regex=r"^[a-zA-Z0-9]{42}$", description="Receiver's wallet address (42 characters alphanumeric)")
    amount: float = Field(..., gt=0, description="Amount to be transferred (must be greater than 0)")
    currency: str = Field(..., regex=r"^[A-Z]{3}$", description="Currency code (e.g., BTC, ETH)")

# Dependency for API key validation
def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        logger.warning("Unauthorized access attempt detected.")
        raise HTTPException(status_code=403, detail=ERROR_INVALID_API_KEY)

# Rate limiting decorator
def rate_limit(key_prefix: str, limit: int, duration: int):
    """
    Rate limiting based on Redis.
    :param key_prefix: Prefix for Redis key (e.g., API key or IP address).
    :param limit: Number of allowed requests.
    :param duration: Time window in seconds.
    """
    def wrapper(func):
        async def inner(*args, **kwargs):
            key = f"{key_prefix}:{int(time.time()) // duration}"
            current_count = redis_client.get(key)

            if current_count and int(current_count) >= limit:
                logger.warning(f"Rate limit exceeded for key: {key_prefix}")
                raise HTTPException(status_code=429, detail=ERROR_RATE_LIMIT)

            redis_client.incr(key)
            redis_client.expire(key, duration)
            return await func(*args, **kwargs)
        return inner
    return wrapper

# Transaction endpoint
@app.post("/transaction", dependencies=[Depends(validate_api_key)])
@rate_limit(key_prefix="transaction", limit=int(config["TRANSACTION_RATE_LIMIT"]), duration=60)
async def create_transaction(transaction: Transaction) -> Dict[str, str]:
    """
    Process cryptocurrency transaction.
    :param transaction: Transaction details provided by the user.
    :return: Confirmation message with transaction ID.
    """
    logger.info(f"Processing transaction: {transaction}")
    
    # Simulate transaction ID generation using hashing
    transaction_id = hashlib.sha256(
        f"{transaction.sender}{transaction.receiver}{transaction.amount}{transaction.currency}{time.time()}".encode()
    ).hexdigest()

    # Simulate storing transaction in database (e.g., logging here for simplicity)
    logger.info(f"Transaction {transaction_id} created: {transaction}")

    return {"transaction_id": transaction_id, "status": "Transaction successful"}

@app.get("/")
async def health_check():
    """
    Health check endpoint.
    :return: Health status of the API.
    """
    logger.info("Health check performed.")
    return {"status": "API is running"}

# Middleware for secure headers
@app.middleware("http")
async def add_security_headers(request, call_next):
    """
    Add secure headers to all responses.
    """
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

# .env file (example)
"""
API_KEY=your_secure_api_key_here
TRANSACTION_RATE_LIMIT=100
"""

# Requirements file for dependencies (requirements.txt)
"""
fastapi==0.89.0
uvicorn==0.22.0
python-dotenv==1.0.0
redis==4.6.0
"""

# Instructions to run:
# 1. Install dependencies: `pip install -r requirements.txt`
# 2. Start Redis server.
# 3. Run the FastAPI app: `uvicorn main:app --reload`
# 4. Use an API client (e.g., Postman) to test the endpoints.
```

This code snippet includes security features, rate limiting, input validation, and logging, ensuring it’s suitable for high-volume transaction systems.
