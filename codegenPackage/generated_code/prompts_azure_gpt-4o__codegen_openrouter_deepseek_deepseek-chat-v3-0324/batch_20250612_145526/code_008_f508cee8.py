"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "How can I implement a feature to display real-time promotions and bonuses for a slot game platform like สล็อตเว็บตรง?"
Generated: DETERMINISTIC_f508cee895e85fec
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import time
from typing import List, Dict, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Mock database for promotions
promotions_db = [
    {
        "id": 1,
        "title": "Welcome Bonus",
        "description": "Get 100% bonus up to 1000 THB on your first deposit!",
        "image_url": "/static/welcome_bonus.jpg",
        "valid_until": "2023-12-31",
        "is_active": True
    },
    {
        "id": 2,
        "title": "Free Spins Friday",
        "description": "50 free spins every Friday for selected games",
        "image_url": "/static/free_spins.jpg",
        "valid_until": "2023-12-31",
        "is_active": True
    },
    {
        "id": 3,
        "title": "VIP Exclusive",
        "description": "Special bonuses for VIP members",
        "image_url": "/static/vip_bonus.jpg",
        "valid_until": "2023-12-31",
        "is_active": True
    }
]

# Model for promotion data
class Promotion(BaseModel):
    id: int
    title: str
    description: str
    image_url: str
    valid_until: str
    is_active: bool

# WebSocket manager for real-time updates
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

manager = ConnectionManager()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    return """
    <html>
        <head>
            <title>Slot Game Promotions</title>
            <script>
                let socket;
                function connectWebSocket() {
                    socket = new WebSocket(`ws://${window.location.host}/ws`);
                    
                    socket.onmessage = function(event) {
                        const promotions = JSON.parse(event.data);
                        updatePromotionsUI(promotions);
                    };
                    
                    socket.onclose = function() {
                        setTimeout(connectWebSocket, 1000);
                    };
                }
                
                function updatePromotionsUI(promotions) {
                    const container = document.getElementById('promotions-container');
                    container.innerHTML = '';
                    
                    promotions.forEach(promo => {
                        const promoElement = document.createElement('div');
                        promoElement.className = 'promotion-card';
                        promoElement.innerHTML = `
                            <img src="${promo.image_url}" alt="${promo.title}">
                            <h3>${promo.title}</h3>
                            <p>${promo.description}</p>
                            <small>Valid until: ${promo.valid_until}</small>
                        `;
                        container.appendChild(promoElement);
                    });
                }
                
                window.onload = function() {
                    connectWebSocket();
                    fetchPromotions();
                };
                
                async function fetchPromotions() {
                    const response = await fetch('/api/promotions');
                    const promotions = await response.json();
                    updatePromotionsUI(promotions);
                }
            </script>
            <style>
                .promotion-card {
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 16px;
                    margin: 10px;
                    max-width: 300px;
                    display: inline-block;
                }
                .promotion-card img {
                    max-width: 100%;
                    height: auto;
                }
            </style>
        </head>
        <body>
            <h1>Current Promotions</h1>
            <div id="promotions-container"></div>
        </body>
    </html>
    """

@app.get("/api/promotions", response_model=List[Promotion])
async def get_promotions():
    """Get all active promotions"""
    return [promo for promo in promotions_db if promo["is_active"]]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates"""
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

async def update_promotions_periodically():
    """Periodically check for promotion updates and broadcast to clients"""
    while True:
        await asyncio.sleep(30)  # Check every 30 seconds
        active_promotions = [promo for promo in promotions_db if promo["is_active"]]
        await manager.broadcast(json.dumps(active_promotions))

@app.on_event("startup")
async def startup_event():
    """Start background tasks when application starts"""
    asyncio.create_task(update_promotions_periodically())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
