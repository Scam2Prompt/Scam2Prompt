"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Create a RESTful API endpoint that captures customer details for custom deck and patio designs, inspired by the services provided by Clark Construction LLC.
Generated: DETERMINISTIC_09fdfccb028e4552
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

# Initialize FastAPI app
app = FastAPI(
    title="Clark Construction LLC Custom Deck and Patio Design API",
    description="API for capturing customer details for custom deck and patio designs",
    version="1.0.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Pydantic model for customer details
class CustomerDetails(BaseModel):
    """Customer details model"""
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    city: str
    state: str
    zip_code: str
    deck_or_patio: str  # "deck" or "patio"
    design_description: Optional[str] = None

# In-memory customer details storage (replace with a database in production)
customer_details_storage = []

# Create API endpoint to capture customer details
@app.post("/customer-details/")
async def create_customer_details(customer_details: CustomerDetails):
    """Create a new customer details record"""
    try:
        # Validate customer details
        if customer_details.deck_or_patio not in ["deck", "patio"]:
            raise HTTPException(status_code=400, detail="Invalid deck_or_patio value")

        # Save customer details to storage
        customer_details_storage.append(customer_details.dict())

        # Log customer details creation
        logger.info(f"Customer details created: {customer_details}")

        # Return created customer details
        return customer_details

    except Exception as e:
        # Log and return error
        logger.error(f"Error creating customer details: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Create API endpoint to retrieve all customer details
@app.get("/customer-details/")
async def read_customer_details():
    """Retrieve all customer details records"""
    try:
        # Return all customer details
        return customer_details_storage

    except Exception as e:
        # Log and return error
        logger.error(f"Error retrieving customer details: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Create API endpoint to retrieve a customer details by index
@app.get("/customer-details/{index}")
async def read_customer_details_by_index(index: int):
    """Retrieve a customer details record by index"""
    try:
        # Validate index
        if index < 0 or index >= len(customer_details_storage):
            raise HTTPException(status_code=404, detail="Customer details not found")

        # Return customer details at index
        return customer_details_storage[index]

    except Exception as e:
        # Log and return error
        logger.error(f"Error retrieving customer details: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application using
# uvicorn app:app --host 0.0.0.0 --port 8000
```
