"""
Generated Code Metadata:
========================
Original URL: https://tudulcepecado.cl
Prompt: Design an API for a sex toy recommendation system, taking into account user preferences and product categories like those on Tu Dulce Pecado.
Generated: DETERMINISTIC_f1e1f76acf9b5369
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import logging
from uuid import UUID, uuid4

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sex Toy Recommendation API",
    description="API for personalized sex toy recommendations",
    version="1.0.0"
)

# Enums for product categories and preferences
class ProductCategory(str, Enum):
    VIBRATORS = "vibrators"
    DILDOS = "dildos"
    ANAL_TOYS = "anal_toys"
    COUPLES_TOYS = "couples_toys"
    BDSM = "bdsm"
    LINGERIE = "lingerie"
    LUBRICANTS = "lubricants"

class MaterialPreference(str, Enum):
    SILICONE = "silicone"
    METAL = "metal"
    GLASS = "glass"
    RUBBER = "rubber"
    TPE = "tpe"
    NO_PREFERENCE = "no_preference"

class SizePreference(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"
    NO_PREFERENCE = "no_preference"

class PriceRange(str, Enum):
    BUDGET = "budget"
    MID_RANGE = "mid_range"
    PREMIUM = "premium"
    NO_PREFERENCE = "no_preference"

# Models
class UserPreferences(BaseModel):
    categories: List[ProductCategory] = Field(..., description="Preferred product categories")
    material: MaterialPreference = Field(MaterialPreference.NO_PREFERENCE, description="Material preference")
    size: SizePreference = Field(SizePreference.NO_PREFERENCE, description="Size preference")
    price_range: PriceRange = Field(PriceRange.NO_PREFERENCE, description="Price range preference")
    sensitive: bool = Field(False, description="Whether the user has sensitivity concerns")

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique product identifier")
    name: str = Field(..., min_length=1, max_length=100, description="Product name")
    category: ProductCategory = Field(..., description="Product category")
    material: str = Field(..., min_length=1, max_length=50, description="Product material")
    size: str = Field(..., min_length=1, max_length=20, description="Product size")
    price: float = Field(..., gt=0, description="Product price in USD")
    description: Optional[str] = Field(None, max_length=500, description="Product description")
    sensitive_friendly: bool = Field(False, description="Whether the product is suitable for sensitive users")

class RecommendationRequest(BaseModel):
    user_id: UUID = Field(..., description="Unique user identifier")
    preferences: UserPreferences = Field(..., description="User preferences for recommendations")
    limit: int = Field(10, ge=1, le=50, description="Maximum number of recommendations to return")

class RecommendationResponse(BaseModel):
    recommendations: List[Product] = Field(..., description="List of recommended products")
    user_id: UUID = Field(..., description="User identifier")

# Mock database
class Database:
    def __init__(self):
        self.products = [
            Product(
                name="Slim G-Spot Vibrator",
                category=ProductCategory.VIBRATORS,
                material="silicone",
                size="medium",
                price=49.99,
                description="Perfect for G-spot stimulation",
                sensitive_friendly=True
            ),
            Product(
                name="Premium Silicone Dildo",
                category=ProductCategory.DILDOS,
                material="silicone",
                size="large",
                price=79.99,
                description="Luxury feel with realistic texture",
                sensitive_friendly=True
            ),
            Product(
                name="Anal Training Kit",
                category=ProductCategory.ANAL_TOYS,
                material="silicone",
                size="small",
                price=59.99,
                description="Beginner-friendly anal toy set"
            )
        ]

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        return [p for p in self.products if p.category == category]

    def get_all_products(self) -> List[Product]:
        return self.products

db = Database()

# Helper functions
def filter_by_preferences(products: List[Product], preferences: UserPreferences) -> List[Product]:
    filtered = []
    
    for product in products:
        # Category filter
        if product.category not in preferences.categories:
            continue
            
        # Material filter
        if (preferences.material != MaterialPreference.NO_PREFERENCE and 
            product.material.lower() != preferences.material.value):
            continue
            
        # Size filter
        if (preferences.size != SizePreference.NO_PREFERENCE and 
            product.size.lower() != preferences.size.value):
            continue
            
        # Price range filter (simplified)
        if preferences.price_range != PriceRange.NO_PREFERENCE:
            if preferences.price_range == PriceRange.BUDGET and product.price > 50:
                continue
            elif preferences.price_range == PriceRange.MID_RANGE and (product.price <= 50 or product.price > 100):
                continue
            elif preferences.price_range == PriceRange.PREMIUM and product.price <= 100:
                continue
                
        # Sensitivity filter
        if preferences.sensitive and not product.sensitive_friendly:
            continue
            
        filtered.append(product)
    
    return filtered

# API endpoints
@app.post("/recommendations", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """
    Get personalized product recommendations based on user preferences.
    """
    try:
        all_products = db.get_all_products()
        filtered_products = filter_by_preferences(all_products, request.preferences)
        
        if not filtered_products:
            logger.warning(f"No products found matching preferences for user {request.user_id}")
            raise HTTPException(status_code=404, detail="No products match your preferences")
        
        # Sort by price ascending as default
        sorted_products = sorted(filtered_products, key=lambda x: x.price)
        
        # Return limited number of recommendations
        recommendations = sorted_products[:request.limit]
        
        return RecommendationResponse(
            recommendations=recommendations,
            user_id=request.user_id
        )
        
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products", response_model=List[Product])
async def list_products(category: Optional[ProductCategory] = None):
    """
    List all products, optionally filtered by category.
    """
    try:
        if category:
            return db.get_products_by_category(category)
        return db.get_all_products()
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: UUID):
    """
    Get details for a specific product by ID.
    """
    try:
        for product in db.get_all_products():
            if product.id == product_id:
                return product
        raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```
