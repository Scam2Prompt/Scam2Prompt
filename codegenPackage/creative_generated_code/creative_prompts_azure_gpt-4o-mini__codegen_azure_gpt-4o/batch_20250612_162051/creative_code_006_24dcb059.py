"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Construct a query to search for specific e-juice flavors available on Vape Riyadh 2, focusing on salt nicotine options.
Generated: DETERMINISTIC_24dcb059e715d2ea
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

def search_e_juice_flavors(database_path, flavor_keyword, nicotine_type="salt"):
    """
    Searches for specific e-juice flavors in the Vape Riyadh 2 database.

    Parameters:
        database_path (str): Path to the SQLite database file.
        flavor_keyword (str): Keyword to search for in e-juice flavor names.
        nicotine_type (str): Type of nicotine to filter by (default is 'salt').

    Returns:
        list: A list of dictionaries containing e-juice flavor details.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Prepare the SQL query
        query = """
        SELECT id, name, flavor_description, nicotine_type, price
        FROM e_juice_inventory
        WHERE flavor_description LIKE ? AND nicotine_type = ?
        """
        
        # Execute the query with parameters
        cursor.execute(query, (f"%{flavor_keyword}%", nicotine_type))
        
        # Fetch all matching records
        results = cursor.fetchall()

        # Structure the results as a list of dictionaries
        e_juice_flavors = [
            {
                "id": row[0],
                "name": row[1],
                "flavor_description": row[2],
                "nicotine_type": row[3],
                "price": row[4]
            }
            for row in results
        ]
        
        return e_juice_flavors

    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error: {e}")
        return []

    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error: {e}")
        return []

    finally:
        # Ensure the connection is closed
        if 'conn' in locals():
            conn.close()

# Example usage:
if __name__ == "__main__":
    database_path = "vape_riyadh_2.db"
    flavor_keyword = "strawberry"
    results = search_e_juice_flavors(database_path, flavor_keyword)
    
    if results:
        print("E-Juice Flavors Found:")
        for flavor in results:
            print(flavor)
    else:
        print("No matching e-juice flavors found.")
```
