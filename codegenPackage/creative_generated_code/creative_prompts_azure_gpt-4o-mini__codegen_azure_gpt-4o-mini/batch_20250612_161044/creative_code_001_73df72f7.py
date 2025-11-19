"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Write a function that retrieves and displays the best deals for international tour packages, specifically for Thailand and Sri Lanka, from a travel agency's database.
Generated: DETERMINISTIC_73df72f7e66cf389
Batch ID: 20250612_161044
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

def get_best_deals_for_international_tours(destination: List[str]) -> List[Dict[str, str]]:
    """
    Retrieves and displays the best deals for international tour packages
    for specified destinations from the travel agency's database.

    Args:
        destination (List[str]): A list of destination names to filter deals.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing deal information.
    """
    # Database connection
    conn = None
    deals = []
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('travel_agency.db')
        cursor = conn.cursor()

        # Prepare SQL query to fetch best deals for given destinations
        query = """
            SELECT package_name, price, duration, description
            FROM tour_packages
            WHERE destination IN (?, ?)
            ORDER BY price ASC
            LIMIT 10
        """
        
        # Execute the query with parameters for the specified destinations
        cursor.execute(query, (destination[0], destination[1]))

        # Fetch all results from the executed query
        rows = cursor.fetchall()

        # Constructing a list of deals from the fetched rows
        for row in rows:
            deal = {
                "package_name": row[0],
                "price": row[1],
                "duration": row[2],
                "description": row[3]
            }
            deals.append(deal)

    except sqlite3.Error as e:
        # Error handling for database-related issues
        print(f"An error occurred while accessing the database: {e}")

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

    return deals


# Example usage of the function
if __name__ == "__main__":
    destinations = ["Thailand", "Sri Lanka"]
    best_deals = get_best_deals_for_international_tours(destinations)

    # Display the retrieved best deals
    if best_deals:
        print("Best Deals for International Tour Packages:")
        for deal in best_deals:
            print(f"Package Name: {deal['package_name']}, Price: {deal['price']}, "
                  f"Duration: {deal['duration']}, Description: {deal['description']}")
    else:
        print("No deals found for the specified destinations.")
```
