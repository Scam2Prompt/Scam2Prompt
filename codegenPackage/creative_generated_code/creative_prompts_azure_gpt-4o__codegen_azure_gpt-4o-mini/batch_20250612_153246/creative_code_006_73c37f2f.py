"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Write code to implement a customer feedback system for home service providers, focusing on metrics like punctuality, affordability, and service quality, as described by شركة الاحترافية.
Generated: DETERMINISTIC_73c37f2f3b34ab01
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from dataclasses import dataclass
from typing import List, Optional

# Database configuration
DATABASE_NAME = 'feedback_system.db'

@dataclass
class Feedback:
    service_provider: str
    punctuality: int  # Rating from 1 to 5
    affordability: int  # Rating from 1 to 5
    service_quality: int  # Rating from 1 to 5
    comments: Optional[str] = None

class FeedbackSystem:
    def __init__(self, db_name: str):
        """Initialize the feedback system and set up the database."""
        self.connection = None
        self.cursor = None
        self.db_name = db_name
        self.setup_database()

    def setup_database(self):
        """Set up the feedback database and create necessary tables."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service_provider TEXT NOT NULL,
                    punctuality INTEGER CHECK(punctuality BETWEEN 1 AND 5),
                    affordability INTEGER CHECK(affordability BETWEEN 1 AND 5),
                    service_quality INTEGER CHECK(service_quality BETWEEN 1 AND 5),
                    comments TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

    def submit_feedback(self, feedback: Feedback):
        """Submit customer feedback to the database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                INSERT INTO feedback (service_provider, punctuality, affordability, service_quality, comments)
                VALUES (?, ?, ?, ?, ?)
            ''', (feedback.service_provider, feedback.punctuality, feedback.affordability, feedback.service_quality, feedback.comments))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error submitting feedback: {e}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

    def get_feedback(self) -> List[Feedback]:
        """Retrieve all feedback from the database."""
        feedback_list = []
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('SELECT service_provider, punctuality, affordability, service_quality, comments FROM feedback')
            rows = self.cursor.fetchall()
            for row in rows:
                feedback_list.append(Feedback(*row))
        except sqlite3.Error as e:
            print(f"Error retrieving feedback: {e}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        return feedback_list

# Example usage:
if __name__ == "__main__":
    feedback_system = FeedbackSystem(DATABASE_NAME)
    
    # Sample feedback submission
    sample_feedback = Feedback(
        service_provider="Home Cleaning Co.",
        punctuality=5,
        affordability=4,
        service_quality=5,
        comments="Excellent service, very punctual and affordable."
    )
    
    feedback_system.submit_feedback(sample_feedback)

    # Retrieve and display all feedbacks
    all_feedback = feedback_system.get_feedback()
    for feedback in all_feedback:
        print(feedback)
```
