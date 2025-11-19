"""
Generated Code Metadata:
========================
Original URL: https://securedintegration.com
Prompt: Suggest best practices for implementing security measures like OAuth 2.0 and TLS/HTTPS in a multi-platform integration tool for meetings and calendars, as outlined by Secured Integration.
Generated: DETERMINISTIC_4a8fcb9a1a9e97e8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ssl
from typing import Optional, Dict, Any
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    # OAuth 2.0 Configuration
    oauth_client_id: str
    oauth_client_secret: str
    oauth_authorization_url: AnyHttpUrl
    oauth_token_url: AnyHttpUrl
    oauth_redirect_url: AnyHttpUrl
    oauth_scopes: Dict[str, str] = {
        "meetings": "Read and write meetings",
        "calendar": "Read and write calendar events"
    }
    
    # TLS Configuration
    tls_cert_path: Optional[str] = None
    tls_key_path: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()

# Initialize FastAPI app
app = FastAPI(
    title="Secured Integration API",
    description="Multi-platform integration tool for meetings and calendars with OAuth 2.0 and TLS security",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

# Force HTTPS in production
if os.getenv("ENVIRONMENT") == "production":
    app.add_middleware(HTTPSRedirectMiddleware)

# OAuth2 Scheme
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=str(settings.oauth_authorization_url),
    tokenUrl=str(settings.oauth_token_url),
    scopes=settings.oauth_scopes
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real implementation, validate the token with your OAuth provider
    # This is a simplified example
    return {"user_id": "example_user", "scopes": token.scopes}

@app.on_event("startup")
async def startup_event():
    # Validate TLS configuration in production
    if os.getenv("ENVIRONMENT") == "production":
        if not settings.tls_cert_path or not settings.tls_key_path:
            raise ValueError("TLS certificate and key paths must be configured in production")
        
        # Verify certificate and key files exist
        if not os.path.exists(settings.tls_cert_path):
            raise FileNotFoundError(f"TLS certificate not found at {settings.tls_cert_path}")
        if not os.path.exists(settings.tls_key_path):
            raise FileNotFoundError(f"TLS key not found at {settings.tls_key_path}")

@app.get("/meetings", tags=["meetings"])
async def list_meetings(user: Dict[str, Any] = Depends(get_current_user)):
    # Check if user has required scope
    if "meetings" not in user["scopes"]:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to access meetings"
        )
    return {"meetings": []}

@app.get("/calendar", tags=["calendar"])
async def list_calendar_events(user: Dict[str, Any] = Depends(get_current_user)):
    # Check if user has required scope
    if "calendar" not in user["scopes"]:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to access calendar"
        )
    return {"events": []}

def run_server():
    import uvicorn
    
    ssl_context = None
    if settings.tls_cert_path and settings.tls_key_path:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(
            certfile=settings.tls_cert_path,
            keyfile=settings.tls_key_path
        )
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=443 if ssl_context else 8000,
        ssl_context=ssl_context
    )

if __name__ == "__main__":
    run_server()
```
