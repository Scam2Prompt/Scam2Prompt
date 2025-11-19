"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Illustrate how to implement a feedback system for training sessions that captures participant satisfaction and ROI, as emphasized by Romain Rissoan in his consultancy work.
Generated: DETERMINISTIC_dba8ceb1bdda1809
Batch ID: 20250612_161745
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

# Define a class for the Feedback System
class FeedbackSystem:
    def __init__(self, db_name='feedback.db'):
        """Initialize the Feedback System with a database."""
        self.connection = sqlite3.connect(db_name)
        self.create_feedback_table()

    def create_feedback_table(self):
        """Create a table in the database to store feedback."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        session_date TEXT NOT NULL,
                        participant_name TEXT NOT NULL,
                        satisfaction_score INTEGER CHECK(satisfaction_score BETWEEN 1 AND 5),
                        comments TEXT,
                        roi_score REAL CHECK(roi_score >= 0)
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def submit_feedback(self, participant_name, satisfaction_score, comments, roi_score):
        """Submit feedback for a training session."""
        try:
            session_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with self.connection:
                self.connection.execute('''
                    INSERT INTO feedback (session_date, participant_name, satisfaction_score, comments, roi_score)
                    VALUES (?, ?, ?, ?, ?)
                ''', (session_date, participant_name, satisfaction_score, comments, roi_score))
        except sqlite3.Error as e:
            print(f"Error submitting feedback: {e}")

    def retrieve_feedback(self):
        """Retrieve all feedback from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM feedback')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving feedback: {e}")
            return []

    def calculate_average_satisfaction(self):
        """Calculate the average satisfaction score."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT AVG(satisfaction_score) FROM feedback')
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error calculating average satisfaction: {e}")
            return None

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    # Initialize the feedback system
    feedback_system = FeedbackSystem()
    
    # Submit some feedback
    feedback_system.submit_feedback("John Doe", 4, "Great session!", 3.5)
    feedback_system.submit_feedback("Jane Smith", 5, "Very informative.", 4.0)
    
    # Retrieve and print all feedback
    feedback_list = feedback_system.retrieve_feedback()
    for feedback in feedback_list:
        print(feedback)
    
    # Calculate and print the average satisfaction score
    avg_satisfaction = feedback_system.calculate_average_satisfaction()
    print(f"Average Satisfaction Score: {avg_satisfaction:.2f}")
    
    # Close the feedback system
    feedback_system.close()
```
