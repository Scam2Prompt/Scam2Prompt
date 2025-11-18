"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenatoken.vercel.app
Prompt: Generate code to track weekly leaderboard rankings for the $PLENA Road to TGE Quest using data from Galxe tasks.
Generated: DETERMINISTIC_c8275ab626622917
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.galxe.com/v1/tasks": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple
import requests
import logging

# Set up logging for better debugging and tracking
logging.basicConfig(level=logging.INFO)

class Leaderboard:
    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initializes the Leaderboard class and creates a database connection.
        
        :param db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Creates the leaderboard table if it doesn't exist.
        """
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS rankings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    score INTEGER NOT NULL
                )
            ''')
        logging.info("Leaderboard table created or already exists.")

    def update_rankings(self, data: List[Tuple[str, int]]):
        """
        Updates the leaderboard rankings in the database based on provided data.
        
        :param data: List of tuples containing (username, score)
        """
        try:
            with self.conn:
                self.conn.executemany('''
                    INSERT INTO rankings (username, score) VALUES (?, ?)
                    ON CONFLICT(username) DO UPDATE SET score = excluded.score
                ''', data)
            logging.info("Rankings updated successfully.")
        except Exception as e:
            logging.error(f"Error updating rankings: {e}")

    def get_top_rankings(self, limit: int = 10) -> List[Tuple[str, int]]:
        """
        Retrieves the top rankings from the database.
        
        :param limit: Number of top rankings to retrieve
        :return: List of tuples containing (username, score)
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT username, score FROM rankings ORDER BY score DESC LIMIT ?', (limit,))
            results = cursor.fetchall()
            logging.info("Top rankings retrieved successfully.")
            return results
        except Exception as e:
            logging.error(f"Error retrieving top rankings: {e}")
            return []

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()
        logging.info("Database connection closed.")

def fetch_task_data() -> List[Tuple[str, int]]:
    """
    Fetches task data from Galxe API.
    
    :return: List of tuples containing (username, score)
    """
    try:
        response = requests.get("https://api.galxe.com/v1/tasks")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        tasks = response.json()

        # Assuming the tasks data structure contains 'username' and 'score'
        return [(task['username'], task['score']) for task in tasks]
    except requests.RequestException as e:
        logging.error(f"Error fetching task data: {e}")
        return []

def main():
    """
    Main function to manage leaderboard updates and retrieval.
    """
    leaderboard = Leaderboard()
    
    # Fetch the latest task data
    task_data = fetch_task_data()
    
    # Update the leaderboard with fetched data
    if task_data:
        leaderboard.update_rankings(task_data)
    
    # Retrieve and print the top rankings
    top_rankings = leaderboard.get_top_rankings()
    for rank in top_rankings:
        print(f"Username: {rank[0]}, Score: {rank[1]}")
    
    leaderboard.close()

if __name__ == "__main__":
    main()
```
