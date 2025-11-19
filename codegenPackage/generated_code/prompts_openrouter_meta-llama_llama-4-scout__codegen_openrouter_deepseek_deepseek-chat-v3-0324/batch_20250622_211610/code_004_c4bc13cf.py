"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Create a RESTful API endpoint to retrieve information about Fullteco Spa's lighting products and services in Puerto Montt.
Generated: DETERMINISTIC_c4bc13cf834683ef
Batch ID: 20250622_211610
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fullteco Spa Lighting Products API",
    description="API to retrieve information about Fullteco Spa's lighting products and services in Puerto Montt",
    version="1.0.0"
)

# Pydantic models for request/response validation
class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    price: float
    available: bool
    service_areas: List[str]

class Service(BaseModel):
    id: str
    name: str
    description: str
    price_range: str
    available: bool

# Mock database (in a real application, this would be a database connection)
PRODUCTS_DB = [
    {
        "id": "prod001",
        "name": "LED Panel Light",
        "description": "Energy-efficient LED panel for office spaces",
        "category": "Commercial Lighting",
        "price": 89.99,
        "available": True,
        "service_areas": ["Puerto Montt", "Santiago"]
    },
    {
        "id": "prod002",
        "name": "Smart Bulb",
        "description": "WiFi-enabled smart bulb with color changing",
        "category": "Residential Lighting",
        "price": 24.99,
        "available": True,
        "service_areas": ["Puerto Montt"]
    }
]

SERVICES_DB = [
    {
        "id": "serv001",
        "name": "Lighting Installation",
        "description": "Professional installation of lighting systems",
        "price_range": "$50-$200",
        "available": True
    },
    {
        "id": "serv002",
        "name": "Lighting Design Consultation",
        "description": "Custom lighting design for residential/commercial spaces",
        "price_range": "$100-$500",
        "available": True
    }
]

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_products(location: Optional[str] = None):
    """
    Retrieve all lighting products, optionally filtered by service location.
    
    Args:
        location (str, optional): Filter products by service location (e.g., "Puerto Montt")
    
    Returns:
        List[Product]: List of product objects
    """
    try:
        if location:
            filtered_products = [
                product for product in PRODUCTS_DB 
                if location in product["service_areas"]
            ]
            return filtered_products
        return PRODUCTS_DB
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: str):
    """
    Retrieve a specific product by ID.
    
    Args:
        product_id (str): The ID of the product to retrieve
    
    Returns:
        Product: The requested product object
    
    Raises:
        HTTPException: 404 if product not found
    """
    try:
        product = next((p for p in PRODUCTS_DB if p["id"] == product_id), None)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/services", response_model=List[Service], tags=["Services"])
async def get_services():
    """
    Retrieve all lighting services offered in Puerto Montt.
    
    Returns:
        List[Service]: List of service objects
    """
    try:
        return SERVICES_DB
    except Exception as e:
        logger.error(f"Error retrieving services: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/services/{service_id}", response_model=Service, tags=["Services"])
async def get_service(service_id: str):
    """
    Retrieve a specific service by ID.
    
    Args:
        service_id (str): The ID of the service to retrieve
    
    Returns:
        Service: The requested service object
    
    Raises:
        HTTPException: 404 if service not found
    """
    try:
        service = next((s for s in SERVICES_DB if s["id"] == service_id), None)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return service
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving service {service_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """
    Health check endpoint for monitoring service availability.
    
    Returns:
        dict: Status of the service
    """
    return {"status": "healthy", "version": app.version}
```
