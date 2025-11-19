"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Create an API endpoint that accepts property details and returns a cash offer estimate, mimicking the functionality of Metis Assets' service.
Generated: DETERMINISTIC_76cf320fb70a671b
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field, validator
from typing import Optional
import logging
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Metis Assets Cash Offer API",
    description="API for estimating cash offers for properties",
    version="1.0.0"
)


class PropertyDetails(BaseModel):
    """Model for property details input"""
    address: str = Field(..., description="Full property address")
    zip_code: str = Field(..., min_length=5, max_length=10, description="ZIP code of the property")
    property_type: str = Field(
        ...,
        description="Type of property (e.g., single_family, condo, townhouse, multi_family)",
        regex="^(single_family|condo|townhouse|multi_family)$"
    )
    bedrooms: int = Field(..., ge=0, description="Number of bedrooms")
    bathrooms: float = Field(..., ge=0, description="Number of bathrooms")
    square_footage: int = Field(..., ge=0, description="Total square footage")
    year_built: int = Field(..., ge=1800, le=2023, description="Year the property was built")
    condition: str = Field(
        ...,
        description="Property condition (excellent, good, fair, poor)",
        regex="^(excellent|good|fair|poor)$"
    )
    market_value: Optional[float] = Field(None, ge=0, description="Estimated market value (optional)")
    has_repairs: Optional[bool] = Field(False, description="Whether the property needs repairs")
    repair_cost_estimate: Optional[float] = Field(
        None,
        ge=0,
        description="Estimated repair costs if has_repairs is True"
    )

    @validator('repair_cost_estimate')
    def validate_repair_cost(cls, v, values):
        if values.get('has_repairs') and v is None:
            raise ValueError('repair_cost_estimate is required when has_repairs is True')
        return v


class CashOfferResponse(BaseModel):
    """Model for cash offer response"""
    property_details: PropertyDetails
    estimated_offer: float = Field(..., description="Estimated cash offer amount")
    confidence_score: float = Field(
        ...,
        ge=0,
        le=1,
        description="Confidence score of the estimate (0-1)"
    )
    currency: str = Field("USD", description="Currency of the offer amount")


def calculate_cash_offer(property_details: PropertyDetails) -> CashOfferResponse:
    """
    Calculate cash offer based on property details.
    This is a simplified version mimicking Metis Assets' algorithm.
    """
    # Base value calculation
    base_value = property_details.market_value or 200000  # Default if no market value provided
    
    # Adjustments based on property details
    adjustments = 0
    
    # Property type adjustments
    if property_details.property_type == "condo":
        adjustments -= 0.05 * base_value
    elif property_details.property_type == "townhouse":
        adjustments -= 0.03 * base_value
    elif property_details.property_type == "multi_family":
        adjustments += 0.08 * base_value
    
    # Condition adjustments
    if property_details.condition == "good":
        adjustments -= 0.02 * base_value
    elif property_details.condition == "fair":
        adjustments -= 0.05 * base_value
    elif property_details.condition == "poor":
        adjustments -= 0.10 * base_value
    
    # Repair cost deduction
    if property_details.has_repairs and property_details.repair_cost_estimate:
        adjustments -= property_details.repair_cost_estimate
    
    # Calculate final offer (typically 70-90% of adjusted value)
    final_offer = (base_value + adjustments) * 0.85
    
    # Confidence score calculation (simplified)
    confidence = 0.9
    if property_details.market_value is None:
        confidence -= 0.2
    if property_details.has_repairs and property_details.repair_cost_estimate is None:
        confidence -= 0.1
    
    return CashOfferResponse(
        property_details=property_details,
        estimated_offer=round(final_offer, 2),
        confidence_score=round(max(0, min(1, confidence)), 2)
    )


@app.post("/estimate", response_model=CashOfferResponse, status_code=status.HTTP_200_OK)
async def get_cash_offer(property_details: PropertyDetails, request: Request):
    """
    Endpoint to get a cash offer estimate for a property.
    
    Args:
        property_details: Property details input
        request: FastAPI request object
    
    Returns:
        CashOfferResponse: Estimated cash offer with details
    """
    try:
        logger.info(f"Received cash offer request for property at {property_details.address}")
        
        # Calculate the cash offer
        offer_response = calculate_cash_offer(property_details)
        
        logger.info(f"Successfully calculated offer for {property_details.address}: ${offer_response.estimated_offer}")
        return offer_response
        
    except Exception as e:
        logger.error(f"Error processing request for {property_details.address}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
```
