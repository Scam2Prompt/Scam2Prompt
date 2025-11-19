"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Write a Python script that fetches and displays pre-owned Royal Enfield motorcycle details from a dealership's database.
Generated: DETERMINISTIC_d2309d9901b0d6b2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict

# Database configuration
DATABASE_FILE = "dealership.db"

def fetch_motorcycle_details() -> List[Dict[str, str]]:
    """
    Fetches pre-owned Royal Enfield motorcycle details from the database.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing motorcycle details.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # SQL query to fetch pre-owned Royal Enfield motorcycle details
        query = """
        SELECT model, year, price, mileage, color
        FROM motorcycles
        WHERE brand = 'Royal Enfield' AND condition = 'Pre-Owned'
        """
        cursor.execute(query)

        # Fetch all records from the query result
        rows = cursor.fetchall()

        # Define the keys for each field
        keys = ["model", "year", "price", "mileage", "color"]

        # Convert rows to a list of dictionaries
        motorcycles = [dict(zip(keys, row)) for row in rows]

        return motorcycles
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    
    finally:
        # Ensure the connection is closed
        if 'conn' in locals() and conn:
            conn.close()

def display_motorcycle_details(motorcycles: List[Dict[str, str]]) -> None:
    """
    Displays the details of pre-owned Royal Enfield motorcycles.

    Args:
        motorcycles (List[Dict[str, str]]): A list of dictionaries containing motorcycle details.
    """
    if not motorcycles:
        print("No pre-owned Royal Enfield motorcycles found.")
        return
    
    print(f"{'Model':<20}{'Year':<10}{'Price':<10}{'Mileage':<10}{'Color':<10}")
    print("-" * 60)
    for motorcycle in motorcycles:
        print(f"{motorcycle['model']:<20}{motorcycle['year']:<10}{motorcycle['price']:<10}{motorcycle['mileage']:<10}{motorcycle['color']:<10}")

def main():
    """
    Main function to fetch and display pre-owned Royal Enfield motorcycle details.
    """
    print("Fetching pre-owned Royal Enfield motorcycle details...")
    
    # Fetch motorcycle details from the database
    motorcycles = fetch_motorcycle_details()
    
    # Display the motorcycle details
    display_motorcycle_details(motorcycles)

if __name__ == "__main__":
    # Execute the main function
    main()
```

### Notes:
- Ensure the `dealership.db` database file exists and has a `motorcycles` table with appropriate columns (`brand`, `model`, `year`, `price`, `mileage`, `color`, `condition`) before running the script.
- This code handles database-related errors gracefully and is structured with clear, maintainable functions.
