"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Illustrate how to implement a feedback system for training sessions that captures participant satisfaction and ROI, as emphasized by Romain Rissoan in his consultancy work.
Generated: DETERMINISTIC_dba8ceb1bdda1809
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup
def initialize_database():
    """
    Initializes the SQLite database to store feedback data.
    Creates a table if it doesn't already exist.
    """
    connection = sqlite3.connect("feedback_system.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_name TEXT NOT NULL,
            session_name TEXT NOT NULL,
            satisfaction_score INTEGER NOT NULL CHECK(satisfaction_score BETWEEN 1 AND 5),
            roi_score INTEGER NOT NULL CHECK(roi_score BETWEEN 1 AND 5),
            comments TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

# Function to collect feedback
def collect_feedback(participant_name, session_name, satisfaction_score, roi_score, comments=""):
    """
    Collects feedback from a participant and stores it in the database.

    Args:
        participant_name (str): Name of the participant.
        session_name (str): Name of the training session.
        satisfaction_score (int): Satisfaction score (1-5).
        roi_score (int): ROI score (1-5).
        comments (str): Additional comments (optional).

    Raises:
        ValueError: If scores are not within the valid range.
    """
    if not (1 <= satisfaction_score <= 5):
        raise ValueError("Satisfaction score must be between 1 and 5.")
    if not (1 <= roi_score <= 5):
        raise ValueError("ROI score must be between 1 and 5.")

    connection = sqlite3.connect("feedback_system.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO feedback (participant_name, session_name, satisfaction_score, roi_score, comments)
        VALUES (?, ?, ?, ?, ?)
    """, (participant_name, session_name, satisfaction_score, roi_score, comments))
    connection.commit()
    connection.close()

# Function to generate a feedback report
def generate_feedback_report():
    """
    Generates a summary report of feedback data, including average scores and comments.

    Returns:
        dict: A dictionary containing the report data.
    """
    connection = sqlite3.connect("feedback_system.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            session_name,
            AVG(satisfaction_score) AS avg_satisfaction,
            AVG(roi_score) AS avg_roi,
            COUNT(*) AS total_feedbacks
        FROM feedback
        GROUP BY session_name
    """)
    report_data = cursor.fetchall()

    cursor.execute("""
        SELECT session_name, comments, timestamp 
        FROM feedback 
        WHERE comments != ''
    """)
    comments_data = cursor.fetchall()

    connection.close()

    # Format the report
    report = {
        "summary": [
            {
                "session_name": row[0],
                "average_satisfaction": round(row[1], 2),
                "average_roi": round(row[2], 2),
                "total_feedbacks": row[3]
            }
            for row in report_data
        ],
        "comments": [
            {
                "session_name": row[0],
                "comment": row[1],
                "timestamp": row[2]
            }
            for row in comments_data
        ]
    }
    return report

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example: Collecting feedback
    try:
        collect_feedback(
            participant_name="John Doe",
            session_name="Leadership Training",
            satisfaction_score=4,
            roi_score=5,
            comments="Very insightful session!"
        )
        collect_feedback(
            participant_name="Jane Smith",
            session_name="Leadership Training",
            satisfaction_score=3,
            roi_score=4
        )
        collect_feedback(
            participant_name="Alice Johnson",
            session_name="Time Management Workshop",
            satisfaction_score=5,
            roi_score=5,
            comments="Loved the practical tips!"
        )
    except ValueError as e:
        print(f"Error: {e}")

    # Generate and display the feedback report
    report = generate_feedback_report()
    print("Feedback Summary Report:")
    for session in report["summary"]:
        print(f"Session: {session['session_name']}")
        print(f"  Average Satisfaction: {session['average_satisfaction']}")
        print(f"  Average ROI: {session['average_roi']}")
        print(f"  Total Feedbacks: {session['total_feedbacks']}")
        print()

    print("Comments:")
    for comment in report["comments"]:
        print(f"Session: {comment['session_name']}")
        print(f"  Comment: {comment['comment']}")
        print(f"  Timestamp: {comment['timestamp']}")
        print()
```
