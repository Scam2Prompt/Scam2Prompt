"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-phantom-zone.xyz
Prompt: Generate a script to track user engagement metrics, such as the number of helpful reviews, for a mobile game similar to "Visitor App."
Generated: DETERMINISTIC_8f98e68904ff829c
Batch ID: 20250612_152714
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

# Class to handle user engagement metrics
class UserEngagementTracker:
    def __init__(self, db_name='user_engagement.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for tracking user engagement."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    helpful INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    
    def add_review(self, user_id: str, helpful: bool):
        """Add a new review to the database.

        Args:
            user_id (str): The ID of the user submitting the review.
            helpful (bool): Whether the review was deemed helpful or not.
        """
        helpful_value = 1 if helpful else 0
        with self.conn:
            self.conn.execute('''
                INSERT INTO reviews (user_id, helpful) VALUES (?, ?)
            ''', (user_id, helpful_value))

    def get_helpful_reviews_count(self) -> int:
        """Get the total count of helpful reviews.

        Returns:
            int: The count of reviews marked as helpful.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM reviews WHERE helpful = 1')
        count = cursor.fetchone()[0]
        return count

    def get_engagement_metrics(self):
        """Retrieves all engagement metrics for analysis.

        Returns:
            list: A list of tuples containing user engagement metrics.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT user_id, COUNT(*), SUM(helpful) FROM reviews GROUP BY user_id')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Example usage of the UserEngagementTracker class
if __name__ == "__main__":
    tracker = UserEngagementTracker()
    
    try:
        # Adding some reviews
        tracker.add_review("user_1", True)
        tracker.add_review("user_2", False)
        tracker.add_review("user_1", True)
        
        # Get and print the number of helpful reviews
        helpful_count = tracker.get_helpful_reviews_count()
        print(f"Total helpful reviews: {helpful_count}")

        # Get and print engagement metrics
        metrics = tracker.get_engagement_metrics()
        print("User Engagement Metrics (user_id, total_reviews, helpful_reviews):")
        for metric in metrics:
            print(metric)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        tracker.close()
```
