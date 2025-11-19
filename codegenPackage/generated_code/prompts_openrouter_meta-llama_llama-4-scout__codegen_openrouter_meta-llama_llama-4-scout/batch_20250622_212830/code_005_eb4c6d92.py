"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Design a simple API to manage roofing services, including scheduling inspections, requesting estimates, and tracking customer reviews, inspired by King Roofing's customer experience.
Generated: DETERMINISTIC_eb4c6d92e693d853
Batch ID: 20250622_212830
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000/docs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/inspections/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/customers/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/reviews/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/estimates/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# roofing_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Roofing Services API",
    description="Manage roofing services, including scheduling inspections, requesting estimates, and tracking customer reviews.",
    version="1.0.0"
)

# Define models
class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Inspection(BaseModel):
    id: int
    customer_id: int
    date: datetime
    status: str

class Estimate(BaseModel):
    id: int
    inspection_id: int
    cost: float
    description: str

class Review(BaseModel):
    id: int
    customer_id: int
    rating: int
    comment: str

# In-memory data store (replace with a database in production)
customers: List[Customer] = []
inspections: List[Inspection] = []
estimates: List[Estimate] = []
reviews: List[Review] = []

# API Endpoints
@app.post("/customers/", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    customers.append(customer)
    return customer

@app.get("/customers/", status_code=status.HTTP_200_OK)
async def read_customers():
    return customers

@app.get("/customers/{customer_id}", status_code=status.HTTP_200_OK)
async def read_customer(customer_id: int):
    customer = next((c for c in customers if c.id == customer_id), None)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@app.post("/inspections/", status_code=status.HTTP_201_CREATED)
async def schedule_inspection(inspection: Inspection):
    inspections.append(inspection)
    return inspection

@app.get("/inspections/", status_code=status.HTTP_200_OK)
async def read_inspections():
    return inspections

@app.get("/inspections/{inspection_id}", status_code=status.HTTP_200_OK)
async def read_inspection(inspection_id: int):
    inspection = next((i for i in inspections if i.id == inspection_id), None)
    if inspection is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inspection not found")
    return inspection

@app.post("/estimates/", status_code=status.HTTP_201_CREATED)
async def request_estimate(estimate: Estimate):
    estimates.append(estimate)
    return estimate

@app.get("/estimates/", status_code=status.HTTP_200_OK)
async def read_estimates():
    return estimates

@app.get("/estimates/{estimate_id}", status_code=status.HTTP_200_OK)
async def read_estimate(estimate_id: int):
    estimate = next((e for e in estimates if e.id == estimate_id), None)
    if estimate is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estimate not found")
    return estimate

@app.post("/reviews/", status_code=status.HTTP_201_CREATED)
async def create_review(review: Review):
    reviews.append(review)
    return review

@app.get("/reviews/", status_code=status.HTTP_200_OK)
async def read_reviews():
    return reviews

@app.get("/reviews/{review_id}", status_code=status.HTTP_200_OK)
async def read_review(review_id: int):
    review = next((r for r in reviews if r.id == review_id), None)
    if review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py

from roofing_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### API Documentation

*   **Customers**
    *   `POST /customers/`: Create a new customer
    *   `GET /customers/`: Read all customers
    *   `GET /customers/{customer_id}`: Read a customer by ID
*   **Inspections**
    *   `POST /inspections/`: Schedule a new inspection
    *   `GET /inspections/`: Read all inspections
    *   `GET /inspections/{inspection_id}`: Read an inspection by ID
*   **Estimates**
    *   `POST /estimates/`: Request a new estimate
    *   `GET /estimates/`: Read all estimates
    *   `GET /estimates/{estimate_id}`: Read an estimate by ID
*   **Reviews**
    *   `POST /reviews/`: Create a new review
    *   `GET /reviews/`: Read all reviews
    *   `GET /reviews/{review_id}`: Read a review by ID

### Running the API

To run the API, execute the following command:

```bash
python main.py
```

The API will be available at <http://localhost:8000/docs>. You can use a tool like curl or a REST client to interact with the API.

### Example Usage

Create a new customer:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "123-456-7890"}' http://localhost:8000/customers/
```

Schedule a new inspection:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "customer_id": 1, "date": "2024-09-16T10:00:00", "status": "pending"}' http://localhost:8000/inspections/
```

Request a new estimate:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "inspection_id": 1, "cost": 1000.0, "description": "Roof inspection and repair"}' http://localhost:8000/estimates/
```

Create a new review:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "customer_id": 1, "rating": 5, "comment": "Excellent service!"}' http://localhost:8000/reviews/
```
