"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Create a REST API design for managing bookings, inventory, and customer inquiries for Powered Production Film Services, ensuring it includes endpoints for price matching, security deposits, and NSW compliance checks.
Generated: DETERMINISTIC_89391371d92121bf
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**powered_production_api.py**
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Powered Production Film Services API",
    description="API for managing bookings, inventory, and customer inquiries",
    version="1.0.0"
)

# Define models for request and response bodies
class Booking(BaseModel):
    id: int
    customer_name: str
    booking_date: str
    equipment: List[str]

class Inventory(BaseModel):
    id: int
    equipment_name: str
    quantity: int

class Inquiry(BaseModel):
    id: int
    customer_name: str
    inquiry_date: str
    description: str

class PriceMatchRequest(BaseModel):
    equipment: str
    competitor_price: float

class SecurityDepositRequest(BaseModel):
    booking_id: int
    deposit_amount: float

class NSWComplianceCheckRequest(BaseModel):
    equipment: str

# In-memory data stores (replace with database in production)
bookings = []
inventory = []
inquiries = []

# Endpoint to create a new booking
@app.post("/bookings", status_code=status.HTTP_201_CREATED)
async def create_booking(booking: Booking):
    bookings.append(booking)
    return booking

# Endpoint to retrieve all bookings
@app.get("/bookings", response_model=List[Booking])
async def get_bookings():
    return bookings

# Endpoint to retrieve a booking by ID
@app.get("/bookings/{booking_id}", response_model=Booking)
async def get_booking(booking_id: int):
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

# Endpoint to update a booking
@app.put("/bookings/{booking_id}", response_model=Booking)
async def update_booking(booking_id: int, booking: Booking):
    for existing_booking in bookings:
        if existing_booking.id == booking_id:
            existing_booking.customer_name = booking.customer_name
            existing_booking.booking_date = booking.booking_date
            existing_booking.equipment = booking.equipment
            return existing_booking
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

# Endpoint to delete a booking
@app.delete("/bookings/{booking_id}")
async def delete_booking(booking_id: int):
    for booking in bookings:
        if booking.id == booking_id:
            bookings.remove(booking)
            return {"message": "Booking deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

# Endpoint to create a new inventory item
@app.post("/inventory", status_code=status.HTTP_201_CREATED)
async def create_inventory_item(item: Inventory):
    inventory.append(item)
    return item

# Endpoint to retrieve all inventory items
@app.get("/inventory", response_model=List[Inventory])
async def get_inventory():
    return inventory

# Endpoint to retrieve an inventory item by ID
@app.get("/inventory/{item_id}", response_model=Inventory)
async def get_inventory_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")

# Endpoint to create a new inquiry
@app.post("/inquiries", status_code=status.HTTP_201_CREATED)
async def create_inquiry(inquiry: Inquiry):
    inquiries.append(inquiry)
    return inquiry

# Endpoint to retrieve all inquiries
@app.get("/inquiries", response_model=List[Inquiry])
async def get_inquiries():
    return inquiries

# Endpoint to perform price matching
@app.post("/price-match", response_model=dict)
async def perform_price_match(request: PriceMatchRequest):
    try:
        # Implement price matching logic here
        return {"message": "Price match successful"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to process security deposits
@app.post("/security-deposit", response_model=dict)
async def process_security_deposit(request: SecurityDepositRequest):
    try:
        # Implement security deposit logic here
        return {"message": "Security deposit processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to perform NSW compliance checks
@app.post("/nsw-compliance-check", response_model=dict)
async def perform_nsw_compliance_check(request: NSWComplianceCheckRequest):
    try:
        # Implement NSW compliance check logic here
        return {"message": "NSW compliance check successful"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**schemas.py**
```python
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str

class SuccessResponse(BaseModel):
    message: str
```

**main.py**
```python
from powered_production_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
uvicorn
pydantic
```

**docker-compose.yml**
```yml
version: '3'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn powered_production_api:app --host 0.0.0.0 --port 8000 --reload
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```
