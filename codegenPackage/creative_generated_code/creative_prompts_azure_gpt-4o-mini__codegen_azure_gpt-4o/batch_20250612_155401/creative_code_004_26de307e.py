"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Illustrate how to implement a user registration system for the Meet A Great American community, focusing on capturing user details and their professional achievements.
Generated: DETERMINISTIC_26de307e3e685b60
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: user_registration_system.py

import re
import sqlite3


class UserRegistrationSystem:
    """
    A user registration system to capture user details and their professional achievements
    for the Meet A Great American community.
    """

    def __init__(self, db_name="user_registration.db"):
        """
        Initialize the system and set up the database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Set up the SQLite database with necessary tables if they don't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    age INTEGER NOT NULL,
                    profession TEXT NOT NULL
                )
            """)

            # Create achievements table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS achievements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    achievement TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def register_user(self, name, email, age, profession):
        """
        Register a new user in the system.
        :param name: Full name of the user.
        :param email: Email address of the user.
        :param age: Age of the user.
        :param profession: Profession of the user.
        :return: The ID of the newly registered user, or None if registration fails.
        """
        # Basic input validation
        if not self._validate_email(email):
            print("Invalid email format.")
            return None
        if not isinstance(age, int) or age < 0:
            print("Invalid age value.")
            return None

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert the user into the database
            cursor.execute("""
                INSERT INTO users (name, email, age, profession)
                VALUES (?, ?, ?, ?)
            """, (name, email, age, profession))

            conn.commit()
            return cursor.lastrowid  # Return the ID of the newly created user
        except sqlite3.IntegrityError:
            print("Error: A user with this email already exists.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()
        return None

    def add_achievement(self, user_id, achievement):
        """
        Add an achievement for a specific user.
        :param user_id: ID of the user.
        :param achievement: Achievement description.
        :return: True if the achievement was added successfully, False otherwise.
        """
        if not achievement:
            print("Achievement cannot be empty.")
            return False

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert the achievement into the database
            cursor.execute("""
                INSERT INTO achievements (user_id, achievement)
                VALUES (?, ?)
            """, (user_id, achievement))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()
        return False

    @staticmethod
    def _validate_email(email):
        """
        Validate the format of an email address.
        :param email: Email address to validate.
        :return: True if the email format is valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None


# Example usage
if __name__ == "__main__":
    system = UserRegistrationSystem()

    # Register a new user
    user_id = system.register_user("John Doe", "john.doe@example.com", 35, "Software Engineer")
    if user_id:
        print(f"User registered successfully with ID: {user_id}")

        # Add achievements for the user
        if system.add_achievement(user_id, "Developed a successful open-source project"):
            print("Achievement added successfully.")
```
