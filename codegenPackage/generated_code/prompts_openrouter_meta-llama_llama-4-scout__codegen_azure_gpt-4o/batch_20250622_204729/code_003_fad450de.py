"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Design a system to vet and track pool builders' performance, ensuring that only high-quality builders are recommended to homeowners, and provide a list of required features for such a system.
Generated: DETERMINISTIC_fad450de5184a890
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pool_builder_tracker.py

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "pool_builders.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create table for pool builders
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pool_builders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_info TEXT NOT NULL,
        rating REAL DEFAULT 0.0,
        total_reviews INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create table for reviews
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        builder_id INTEGER NOT NULL,
        homeowner_name TEXT NOT NULL,
        review_text TEXT NOT NULL,
        rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (builder_id) REFERENCES pool_builders (id)
    )
    """)
    
    conn.commit()
    conn.close()

# Feature 1: Add a new pool builder
def add_pool_builder(name, contact_info):
    """
    Adds a new pool builder to the database.
    :param name: Name of the pool builder
    :param contact_info: Contact information of the pool builder
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pool_builders (name, contact_info)
        VALUES (?, ?)
        """, (name, contact_info))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding pool builder: {e}")
    finally:
        conn.close()

# Feature 2: Add a review for a pool builder
def add_review(builder_id, homeowner_name, review_text, rating):
    """
    Adds a review for a specific pool builder.
    :param builder_id: ID of the pool builder
    :param homeowner_name: Name of the homeowner providing the review
    :param review_text: Text of the review
    :param rating: Rating (1-5) provided by the homeowner
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Insert the review
        cursor.execute("""
        INSERT INTO reviews (builder_id, homeowner_name, review_text, rating)
        VALUES (?, ?, ?, ?)
        """, (builder_id, homeowner_name, review_text, rating))
        
        # Update the builder's rating and total reviews
        cursor.execute("""
        SELECT rating, total_reviews FROM pool_builders WHERE id = ?
        """, (builder_id,))
        builder = cursor.fetchone()
        if builder:
            current_rating, total_reviews = builder
            new_total_reviews = total_reviews + 1
            new_rating = ((current_rating * total_reviews) + rating) / new_total_reviews
            cursor.execute("""
            UPDATE pool_builders
            SET rating = ?, total_reviews = ?
            WHERE id = ?
            """, (new_rating, new_total_reviews, builder_id))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding review: {e}")
    finally:
        conn.close()

# Feature 3: Get top-rated pool builders
def get_top_rated_builders(limit=5):
    """
    Retrieves the top-rated pool builders.
    :param limit: Number of builders to retrieve (default is 5)
    :return: List of top-rated builders
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, name, contact_info, rating, total_reviews
        FROM pool_builders
        ORDER BY rating DESC, total_reviews DESC
        LIMIT ?
        """, (limit,))
        builders = cursor.fetchall()
        return builders
    except sqlite3.Error as e:
        print(f"Error retrieving top-rated builders: {e}")
        return []
    finally:
        conn.close()

# Feature 4: Get reviews for a specific builder
def get_reviews(builder_id):
    """
    Retrieves all reviews for a specific pool builder.
    :param builder_id: ID of the pool builder
    :return: List of reviews
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT homeowner_name, review_text, rating, created_at
        FROM reviews
        WHERE builder_id = ?
        ORDER BY created_at DESC
        """, (builder_id,))
        reviews = cursor.fetchall()
        return reviews
    except sqlite3.Error as e:
        print(f"Error retrieving reviews: {e}")
        return []
    finally:
        conn.close()

# Feature 5: Delete a pool builder
def delete_pool_builder(builder_id):
    """
    Deletes a pool builder and their associated reviews from the database.
    :param builder_id: ID of the pool builder to delete
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Delete reviews associated with the builder
        cursor.execute("""
        DELETE FROM reviews WHERE builder_id = ?
        """, (builder_id,))
        
        # Delete the builder
        cursor.execute("""
        DELETE FROM pool_builders WHERE id = ?
        """, (builder_id,))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting pool builder: {e}")
    finally:
        conn.close()

# Initialize the database
if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")
```

### Required Features for the System:
1. Add new pool builders with their contact information.
2. Allow homeowners to submit reviews and ratings (1-5) for builders.
3. Calculate and update builder ratings based on reviews.
4. Retrieve top-rated builders for homeowners to choose from.
5. Retrieve all reviews for a specific builder.
6. Delete builders and their associated reviews if necessary.
7. Ensure proper error handling and data validation.
