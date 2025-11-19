"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Create a script that tracks the usage of invitation codes in the Worldcoin system and reports on the rewards earned by users.
Generated: DETERMINISTIC_d62268bf22b56bc9
Batch ID: 20250612_155651
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

class InvitationCodeTracker:
    def __init__(self, db_name="worldcoin.db"):
        """
        Initialize the tracker with a database.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary tables if they don't already exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS invitation_codes (
                code TEXT PRIMARY KEY,
                creator TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS rewards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL,
                user TEXT NOT NULL,
                reward_amount REAL NOT NULL,
                used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (code) REFERENCES invitation_codes (code)
            )
            """)
            
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def create_invitation_code(self, code, creator):
        """
        Register a new invitation code in the system.

        :param code: The invitation code as a string.
        :param creator: The username of the code creator.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            cursor.execute("""
            INSERT INTO invitation_codes (code, creator)
            VALUES (?, ?)
            """, (code, creator))
            
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: The invitation code '{code}' already exists.")
        except sqlite3.Error as e:
            print(f"Error creating invitation code: {e}")
        finally:
            connection.close()

    def use_invitation_code(self, code, user, reward_amount):
        """
        Log the usage of an invitation code and the reward earned.

        :param code: The invitation code used.
        :param user: The username of the user who used the code.
        :param reward_amount: The reward amount earned by the user for using the code.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Check if the code exists
            cursor.execute("""
            SELECT code FROM invitation_codes WHERE code = ?
            """, (code,))
            if cursor.fetchone() is None:
                print(f"Error: The invitation code '{code}' does not exist.")
                return

            # Insert reward information
            cursor.execute("""
            INSERT INTO rewards (code, user, reward_amount)
            VALUES (?, ?, ?)
            """, (code, user, reward_amount))
            
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error using invitation code: {e}")
        finally:
            connection.close()

    def report_rewards(self):
        """
        Generate a report of rewards earned by users.

        :return: A list of dictionaries containing reward information.
        """
        rewards_report = []
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            cursor.execute("""
            SELECT code, user, reward_amount, used_at FROM rewards
            """)
            rewards = cursor.fetchall()

            for reward in rewards:
                rewards_report.append({
                    "code": reward[0],
                    "user": reward[1],
                    "reward_amount": reward[2],
                    "used_at": reward[3]
                })
        except sqlite3.Error as e:
            print(f"Error generating rewards report: {e}")
        finally:
            connection.close()

        return rewards_report

# Example usage
if __name__ == "__main__":
    tracker = InvitationCodeTracker()

    # Create invitation codes
    tracker.create_invitation_code("CODE123", "Alice")
    tracker.create_invitation_code("CODE456", "Bob")

    # Use invitation codes
    tracker.use_invitation_code("CODE123", "Charlie", 10.0)
    tracker.use_invitation_code("CODE456", "Dave", 15.0)

    # Report rewards
    report = tracker.report_rewards()
    for entry in report:
        print(entry)
```
