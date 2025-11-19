"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Create a REST API endpoint that provides information on the benefits of using organic materials in mattresses, similar to those used in Spinetress products, and how they contribute to better sleep quality.
Generated: DETERMINISTIC_c648a66ab265c532
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI application
app = FastAPI(
    title="Organic Mattress Benefits API",
    description="Provides information on benefits of using organic materials in mattresses",
    version="1.0.0"
)

# Define a model for the response data
class MattressBenefit(BaseModel):
    id: int
    title: str
    description: str

# Define a model for the request query parameters
class MattressBenefitQuery(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 10

# In-memory data store for demonstration purposes
# Replace with a database connection in a production environment
mattress_benefits = [
    MattressBenefit(id=1, title="Breathability", description="Organic materials allow for better airflow and regulate body temperature"),
    MattressBenefit(id=2, title="Hypoallergenic", description="Organic materials reduce the risk of allergic reactions and respiratory issues"),
    MattressBenefit(id=3, title="Eco-Friendly", description="Organic materials are biodegradable and reduce environmental impact"),
    MattressBenefit(id=4, title="Durability", description="Organic materials are often more durable and long-lasting"),
    MattressBenefit(id=5, title="Sustainable", description="Organic materials promote sustainable farming practices and reduce carbon footprint"),
]

# Define the API endpoint
@app.get("/mattress-benefits/", response_model=list[MattressBenefit])
async def read_mattress_benefits(query: MattressBenefitQuery):
    try:
        # Paginate the results
        start = (query.page - 1) * query.limit
        end = start + query.limit
        return mattress_benefits[start:end]
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Define a detailed endpoint for a specific benefit
@app.get("/mattress-benefits/{benefit_id}", response_model=MattressBenefit)
async def read_mattress_benefit(benefit_id: int):
    try:
        # Find the benefit by ID
        benefit = next((b for b in mattress_benefits if b.id == benefit_id), None)
        if benefit is None:
            # Return a 404 error if the benefit is not found
            raise HTTPException(status_code=404, detail="Benefit not found")
        return benefit
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
