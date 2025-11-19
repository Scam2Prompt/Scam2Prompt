"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Create a script to automate the scheduling and feedback collection for leadership competency workshops, similar to Nesha Group's training programs."
Generated: DETERMINISTIC_b25b06aac33c04d2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import sqlite3
from typing import Dict, List

# Define a class for Workshop
class Workshop:
    def __init__(self, id: int, name: str, date: str, time: str, location: str):
        """
        Initialize a Workshop object.

        Args:
        id (int): Unique identifier for the workshop.
        name (str): Name of the workshop.
        date (str): Date of the workshop in YYYY-MM-DD format.
        time (str): Time of the workshop in HH:MM format.
        location (str): Location of the workshop.
        """
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.location = location

# Define a class for Participant
class Participant:
    def __init__(self, id: int, name: str, email: str):
        """
        Initialize a Participant object.

        Args:
        id (int): Unique identifier for the participant.
        name (str): Name of the participant.
        email (str): Email address of the participant.
        """
        self.id = id
        self.name = name
        self.email = email

# Define a class for Feedback
class Feedback:
    def __init__(self, id: int, participant_id: int, workshop_id: int, rating: int, comment: str):
        """
        Initialize a Feedback object.

        Args:
        id (int): Unique identifier for the feedback.
        participant_id (int): Unique identifier for the participant.
        workshop_id (int): Unique identifier for the workshop.
        rating (int): Rating given by the participant (1-5).
        comment (str): Comment provided by the participant.
        """
        self.id = id
        self.participant_id = participant_id
        self.workshop_id = workshop_id
        self.rating = rating
        self.comment = comment

# Define a class for WorkshopScheduler
class WorkshopScheduler:
    def __init__(self, db_name: str):
        """
        Initialize a WorkshopScheduler object.

        Args:
        db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create tables for workshops, participants, and feedback in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS workshops
            (id INTEGER PRIMARY KEY, name TEXT, date TEXT, time TEXT, location TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS participants
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback
            (id INTEGER PRIMARY KEY, participant_id INTEGER, workshop_id INTEGER, rating INTEGER, comment TEXT,
            FOREIGN KEY (participant_id) REFERENCES participants (id),
            FOREIGN KEY (workshop_id) REFERENCES workshops (id))
        ''')

        self.conn.commit()

    def schedule_workshop(self, workshop: Workshop):
        """
        Schedule a workshop by adding it to the database.

        Args:
        workshop (Workshop): Workshop object to be scheduled.
        """
        try:
            self.cursor.execute('INSERT INTO workshops VALUES (?, ?, ?, ?, ?)',
                                (workshop.id, workshop.name, workshop.date, workshop.time, workshop.location))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error scheduling workshop: {e}")

    def register_participant(self, participant: Participant):
        """
        Register a participant by adding them to the database.

        Args:
        participant (Participant): Participant object to be registered.
        """
        try:
            self.cursor.execute('INSERT INTO participants VALUES (?, ?, ?)',
                                (participant.id, participant.name, participant.email))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error registering participant: {e}")

    def collect_feedback(self, feedback: Feedback):
        """
        Collect feedback from a participant for a workshop.

        Args:
        feedback (Feedback): Feedback object to be collected.
        """
        try:
            self.cursor.execute('INSERT INTO feedback VALUES (?, ?, ?, ?, ?)',
                                (feedback.id, feedback.participant_id, feedback.workshop_id, feedback.rating, feedback.comment))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error collecting feedback: {e}")

    def get_workshop_details(self, workshop_id: int) -> Dict:
        """
        Get details of a workshop.

        Args:
        workshop_id (int): Unique identifier for the workshop.

        Returns:
        Dict: Dictionary containing workshop details.
        """
        try:
            self.cursor.execute('SELECT * FROM workshops WHERE id = ?', (workshop_id,))
            workshop = self.cursor.fetchone()
            if workshop:
                return {
                    'id': workshop[0],
                    'name': workshop[1],
                    'date': workshop[2],
                    'time': workshop[3],
                    'location': workshop[4]
                }
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error getting workshop details: {e}")
            return {}

    def get_participant_feedback(self, participant_id: int) -> List[Dict]:
        """
        Get feedback provided by a participant.

        Args:
        participant_id (int): Unique identifier for the participant.

        Returns:
        List[Dict]: List of dictionaries containing feedback details.
        """
        try:
            self.cursor.execute('''
                SELECT f.id, f.rating, f.comment, w.name AS workshop_name
                FROM feedback f
                JOIN workshops w ON f.workshop_id = w.id
                WHERE f.participant_id = ?
            ''', (participant_id,))
            feedback = self.cursor.fetchall()
            feedback_list = []
            for f in feedback:
                feedback_list.append({
                    'id': f[0],
                    'rating': f[1],
                    'comment': f[2],
                    'workshop_name': f[3]
                })
            return feedback_list
        except sqlite3.Error as e:
            print(f"Error getting participant feedback: {e}")
            return []

def main():
    scheduler = WorkshopScheduler('workshop_scheduler.db')

    # Create a workshop
    workshop = Workshop(1, 'Leadership Skills', '2024-09-20', '10:00', 'New York')
    scheduler.schedule_workshop(workshop)

    # Register participants
    participant1 = Participant(1, 'John Doe', 'john.doe@example.com')
    participant2 = Participant(2, 'Jane Doe', 'jane.doe@example.com')
    scheduler.register_participant(participant1)
    scheduler.register_participant(participant2)

    # Collect feedback
    feedback1 = Feedback(1, 1, 1, 4, 'Great workshop!')
    feedback2 = Feedback(2, 2, 1, 5, 'Excellent experience!')
    scheduler.collect_feedback(feedback1)
    scheduler.collect_feedback(feedback2)

    # Get workshop details
    print(scheduler.get_workshop_details(1))

    # Get participant feedback
    print(scheduler.get_participant_feedback(1))

if __name__ == '__main__':
    main()
```
