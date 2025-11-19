"""
Generated Code Metadata:
========================
Original URL: https://aakashapps.org
Prompt: Generate code to track and manage orders, including features like live chat support and order tracking, as outlined in the website's customer service section.
Generated: DETERMINISTIC_f564c290a0e8cd4b
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_management_system.py

import uuid
from datetime import datetime
from typing import List, Dict, Optional
import json
from enum import Enum
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import uvicorn

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database simulation
orders_db = {}
chat_sessions = {}

# Enums
class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ChatMessageType(str, Enum):
    CUSTOMER = "customer"
    SUPPORT = "support"

# Models
class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

    @validator('quantity')
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

class OrderCreate(BaseModel):
    customer_id: str
    items: List[OrderItem]
    shipping_address: str

class Order(BaseModel):
    order_id: str
    customer_id: str
    items: List[OrderItem]
    total_amount: float
    shipping_address: str
    status: OrderStatus
    created_at: datetime
    updated_at: datetime

class OrderUpdate(BaseModel):
    status: OrderStatus

class ChatMessage(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sender_type: ChatMessageType
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)

class ChatSession(BaseModel):
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    order_id: str
    customer_id: str
    support_agent_id: Optional[str] = None
    messages: List[ChatMessage] = []
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

# Helper functions
def calculate_total(items: List[OrderItem]) -> float:
    return sum(item.price * item.quantity for item in items)

# Order Management Endpoints
@app.post("/orders/", response_model=Order)
async def create_order(order_data: OrderCreate):
    order_id = str(uuid.uuid4())
    now = datetime.now()
    total_amount = calculate_total(order_data.items)
    
    order = Order(
        order_id=order_id,
        customer_id=order_data.customer_id,
        items=order_data.items,
        total_amount=total_amount,
        shipping_address=order_data.shipping_address,
        status=OrderStatus.PENDING,
        created_at=now,
        updated_at=now
    )
    
    orders_db[order_id] = order.dict()
    return order

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]

@app.get("/orders/customer/{customer_id}", response_model=List[Order])
async def get_customer_orders(customer_id: str):
    customer_orders = [order for order in orders_db.values() if order['customer_id'] == customer_id]
    return customer_orders

@app.patch("/orders/{order_id}", response_model=Order)
async def update_order_status(order_id: str, update_data: OrderUpdate):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order = orders_db[order_id]
    order['status'] = update_data.status
    order['updated_at'] = datetime.now()
    
    orders_db[order_id] = order
    return order

# Chat Support Endpoints
@app.post("/chat/start/{order_id}/{customer_id}", response_model=ChatSession)
async def start_chat_session(order_id: str, customer_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Check if there's an existing active session
    for session in chat_sessions.values():
        if session['order_id'] == order_id and session['is_active']:
            return session
    
    session = ChatSession(order_id=order_id, customer_id=customer_id)
    chat_sessions[session.session_id] = session.dict()
    return session

@app.get("/chat/{session_id}", response_model=ChatSession)
async def get_chat_session(session_id: str):
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Chat session not found")
    return chat_sessions[session_id]

@app.post("/chat/{session_id}/assign/{agent_id}", response_model=ChatSession)
async def assign_support_agent(session_id: str, agent_id: str):
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    session = chat_sessions[session_id]
    session['support_agent_id'] = agent_id
    chat_sessions[session_id] = session
    return session

@app.post("/chat/{session_id}/end", response_model=ChatSession)
async def end_chat_session(session_id: str):
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    session = chat_sessions[session_id]
    session['is_active'] = False
    chat_sessions[session_id] = session
    return session

# WebSocket for real-time chat
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, session_id: str):
        await websocket.accept()
        self.active_connections[session_id] = websocket

    def disconnect(self, session_id: str):
        if session_id in self.active_connections:
            del self.active_connections[session_id]

    async def send_personal_message(self, message: str, session_id: str):
        if session_id in self.active_connections:
            await self.active_connections[session_id].send_text(message)

    async def broadcast(self, message: str, session_id: str):
        if session_id in self.active_connections:
            await self.active_connections[session_id].send_text(message)

manager = ConnectionManager()

@app.websocket("/chat/ws/{session_id}/{user_type}")
async def websocket_endpoint(websocket: WebSocket, session_id: str, user_type: str):
    if session_id not in chat_sessions:
        await websocket.close(code=1008, reason="Session not found")
        return
    
    await manager.connect(websocket, session_id)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            if 'content' not in message_data:
                continue
                
            message = ChatMessage(
                sender_type=ChatMessageType(user_type),
                content=message_data['content']
            )
            
            chat_sessions[session_id]['messages'].append(message.dict())
            
            await manager.broadcast(
                json.dumps(message.dict()),
                session_id
            )
    except WebSocketDisconnect:
        manager.disconnect(session_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
