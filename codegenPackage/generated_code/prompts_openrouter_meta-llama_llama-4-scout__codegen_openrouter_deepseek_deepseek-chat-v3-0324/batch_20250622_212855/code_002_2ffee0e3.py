"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Design a simple API to retrieve information about high-end cars, including their performance, price, and features, and provide a JSON response example.
Generated: DETERMINISTIC_2ffee0e31d50a75b
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="High-End Car API",
    description="API for retrieving information about high-end cars",
    version="1.0.0"
)

class CarFeature(BaseModel):
    name: str
    description: str

class CarPerformance(BaseModel):
    top_speed: int  # in km/h
    acceleration: float  # 0-100 km/h in seconds
    horsepower: int

class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    price: float  # in USD
    performance: CarPerformance
    features: List[CarFeature]

# In-memory database for demonstration
cars_db = [
    Car(
        id=1,
        make="Ferrari",
        model="SF90 Stradale",
        year=2023,
        price=625000.00,
        performance=CarPerformance(
            top_speed=340,
            acceleration=2.5,
            horsepower=986
        ),
        features=[
            CarFeature(name="Hybrid Powertrain", description="Combines V8 engine with three electric motors"),
            CarFeature(name="Active Aerodynamics", description="Adjustable rear spoiler for optimal downforce")
        ]
    ),
    Car(
        id=2,
        make="Porsche",
        model="911 Turbo S",
        year=2023,
        price=207000.00,
        performance=CarPerformance(
            top_speed=330,
            acceleration=2.7,
            horsepower=640
        ),
        features=[
            CarFeature(name="All-Wheel Drive", description="Porsche Traction Management system"),
            CarFeature(name="Adaptive Suspension", description="Porsche Active Suspension Management")
        ]
    )
]

@app.get("/cars", response_model=List[Car], tags=["Cars"])
async def get_all_cars():
    """Retrieve all high-end cars in the database"""
    return cars_db

@app.get("/cars/{car_id}", response_model=Car, tags=["Cars"])
async def get_car_by_id(car_id: int):
    """Retrieve a specific car by its ID"""
    car = next((car for car in cars_db if car.id == car_id), None)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.get("/cars/make/{make}", response_model=List[Car], tags=["Cars"])
async def get_cars_by_make(make: str):
    """Retrieve all cars from a specific manufacturer"""
    filtered_cars = [car for car in cars_db if car.make.lower() == make.lower()]
    if not filtered_cars:
        raise HTTPException(
            status_code=404,
            detail=f"No cars found from manufacturer: {make}"
        )
    return filtered_cars

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Example JSON response (for GET /cars/1):
```json
{
    "id": 1,
    "make": "Ferrari",
    "model": "SF90 Stradale",
    "year": 2023,
    "price": 625000.0,
    "performance": {
        "top_speed": 340,
        "acceleration": 2.5,
        "horsepower": 986
    },
    "features": [
        {
            "name": "Hybrid Powertrain",
            "description": "Combines V8 engine with three electric motors"
        },
        {
            "name": "Active Aerodynamics",
            "description": "Adjustable rear spoiler for optimal downforce"
        }
    ]
}
```
