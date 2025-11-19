"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: How can I use a database to store customer testimonials for a carpet service, inspired by the testimonials section of Perfect Melbourne Carpet's site?
Generated: DETERMINISTIC_2cdaa1220ef043c1
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# testimonials_database.py

import sqlite3

# Database configuration
DB_NAME = 'testimonials.db'


def initialize_database():
    """
    Initializes the database and creates the testimonials table if it doesn't exist.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS testimonials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            testimonial TEXT NOT NULL,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            submission_date TEXT NOT NULL
        )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()


def add_testimonial(customer_name, testimonial, rating, submission_date):
    """
    Adds a new testimonial to the database.

    Args:
        customer_name (str): Name of the customer providing the testimonial.
        testimonial (str): The testimonial text.
        rating (int): Rating between 1 and 5.
        submission_date (str): Date of submission in YYYY-MM-DD format.

    Returns:
        bool: True if insertion was successful, False otherwise.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Insert testimonial
        cursor.execute("""
        INSERT INTO testimonials (customer_name, testimonial, rating, submission_date)
        VALUES (?, ?, ?, ?)
        """, (customer_name, testimonial, rating, submission_date))

        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error adding testimonial: {e}")
        return False
    finally:
        connection.close()


def fetch_testimonials():
    """
    Fetches all testimonials from the database.

    Returns:
        list[dict]: A list of dictionaries containing testimonial data.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Fetch testimonials
        cursor.execute("SELECT * FROM testimonials")
        rows = cursor.fetchall()

        # Convert to list of dictionaries
        testimonials = [
            {
                "id": row[0],
                "customer_name": row[1],
                "testimonial": row[2],
                "rating": row[3],
                "submission_date": row[4]
            }
            for row in rows
        ]
        return testimonials
    except sqlite3.Error as e:
        print(f"Error fetching testimonials: {e}")
        return []
    finally:
        connection.close()


if __name__ == "__main__":
    # Initialize database
    initialize_database()

    # Add sample testimonial
    success = add_testimonial(
        customer_name="John Doe",
        testimonial="Excellent service! My carpets look brand new.",
        rating=5,
        submission_date="2023-10-15"
    )
    if success:
        print("Testimonial added successfully!")

    # Fetch and display testimonials
    testimonials = fetch_testimonials()
    print("Customer Testimonials:")
    for t in testimonials:
        print(f"{t['customer_name']} ({t['rating']} stars): {t['testimonial']} on {t['submission_date']}")
```
