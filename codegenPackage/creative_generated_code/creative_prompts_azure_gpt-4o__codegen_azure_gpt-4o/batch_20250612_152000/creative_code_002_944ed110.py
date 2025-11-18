"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Recommend an API or library to implement a search feature for automotive parts based on product codes, similar to the functionality on "autopecasbrazz."
Generated: DETERMINISTIC_944ed1106da45f74
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a search feature for automotive parts based on product codes
using the FastAPI framework and SQLite database for simplicity. It provides endpoints
to search parts by product code and retrieve details. Proper error handling has been implemented.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import sqlite3

# Initialize FastAPI application
app = FastAPI()

# Database connection function
def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        connection = sqlite3.connect('automotive_parts.db')
        connection.row_factory = sqlite3.Row  # Allows us to return rows as dicts
        return connection
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

# Pydantic model for API response
class Part(BaseModel):
    product_code: str
    name: str
    description: str
    price: float

# API endpoint to search parts by product code
@app.get("/search/", response_model=Part)
async def search_part(product_code: str = Query(..., description="Product code to search for")):
    """
    Search for an automotive part by its product code.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Execute query to find the part by product code
        cursor.execute("SELECT * FROM parts WHERE product_code = ?", (product_code,))
        part_data = cursor.fetchone()

        if part_data is None:
            raise HTTPException(status_code=404, detail="Part not found")

        # Convert database row into response format
        part = Part(
            product_code=part_data["product_code"],
            name=part_data["name"],
            description=part_data["description"],
            price=part_data["price"]
        )
        return part

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

    finally:
        connection.close()

# Function to initialize database with sample data (for demonstration purposes)
def initialize_database():
    """
    Initialize the SQLite database and create the parts table.
    Populate the database with sample data.
    """
    connection = sqlite3.connect('automotive_parts.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parts (
        product_code TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)

    # Sample data
    sample_data = [
        ("ABC123", "Brake Pad", "High-quality brake pad", 29.99),
        ("XYZ789", "Oil Filter", "Durable oil filter", 15.50),
        ("LMN456", "Car Battery", "Long-lasting car battery", 120.00)
    ]

    cursor.executemany("INSERT OR IGNORE INTO parts (product_code, name, description, price) VALUES (?, ?, ?, ?)", sample_data)
    connection.commit()
    connection.close()

# Initialize database at startup
initialize_database()
```

### Notes:
1. To run this script, install FastAPI (`pip install fastapi`) and an ASGI server like Uvicorn (`pip install uvicorn`).
2. Launch the app using `uvicorn filename:app --reload`, where `filename` is the name of your Python file.
3. The database initialization function creates a SQLite database and prepopulates it with sample data. This is for demonstration purposes only and should be replaced with real data for production use.
