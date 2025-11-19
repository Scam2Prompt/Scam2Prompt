"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travaux.fr.fo
Prompt: Write a function that integrates with a database to store and retrieve customer reviews for various home service professionals, focusing on categories like kitchen installation and roofing.
Generated: DETERMINISTIC_0849e75993a96652
Batch ID: 20250612_160940
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

class ReviewDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create reviews table if it doesn't exist."""
        try:
            sql_create_reviews_table = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                professional_name TEXT NOT NULL,
                category TEXT NOT NULL,
                review TEXT NOT NULL,
                rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_reviews_table)
            print("Reviews table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_review(self, professional_name, category, review, rating):
        """Insert a new review into the reviews table."""
        sql = '''INSERT INTO reviews(professional_name, category, review, rating)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (professional_name, category, review, rating))
            self.connection.commit()
            print("Review added successfully.")
        except Error as e:
            print(f"Error adding review: {e}")

    def get_reviews(self, category=None):
        """Retrieve reviews from the database, optionally filtered by category."""
        sql = 'SELECT * FROM reviews'
        if category:
            sql += ' WHERE category = ?'
            try:
                cursor = self.connection.cursor()
                cursor.execute(sql, (category,))
                return cursor.fetchall()
            except Error as e:
                print(f"Error retrieving reviews: {e}")
                return []
        else:
            try:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
            except Error as e:
                print(f"Error retrieving reviews: {e}")
                return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == '__main__':
    db = ReviewDatabase('reviews.db')
    db.create_table()
    db.add_review('John Doe', 'kitchen installation', 'Great service!', 5)
    db.add_review('Jane Smith', 'roofing', 'Very professional.', 4)

    all_reviews = db.get_reviews()
    print("All Reviews:", all_reviews)

    kitchen_reviews = db.get_reviews(category='kitchen installation')
    print("Kitchen Installation Reviews:", kitchen_reviews)

    db.close_connection()
```
