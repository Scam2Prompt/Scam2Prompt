"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: Write a code snippet that demonstrates how to create a user-friendly onboarding process with Google or Apple accounts in a Sophon-based app.
Generated: DETERMINISTIC_ea77338f7fbb059c
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Define the FastAPI app
app = FastAPI()

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define the user model
class User(BaseModel):
    id: int
    username: str
    email: str

# Define the token model
class Token(BaseModel):
    access_token: str
    token_type: str

# Define the Google OAuth2 credentials model
class GoogleCredentials(BaseModel):
    creds: Credentials

# Define the Apple OAuth2 credentials model
class AppleCredentials(BaseModel):
    id_token: str
    authorization_code: str

# Google OAuth2 client ID and secret
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

# Apple OAuth2 client ID and secret
APPLE_CLIENT_ID = os.environ.get("APPLE_CLIENT_ID")
APPLE_CLIENT_SECRET = os.environ.get("APPLE_CLIENT_SECRET")

# Define the onboarding process endpoint
@app.post("/onboard/")
async def onboard_user(credentials: GoogleCredentials or AppleCredentials):
    try:
        # Validate Google credentials
        if isinstance(credentials, GoogleCredentials):
            creds = credentials.creds
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        "credentials.json", SCOPES=["profile", "email"]
                    )
                    creds = flow.run_local_server(port=0)
            user_info = build("oauth2", "v2", credentials=creds).userinfo().get().execute()
            user = User(id=user_info["id"], username=user_info["name"], email=user_info["email"])
        
        # Validate Apple credentials
        elif isinstance(credentials, AppleCredentials):
            # Verify Apple ID token
            id_token = credentials.id_token
            # Use a library like pyjwt to verify the token
            # For simplicity, assume the token is valid
            user_info = {"id": "apple_user_id", "username": "Apple User", "email": "apple@example.com"}
            user = User(id=user_info["id"], username=user_info["username"], email=user_info["email"])
        
        # Create a new user
        # For simplicity, assume a user is created successfully
        return {"message": "User created successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Define the login endpoint for Google OAuth2
@app.post("/login/google/")
async def login_google(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # Use the Google OAuth2 client to authenticate the user
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES=["profile", "email"]
        )
        creds = flow.run_local_server(port=0)
        user_info = build("oauth2", "v2", credentials=creds).userinfo().get().execute()
        user = User(id=user_info["id"], username=user_info["name"], email=user_info["email"])
        # Return a token
        return Token(access_token="google_token", token_type="bearer")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Define the login endpoint for Apple OAuth2
@app.post("/login/apple/")
async def login_apple(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # Use the Apple OAuth2 client to authenticate the user
        # For simplicity, assume the user is authenticated successfully
        user = User(id="apple_user_id", username="Apple User", email="apple@example.com")
        # Return a token
        return Token(access_token="apple_token", token_type="bearer")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
