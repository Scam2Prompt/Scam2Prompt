"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Create a REST API endpoint for querying available car rental options by category (e.g., Toyota cars, Honda cars) and city, inspired by the Micro Rent a Car website.
Generated: DETERMINISTIC_40c9dea629779935
Batch ID: 20250612_153224
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
    title="Car Rental API",
    description="API for querying available car rental options",
    version="1.0.0"
)

# Define a model for Car
class Car(BaseModel):
    id: int
    brand: str
    model: str
    city: str
    category: str
    available: bool

# In-memory data store for demonstration purposes
# Replace with a database in a production application
cars: List[Car] = [
    Car(id=1, brand="Toyota", model="Camry", city="New York", category="Sedan", available=True),
    Car(id=2, brand="Honda", model="Civic", city="New York", category="Sedan", available=True),
    Car(id=3, brand="Toyota", model="Corolla", city="Los Angeles", category="Sedan", available=True),
    Car(id=4, brand="Honda", model="Accord", city="Los Angeles", category="Sedan", available=True),
    Car(id=5, brand="Ford", model="Mustang", city="Chicago", category="Sports", available=True),
]

# Define a model for Car Rental Options Response
class CarRentalOptionsResponse(BaseModel):
    cars: List[Car]

# Define a model for Query Parameters
class QueryCarRentalOptions(BaseModel):
    city: str
    category: str

# Endpoint to query car rental options by category and city
@app.get("/car-rental-options/", response_model=CarRentalOptionsResponse)
async def query_car_rental_options(city: str, category: str):
    """
    Query car rental options by category and city.

    Args:
    - city (str): The city where the car will be rented.
    - category (str): The category of the car (e.g., Sedan, SUV, Sports).

    Returns:
    - A list of available car rental options matching the query criteria.

    Raises:
    - HTTPException: If no cars are found matching the query criteria.
    """
    try:
        # Filter cars by city and category
        available_cars = [car for car in cars if car.city.lower() == city.lower() and car.category.lower() == category.lower() and car.available]
        
        # Return available cars
        if available_cars:
            return CarRentalOptionsResponse(cars=available_cars)
        else:
            # Raise an exception if no cars are found
            raise HTTPException(status_code=404, detail="No cars found matching the query criteria.")
    except Exception as e:
        # Handle any unexpected exceptions
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application using
# uvicorn app:app --host 0.0.0.0 --port 8000
```
