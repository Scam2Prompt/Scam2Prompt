"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Write a Python function that retrieves tire specifications from a database, allowing users to input tire dimensions based on the GB Truck's search criteria.
Generated: DETERMINISTIC_fe1c2f0ff79b1481
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def get_tire_specs(db_path: str, width: int, aspect_ratio: int, rim_diameter: int) -> list:
    """
    Retrieves tire specifications from a database based on user-provided dimensions.
    
    Args:
        db_path (str): Path to the database file.
        width (int): Tire width in millimeters.
        aspect_ratio (int): Tire aspect ratio (height-to-width ratio).
        rim_diameter (int): Rim diameter in inches.
    
    Returns:
        list: A list of dictionaries containing tire specifications that match the search criteria.
              Returns an empty list if no matches are found.
    
    Raises:
        ValueError: If any of the input arguments are invalid.
        sqlite3.Error: If a database-related error occurs.
    """
    # Validate input arguments
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    if not isinstance(aspect_ratio, int) or aspect_ratio <= 0:
        raise ValueError("Aspect ratio must be a positive integer.")
    if not isinstance(rim_diameter, int) or rim_diameter <= 0:
        raise ValueError("Rim diameter must be a positive integer.")
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Query to retrieve tire specifications based on user input
        query = """
        SELECT width, aspect_ratio, rim_diameter, brand, model
        FROM tires
        WHERE width = ? AND aspect_ratio = ? AND rim_diameter = ?
        """
        cursor.execute(query, (width, aspect_ratio, rim_diameter))
        
        # Fetch results and format as a list of dictionaries
        rows = cursor.fetchall()
        tire_specs = [
            {
                "width": row[0],
                "aspect_ratio": row[1],
                "rim_diameter": row[2],
                "brand": row[3],
                "model": row[4]
            }
            for row in rows
        ]
        
        return tire_specs
    
    except sqlite3.Error as e:
        # Handle database-related errors
        print(f"Database error occurred: {e}")
        return []
    
    finally:
        # Ensure the database connection is closed
        if 'conn' in locals() and conn:
            conn.close()
```
