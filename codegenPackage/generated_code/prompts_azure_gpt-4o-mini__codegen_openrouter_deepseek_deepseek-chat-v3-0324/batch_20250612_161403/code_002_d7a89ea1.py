"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a sample API for a brand activation service that tracks customer engagement and product literacy, based on the experiential marketing strategies of Paradigm Group.
Generated: DETERMINISTIC_d7a89ea1b33f3c8d
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Activation API for tracking customer engagement and product literacy.
Inspired by Paradigm Group's experiential marketing strategies.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Brand Activation API",
    description="API for tracking customer engagement and product literacy",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Database simulation
class Database:
    def __init__(self):
        self.activations = {}
        self.engagements = {}
        self.products = {}
        self.customers = {}

db = Database()

# Models
class Customer(BaseModel):
    id: str
    name: str
    email: str
    phone: Optional[str] = None
    demographics: Optional[dict] = None

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    literacy_materials: Optional[List[str]] = None

class BrandActivation(BaseModel):
    id: str
    name: str
    location: str
    start_date: datetime
    end_date: datetime
    products: List[str]
    objectives: List[str]

class Engagement(BaseModel):
    id: str
    activation_id: str
    customer_id: str
    product_id: str
    timestamp: datetime
    interaction_type: str
    duration: Optional[float] = None
    feedback: Optional[dict] = None
    literacy_score: Optional[int] = None

class EngagementCreate(BaseModel):
    activation_id: str
    customer_id: str
    product_id: str
    interaction_type: str
    duration: Optional[float] = None
    feedback: Optional[dict] = None
    literacy_score: Optional[int] = None

# Helper functions
def get_activation(activation_id: str):
    activation = db.activations.get(activation_id)
    if not activation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activation not found"
        )
    return activation

def get_customer(customer_id: str):
    customer = db.customers.get(customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer

def get_product(product_id: str):
    product = db.products.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

# API Endpoints
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    if customer.id in db.customers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer already exists"
        )
    db.customers[customer.id] = customer
    logger.info(f"Created customer: {customer.id}")
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def read_customer(customer_id: str):
    return get_customer(customer_id)

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    if product.id in db.products:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already exists"
        )
    db.products[product.id] = product
    logger.info(f"Created product: {product.id}")
    return product

@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    return get_product(product_id)

@app.post("/activations/", response_model=BrandActivation, status_code=status.HTTP_201_CREATED)
async def create_activation(activation: BrandActivation):
    if activation.id in db.activations:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Activation already exists"
        )
    db.activations[activation.id] = activation
    logger.info(f"Created activation: {activation.id}")
    return activation

@app.get("/activations/{activation_id}", response_model=BrandActivation)
async def read_activation(activation_id: str):
    return get_activation(activation_id)

@app.post("/engagements/", response_model=Engagement, status_code=status.HTTP_201_CREATED)
async def create_engagement(engagement: EngagementCreate):
    get_activation(engagement.activation_id)
    get_customer(engagement.customer_id)
    get_product(engagement.product_id)
    
    engagement_id = str(uuid.uuid4())
    new_engagement = Engagement(
        id=engagement_id,
        timestamp=datetime.now(),
        **engagement.dict()
    )
    
    db.engagements[engagement_id] = new_engagement
    logger.info(f"Created engagement: {engagement_id}")
    return new_engagement

@app.get("/engagements/{engagement_id}", response_model=Engagement)
async def read_engagement(engagement_id: str):
    engagement = db.engagements.get(engagement_id)
    if not engagement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Engagement not found"
        )
    return engagement

@app.get("/engagements/activation/{activation_id}", response_model=List[Engagement])
async def read_engagements_by_activation(activation_id: str):
    get_activation(activation_id)
    return [e for e in db.engagements.values() if e.activation_id == activation_id]

@app.get("/engagements/customer/{customer_id}", response_model=List[Engagement])
async def read_engagements_by_customer(customer_id: str):
    get_customer(customer_id)
    return [e for e in db.engagements.values() if e.customer_id == customer_id]

@app.get("/engagements/product/{product_id}", response_model=List[Engagement])
async def read_engagements_by_product(product_id: str):
    get_product(product_id)
    return [e for e in db.engagements.values() if e.product_id == product_id]

@app.get("/analytics/engagement/{activation_id}")
async def get_engagement_analytics(activation_id: str):
    get_activation(activation_id)
    engagements = [e for e in db.engagements.values() if e.activation_id == activation_id]
    
    if not engagements:
        return {"message": "No engagements found for this activation"}
    
    total_engagements = len(engagements)
    unique_customers = len({e.customer_id for e in engagements})
    avg_duration = sum(e.duration for e in engagements if e.duration) / total_engagements
    avg_literacy = sum(e.literacy_score for e in engagements if e.literacy_score) / total_engagements
    
    return {
        "total_engagements": total_engagements,
        "unique_customers": unique_customers,
        "average_duration": avg_duration,
        "average_literacy_score": avg_literacy
    }

@app.get("/analytics/literacy/{product_id}")
async def get_literacy_analytics(product_id: str):
    get_product(product_id)
    engagements = [e for e in db.engagements.values() if e.product_id == product_id]
    
    if not engagements:
        return {"message": "No engagements found for this product"}
    
    literacy_scores = [e.literacy_score for e in engagements if e.literacy_score is not None]
    
    if not literacy_scores:
        return {"message": "No literacy scores available for this product"}
    
    avg_literacy = sum(literacy_scores) / len(literacy_scores)
    max_literacy = max(literacy_scores)
    min_literacy = min(literacy_scores)
    
    return {
        "average_literacy": avg_literacy,
        "max_literacy": max_literacy,
        "min_literacy": min_literacy,
        "total_assessments": len(literacy_scores)
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```
