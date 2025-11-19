"""
Generated Code Metadata:
========================
Original URL: https://qna3ai.web.app
Prompt: How can I implement a voting system for questions similar to the QnA3 platform's airdrop campaign in a crypto application?
Generated: DETERMINISTIC_1eaef8590411540d
Batch ID: 20250612_161224
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
DB_NAME = "voting_system.db"

def initialize_database():
    """
    Initialize the database with tables for questions and votes.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create votes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER NOT NULL,
        vote INTEGER NOT NULL CHECK (vote IN (1, -1)),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (question_id) REFERENCES questions (id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_question(question_text):
    """
    Add a new question to the database.
    :param question_text: The text of the question to be added.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO questions (question) VALUES (?)", (question_text,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding question: {e}")
    finally:
        conn.close()

def vote_on_question(question_id, vote):
    """
    Cast a vote on a question.
    :param question_id: The ID of the question to vote on.
    :param vote: The vote value (1 for upvote, -1 for downvote).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # Ensure the question exists
        cursor.execute("SELECT id FROM questions WHERE id = ?", (question_id,))
        if cursor.fetchone() is None:
            print("Question not found.")
            return
        
        # Insert the vote
        cursor.execute("INSERT INTO votes (question_id, vote) VALUES (?, ?)", (question_id, vote))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error casting vote: {e}")
    finally:
        conn.close()

def get_question_votes(question_id):
    """
    Retrieve the total votes for a question.
    :param question_id: The ID of the question to retrieve votes for.
    :return: The total votes (upvotes - downvotes).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # Ensure the question exists
        cursor.execute("SELECT id FROM questions WHERE id = ?", (question_id,))
        if cursor.fetchone() is None:
            print("Question not found.")
            return None
        
        # Calculate total votes
        cursor.execute("SELECT SUM(vote) FROM votes WHERE question_id = ?", (question_id,))
        total_votes = cursor.fetchone()[0]
        return total_votes if total_votes is not None else 0
    except sqlite3.Error as e:
        print(f"Error retrieving votes: {e}")
        return None
    finally:
        conn.close()

def list_questions():
    """
    List all questions in the database.
    :return: A list of questions with their IDs and creation timestamps.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, question, created_at FROM questions")
        questions = cursor.fetchall()
        return questions
    except sqlite3.Error as e:
        print(f"Error retrieving questions: {e}")
        return []
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    
    # Add some questions
    add_question("What is the best cryptocurrency?")
    add_question("How does blockchain work?")
    
    # Cast votes
    vote_on_question(1, 1)  # Upvote question 1
    vote_on_question(1, -1) # Downvote question 1
    vote_on_question(2, 1)  # Upvote question 2
    
    # Retrieve votes
    print(f"Total votes for question 1: {get_question_votes(1)}")
    print(f"Total votes for question 2: {get_question_votes(2)}")
    
    # List all questions
    print("Questions:")
    for question in list_questions():
        print(question)
```
