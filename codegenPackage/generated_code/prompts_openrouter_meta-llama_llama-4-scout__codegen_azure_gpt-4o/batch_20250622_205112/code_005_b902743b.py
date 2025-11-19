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
# Import necessary libraries
import mysql.connector
from mysql.connector import Error

class Leaderboard:
    def __init__(self, host, user, password, database):
        """
        Initialize the Leaderboard class with database connection details.
        """
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def create_table(self):
        """
        Create the leaderboard table if it doesn't already exist.
        """
        try:
            cursor = self.connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                score INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_score(self, username, score):
        """
        Add a new score to the leaderboard.
        """
        try:
            cursor = self.connection.cursor()
            insert_query = "INSERT INTO leaderboard (username, score) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, score))
            self.connection.commit()
        except Error as e:
            print(f"Error adding score: {e}")
            raise

    def get_top_scores(self, limit=10):
        """
        Retrieve the top scores from the leaderboard.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            select_query = "SELECT username, score FROM leaderboard ORDER BY score DESC, created_at ASC LIMIT %s"
            cursor.execute(select_query, (limit,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving top scores: {e}")
            raise

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    # Database connection details
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "password"
    DB_NAME = "leaderboard_db"

    # Initialize the leaderboard system
    leaderboard = Leaderboard(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    # Create the leaderboard table
    leaderboard.create_table()

    # Add some scores
    leaderboard.add_score("Alice", 150)
    leaderboard.add_score("Bob", 200)
    leaderboard.add_score("Charlie", 180)

    # Retrieve and display the top scores
    top_scores = leaderboard.get_top_scores(limit=5)
    print("Top Scores:")
    for rank, entry in enumerate(top_scores, start=1):
        print(f"{rank}. {entry['username']} - {entry['score']}")

    # Close the database connection
    leaderboard.close_connection()
```

### Notes:
- Ensure you have a MySQL database named `leaderboard_db` created before running the script.
- Replace `DB_HOST`, `DB_USER`, and `DB_PASSWORD` with your actual database credentials.
- Install the `mysql-connector-python` library if not already installed: `pip install mysql-connector-python`.
