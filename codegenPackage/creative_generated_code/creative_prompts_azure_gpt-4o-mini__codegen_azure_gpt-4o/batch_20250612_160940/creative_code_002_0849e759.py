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
from typing import List, Dict, Union

# Database setup function to initialize tables if they don't already exist
def initialize_database(db_path: str = "reviews.db"):
    """
    Initializes the SQLite database by creating the 'reviews' table.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            professional_name TEXT NOT NULL,
            category TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            review TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

# Function to add a new review to the database
def add_review(db_path: str, review_data: Dict[str, Union[str, int]]) -> bool:
    """
    Adds a new customer review to the database.

    :param db_path: Path to the SQLite database
    :param review_data: Dictionary containing review details. Keys: 
                        'professional_name', 'category', 'customer_name', 
                        'review', 'rating'
    :return: True if the review was successfully added, False otherwise
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO reviews (professional_name, category, customer_name, review, rating)
        VALUES (:professional_name, :category, :customer_name, :review, :rating)
        """, review_data)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error adding review: {e}")
        return False
    finally:
        if conn:
            conn.close()

# Function to retrieve reviews based on category
def get_reviews_by_category(db_path: str, category: str) -> List[Dict[str, Union[str, int]]]:
    """
    Retrieves all reviews for a specific category.

    :param db_path: Path to the SQLite database
    :param category: Category of home service (e.g., 'Kitchen Installation', 'Roofing')
    :return: List of dictionaries containing review data
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT professional_name, customer_name, review, rating, created_at
        FROM reviews
        WHERE category = ?
        ORDER BY created_at DESC
        """, (category,))
        rows = cursor.fetchall()
        # Convert rows into a list of dictionaries
        reviews = [
            {
                "professional_name": row[0],
                "customer_name": row[1],
                "review": row[2],
                "rating": row[3],
                "created_at": row[4],
            }
            for row in rows
        ]
        return reviews
    except sqlite3.Error as e:
        print(f"Error retrieving reviews: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add a new review
    review = {
        "professional_name": "John Doe",
        "category": "Kitchen Installation",
        "customer_name": "Jane Smith",
        "review": "Excellent work, very professional!",
        "rating": 5
    }
    success = add_review("reviews.db", review)
    if success:
        print("Review added successfully.")

    # Retrieve reviews for a category
    category_reviews = get_reviews_by_category("reviews.db", "Kitchen Installation")
    for r in category_reviews:
        print(r)
```
