"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Develop a tool to track and audit reward distributions from the Story Staking platform, ensuring transparency and fairness.
Generated: DETERMINISTIC_9b98a6877a03c028
Batch ID: 20250612_153832
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

class RewardAuditTool:
    """
    A tool to track and audit reward distributions from the Story Staking platform.
    """

    def __init__(self, db_name='reward_audit.db'):
        """
        Initialize the database connection and create the necessary table if it doesn't exist.

        :param db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Create the reward_distributions table if it does not exist.
        """
        try:
            with self.conn:
                self.conn.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS reward_distributions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT NOT NULL,
                        reward_amount REAL NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        reason TEXT
                    )
                    '''
                )
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {e}")

    def add_distribution(self, user_id, reward_amount, reason):
        """
        Add a new reward distribution record to the database.

        :param user_id: The ID of the user receiving the reward.
        :param reward_amount: The amount of reward distributed.
        :param reason: The reason for the reward distribution.
        """
        try:
            with self.conn:
                self.conn.execute(
                    '''
                    INSERT INTO reward_distributions (user_id, reward_amount, reason)
                    VALUES (?, ?, ?)
                    ''',
                    (user_id, reward_amount, reason)
                )
            print(f"Successfully added reward distribution for user {user_id}.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding the distribution: {e}")

    def audit_distributions(self):
        """
        Retrieve and display all reward distributions from the database.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM reward_distributions")
            rows = cursor.fetchall()
            print("ID | User ID | Reward Amount | Timestamp | Reason")
            print("-" * 50)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        except sqlite3.Error as e:
            print(f"An error occurred while fetching distributions: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Example usage of the RewardAuditTool
    audit_tool = RewardAuditTool()

    # Adding some example reward distributions
    audit_tool.add_distribution(user_id="user123", reward_amount=50.0, reason="Participation in event.")
    audit_tool.add_distribution(user_id="user456", reward_amount=25.0, reason="Referral bonus.")

    # Auditing all distributions
    audit_tool.audit_distributions()

    # Close the tool
    audit_tool.close()
```
