"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Develop a simple leaderboard system using a database (e.g., MySQL) and a programming language (e.g., Python), inspired by Big Time's leaderboard features.
Generated: DETERMINISTIC_b902743b5ebd1f89
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import mysql.connector
from mysql.connector import Error

class Leaderboard:
    def __init__(self, host, database, user, password):
        """Initialize the database connection."""
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Successfully connected to the database.")
        except Error as e:
            print(f"Error: {e}")
            raise

    def create_table(self):
        """Create the leaderboard table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            score INT NOT NULL,
            UNIQUE (username)
        )
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(create_table_query)
            self.connection.commit()
            print("Leaderboard table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()

    def add_score(self, username, score):
        """Add or update a user's score in the leaderboard."""
        insert_score_query = """
        INSERT INTO leaderboard (username, score) VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE score = GREATEST(score, VALUES(score))
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(insert_score_query, (username, score))
            self.connection.commit()
            print(f"Score for {username} added/updated successfully.")
        except Error as e:
            print(f"Error adding/updating score: {e}")
        finally:
            cursor.close()

    def get_leaderboard(self, limit=10):
        """Retrieve the top scores from the leaderboard."""
        select_query = "SELECT username, score FROM leaderboard ORDER BY score DESC LIMIT %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(select_query, (limit,))
            results = cursor.fetchall()
            print("Leaderboard:")
            for idx, (username, score) in enumerate(results, start=1):
                print(f"{idx}. {username}: {score}")
        except Error as e:
            print(f"Error retrieving leaderboard: {e}")
        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Replace with your actual database credentials
    db_host = 'localhost'
    db_name = 'leaderboard_db'
    db_user = 'root'
    db_password = 'password'

    leaderboard = Leaderboard(db_host, db_name, db_user, db_password)
    leaderboard.create_table()
    leaderboard.add_score('Alice', 150)
    leaderboard.add_score('Bob', 200)
    leaderboard.add_score('Charlie', 100)
    leaderboard.get_leaderboard()
    leaderboard.close_connection()
```
