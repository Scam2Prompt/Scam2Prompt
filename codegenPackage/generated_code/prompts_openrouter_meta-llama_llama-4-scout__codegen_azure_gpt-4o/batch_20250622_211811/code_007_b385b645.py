"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Design a chatbot that uses a database of random questions to engage users in conversation, and provide a simple implementation in Python.
Generated: DETERMINISTIC_b385b645bf0c7c15
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import random

class Chatbot:
    def __init__(self, db_path):
        """
        Initialize the chatbot with a connection to the SQLite database.
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None
        self._connect_to_db()

    def _connect_to_db(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def get_random_question(self):
        """
        Fetch a random question from the database.
        :return: A random question string.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT question FROM questions ORDER BY RANDOM() LIMIT 1;")
            result = cursor.fetchone()
            return result[0] if result else "No questions available in the database."
        except sqlite3.Error as e:
            print(f"Error fetching question: {e}")
            return "Sorry, I encountered an error while fetching a question."

    def engage_user(self):
        """
        Engage the user in conversation by asking random questions.
        """
        print("Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
            question = self.get_random_question()
            print(f"Chatbot: {question}")

    def close_connection(self):
        """
        Close the connection to the SQLite database.
        """
        if self.connection:
            self.connection.close()

# Database setup (run this once to create the database and populate it with questions)
def setup_database(db_path):
    """
    Create and populate the SQLite database with random questions.
    :param db_path: Path to the SQLite database file.
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL
            );
        """)
        # Add sample questions
        sample_questions = [
            "What is your favorite hobby?",
            "If you could travel anywhere, where would you go?",
            "What is your favorite food?",
            "Do you prefer cats or dogs?",
            "What is your dream job?"
        ]
        cursor.executemany("INSERT INTO questions (question) VALUES (?);", [(q,) for q in sample_questions])
        connection.commit()
        connection.close()
        print("Database setup complete.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
        raise

# Main function to run the chatbot
def main():
    """
    Main function to initialize and run the chatbot.
    """
    db_path = "chatbot_questions.db"
    # Uncomment the line below to set up the database (run once)
    # setup_database(db_path)
    
    chatbot = Chatbot(db_path)
    try:
        chatbot.engage_user()
    finally:
        chatbot.close_connection()

if __name__ == "__main__":
    main()
```
