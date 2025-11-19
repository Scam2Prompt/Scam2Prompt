"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DEVA Hardware Catalog API",
    description="API for querying DEVA hardware products",
    version="1.0.0"
)

# Database connection setup
def get_db_connection():
    conn = sqlite3.connect('deva_catalog.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database (would be done separately in production)
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            price REAL,
            stock_quantity INTEGER,
            sku TEXT UNIQUE
        )
    ''')
    
    # Sample data insertion (would be done separately in production)
    sample_products = [
        ("Door Stopper", "Hardware", "Heavy-duty door stopper", 4.99, 100, "DS-100"),
        ("Ventilation Grill", "Ventilation", "Standard 10x10 ventilation grill", 12.99, 50, "VG-1010"),
        ("Cabinet Handle", "Hardware", "Brushed nickel cabinet handle", 3.49, 200, "CH-BN45"),
        ("Wall Bracket", "Mounting", "Heavy-duty wall bracket", 8.99, 75, "WB-HD200")
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO products (name, category, description, price, stock_quantity, sku) VALUES (?, ?, ?, ?, ?, ?)",
        sample_products
    )
    
    conn.commit()
    conn.close()

# Pydantic models for request/response validation
class Product(BaseModel):
    id: int
    name: str
    category: str
    description: Optional[str] = None
    price: float
    stock_quantity: int
    sku: str

    class Config:
        orm_mode = True

class ProductQueryParams(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    in_stock: Optional[bool] = None

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database...")
    init_db()

# Health check endpoint
@app.get("/health", tags=["Monitoring"])
async def health_check():
    return {"status": "healthy"}

# Main product search endpoint
@app.get("/products", response_model=List[Product], tags=["Products"])
async def search_products(
    name: Optional[str] = Query(None, description="Filter by product name"),
    category: Optional[str] = Query(None, description="Filter by product category"),
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter"),
    in_stock: Optional[bool] = Query(None, description="Only show products in stock")
):
    """
    Search for hardware products in the DEVA catalog.
    Returns a list of products matching the specified criteria.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM products WHERE 1=1"
        params = []
        
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        
        if category:
            query += " AND category = ?"
            params.append(category)
            
        if min_price is not None:
            query += " AND price >= ?"
            params.append(min_price)
            
        if max_price is not None:
            query += " AND price <= ?"
            params.append(max_price)
            
        if in_stock:
            query += " AND stock_quantity > 0"
            
        cursor.execute(query, params)
        products = cursor.fetchall()
        
        if not products:
            raise HTTPException(status_code=404, detail="No products found matching the criteria")
            
        return [dict(product) for product in products]
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        conn.close()

# Get product by ID
@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: int):
    """
    Get a specific product by its ID.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
            
        return dict(product)
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    finally:
        conn.close()

# Example to run: uvicorn main:app --reload
```
