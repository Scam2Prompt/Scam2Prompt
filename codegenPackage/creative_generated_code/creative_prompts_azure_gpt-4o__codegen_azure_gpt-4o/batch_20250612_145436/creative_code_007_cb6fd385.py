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
import sys
from tabulate import tabulate

def connect_to_database(db_name):
    """
    Connect to the SQLite database.

    :param db_name: Name of the SQLite database file.
    :return: SQLite connection object.
    """
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def fetch_flight_deals(connection):
    """
    Fetch premium and first-class flight deals from the database.

    :param connection: SQLite connection object.
    :return: List of tuples containing flight information.
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT flight_number, airline, origin, destination, price, travel_date, class
        FROM flight_deals
        WHERE class IN ('Premium', 'First-Class')
        ORDER BY travel_date ASC;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return []

def display_flight_deals(flights):
    """
    Display flight deals in a user-friendly tabular format.

    :param flights: List of tuples containing flight information.
    """
    if not flights:
        print("No premium or first-class flight deals available.")
        return

    headers = ["Flight Number", "Airline", "Origin", "Destination", "Price", "Travel Date", "Class"]
    print(tabulate(flights, headers=headers, tablefmt="grid"))

def main():
    """
    Main function to retrieve and display flight information.
    """
    database_name = "first_fly_travel.db"  # Replace with the actual name of the database file

    # Connect to the database
    connection = connect_to_database(database_name)

    # Fetch flight deals
    flights = fetch_flight_deals(connection)

    # Display flight deals
    display_flight_deals(flights)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
```
