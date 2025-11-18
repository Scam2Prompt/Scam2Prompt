"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawscommunity.life
Prompt: Write a script to track the delivery time of Telegram Stars orders on the Buy&Stars platform and calculate the average completion time based on historical data.
Generated: DETERMINISTIC_147f467e5f809b6f
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = 'orders.db'

def initialize_database():
    """
    Initializes the SQLite database if it doesn't exist.
    Creates the 'orders' table to store order delivery details.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            delivery_date TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_order(order_id, order_date, delivery_date):
    """
    Adds a new order to the database.

    Args:
        order_id (int): Unique identifier for the order.
        order_date (str): Date and time the order was placed (ISO format).
        delivery_date (str): Date and time the order was delivered (ISO format).
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO orders (order_id, order_date, delivery_date)
            VALUES (?, ?, ?)
        """, (order_id, order_date, delivery_date))
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error adding order to database: {e}")
    finally:
        connection.close()

def calculate_average_delivery_time():
    """
    Calculates the average delivery time for all orders in the database.

    Returns:
        float: Average delivery time in hours, or None if no orders exist.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("SELECT order_date, delivery_date FROM orders")
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            print("No orders found in the database.")
            return None

        total_delivery_time = 0
        order_count = len(rows)

        for order_date, delivery_date in rows:
            order_dt = datetime.fromisoformat(order_date)
            delivery_dt = datetime.fromisoformat(delivery_date)
            delivery_time = (delivery_dt - order_dt).total_seconds() / 3600  # Convert seconds to hours
            total_delivery_time += delivery_time
        
        average_delivery_time = total_delivery_time / order_count
        return average_delivery_time

    except sqlite3.Error as e:
        print(f"Error reading from database: {e}")
        return None
    except ValueError as ve:
        print(f"Error parsing dates: {ve}")
        return None

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add some sample data (This would typically come from external input in a real-world scenario)
    add_order(order_id=1, order_date="2023-10-01T14:00:00", delivery_date="2023-10-01T16:30:00")
    add_order(order_id=2, order_date="2023-10-02T10:00:00", delivery_date="2023-10-02T14:00:00")
    add_order(order_id=3, order_date="2023-10-03T09:00:00", delivery_date="2023-10-03T13:00:00")

    # Calculate and display the average delivery time
    average_time = calculate_average_delivery_time()
    if average_time is not None:
        print(f"The average delivery time is {average_time:.2f} hours.")
```
