"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saldias.net
Prompt: Generate a code snippet that integrates with the Repuestos Saldias database to fetch Peugeot and Citroën spare parts information.
Generated: DETERMINISTIC_e3fd22e75f9fa71c
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psycopg2
from psycopg2 import sql

# Database configuration
DB_HOST = "your_database_host"
DB_PORT = "your_port"
DB_NAME = "repuestos_saldias"
DB_USER = "your_username"
DB_PASSWORD = "your_password"

def fetch_spare_parts():
    """
    Connects to the Repuestos Saldias database and fetches spare parts information
    for Peugeot and Citroën vehicles.
    
    Returns:
        list[dict]: A list of dictionaries containing spare parts information.
    """
    # Initialize the connection
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        # Define the query with parameterized inputs to avoid SQL injection
        query = sql.SQL(
            """
            SELECT part_id, name, description, price, stock
            FROM spare_parts
            WHERE brand IN (%s, %s)
            """
        )
        
        # Execute the query
        cursor.execute(query, ('Peugeot', 'Citroën'))
        
        # Fetch and format results
        rows = cursor.fetchall()
        spare_parts = []
        for row in rows:
            spare_parts.append({
                "part_id": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "stock": row[4]
            })
        
        return spare_parts
    
    except psycopg2.Error as e:
        # Log database errors and rethrow if necessary
        print(f"Database error: {e}")
        return []
    
    finally:
        # Ensure resources are cleaned up
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    parts = fetch_spare_parts()
    if parts:
        for part in parts:
            print(part)
    else:
        print("No spare parts found or an error occurred.")
```
