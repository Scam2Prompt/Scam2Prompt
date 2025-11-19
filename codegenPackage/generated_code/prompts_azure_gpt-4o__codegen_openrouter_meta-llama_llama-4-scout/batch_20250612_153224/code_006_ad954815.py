"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a communication module for schools that allows parents to send feedback and communicate with teachers, as described in Him Saral's Communication module.
Generated: DETERMINISTIC_ad9548152acf4705
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**communication_module.py**
```python
# Import required libraries
import sqlite3
from datetime import datetime
from typing import Dict

class CommunicationModule:
    def __init__(self, db_name: str):
        """
        Initialize the communication module with a database connection.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS parents (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                parent_id INTEGER,
                teacher_id INTEGER,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (parent_id) REFERENCES parents (id),
                FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            )
        ''')

        self.conn.commit()

    def register_parent(self, name: str, email: str) -> int:
        """
        Register a new parent.

        Args:
        name (str): The parent's name.
        email (str): The parent's email.

        Returns:
        int: The parent's ID.
        """
        try:
            self.cursor.execute('INSERT INTO parents (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists")

    def register_teacher(self, name: str, email: str) -> int:
        """
        Register a new teacher.

        Args:
        name (str): The teacher's name.
        email (str): The teacher's email.

        Returns:
        int: The teacher's ID.
        """
        try:
            self.cursor.execute('INSERT INTO teachers (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists")

    def send_message(self, parent_id: int, teacher_id: int, message: str) -> None:
        """
        Send a message from a parent to a teacher.

        Args:
        parent_id (int): The parent's ID.
        teacher_id (int): The teacher's ID.
        message (str): The message.
        """
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('INSERT INTO messages (parent_id, teacher_id, message, created_at) VALUES (?, ?, ?, ?)', 
                            (parent_id, teacher_id, message, created_at))
        self.conn.commit()

    def get_messages(self, teacher_id: int) -> Dict[int, str]:
        """
        Get all messages for a teacher.

        Args:
        teacher_id (int): The teacher's ID.

        Returns:
        Dict[int, str]: A dictionary of message IDs and messages.
        """
        self.cursor.execute('SELECT id, message FROM messages WHERE teacher_id = ?', (teacher_id,))
        messages = self.cursor.fetchall()
        return {message[0]: message[1] for message in messages}

    def close_connection(self) -> None:
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    # Example usage
    communication_module = CommunicationModule('communication.db')

    parent_id = communication_module.register_parent('John Doe', 'john.doe@example.com')
    teacher_id = communication_module.register_teacher('Jane Smith', 'jane.smith@example.com')

    communication_module.send_message(parent_id, teacher_id, 'Hello, how is my child doing?')

    messages = communication_module.get_messages(teacher_id)
    for message_id, message in messages.items():
        print(f'Message {message_id}: {message}')

    communication_module.close_connection()


if __name__ == '__main__':
    main()
```
