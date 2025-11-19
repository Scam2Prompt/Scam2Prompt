"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.io
Prompt: Design an API endpoint to retrieve information on different types of investment products (e.g., stocks, bonds, cryptocurrencies) and their associated risks, as per Arbiquant's focus on financial education.
Generated: DETERMINISTIC_617520019ed53e45
Batch ID: 20250622_211310
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
from enum import Enum

app = FastAPI(
    title="Arbiquant Investment Products API",
    description="API for retrieving information on investment products and their risks",
    version="1.0.0"
)

class ProductType(str, Enum):
    STOCK = "stock"
    BOND = "bond"
    CRYPTOCURRENCY = "cryptocurrency"
    ETF = "etf"
    MUTUAL_FUND = "mutual_fund"

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"

class InvestmentProduct(BaseModel):
    id: str
    name: str
    type: ProductType
    description: str
    risk_level: RiskLevel
    typical_return: Optional[float] = None
    volatility: Optional[float] = None
    liquidity: Optional[str] = None

# Mock database of investment products
investment_products_db = [
    InvestmentProduct(
        id="stock_1",
        name="Blue Chip Stocks",
        type=ProductType.STOCK,
        description="Shares of large, established companies with stable earnings",
        risk_level=RiskLevel.MEDIUM,
        typical_return=7.0,
        volatility=15.0,
        liquidity="high"
    ),
    InvestmentProduct(
        id="bond_1",
        name="Government Bonds",
        type=ProductType.BOND,
        description="Debt securities issued by governments",
        risk_level=RiskLevel.LOW,
        typical_return=3.0,
        volatility=5.0,
        liquidity="medium"
    ),
    InvestmentProduct(
        id="crypto_1",
        name="Bitcoin",
        type=ProductType.CRYPTO,
        description="Decentralized digital currency",
        risk_level=RiskLevel.VERY_HIGH,
        typical_return=None,
        volatility=80.0,
        liquidity="varies"
    )
]

@app.get("/products", response_model=List[InvestmentProduct], tags=["Products"])
async def get_all_products():
    """
    Retrieve all available investment products
    """
    return investment_products_db

@app.get("/products/{product_id}", response_model=InvestmentProduct, tags=["Products"])
async def get_product_by_id(product_id: str):
    """
    Retrieve a specific investment product by ID
    
    Args:
        product_id: The unique identifier for the investment product
    """
    product = next((p for p in investment_products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/type/{product_type}", response_model=List[InvestmentProduct], tags=["Products"])
async def get_products_by_type(product_type: ProductType):
    """
    Retrieve investment products by type
    
    Args:
        product_type: The type of investment product (stock, bond, etc.)
    """
    products = [p for p in investment_products_db if p.type == product_type]
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No products found for type {product_type}"
        )
    return products

@app.get("/products/risk/{risk_level}", response_model=List[InvestmentProduct], tags=["Products"])
async def get_products_by_risk(risk_level: RiskLevel):
    """
    Retrieve investment products by risk level
    
    Args:
        risk_level: The risk level of the investment product
    """
    products = [p for p in investment_products_db if p.risk_level == risk_level]
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No products found with risk level {risk_level}"
        )
    return products
```
