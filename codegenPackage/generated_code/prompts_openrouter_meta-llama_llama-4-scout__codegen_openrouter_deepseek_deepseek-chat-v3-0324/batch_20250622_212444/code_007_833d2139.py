"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Create a RESTful API endpoint to retrieve product information for a specific category, such as 'Valves' or 'PEX F1960', from a construction supply company's database."
Generated: DETERMINISTIC_833d21393e272ebe
Batch ID: 20250622_212444
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
import sqlite3
import os

# Database setup
DATABASE_NAME = "construction_supply.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    if not os.path.exists(DATABASE_NAME):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                price REAL,
                stock_quantity INTEGER,
                sku TEXT UNIQUE
            )
        ''')
        # Insert sample data
        cursor.executemany('''
            INSERT INTO products (name, category, description, price, stock_quantity, sku)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', [
            ("Ball Valve", "Valves", "1/2 inch brass ball valve", 12.99, 50, "VAL-BALL-001"),
            ("Gate Valve", "Valves", "3/4 inch gate valve", 18.50, 30, "VAL-GATE-002"),
            ("PEX F1960", "PEX Fittings", "1/2 inch PEX crimp fitting", 1.25, 200, "PEX-1960-001"),
            ("PEX F1960", "PEX Fittings", "3/4 inch PEX crimp fitting", 1.75, 150, "PEX-1960-002")
        ])
        conn.commit()
        conn.close()

# Initialize the database
initialize_database()

# Pydantic models
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

# FastAPI app
app = FastAPI(
    title="Construction Supply API",
    description="API for retrieving construction supply product information",
    version="1.0.0"
)

@app.get("/products/{category}", response_model=List[Product], tags=["Products"])
def get_products_by_category(category: str):
    """
    Retrieve all products in a specific category.
    
    Parameters:
    - category: The product category to filter by (e.g., 'Valves', 'PEX F1960')
    
    Returns:
    - List of products in the specified category
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Case-insensitive search and sanitize input
        category = category.strip().lower()
        cursor.execute(
            "SELECT * FROM products WHERE LOWER(category) = ?",
            (category,)
        )
        
        products = cursor.fetchall()
        conn.close()
        
        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No products found in category '{category}'"
            )
            
        return [dict(product) for product in products]
        
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
