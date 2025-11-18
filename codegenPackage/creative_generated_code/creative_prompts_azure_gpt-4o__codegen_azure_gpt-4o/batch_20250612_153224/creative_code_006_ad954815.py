"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a communication module for schools that allows parents to send feedback and communicate with teachers, as described in Him Saral's Communication module.
Generated: DETERMINISTIC_ad9548152acf4705
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested production-ready code for a communication module in Python:

```python
"""
Communication Module for Schools
Allows parents to send feedback and communicate with teachers.
"""

import sqlite3
from datetime import datetime

class CommunicationModule:
    def __init__(self, db_name="school_communication.db"):
        """
        Initialize the communication module and set up the database.
        Args:
            db_name (str): SQLite database file name.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Set up the SQLite database with required tables for storing messages.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create a table for messages
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT NOT NULL,  -- Sender's name (e.g., parent)
                recipient TEXT NOT NULL,  -- Recipient's name (e.g., teacher)
                message TEXT NOT NULL,  -- The communication message
                timestamp TEXT NOT NULL  -- When the message was sent
            )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
        finally:
            conn.close()

    def send_message(self, sender, recipient, message):
        """
        Send a message from a parent to a teacher.
        Args:
            sender (str): Name of the sender (parent).
            recipient (str): Name of the recipient (teacher).
            message (str): Message content.
        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert the message into the database
            cursor.execute("""
            INSERT INTO messages (sender, recipient, message, timestamp)
            VALUES (?, ?, ?, ?)
            """, (sender, recipient, message, datetime.now().isoformat()))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error sending message: {e}")
            return False
        finally:
            conn.close()

    def view_messages(self, recipient):
        """
        View all messages sent to a specific recipient (e.g., teacher).
        Args:
            recipient (str): Name of the recipient whose messages will be retrieved.
        Returns:
            list: List of messages sent to the recipient.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Retrieve messages for the specified recipient
            cursor.execute("""
            SELECT sender, message, timestamp
            FROM messages
            WHERE recipient = ?
            ORDER BY timestamp DESC
            """, (recipient,))

            messages = cursor.fetchall()
            return messages
        except sqlite3.Error as e:
            print(f"Error retrieving messages: {e}")
            return []
        finally:
            conn.close()

    def delete_message(self, message_id):
        """
        Delete a message from the database using its ID.
        Args:
            message_id (int): ID of the message to delete.
        Returns:
            bool: True if the message was deleted successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Delete the message by its ID
            cursor.execute("""
            DELETE FROM messages
            WHERE id = ?
            """, (message_id,))

            conn.commit()
            return cursor.rowcount > 0  # Returns True if at least one row was deleted
        except sqlite3.Error as e:
            print(f"Error deleting message: {e}")
            return False
        finally:
            conn.close()


if __name__ == "__main__":
    # Example usage of the CommunicationModule
    module = CommunicationModule()

    # Sending a message
    if module.send_message("Parent A", "Teacher B", "My child needs help with homework."):
        print("Message sent successfully!")
    else:
        print("Failed to send message.")

    # Viewing messages
    print("\nMessages for Teacher B:")
    messages = module.view_messages("Teacher B")
    for sender, message, timestamp in messages:
        print(f"[{timestamp}] {sender}: {message}")

    # Deleting a message
    message_id_to_delete = 1  # Example ID
    if module.delete_message(message_id_to_delete):
        print(f"Message with ID {message_id_to_delete} deleted successfully.")
    else:
        print(f"Failed to delete message with ID {message_id_to_delete}.")
```

This code fulfills your requirements, including error handling, documentation, best practices, and production readiness. Adjust the database name or structure based on your specific needs.
