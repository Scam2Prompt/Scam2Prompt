"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Recommend Python libraries for creating a searchable database of aroma materials, including features for filtering by type (e.g., fragrances, essential oils, specialty products) as seen on Karnataka Aromas' product lineup.
Generated: DETERMINISTIC_5ef872d399fc33db
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends Python libraries for creating a searchable database of aroma materials
and provides a basic implementation using SQLite and FastAPI for the backend with filtering capabilities.
"""

# Import required libraries
import sqlite3  # SQLite database for storage
from fastapi import FastAPI, HTTPException, Query
from typing import List

# Initialize FastAPI application
app = FastAPI()

# Database setup
DATABASE = "aroma_materials.db"

# Create the database and the table if not already created
def initialize_database():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # Create a table for aroma materials
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aroma_materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT
            )
        """)
        conn.commit()
    finally:
        conn.close()

initialize_database()

# Function to add aroma material to the database
@app.post("/add_aroma_material/")
def add_aroma_material(name: str, type: str, description: str = None):
    """
    API endpoint to add a new aroma material to the database.
    :param name: Name of the aroma material.
    :param type: Type of aroma material (e.g., fragrance, essential oil, etc.).
    :param description: Optional description of the material.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO aroma_materials (name, type, description) VALUES (?, ?, ?)", (name, type, description))
        conn.commit()
        return {"message": "Aroma material added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Function to search and filter aroma materials
@app.get("/search_aroma_materials/")
def search_aroma_materials(type: str = Query(None), name: str = Query(None)) -> List[dict]:
    """
    API endpoint to search aroma materials in the database with optional filtering by type and name.
    :param type: Filter by type of aroma material (e.g., fragrance, essential oil, etc.).
    :param name: Partial or full name to search aroma materials.
    :return: List of aroma materials matching the criteria.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Build the query dynamically based on filters
        query = "SELECT id, name, type, description FROM aroma_materials WHERE 1=1"
        params = []
        if type:
            query += " AND type = ?"
            params.append(type)
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        
        cursor.execute(query, params)
        rows = cursor.fetchall()

        # Format the result as a list of dictionaries
        result = [{"id": row[0], "name": row[1], "type": row[2], "description": row[3]} for row in rows]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Function to delete an aroma material by ID
@app.delete("/delete_aroma_material/{material_id}")
def delete_aroma_material(material_id: int):
    """
    API endpoint to delete an aroma material from the database by ID.
    :param material_id: ID of the aroma material to delete.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM aroma_materials WHERE id = ?", (material_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Aroma material not found.")
        conn.commit()
        return {"message": "Aroma material deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Main libraries used:
# 1. SQLite: Lightweight database to store aroma materials.
# 2. FastAPI: Framework to build APIs for data retrieval and manipulation.
# 3. Typing: Provides type hints for better code clarity and validation.
# 4. HTTPException: Handles errors gracefully.
```
