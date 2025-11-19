"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Write a Python script that retrieves customer testimonials for UPVC window systems from a database, similar to the client feedback featured on the DEXODOOR site.
Generated: DETERMINISTIC_dc2a5b1a90f8c1ec
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

# Database configuration
DATABASE = 'testimonials.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_testimonials(conn):
    """Fetch all customer testimonials from the database."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT customer_name, testimonial FROM testimonials WHERE product_type='UPVC'")

        # Fetch all results
        rows = cur.fetchall()

        return rows
    except Error as e:
        print(f"Error fetching testimonials: {e}")
        return []

def display_testimonials(testimonials):
    """Display the fetched testimonials."""
    if not testimonials:
        print("No testimonials found.")
        return

    print("Customer Testimonials for UPVC Window Systems:")
    print("=" * 40)
    for name, testimonial in testimonials:
        print(f"Customer Name: {name}")
        print(f"Testimonial: {testimonial}")
        print("-" * 40)

def main():
    """Main function to retrieve and display UPVC window testimonials."""
    # Create a database connection
    conn = create_connection(DATABASE)

    if conn:
        testimonials = fetch_testimonials(conn)
        display_testimonials(testimonials)

        # Close the connection
        conn.close()
    else:
        print("Failed to establish a database connection.")

if __name__ == "__main__":
    main()
```

### Note:
- This script connects to an SQLite database to retrieve customer testimonials for UPVC window systems. Make sure to replace `testimonials.db` with your actual database file path.
- The database should have a table named `testimonials` with columns `customer_name`, `testimonial`, and `product_type`.
