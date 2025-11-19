"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Develop a use case for a Geographic Information System (GIS) to manage and analyze geological and geotechnical data for construction projects, similar to those undertaken by URANPRES, s.r.o."
Generated: DETERMINISTIC_074c24ca2361e0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import json
from typing import List, Dict, Any

# Define the database schema for storing geological and geotechnical data
DATABASE_NAME = "gis_geotechnical_data.db"

def initialize_database():
    """
    Initialize the SQLite database and create necessary tables.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create a table for geological data
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS geological_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            rock_type TEXT NOT NULL,
            depth REAL NOT NULL,
            description TEXT
        )
        """)

        # Create a table for geotechnical data
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS geotechnical_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            soil_type TEXT NOT NULL,
            bearing_capacity REAL NOT NULL,
            water_table_depth REAL NOT NULL,
            description TEXT
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_geological_data(location: str, rock_type: str, depth: float, description: str = ""):
    """
    Add a new geological data entry to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO geological_data (location, rock_type, depth, description)
        VALUES (?, ?, ?, ?)
        """, (location, rock_type, depth, description))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding geological data: {e}")
    finally:
        conn.close()

def add_geotechnical_data(location: str, soil_type: str, bearing_capacity: float, water_table_depth: float, description: str = ""):
    """
    Add a new geotechnical data entry to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO geotechnical_data (location, soil_type, bearing_capacity, water_table_depth, description)
        VALUES (?, ?, ?, ?, ?)
        """, (location, soil_type, bearing_capacity, water_table_depth, description))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding geotechnical data: {e}")
    finally:
        conn.close()

def query_geological_data(location: str) -> List[Dict[str, Any]]:
    """
    Query geological data for a specific location.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM geological_data WHERE location = ?
        """, (location,))
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        data = [
            {"id": row[0], "location": row[1], "rock_type": row[2], "depth": row[3], "description": row[4]}
            for row in rows
        ]
        return data
    except sqlite3.Error as e:
        print(f"Error querying geological data: {e}")
        return []
    finally:
        conn.close()

def query_geotechnical_data(location: str) -> List[Dict[str, Any]]:
    """
    Query geotechnical data for a specific location.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM geotechnical_data WHERE location = ?
        """, (location,))
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        data = [
            {"id": row[0], "location": row[1], "soil_type": row[2], "bearing_capacity": row[3], "water_table_depth": row[4], "description": row[5]}
            for row in rows
        ]
        return data
    except sqlite3.Error as e:
        print(f"Error querying geotechnical data: {e}")
        return []
    finally:
        conn.close()

def export_data_to_json(location: str, output_file: str):
    """
    Export geological and geotechnical data for a specific location to a JSON file.
    """
    try:
        geological_data = query_geological_data(location)
        geotechnical_data = query_geotechnical_data(location)

        combined_data = {
            "location": location,
            "geological_data": geological_data,
            "geotechnical_data": geotechnical_data
        }

        with open(output_file, "w") as file:
            json.dump(combined_data, file, indent=4)

        print(f"Data exported successfully to {output_file}")
    except Exception as e:
        print(f"Error exporting data to JSON: {e}")

# Main execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample data
    add_geological_data("Site A", "Granite", 50.0, "Hard rock suitable for foundation.")
    add_geotechnical_data("Site A", "Clay", 150.0, 10.0, "Moderate bearing capacity.")

    # Query and export data
    export_data_to_json("Site A", "site_a_data.json")
```
