"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Generate a code snippet that demonstrates how to track bonuses earned through tasks on Claim USDT Box.
Generated: DETERMINISTIC_456ffbea1e40be5a
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

class BonusTracker:
    """
    A class to track bonuses earned through tasks on Claim USDT Box.
    """

    def __init__(self, db_name: str = 'bonuses.db'):
        """
        Initializes the BonusTracker with a SQLite database.

        :param db_name: The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Creates the bonuses table if it doesn't exist."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS bonuses (
                        id INTEGER PRIMARY KEY,
                        task_name TEXT NOT NULL,
                        bonus_amount REAL NOT NULL,
                        date_earned TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_bonus(self, task_name: str, bonus_amount: float, date_earned: str):
        """
        Adds a bonus to the database.

        :param task_name: The name of the task for which the bonus was earned.
        :param bonus_amount: The amount of the bonus earned.
        :param date_earned: The date when the bonus was earned.
        """
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO bonuses (task_name, bonus_amount, date_earned)
                    VALUES (?, ?, ?)
                ''', (task_name, bonus_amount, date_earned))
        except sqlite3.Error as e:
            print(f"Error adding bonus: {e}")

    def get_all_bonuses(self) -> List[Tuple[int, str, float, str]]:
        """
        Retrieves all bonuses from the database.

        :return: A list of tuples containing all bonuses.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM bonuses')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving bonuses: {e}")
            return []

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == '__main__':
    tracker = BonusTracker()

    # Adding some bonuses
    tracker.add_bonus('Complete Survey', 10.0, '2023-10-01')
    tracker.add_bonus('Watch Video', 5.0, '2023-10-02')

    # Retrieving and printing all bonuses
    bonuses = tracker.get_all_bonuses()
    for bonus in bonuses:
        print(f"ID: {bonus[0]}, Task: {bonus[1]}, Amount: {bonus[2]}, Date: {bonus[3]}")

    # Closing the tracker
    tracker.close()
```
