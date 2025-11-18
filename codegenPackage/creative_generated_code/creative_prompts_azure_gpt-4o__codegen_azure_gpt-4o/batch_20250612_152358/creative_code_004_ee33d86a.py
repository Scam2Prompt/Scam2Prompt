"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomnetwork.pages.dev
Prompt: Create a script to track leaderboard XP history for Venom Network users and visualize their progress over multiple stages.
Generated: DETERMINISTIC_ee33d86a6d1732f2
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import matplotlib.pyplot as plt


class LeaderboardTracker:
    """
    Tracks and visualizes leaderboard XP history for Venom Network users.
    """

    def __init__(self, db_name="leaderboard.db"):
        """
        Initialize the leaderboard tracker with a database connection.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary database table if it doesn't exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS xp_history (
                        user_id TEXT NOT NULL,
                        stage INTEGER NOT NULL,
                        xp INTEGER NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY (user_id, stage)
                    )
                """)
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise

    def record_xp(self, user_id, stage, xp):
        """
        Record a user's XP at a specific stage.
        :param user_id: Unique identifier for the user.
        :param stage: The stage number.
        :param xp: The XP value.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO xp_history (user_id, stage, xp)
                    VALUES (?, ?, ?)
                """, (user_id, stage, xp))
        except sqlite3.Error as e:
            print(f"Error recording XP: {e}")
            raise

    def fetch_xp_history(self, user_id):
        """
        Fetch the XP history for a specific user.
        :param user_id: Unique identifier for the user.
        :return: List of tuples containing stage and XP.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT stage, xp FROM xp_history
                    WHERE user_id = ?
                    ORDER BY stage ASC
                """, (user_id,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching XP history: {e}")
            raise

    def visualize_progress(self, user_id):
        """
        Visualize the user's XP progress over multiple stages.
        :param user_id: Unique identifier for the user.
        """
        try:
            data = self.fetch_xp_history(user_id)
            if not data:
                print(f"No data found for user_id: {user_id}")
                return

            stages, xp_values = zip(*data)

            plt.figure(figsize=(10, 6))
            plt.plot(stages, xp_values, marker='o', label=f"User: {user_id}")
            plt.title(f"XP Progress for {user_id}")
            plt.xlabel("Stage")
            plt.ylabel("XP")
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error visualizing progress: {e}")
            raise


# Usage example:
if __name__ == "__main__":
    tracker = LeaderboardTracker()

    # Example data recording
    tracker.record_xp("user123", 1, 150)
    tracker.record_xp("user123", 2, 250)
    tracker.record_xp("user123", 3, 400)

    tracker.record_xp("user456", 1, 100)
    tracker.record_xp("user456", 2, 300)

    # Fetch XP history and visualize progress
    tracker.visualize_progress("user123")
    tracker.visualize_progress("user456")
```
