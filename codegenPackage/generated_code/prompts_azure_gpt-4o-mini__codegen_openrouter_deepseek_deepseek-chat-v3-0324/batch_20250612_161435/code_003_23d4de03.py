"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Develop a RESTful API for a service that provides quotes for retractable screens, similar to the customer support features of Ontario Screen Systems Inc.
Generated: DETERMINISTIC_23d4de03f2fa8766
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Retractable Screen Quote API",
    description="API for generating quotes for retractable screens",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@screensystems.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, replace with actual database)
quotes_db = []
screen_types_db = [
    {"id": 1, "name": "Standard", "price_per_sqft": 15.50},
    {"id": 2, "name": "Premium", "price_per_sqft": 22.75},
    {"id": 3, "name": "Commercial", "price_per_sqft": 30.00},
]

class ScreenType(BaseModel):
    id: int
    name: str
    price_per_sqft: float

class QuoteRequest(BaseModel):
    customer_name: str
    email: str
    phone: str
    width_ft: float
    height_ft: float
    screen_type_id: int
    installation_required: bool = False
    notes: Optional[str] = None

class QuoteResponse(BaseModel):
    quote_id: str
    customer_name: str
    email: str
    phone: str
    width_ft: float
    height_ft: float
    screen_type: ScreenType
    installation_required: bool
    subtotal: float
    tax: float
    total: float
    notes: Optional[str] = None
    created_at: datetime

@app.get("/screen-types", response_model=List[ScreenType], tags=["Products"])
async def get_screen_types():
    """Get all available screen types"""
    return screen_types_db

@app.get("/screen-types/{screen_type_id}", response_model=ScreenType, tags=["Products"])
async def get_screen_type(screen_type_id: int):
    """Get a specific screen type by ID"""
    screen_type = next((st for st in screen_types_db if st["id"] == screen_type_id), None)
    if not screen_type:
        raise HTTPException(status_code=404, detail="Screen type not found")
    return screen_type

@app.post("/quotes", response_model=QuoteResponse, status_code=201, tags=["Quotes"])
async def create_quote(quote_request: QuoteRequest):
    """Create a new quote for retractable screens"""
    try:
        # Validate screen type exists
        screen_type = next((st for st in screen_types_db if st["id"] == quote_request.screen_type_id), None)
        if not screen_type:
            raise HTTPException(status_code=400, detail="Invalid screen type ID")

        # Calculate quote
        area = quote_request.width_ft * quote_request.height_ft
        subtotal = area * screen_type["price_per_sqft"]
        
        # Add installation fee if needed
        if quote_request.installation_required:
            subtotal += 150.00  # Flat installation fee
            
        tax = subtotal * 0.13  # Assuming 13% tax (HST in Ontario)
        total = subtotal + tax

        # Create quote response
        quote_id = f"Q-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        created_at = datetime.now()
        
        quote_response = {
            "quote_id": quote_id,
            "customer_name": quote_request.customer_name,
            "email": quote_request.email,
            "phone": quote_request.phone,
            "width_ft": quote_request.width_ft,
            "height_ft": quote_request.height_ft,
            "screen_type": screen_type,
            "installation_required": quote_request.installation_required,
            "subtotal": round(subtotal, 2),
            "tax": round(tax, 2),
            "total": round(total, 2),
            "notes": quote_request.notes,
            "created_at": created_at
        }

        # Store quote (in production, this would be a database insert)
        quotes_db.append(quote_response)
        logger.info(f"Created new quote {quote_id} for {quote_request.customer_name}")

        return quote_response

    except Exception as e:
        logger.error(f"Error creating quote: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing quote")

@app.get("/quotes/{quote_id}", response_model=QuoteResponse, tags=["Quotes"])
async def get_quote(quote_id: str):
    """Get a specific quote by ID"""
    quote = next((q for q in quotes_db if q["quote_id"] == quote_id), None)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@app.get("/quotes", response_model=List[QuoteResponse], tags=["Quotes"])
async def list_quotes(
    customer_name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    """List all quotes with optional filtering"""
    try:
        filtered_quotes = quotes_db.copy()
        
        if customer_name:
            filtered_quotes = [q for q in filtered_quotes if customer_name.lower() in q["customer_name"].lower()]
        
        if email:
            filtered_quotes = [q for q in filtered_quotes if email.lower() == q["email"].lower()]
        
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            filtered_quotes = [q for q in filtered_quotes if q["created_at"] >= start_date]
        
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            filtered_quotes = [q for q in filtered_quotes if q["created_at"].date() <= end_date.date()]
        
        return filtered_quotes
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    except Exception as e:
        logger.error(f"Error listing quotes: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving quotes")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
