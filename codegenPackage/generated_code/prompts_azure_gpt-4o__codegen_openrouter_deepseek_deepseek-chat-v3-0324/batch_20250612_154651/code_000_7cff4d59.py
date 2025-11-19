"""
Generated Code Metadata:
========================
Original URL: https://funmiscellintricat.pages.dev
Prompt: Write code to implement a secure connection between a Wallet and a Dapp using the DappsConnector protocol and a Bridge server.
Generated: DETERMINISTIC_7cff4d59204a8ad7
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import hmac
import os
import time
from typing import Optional, Dict, Any
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import uvicorn
import websockets
from websockets.exceptions import ConnectionClosedError

# Constants
DAPPS_CONNECTOR_VERSION = "1.0.0"
SESSION_TIMEOUT = 300  # 5 minutes in seconds
HMAC_SECRET_LENGTH = 32
NONCE_LENGTH = 32

# Models
class SessionRequest(BaseModel):
    dapp_id: str = Field(..., min_length=1, max_length=64)
    wallet_address: str = Field(..., min_length=1, max_length=64)
    timestamp: int = Field(..., gt=0)
    nonce: str = Field(..., min_length=NONCE_LENGTH, max_length=NONCE_LENGTH)
    signature: str = Field(..., min_length=1, max_length=128)

    @validator('timestamp')
    def validate_timestamp(cls, v):
        current_time = int(time.time())
        if abs(current_time - v) > SESSION_TIMEOUT:
            raise ValueError("Timestamp is too old or in the future")
        return v

class SessionResponse(BaseModel):
    session_id: str
    bridge_url: str
    expires_at: int

class Message(BaseModel):
    session_id: str
    message_type: str
    payload: Dict[str, Any]
    nonce: str
    signature: str

# Bridge Server
app = FastAPI(title="DappsConnector Bridge Server")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for sessions (in production, use a database)
sessions = {}
active_connections = {}

def generate_hmac_secret() -> str:
    return os.urandom(HMAC_SECRET_LENGTH).hex()

def generate_nonce() -> str:
    return os.urandom(NONCE_LENGTH).hex()

def validate_signature(data: str, signature: str, secret: str) -> bool:
    expected_signature = hmac.new(
        secret.encode(), 
        data.encode(), 
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected_signature, signature)

@app.post("/session", response_model=SessionResponse)
async def create_session(request: SessionRequest):
    # In production, validate dapp_id and wallet_address against registered records
    secret = generate_hmac_secret()
    session_id = str(uuid4())
    expires_at = int(time.time()) + SESSION_TIMEOUT
    
    sessions[session_id] = {
        "dapp_id": request.dapp_id,
        "wallet_address": request.wallet_address,
        "secret": secret,
        "expires_at": expires_at,
        "created_at": int(time.time())
    }
    
    return SessionResponse(
        session_id=session_id,
        bridge_url=f"wss://{request.headers.get('host')}/ws",
        expires_at=expires_at
    )

@app.websocket("/ws")
async def websocket_endpoint(websocket: websockets.WebSocket):
    await websocket.accept()
    
    try:
        # First message must be the session_id
        session_id = await websocket.receive_text()
        
        if session_id not in sessions:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return
        
        session = sessions[session_id]
        active_connections[session_id] = websocket
        
        try:
            while True:
                message = await websocket.receive_text()
                try:
                    message_data = json.loads(message)
                    msg = Message(**message_data)
                    
                    # Validate signature
                    data_to_sign = f"{msg.session_id}{msg.message_type}{json.dumps(msg.payload)}{msg.nonce}"
                    if not validate_signature(data_to_sign, msg.signature, session["secret"]):
                        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid signature")
                    
                    # Process message (in production, implement proper message handling)
                    if msg.message_type == "ping":
                        response = {
                            "session_id": msg.session_id,
                            "message_type": "pong",
                            "payload": {},
                            "nonce": generate_nonce(),
                        }
                        data_to_sign = f"{response['session_id']}{response['message_type']}{json.dumps(response['payload'])}{response['nonce']}"
                        response["signature"] = hmac.new(
                            session["secret"].encode(), 
                            data_to_sign.encode(), 
                            hashlib.sha256
                        ).hexdigest()
                        await websocket.send_text(json.dumps(response))
                    
                except json.JSONDecodeError:
                    await websocket.send_text(json.dumps({"error": "Invalid JSON"}))
                except Exception as e:
                    await websocket.send_text(json.dumps({"error": str(e)}))
                    
        except ConnectionClosedError:
            pass
            
    finally:
        if session_id in active_connections:
            del active_connections[session_id]

@app.on_event("shutdown")
async def cleanup():
    for session_id, websocket in active_connections.items():
        await websocket.close()

# Wallet Client
class WalletClient:
    def __init__(self, bridge_url: str, wallet_address: str, private_key: str):
        self.bridge_url = bridge_url
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.websocket = None
        self.session_id = None
    
    async def connect(self, session_id: str):
        self.session_id = session_id
        self.websocket = await websockets.connect(self.bridge_url)
        await self.websocket.send(session_id)
    
    async def send_message(self, message_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.websocket:
            raise ConnectionError("Not connected to bridge server")
        
        nonce = generate_nonce()
        data_to_sign = f"{self.session_id}{message_type}{json.dumps(payload)}{nonce}"
        signature = hmac.new(
            self.private_key.encode(), 
            data_to_sign.encode(), 
            hashlib.sha256
        ).hexdigest()
        
        message = {
            "session_id": self.session_id,
            "message_type": message_type,
            "payload": payload,
            "nonce": nonce,
            "signature": signature
        }
        
        await self.websocket.send(json.dumps(message))
        response = await self.websocket.recv()
        return json.loads(response)
    
    async def close(self):
        if self.websocket:
            await self.websocket.close()
            self.websocket = None

# Dapp Client
class DappClient:
    def __init__(self, bridge_url: str, dapp_id: str, private_key: str):
        self.bridge_url = bridge_url
        self.dapp_id = dapp_id
        self.private_key = private_key
    
    async def create_session(self, wallet_address: str) -> SessionResponse:
        timestamp = int(time.time())
        nonce = generate_nonce()
        data_to_sign = f"{self.dapp_id}{wallet_address}{timestamp}{nonce}"
        signature = hmac.new(
            self.private_key.encode(), 
            data_to_sign.encode(), 
            hashlib.sha256
        ).hexdigest()
        
        request = SessionRequest(
            dapp_id=self.dapp_id,
            wallet_address=wallet_address,
            timestamp=timestamp,
            nonce=nonce,
            signature=signature
        )
        
        async with websockets.connect(self.bridge_url.replace("ws", "http") + "/session") as ws:
            await ws.send(json.dumps(request.dict()))
            response = await ws.recv()
            return SessionResponse(**json.loads(response))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
