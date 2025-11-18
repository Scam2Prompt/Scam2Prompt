"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Write code to implement a "mentor helpline" feature where users can submit questions to a database and receive responses from mentors, as outlined on uEmbark.
Generated: DETERMINISTIC_d1cfcfb4a9e9e643
Batch ID: 20250612_154632
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

class MentorHelpline:
    """
    A Mentor Helpline class that allows users to submit questions
    and mentors to respond to questions. It uses SQLite as the database backend.
    """

    def __init__(self, db_name="mentor_helpline.db"):
        """
        Initializes the database connection and sets up required tables.
        """
        self.db_name = db_name
        self._connect_db()
        self._setup_tables()

    def _connect_db(self):
        """
        Connect to the SQLite database.
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def _setup_tables(self):
        """
        Create tables if they do not exist.
        """
        # Questions table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                user_email TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                answered INTEGER DEFAULT 0,
                mentor_response TEXT DEFAULT NULL
            )
        """)
        self.conn.commit()

    def submit_question(self, question, user_email):
        """
        Allows a user to submit a question.
        
        Args:
            question (str): The user's question.
            user_email (str): The email address of the user submitting the question.
        
        Returns:
            str: Success message or error message.
        """
        try:
            self.cursor.execute("""
                INSERT INTO questions (question, user_email) VALUES (?, ?)
            """, (question, user_email))
            self.conn.commit()
            return "Your question has been submitted successfully!"
        except sqlite3.Error as e:
            return f"An error occurred while submitting your question: {e}"

    def respond_to_question(self, question_id, mentor_response):
        """
        Allows a mentor to respond to a user's question.
        
        Args:
            question_id (int): The ID of the question to respond to.
            mentor_response (str): The mentor's response to the question.

        Returns:
            str: Success message or error message.
        """
        try:
            self.cursor.execute("""
                UPDATE questions
                SET mentor_response = ?, answered = 1
                WHERE id = ? AND answered = 0
            """, (mentor_response, question_id))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                return "Response submitted successfully!"
            else:
                return "Error: Question not found or already answered."
        except sqlite3.Error as e:
            return f"An error occurred while submitting your response: {e}"

    def fetch_unanswered_questions(self):
        """
        Fetch all unanswered questions from the database.

        Returns:
            list: A list of dictionaries containing unanswered questions.
        """
        try:
            self.cursor.execute("""
                SELECT id, question, user_email, created_at
                FROM questions
                WHERE answered = 0
            """)
            rows = self.cursor.fetchall()
            return [
                {"id": row[0], "question": row[1], "user_email": row[2], "created_at": row[3]}
                for row in rows
            ]
        except sqlite3.Error as e:
            return f"An error occurred while fetching unanswered questions: {e}"

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    helpline = MentorHelpline()

    # Submit a question
    print(helpline.submit_question(
        question="How do I improve my programming skills?",
        user_email="user@example.com"
    ))

    # Fetch unanswered questions
    print(helpline.fetch_unanswered_questions())

    # Respond to a question
    print(helpline.respond_to_question(
        question_id=1,
        mentor_response="Practice daily and work on real-world projects."
    ))

    # Close the database connection
    helpline.close_connection()
```
