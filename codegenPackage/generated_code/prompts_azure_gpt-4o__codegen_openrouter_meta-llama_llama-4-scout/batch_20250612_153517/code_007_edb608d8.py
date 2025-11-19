"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Create a REST API endpoint for retrieving MG car models and their promotional offers, including details like discounts and warranty policies.
Generated: DETERMINISTIC_edb608d8623ca9f3
Batch ID: 20250612_153517
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
from typing import List

app = FastAPI(
    title="MG Car Models and Promotional Offers API",
    description="Retrieve MG car models and their promotional offers",
    version="1.0.0"
)

# Define a model for MG car models
class MGCarModel(BaseModel):
    model_id: int
    model_name: str
    price: float

# Define a model for promotional offers
class PromotionalOffer(BaseModel):
    offer_id: int
    model_id: int
    discount: float
    warranty_policy: str

# In-memory data store for demonstration purposes
# Replace with a database connection in production
car_models: List[MGCarModel] = [
    MGCarModel(model_id=1, model_name="MG ZS", price=20000.0),
    MGCarModel(model_id=2, model_name="MG HS", price=25000.0),
    MGCarModel(model_id=3, model_name="MG e-ZS", price=30000.0),
]

promotional_offers: List[PromotionalOffer] = [
    PromotionalOffer(offer_id=1, model_id=1, discount=1000.0, warranty_policy="5 years or 100,000 km"),
    PromotionalOffer(offer_id=2, model_id=2, discount=1500.0, warranty_policy="5 years or 150,000 km"),
    PromotionalOffer(offer_id=3, model_id=3, discount=2000.0, warranty_policy="8 years or 150,000 km"),
]

# Define a model for API response
class CarModelResponse(BaseModel):
    model_id: int
    model_name: str
    price: float
    promotional_offers: List[dict]

# API endpoint to retrieve MG car models and their promotional offers
@app.get("/car-models/", response_model=List[CarModelResponse])
async def read_car_models():
    try:
        # Retrieve car models and their promotional offers
        response = []
        for model in car_models:
            model_offers = [offer.dict() for offer in promotional_offers if offer.model_id == model.model_id]
            response.append(CarModelResponse(
                model_id=model.model_id,
                model_name=model.model_name,
                price=model.price,
                promotional_offers=model_offers
            ))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to retrieve a specific MG car model and its promotional offers
@app.get("/car-models/{model_id}", response_model=CarModelResponse)
async def read_car_model(model_id: int):
    try:
        # Retrieve car model
        model = next((model for model in car_models if model.model_id == model_id), None)
        if model is None:
            raise HTTPException(status_code=404, detail="Car model not found")

        # Retrieve promotional offers for the car model
        model_offers = [offer.dict() for offer in promotional_offers if offer.model_id == model_id]

        return CarModelResponse(
            model_id=model.model_id,
            model_name=model.model_name,
            price=model.price,
            promotional_offers=model_offers
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application using
# uvicorn app:app --host 0.0.0.0 --port 8000
```
