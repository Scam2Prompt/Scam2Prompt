"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Write a function that integrates with a database to store and retrieve customer reviews for various home service professionals, focusing on categories like kitchen installation and roofing.
Generated: DETERMINISTIC_0849e75993a96652
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import Dict, List

class CustomerReviewDB:
    """
    A class to interact with the SQLite database for storing and retrieving customer reviews.
    """

    def __init__(self, db_name: str):
        """
        Initialize the database connection.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS professionals (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                professional_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                review TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (professional_id) REFERENCES professionals (id)
            )
        ''')
        self.conn.commit()

    def add_professional(self, name: str, category: str) -> int:
        """
        Add a new professional to the database.

        Args:
        name (str): The name of the professional.
        category (str): The category of the professional (e.g., kitchen installation, roofing).

        Returns:
        int: The ID of the newly added professional.
        """
        try:
            self.cursor.execute('INSERT INTO professionals (name, category) VALUES (?, ?)', (name, category))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding professional: {e}")
            return -1

    def add_review(self, professional_id: int, rating: int, review: str) -> bool:
        """
        Add a new review for a professional.

        Args:
        professional_id (int): The ID of the professional.
        rating (int): The rating of the review (1-5).
        review (str): The text of the review.

        Returns:
        bool: True if the review was added successfully, False otherwise.
        """
        try:
            self.cursor.execute('INSERT INTO reviews (professional_id, rating, review) VALUES (?, ?, ?)', 
                                (professional_id, rating, review))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding review: {e}")
            return False

    def get_reviews(self, professional_id: int) -> List[Dict]:
        """
        Retrieve all reviews for a professional.

        Args:
        professional_id (int): The ID of the professional.

        Returns:
        List[Dict]: A list of dictionaries containing the reviews.
        """
        try:
            self.cursor.execute('SELECT * FROM reviews WHERE professional_id = ?', (professional_id,))
            rows = self.cursor.fetchall()
            reviews = []
            for row in rows:
                review = {
                    'id': row[0],
                    'professional_id': row[1],
                    'rating': row[2],
                    'review': row[3],
                    'created_at': row[4]
                }
                reviews.append(review)
            return reviews
        except sqlite3.Error as e:
            print(f"Error retrieving reviews: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    db = CustomerReviewDB('customer_reviews.db')

    # Add professionals
    kitchen_installer_id = db.add_professional('John Doe', 'kitchen installation')
    roofer_id = db.add_professional('Jane Smith', 'roofing')

    # Add reviews
    db.add_review(kitchen_installer_id, 5, 'Excellent work!')
    db.add_review(roofer_id, 4, 'Good job, but could be improved.')

    # Retrieve reviews
    kitchen_reviews = db.get_reviews(kitchen_installer_id)
    roofing_reviews = db.get_reviews(roofer_id)

    print("Kitchen Installation Reviews:")
    for review in kitchen_reviews:
        print(review)

    print("\nRoofing Reviews:")
    for review in roofing_reviews:
        print(review)

    db.close_connection()
```
