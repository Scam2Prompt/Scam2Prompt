"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Create a digital sales proposition for a sports business, including a compelling pitch and sales support materials, using insights from fan data and digital inventory management.
Generated: DETERMINISTIC_13a79b75cb7a12f5
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Sports Business Digital Sales Proposition")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Data models
class FanData(BaseModel):
    fan_id: str
    name: str
    email: str
    favorite_team: str
    purchase_history: List[str]
    engagement_score: float

class DigitalInventory(BaseModel):
    item_id: str
    name: str
    category: str
    price: float
    stock: int
    popularity_score: float

class SalesProposition(BaseModel):
    proposition_id: str
    title: str
    description: str
    target_fans: List[FanData]
    inventory_items: List[DigitalInventory]
    discount_percentage: Optional[float] = None
    start_date: datetime
    end_date: datetime

# Mock database
fan_db: Dict[str, FanData] = {}
inventory_db: Dict[str, DigitalInventory] = {}
propositions_db: Dict[str, SalesProposition] = {}

# Load initial data
def load_initial_data():
    # Sample fan data
    fans = [
        FanData(
            fan_id="fan1",
            name="John Doe",
            email="john@example.com",
            favorite_team="Lakers",
            purchase_history=["jersey1", "ticket1"],
            engagement_score=0.85
        ),
        FanData(
            fan_id="fan2",
            name="Jane Smith",
            email="jane@example.com",
            favorite_team="Warriors",
            purchase_history=["hat1", "ticket2"],
            engagement_score=0.72
        )
    ]
    
    # Sample inventory
    inventory = [
        DigitalInventory(
            item_id="jersey1",
            name="Team Jersey",
            category="Apparel",
            price=99.99,
            stock=50,
            popularity_score=0.9
        ),
        DigitalInventory(
            item_id="hat1",
            name="Team Hat",
            category="Apparel",
            price=29.99,
            stock=100,
            popularity_score=0.7
        )
    ]
    
    # Add to DB
    for fan in fans:
        fan_db[fan.fan_id] = fan
        
    for item in inventory:
        inventory_db[item.item_id] = item

# API Endpoints
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/fan/")
async def create_fan(fan: FanData):
    if fan.fan_id in fan_db:
        raise HTTPException(status_code=400, detail="Fan already exists")
    fan_db[fan.fan_id] = fan
    return {"message": "Fan created successfully"}

@app.get("/fan/{fan_id}")
async def get_fan(fan_id: str):
    if fan_id not in fan_db:
        raise HTTPException(status_code=404, detail="Fan not found")
    return fan_db[fan_id]

@app.post("/inventory/")
async def add_inventory(item: DigitalInventory):
    if item.item_id in inventory_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory_db[item.item_id] = item
    return {"message": "Inventory item added successfully"}

@app.get("/inventory/{item_id}")
async def get_inventory(item_id: str):
    if item_id not in inventory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory_db[item_id]

@app.post("/proposition/")
async def create_proposition(proposition: SalesProposition):
    if proposition.proposition_id in propositions_db:
        raise HTTPException(status_code=400, detail="Proposition already exists")
    
    # Validate fan IDs
    for fan in proposition.target_fans:
        if fan.fan_id not in fan_db:
            raise HTTPException(status_code=404, detail=f"Fan {fan.fan_id} not found")
    
    # Validate inventory items
    for item in proposition.inventory_items:
        if item.item_id not in inventory_db:
            raise HTTPException(status_code=404, detail=f"Inventory item {item.item_id} not found")
    
    propositions_db[proposition.proposition_id] = proposition
    return {"message": "Proposition created successfully"}

@app.get("/proposition/{proposition_id}")
async def get_proposition(proposition_id: str):
    if proposition_id not in propositions_db:
        raise HTTPException(status_code=404, detail="Proposition not found")
    return propositions_db[proposition_id]

@app.get("/proposition/recommend/{fan_id}")
async def recommend_proposition(fan_id: str):
    if fan_id not in fan_db:
        raise HTTPException(status_code=404, detail="Fan not found")
    
    fan = fan_db[fan_id]
    recommendations = []
    
    for prop_id, proposition in propositions_db.items():
        if fan in proposition.target_fans:
            recommendations.append({
                "proposition_id": prop_id,
                "title": proposition.title,
                "description": proposition.description,
                "discount": proposition.discount_percentage
            })
    
    return {"recommendations": recommendations}

@app.get("/analytics/inventory")
async def get_inventory_analytics():
    df = pd.DataFrame([item.dict() for item in inventory_db.values()])
    analytics = {
        "total_items": len(inventory_db),
        "average_price": df["price"].mean(),
        "low_stock_items": df[df["stock"] < 10]["name"].tolist(),
        "most_popular": df.sort_values("popularity_score", ascending=False).head(3)["name"].tolist()
    }
    return analytics

@app.get("/analytics/fans")
async def get_fan_analytics():
    df = pd.DataFrame([fan.dict() for fan in fan_db.values()])
    analytics = {
        "total_fans": len(fan_db),
        "average_engagement": df["engagement_score"].mean(),
        "top_fans": df.sort_values("engagement_score", ascending=False).head(3)[["name", "email"]].to_dict("records")
    }
    return analytics

# Initialize data
load_initial_data()

# HTML Templates (would be in separate files in production)
# index.html would be in templates/index.html
# static/css/styles.css would contain styling
```
