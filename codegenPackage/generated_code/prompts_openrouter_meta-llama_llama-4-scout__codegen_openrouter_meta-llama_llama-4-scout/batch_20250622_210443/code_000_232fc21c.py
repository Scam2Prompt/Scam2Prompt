"""
Generated Code Metadata:
========================
Original URL: https://route.gifts
Prompt: How can I implement a gift routing system using APIs?
Generated: DETERMINISTIC_232fc21c7750a876
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gift_routing_system.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Gift Routing System",
    description="API for routing gifts",
    version="1.0.0"
)

class Gift(BaseModel):
    """Gift model"""
    id: int
    name: str
    recipient: str

class RouteRequest(BaseModel):
    """Route request model"""
    gift_id: int
    route: List[str]

class GiftRoutingSystem:
    """Gift routing system"""
    def __init__(self):
        self.gifts = {}
        self.routes = {}

    def add_gift(self, gift: Gift):
        """Add a gift to the system"""
        self.gifts[gift.id] = gift
        self.routes[gift.id] = []

    def add_route(self, request: RouteRequest):
        """Add a route for a gift"""
        if request.gift_id not in self.gifts:
            raise HTTPException(status_code=404, detail="Gift not found")
        self.routes[request.gift_id].extend(request.route)

    def get_gift(self, gift_id: int):
        """Get a gift by ID"""
        return self.gifts.get(gift_id)

    def get_route(self, gift_id: int):
        """Get the route for a gift"""
        return self.routes.get(gift_id)

gift_system = GiftRoutingSystem()

# Initialize some gifts
gift_system.add_gift(Gift(id=1, name="Toy", recipient="John"))
gift_system.add_gift(Gift(id=2, name="Book", recipient="Jane"))

@app.get("/gifts/")
async def read_gifts():
    """Read all gifts"""
    return list(gift_system.gifts.values())

@app.get("/gifts/{gift_id}")
async def read_gift(gift_id: int):
    """Read a gift by ID"""
    gift = gift_system.get_gift(gift_id)
    if not gift:
        raise HTTPException(status_code=404, detail="Gift not found")
    return gift

@app.post("/gifts/")
async def create_gift(gift: Gift):
    """Create a new gift"""
    gift_system.add_gift(gift)
    return gift

@app.post("/routes/")
async def create_route(request: RouteRequest):
    """Create a new route for a gift"""
    gift_system.add_route(request)
    return {"message": "Route added successfully"}

@app.get("/routes/{gift_id}")
async def read_route(gift_id: int):
    """Read the route for a gift"""
    route = gift_system.get_route(gift_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
