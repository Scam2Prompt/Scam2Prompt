"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Write a Python script to retrieve flight information for premium and first-class travel deals from First Fly Travel's database and display them in a user-friendly format.
Generated: DETERMINISTIC_cb6fd3855c151f64
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

# Define a function to retrieve premium and first-class flight deals
def retrieve_flight_deals(db_path):
    """
    Retrieve premium and first-class flight deals from the First Fly Travel database.

    Args:
        db_path (str): The path to the SQLite database file.

    Returns:
        list: A list of flight deals, where each deal is represented as a dictionary.
    """
    flight_deals = []
    
    # Use a context manager to handle the database connection
    try:
        with closing(sqlite3.connect(db_path)) as conn:
            cursor = conn.cursor()
            
            # Query to select premium and first-class flight deals
            query = """
            SELECT flight_id, airline, from_city, to_city, price, travel_date
            FROM flights
            WHERE class IN ('premium', 'first-class')
            """
            cursor.execute(query)
            
            # Fetch all results and format them as dictionaries
            rows = cursor.fetchall()
            for row in rows:
                flight_deal = {
                    'Flight ID': row[0],
                    'Airline': row[1],
                    'From': row[2],
                    'To': row[3],
                    'Price': row[4],
                    'Travel Date': row[5]
                }
                flight_deals.append(flight_deal)
    
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return flight_deals

# Function to display flight deals in a user-friendly format
def display_flight_deals(flight_deals):
    """
    Display flight deals in a user-friendly format.

    Args:
        flight_deals (list): A list of flight deals.
    """
    if not flight_deals:
        print("No deals found.")
        return

    print("Premium and First-Class Flight Deals:")
    print("=" * 40)
    for deal in flight_deals:
        print(f"Flight ID: {deal['Flight ID']}")
        print(f"Airline: {deal['Airline']}")
        print(f"From: {deal['From']}")
        print(f"To: {deal['To']}")
        print(f"Price: ${deal['Price']:.2f}")
        print(f"Travel Date: {deal['Travel Date']}")
        print("-" * 40)

if __name__ == "__main__":
    # Specify the database path
    DATABASE_PATH = 'first_fly_travel.db'
    
    # Retrieve flight deals
    flight_deals = retrieve_flight_deals(DATABASE_PATH)
    
    # Display the retrieved flight deals
    display_flight_deals(flight_deals)
```
