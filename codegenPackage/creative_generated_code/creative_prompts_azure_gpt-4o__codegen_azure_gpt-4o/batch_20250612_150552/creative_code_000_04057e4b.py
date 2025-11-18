"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-bsquarednetwork.pages.dev
Prompt: Write a script to track $B2 rewards history using data from a staked BTC balance and display the reward type, amount, and transaction details.
Generated: DETERMINISTIC_04057e4ba77bad71
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sqlite3

# Database setup
DB_NAME = "rewards_tracker.db"

def initialize_database():
    """
    Initialize the database structure for storing rewards history.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reward_type TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_details TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def log_reward(reward_type, amount, transaction_details):
    """
    Logs reward details into the database.
    :param reward_type: Type of reward (e.g., "staking", "bonus").
    :param amount: Amount of reward in $B2.
    :param transaction_details: Additional transaction details (e.g., transaction ID or description).
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Insert reward record
        cursor.execute("""
            INSERT INTO rewards_history (reward_type, amount, transaction_details, timestamp)
            VALUES (?, ?, ?, ?)
        """, (reward_type, amount, transaction_details, datetime.datetime.now().isoformat()))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def fetch_rewards_history():
    """
    Fetches all reward entries from the database.
    Returns a list of dictionaries with reward details.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Query all rewards
        cursor.execute("SELECT * FROM rewards_history")
        rows = cursor.fetchall()

        # Convert rows to list of dictionaries
        rewards = []
        for row in rows:
            rewards.append({
                "id": row[0],
                "reward_type": row[1],
                "amount": row[2],
                "transaction_details": row[3],
                "timestamp": row[4],
            })

        return rewards
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        connection.close()

def display_rewards_history():
    """
    Displays the rewards history in a user-friendly format.
    """
    rewards = fetch_rewards_history()
    if not rewards:
        print("No rewards history available.")
        return

    print("\nRewards History:")
    print("--------------------------------------------------------")
    for reward in rewards:
        print(f"ID: {reward['id']}")
        print(f"Reward Type: {reward['reward_type']}")
        print(f"Amount: {reward['amount']}")
        print(f"Transaction Details: {reward['transaction_details']}")
        print(f"Timestamp: {reward['timestamp']}")
        print("--------------------------------------------------------")

# Main script execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example: Log a new reward
    log_reward("staking", 12.5, "Transaction ID: abc123")

    # Example: Fetch and display rewards history
    display_rewards_history()
```
