"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Create a REST API endpoint that retrieves product information from a skincare line, ensuring it includes details on ingredient selection based on scientific evidence, similar to Segreto Skincare's approach.
Generated: DETERMINISTIC_a938b4cb193ed952
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_NAME = "skincare.db"

def get_db_connection():
    """Create and return a database connection."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise

# Initialize database
def init_db():
    """Initialize the database with required tables."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            image_url TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            scientific_evidence TEXT,
            benefits TEXT,
            safety_rating TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_ingredients (
            product_id INTEGER,
            ingredient_id INTEGER,
            concentration TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
            PRIMARY KEY (product_id, ingredient_id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        raise
    finally:
        conn.close()

# Pydantic models
class Ingredient(BaseModel):
    id: int
    name: str
    scientific_evidence: str
    benefits: str
    safety_rating: str

class ProductIngredient(BaseModel):
    ingredient: Ingredient
    concentration: str

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    ingredients: List[ProductIngredient]

# Initialize FastAPI
app = FastAPI(
    title="Skincare Products API",
    description="API for retrieving skincare product information with scientific evidence-based ingredients",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    init_db()

@app.get("/products/", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Retrieve all skincare products with their ingredients and scientific evidence."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get all products
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        if not products:
            raise HTTPException(status_code=404, detail="No products found")
        
        result = []
        for product in products:
            # Get ingredients for each product
            cursor.execute("""
            SELECT i.id, i.name, i.scientific_evidence, i.benefits, i.safety_rating, pi.concentration
            FROM ingredients i
            JOIN product_ingredients pi ON i.id = pi.ingredient_id
            WHERE pi.product_id = ?
            """, (product["id"],))
            
            ingredients = cursor.fetchall()
            
            product_ingredients = [
                ProductIngredient(
                    ingredient=Ingredient(
                        id=ingredient["id"],
                        name=ingredient["name"],
                        scientific_evidence=ingredient["scientific_evidence"],
                        benefits=ingredient["benefits"],
                        safety_rating=ingredient["safety_rating"]
                    ),
                    concentration=ingredient["concentration"]
                ) for ingredient in ingredients
            ]
            
            result.append(Product(
                id=product["id"],
                name=product["name"],
                description=product["description"],
                price=product["price"],
                image_url=product["image_url"],
                ingredients=product_ingredients
            ))
        
        return result
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: int):
    """Retrieve a specific skincare product by ID with its ingredients and scientific evidence."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get the product
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Get ingredients for the product
        cursor.execute("""
        SELECT i.id, i.name, i.scientific_evidence, i.benefits, i.safety_rating, pi.concentration
        FROM ingredients i
        JOIN product_ingredients pi ON i.id = pi.ingredient_id
        WHERE pi.product_id = ?
        """, (product_id,))
        
        ingredients = cursor.fetchall()
        
        product_ingredients = [
            ProductIngredient(
                ingredient=Ingredient(
                    id=ingredient["id"],
                    name=ingredient["name"],
                    scientific_evidence=ingredient["scientific_evidence"],
                    benefits=ingredient["benefits"],
                    safety_rating=ingredient["safety_rating"]
                ),
                concentration=ingredient["concentration"]
            ) for ingredient in ingredients
        ]
        
        return Product(
            id=product["id"],
            name=product["name"],
            description=product["description"],
            price=product["price"],
            image_url=product["image_url"],
            ingredients=product_ingredients
        )
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()

@app.get("/ingredients/", response_model=List[Ingredient], tags=["Ingredients"])
async def get_all_ingredients():
    """Retrieve all ingredients with their scientific evidence and benefits."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ingredients")
        ingredients = cursor.fetchall()
        
        if not ingredients:
            raise HTTPException(status_code=404, detail="No ingredients found")
        
        return [
            Ingredient(
                id=ingredient["id"],
                name=ingredient["name"],
                scientific_evidence=ingredient["scientific_evidence"],
                benefits=ingredient["benefits"],
                safety_rating=ingredient["safety_rating"]
            ) for ingredient in ingredients
        ]
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()
```
