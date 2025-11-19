"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Create a RESTful API endpoint that accepts user input (e.g., property type, location) and returns a list of properties that match the criteria, using a database that is familiar with local and regional planning policies.
Generated: DETERMINISTIC_3232ab8df15d3842
Batch ID: 20250622_210703
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
from typing import Optional, List
import sqlite3
from contextlib import closing

app = FastAPI()

# Database configuration
DATABASE = "property_db.sqlite"

# Pydantic models for request/response
class PropertyCriteria(BaseModel):
    property_type: Optional[str] = None
    location: Optional[str] = None
    min_bedrooms: Optional[int] = None
    max_bedrooms: Optional[int] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None

class Property(BaseModel):
    id: int
    property_type: str
    location: str
    bedrooms: int
    price: float
    description: str
    planning_policy: str

# Database initialization
def init_db():
    with closing(sqlite3.connect(DATABASE)) as conn:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    property_type TEXT NOT NULL,
                    location TEXT NOT NULL,
                    bedrooms INTEGER NOT NULL,
                    price REAL NOT NULL,
                    description TEXT,
                    planning_policy TEXT NOT NULL
                )
            """)

# Helper function to execute database queries
def execute_query(query: str, params: tuple = ()):
    try:
        with closing(sqlite3.connect(DATABASE)) as conn:
            conn.row_factory = sqlite3.Row
            with conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/properties/", response_model=List[Property])
async def get_properties(
    property_type: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    min_bedrooms: Optional[int] = Query(None, ge=0),
    max_bedrooms: Optional[int] = Query(None, ge=0),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0)
):
    """
    Retrieve properties matching the specified criteria.
    """
    query = "SELECT * FROM properties WHERE 1=1"
    params = []
    
    if property_type:
        query += " AND property_type = ?"
        params.append(property_type)
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if min_bedrooms is not None:
        query += " AND bedrooms >= ?"
        params.append(min_bedrooms)
    if max_bedrooms is not None:
        query += " AND bedrooms <= ?"
        params.append(max_bedrooms)
    if min_price is not None:
        query += " AND price >= ?"
        params.append(min_price)
    if max_price is not None:
        query += " AND price <= ?"
        params.append(max_price)
    
    try:
        results = execute_query(query, tuple(params))
        return [dict(row) for row in results]
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/properties/search", response_model=List[Property])
async def search_properties(criteria: PropertyCriteria):
    """
    Search properties using a JSON payload with search criteria.
    """
    query = "SELECT * FROM properties WHERE 1=1"
    params = []
    
    if criteria.property_type:
        query += " AND property_type = ?"
        params.append(criteria.property_type)
    if criteria.location:
        query += " AND location LIKE ?"
        params.append(f"%{criteria.location}%")
    if criteria.min_bedrooms is not None:
        query += " AND bedrooms >= ?"
        params.append(criteria.min_bedrooms)
    if criteria.max_bedrooms is not None:
        query += " AND bedrooms <= ?"
        params.append(criteria.max_bedrooms)
    if criteria.min_price is not None:
        query += " AND price >= ?"
        params.append(criteria.min_price)
    if criteria.max_price is not None:
        query += " AND price <= ?"
        params.append(criteria.max_price)
    
    try:
        results = execute_query(query, tuple(params))
        return [dict(row) for row in results]
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Sample data insertion endpoint (for testing)
@app.post("/properties/sample-data")
async def insert_sample_data():
    """
    Insert sample property data into the database (for testing purposes).
    """
    sample_data = [
        ("House", "London", 3, 500000.0, "Beautiful family home", "Residential Zone A"),
        ("Apartment", "Manchester", 2, 250000.0, "Modern city apartment", "Mixed Use Zone B"),
        ("Cottage", "Cotswolds", 2, 350000.0, "Charming countryside cottage", "Green Belt"),
        ("Flat", "Birmingham", 1, 150000.0, "City center flat", "High Density Residential"),
        ("Villa", "Edinburgh", 4, 750000.0, "Luxury villa with views", "Residential Zone C")
    ]
    
    try:
        with closing(sqlite3.connect(DATABASE)) as conn:
            with conn:
                conn.executemany(
                    "INSERT INTO properties (property_type, location, bedrooms, price, description, planning_policy) VALUES (?, ?, ?, ?, ?, ?)",
                    sample_data
                )
        return {"message": "Sample data inserted successfully"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
```
