"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neami.shop
Prompt: Illustrate how to implement a feedback system for a business collaboration platform, where users can rate their experiences and build a community of trust.
Generated: DETERMINISTIC_afbbcee1f5e92a57
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'feedback.db'

def initialize_database():
    """
    Initializes the SQLite database for the feedback system.
    Creates necessary tables if they do not exist.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Create the feedback table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            collaboration_id INTEGER NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def submit_feedback(user_id, collaboration_id, rating, comment=None):
    """
    Submits feedback to the database.

    Parameters:
        user_id (int): ID of the user providing the feedback
        collaboration_id (int): ID of the collaboration being rated
        rating (int): Rating between 1 and 5
        comment (str): Optional text feedback provided by the user
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Insert feedback into the table
        cursor.execute("""
            INSERT INTO feedback (user_id, collaboration_id, rating, comment)
            VALUES (?, ?, ?, ?)
        """, (user_id, collaboration_id, rating, comment))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error occurred while submitting feedback: {e}")
    finally:
        connection.close()

def view_feedback(collaboration_id):
    """
    Retrieves feedback for a specific collaboration.

    Parameters:
        collaboration_id (int): ID of the collaboration to query feedback for

    Returns:
        List[Dict]: A list of feedback records as dictionaries
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        # Query feedback for the specific collaboration
        cursor.execute("""
            SELECT user_id, rating, comment, created_at
            FROM feedback
            WHERE collaboration_id = ?
        """, (collaboration_id,))

        rows = cursor.fetchall()
        feedback_list = [dict(row) for row in rows]
        return feedback_list
    except sqlite3.Error as e:
        print(f"Error occurred while retrieving feedback: {e}")
        return []
    finally:
        connection.close()

def calculate_average_rating(collaboration_id):
    """
    Calculates the average rating for a specific collaboration.

    Parameters:
        collaboration_id (int): ID of the collaboration to calculate the average rating for

    Returns:
        float: The average rating value (or None if no feedback exists)
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Query the average rating
        cursor.execute("""
            SELECT AVG(rating) AS average_rating
            FROM feedback
            WHERE collaboration_id = ?
        """, (collaboration_id,))

        result = cursor.fetchone()
        return result[0] if result[0] is not None else None
    except sqlite3.Error as e:
        print(f"Error occurred while calculating average rating: {e}")
        return None
    finally:
        connection.close()

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    submit_feedback(user_id=1, collaboration_id=101, rating=5, comment="Great experience!")
    submit_feedback(user_id=2, collaboration_id=101, rating=4, comment="Good collaboration overall.")

    feedback = view_feedback(collaboration_id=101)
    print("Feedback for collaboration 101:", feedback)

    avg_rating = calculate_average_rating(collaboration_id=101)
    print("Average rating for collaboration 101:", avg_rating)
```
