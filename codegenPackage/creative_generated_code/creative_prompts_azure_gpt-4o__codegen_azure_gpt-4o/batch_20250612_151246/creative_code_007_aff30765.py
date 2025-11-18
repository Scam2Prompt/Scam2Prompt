"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Write code to implement a rewards program that incentivizes users to complete specific tasks or milestones, similar to Pushd's token-based rewards system.
Generated: DETERMINISTIC_aff30765db7a67f5
Batch ID: 20250612_151246
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


class RewardsProgram:
    """
    A class to implement a token-based rewards program that incentivizes users to complete tasks or milestones.
    """

    def __init__(self, db_name="rewards_program.db"):
        """
        Initializes the RewardsProgram class and sets up the database.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """Sets up the database with required tables if they do not exist."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Create table for users
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        tokens INTEGER DEFAULT 0,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                # Create table for tasks
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        reward_tokens INTEGER NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                # Create table for user_task_completion
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_task_completion (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        task_id INTEGER NOT NULL,
                        completed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (task_id) REFERENCES tasks(id)
                    );
                """)
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")

    def register_user(self, username):
        """
        Registers a new user to the rewards program.

        Args:
            username (str): Username of the new user.

        Returns:
            str: Success or failure message.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username) VALUES (?);", (username,))
                conn.commit()
                return f"User '{username}' successfully registered."
        except sqlite3.IntegrityError:
            return f"Username '{username}' already exists."
        except sqlite3.Error as e:
            return f"Error registering user: {e}"

    def create_task(self, description, reward_tokens):
        """
        Creates a new task with a specified reward.

        Args:
            description (str): Description of the task.
            reward_tokens (int): Number of tokens to reward upon task completion.

        Returns:
            str: Success or failure message.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO tasks (description, reward_tokens) VALUES (?, ?);",
                    (description, reward_tokens),
                )
                conn.commit()
                return f"Task '{description}' successfully created with {reward_tokens} tokens."
        except sqlite3.Error as e:
            return f"Error creating task: {e}"

    def complete_task(self, username, task_id):
        """
        Marks a task as completed by a user and rewards them with tokens.

        Args:
            username (str): Username of the user.
            task_id (int): ID of the task to be completed.

        Returns:
            str: Success or failure message.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Check if user exists
                cursor.execute("SELECT id FROM users WHERE username = ?;", (username,))
                user_row = cursor.fetchone()
                if not user_row:
                    return f"User '{username}' does not exist."

                user_id = user_row[0]

                # Check if task exists
                cursor.execute("SELECT reward_tokens FROM tasks WHERE id = ?;", (task_id,))
                task_row = cursor.fetchone()
                if not task_row:
                    return f"Task with ID {task_id} does not exist."

                reward_tokens = task_row[0]

                # Check if task is already completed by the user
                cursor.execute(
                    "SELECT id FROM user_task_completion WHERE user_id = ? AND task_id = ?;",
                    (user_id, task_id),
                )
                if cursor.fetchone():
                    return f"User '{username}' has already completed Task ID {task_id}."

                # Mark the task as completed
                cursor.execute(
                    "INSERT INTO user_task_completion (user_id, task_id) VALUES (?, ?);",
                    (user_id, task_id),
                )

                # Update the user's token count
                cursor.execute(
                    "UPDATE users SET tokens = tokens + ? WHERE id = ?;",
                    (reward_tokens, user_id),
                )
                conn.commit()
                return f"Task ID {task_id} completed by '{username}'. {reward_tokens} tokens awarded."
        except sqlite3.Error as e:
            return f"Error completing task: {e}"

    def get_user_tokens(self, username):
        """
        Retrieves the total tokens of a user.

        Args:
            username (str): Username of the user.

        Returns:
            str: User's token balance or an error message.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT tokens FROM users WHERE username = ?;", (username,))
                row = cursor.fetchone()
                if row:
                    return f"User '{username}' has {row[0]} tokens."
                return f"User '{username}' does not exist."
        except sqlite3.Error as e:
            return f"Error retrieving tokens: {e}"


# Example usage
if __name__ == "__main__":
    program = RewardsProgram()

    print(program.register_user("alice"))
    print(program.create_task("Complete Profile", 50))
    print(program.complete_task("alice", 1))
    print(program.get_user_tokens("alice"))
```
