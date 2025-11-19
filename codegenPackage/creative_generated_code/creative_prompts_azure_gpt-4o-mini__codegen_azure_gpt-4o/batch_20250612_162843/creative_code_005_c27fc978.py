"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Describe how to implement a customer feedback system for a travel agency that specializes in luxury safaris, ensuring exceptional service is highlighted.
Generated: DETERMINISTIC_c27fc978d5a5b59f
Batch ID: 20250612_162843
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


class FeedbackSystem:
    """
    A customer feedback system for a travel agency specializing in luxury safaris.
    This system allows customers to submit feedback and stores it in a database.
    """

    def __init__(self, db_name="feedback.db"):
        """
        Initializes the feedback system and sets up the database connection.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Sets up the database schema.
        Creates the 'feedback' table if it does not already exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    feedback TEXT NOT NULL,
                    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
                    timestamp TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def submit_feedback(self, customer_name, email, feedback, rating):
        """
        Submits feedback from a customer.
        :param customer_name: Name of the customer.
        :param email: Email address of the customer.
        :param feedback: Customer's feedback message.
        :param rating: Customer's rating (1-5).
        :return: Confirmation message or error.
        """
        try:
            # Validate input
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5.")

            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert feedback into the database
            cursor.execute("""
                INSERT INTO feedback (customer_name, email, feedback, rating, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (customer_name, email, feedback, rating, datetime.now().isoformat()))

            conn.commit()
            return "Thank you for your feedback!"
        except sqlite3.Error as e:
            return f"Error saving feedback: {e}"
        except ValueError as ve:
            return str(ve)
        finally:
            conn.close()

    def view_feedback(self, minimum_rating=5):
        """
        Retrieves feedback from the database with a minimum rating filter.
        :param minimum_rating: Minimum rating to filter feedback (default is 5).
        :return: List of feedback entries.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query feedback with the specified minimum rating
            cursor.execute("""
                SELECT customer_name, email, feedback, rating, timestamp
                FROM feedback
                WHERE rating >= ?
                ORDER BY timestamp DESC
            """, (minimum_rating,))

            feedback_entries = cursor.fetchall()
            return feedback_entries
        except sqlite3.Error as e:
            print(f"Error retrieving feedback: {e}")
            return []
        finally:
            conn.close()


# Example Usage
if __name__ == "__main__":
    # Initialize the feedback system
    system = FeedbackSystem()

    # Submit feedback
    print(system.submit_feedback(
        customer_name="John Doe",
        email="john.doe@example.com",
        feedback="The safari experience was excellent! The guide was very knowledgeable.",
        rating=5
    ))

    # View feedback with a minimum rating of 5
    feedback_list = system.view_feedback(minimum_rating=5)
    for entry in feedback_list:
        print(f"Name: {entry[0]}, Email: {entry[1]}, Feedback: {entry[2]}, Rating: {entry[3]}, Timestamp: {entry[4]}")
```
