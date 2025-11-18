"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Create a leaderboard tracking system using ChainGPT or similar tools for participants in the $PLENA Quest campaign.
Generated: DETERMINISTIC_a20cbcfb51c34efc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sqlite3
from datetime import datetime


# Leaderboard class definition
class Leaderboard:
    def __init__(self, db_name="leaderboard.db"):
        """
        Initialize the leaderboard system.
        Creates or connects to a database and sets up the required table.

        :param db_name: Name of the database file to store leaderboard data.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the database by creating a leaderboard table if it doesn't exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Create leaderboard table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    participant_name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    last_updated TIMESTAMP NOT NULL
                )
                """
            )

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error setting up the database: {e}")
        finally:
            if connection:
                connection.close()

    def add_or_update_participant(self, participant_name, score):
        """
        Adds a new participant or updates the score of an existing participant.

        :param participant_name: Name of the participant.
        :param score: Score to update/add for the participant.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Check if participant already exists
            cursor.execute(
                "SELECT id FROM leaderboard WHERE participant_name = ?", (participant_name,)
            )
            result = cursor.fetchone()

            current_time = datetime.now()

            if result:
                # Update existing participant's score
                cursor.execute(
                    "UPDATE leaderboard SET score = ?, last_updated = ? WHERE id = ?",
                    (score, current_time, result[0]),
                )
            else:
                # Add new participant
                cursor.execute(
                    "INSERT INTO leaderboard (participant_name, score, last_updated) VALUES (?, ?, ?)",
                    (participant_name, score, current_time),
                )

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding/updating participant: {e}")
        finally:
            if connection:
                connection.close()

    def get_leaderboard(self):
        """
        Retrieves the leaderboard sorted by score in descending order.

        :return: List of leaderboard entries, each entry being a dictionary with participant name, score, and last updated.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute(
                "SELECT participant_name, score, last_updated FROM leaderboard ORDER BY score DESC"
            )
            rows = cursor.fetchall()

            return [
                {"participant_name": row[0], "score": row[1], "last_updated": row[2]}
                for row in rows
            ]
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            return []
        finally:
            if connection:
                connection.close()

    def delete_participant(self, participant_name):
        """
        Deletes a participant from the leaderboard.

        :param participant_name: Name of the participant to delete.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM leaderboard WHERE participant_name = ?",
                (participant_name,),
            )

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting participant: {e}")
        finally:
            if connection:
                connection.close()


# Example usage of the Leaderboard class
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add or update participants
    leaderboard.add_or_update_participant("Alice", 1200)
    leaderboard.add_or_update_participant("Bob", 900)
    leaderboard.add_or_update_participant("Charlie", 1500)

    # Retrieve and print leaderboard
    print("Leaderboard:")
    for entry in leaderboard.get_leaderboard():
        print(entry)

    # Delete a participant
    leaderboard.delete_participant("Bob")

    # Print leaderboard after deletion
    print("\nLeaderboard after deletion:")
    for entry in leaderboard.get_leaderboard():
        print(entry)
```
