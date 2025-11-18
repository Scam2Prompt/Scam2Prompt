"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Write code to implement a customer feedback system for a cleaning service business, ensuring feedback is tied to specific services like "move-in/move-out cleaning" or "spring cleaning."
Generated: DETERMINISTIC_f5b1ed0e176ecdc0
Batch ID: 20250612_153225
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

# Database setup for storing customer feedback
class FeedbackDatabase:
    def __init__(self, db_name="feedback.db"):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_feedback_table()

    def _create_feedback_table(self):
        """Create the feedback table, if it doesn't already exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            service_type TEXT NOT NULL,
            feedback TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
            timestamp TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add_feedback(self, customer_name, service_type, feedback, rating):
        """
        Add customer feedback to the database.
        
        Args:
        - customer_name (str): Name of the customer.
        - service_type (str): Type of cleaning service (e.g., "spring cleaning").
        - feedback (str): Feedback provided by the customer.
        - rating (int): Rating between 1 and 5.
        
        Returns:
        - None
        """
        try:
            timestamp = datetime.now().isoformat()
            self.cursor.execute("""
            INSERT INTO feedback (customer_name, service_type, feedback, rating, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """, (customer_name, service_type, feedback, rating, timestamp))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_feedback_by_service(self, service_type):
        """
        Retrieve all feedback for a specific service type.
        
        Args:
        - service_type (str): Type of cleaning service.
        
        Returns:
        - List of tuples containing feedback data.
        """
        try:
            self.cursor.execute("""
            SELECT customer_name, feedback, rating, timestamp 
            FROM feedback 
            WHERE service_type = ?
            """, (service_type,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()


# User-facing interface for feedback collection
def collect_feedback():
    """
    Collects feedback from the customer and stores it in the database.
    """
    print("Welcome to the Cleaning Service Feedback System!")
    customer_name = input("Enter your name: ").strip()
    service_type = input("Enter the type of cleaning service (e.g., 'spring cleaning', 'move-in/move-out cleaning'): ").strip()
    feedback = input("Enter your feedback: ").strip()
    while True:
        try:
            rating = int(input("Rate the service (1-5): ").strip())
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    db = FeedbackDatabase()
    db.add_feedback(customer_name, service_type, feedback, rating)
    print("Thank you for your feedback!")
    db.close_connection()


def display_feedback():
    """
    Displays feedback for a specific service type.
    """
    service_type = input("Enter the type of cleaning service to view feedback (e.g., 'spring cleaning'): ").strip()

    db = FeedbackDatabase()
    feedback_list = db.get_feedback_by_service(service_type)

    if feedback_list:
        print(f"\nFeedback for '{service_type}':")
        for customer_name, feedback, rating, timestamp in feedback_list:
            print(f"- {customer_name} ({timestamp}): {feedback} [Rating: {rating}/5]")
    else:
        print(f"No feedback available for service type '{service_type}'.")
    
    db.close_connection()


# Main application logic
if __name__ == "__main__":
    while True:
        print("\nCleaning Service Feedback System")
        print("1. Submit Feedback")
        print("2. View Feedback")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            collect_feedback()
        elif choice == "2":
            display_feedback()
        elif choice == "3":
            print("Thank you for using the feedback system!")
            break
        else:
            print("Invalid choice. Please try again.")
```
