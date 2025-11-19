"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Create an API endpoint for a property management service that allows users to submit inquiries about tailored investment solutions, similar to the services offered by Bebold Properties.
Generated: DETERMINISTIC_32d7a6933b8f93ca
Batch ID: 20250612_164139
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
    title="Property Management Service API",
    description="API for submitting inquiries about tailored investment solutions",
    version="1.0.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Pydantic model for inquiry request
class InquiryRequest(BaseModel):
    """Inquiry request model"""
    name: str
    email: str
    phone_number: str
    property_type: str
    investment_goal: str
    message: Optional[str] = None

# Define Pydantic model for inquiry response
class InquiryResponse(BaseModel):
    """Inquiry response model"""
    id: int
    name: str
    email: str
    phone_number: str
    property_type: str
    investment_goal: str
    message: Optional[str] = None

# In-memory storage for inquiries (replace with database in production)
inquiries = []
inquiry_id = 1

# API endpoint to submit inquiry
@app.post("/inquiries", response_model=InquiryResponse)
async def create_inquiry(inquiry: InquiryRequest):
    """Create a new inquiry"""
    global inquiry_id
    try:
        # Validate inquiry request
        if not inquiry.name or not inquiry.email or not inquiry.phone_number:
            raise HTTPException(status_code=400, detail="Name, email, and phone number are required")

        # Create new inquiry
        new_inquiry = InquiryResponse(
            id=inquiry_id,
            name=inquiry.name,
            email=inquiry.email,
            phone_number=inquiry.phone_number,
            property_type=inquiry.property_type,
            investment_goal=inquiry.investment_goal,
            message=inquiry.message
        )
        inquiries.append(new_inquiry)
        inquiry_id += 1

        # Log inquiry creation
        logger.info(f"Inquiry created: {new_inquiry}")

        return new_inquiry
    except Exception as e:
        # Log and handle exception
        logger.error(f"Error creating inquiry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create inquiry")

# API endpoint to retrieve all inquiries
@app.get("/inquiries", response_model=list[InquiryResponse])
async def read_inquiries():
    """Retrieve all inquiries"""
    try:
        return inquiries
    except Exception as e:
        # Log and handle exception
        logger.error(f"Error retrieving inquiries: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve inquiries")

# API endpoint to retrieve inquiry by ID
@app.get("/inquiries/{inquiry_id}", response_model=InquiryResponse)
async def read_inquiry(inquiry_id: int):
    """Retrieve inquiry by ID"""
    try:
        for inquiry in inquiries:
            if inquiry.id == inquiry_id:
                return inquiry
        raise HTTPException(status_code=404, detail="Inquiry not found")
    except Exception as e:
        # Log and handle exception
        logger.error(f"Error retrieving inquiry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve inquiry")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
