"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Provide a code example for creating a secure API bridge based on the structure outlined in `api_secure_bridge`.
Generated: DETERMINISTIC_bec7f944602f96e3
Batch ID: 20250612_155057
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
import logging
from functools import wraps
from typing import Callable, Any, Dict, Optional
from datetime import datetime, timedelta
import secrets
import hashlib
import hmac
import base64
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Security constants
API_KEY_HEADER = "X-API-Key"
HMAC_HEADER = "X-HMAC-Signature"
TIMESTAMP_HEADER = "X-Timestamp"
TOKEN_EXPIRATION_MINUTES = 30
HMAC_SECRET = os.getenv("HMAC_SECRET", secrets.token_hex(32))
API_KEYS = {
    os.getenv("API_KEY_1", "default_key_1"): {"name": "client_1", "permissions": ["read", "write"]},
    os.getenv("API_KEY_2", "default_key_2"): {"name": "client_2", "permissions": ["read"]}
}

# Models
class RequestModel(BaseModel):
    data: Dict[str, Any]

class ResponseModel(BaseModel):
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None

# Security utils
def generate_hmac_signature(data: str, secret: str) -> str:
    """Generate HMAC signature for data."""
    hmac_obj = hmac.new(secret.encode(), data.encode(), hashlib.sha256)
    return base64.b64encode(hmac_obj.digest()).decode()

def validate_timestamp(timestamp: str) -> bool:
    """Validate request timestamp is within allowed window."""
    try:
        request_time = datetime.fromisoformat(timestamp)
        current_time = datetime.utcnow()
        time_diff = current_time - request_time
        return time_diff <= timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    except (ValueError, TypeError):
        return False

# Security dependencies
class HMACAuth(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        return credentials

def api_key_auth(api_key: str = Depends(HTTPBearer())) -> Dict[str, Any]:
    """Validate API key and return client info."""
    if api_key.credentials not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return API_KEYS[api_key.credentials]

def hmac_auth(request: Request) -> None:
    """Validate HMAC signature."""
    try:
        timestamp = request.headers[TIMESTAMP_HEADER]
        hmac_signature = request.headers[HMAC_HEADER]
        body = request.body().decode()
        
        if not validate_timestamp(timestamp):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Expired timestamp"
            )
        
        expected_signature = generate_hmac_signature(f"{timestamp}{body}", HMAC_SECRET)
        if not hmac.compare_digest(hmac_signature, expected_signature):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid HMAC signature"
            )
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing required header: {e}"
        )

# Decorators
def secure_endpoint(func: Callable) -> Callable:
    """Decorator to secure API endpoints with HMAC and API key auth."""
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        try:
            hmac_auth(request)
            return await func(request, *args, **kwargs)
        except HTTPException as e:
            logger.error(f"Security error: {e.detail}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )
    return wrapper

# API setup
app = FastAPI(
    title="Secure API Bridge",
    description="A secure API bridge with HMAC and API key authentication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

# Example endpoint
@app.post("/api/process", response_model=ResponseModel)
@secure_endpoint
async def process_data(
    request: Request,
    payload: RequestModel,
    client_info: Dict[str, Any] = Depends(api_key_auth)
) -> JSONResponse:
    """Process data with authentication and validation."""
    try:
        # Business logic here
        processed_data = {"processed": True, "input": payload.data}
        
        return JSONResponse(
            content={
                "status": "success",
                "message": "Data processed successfully",
                "data": processed_data
            },
            status_code=status.HTTP_200_OK
        )
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid request data"
        )
    except Exception as e:
        logger.error(f"Processing error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process data"
        )

# Health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
