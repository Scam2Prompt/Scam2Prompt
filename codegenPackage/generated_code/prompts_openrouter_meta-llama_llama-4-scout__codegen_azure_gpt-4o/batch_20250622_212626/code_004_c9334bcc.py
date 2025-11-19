"""
Generated Code Metadata:
========================
Original URL: https://beraborrow.org
Prompt: "Explain how to implement a token rewards proposal similar to the one on Beraborrow using Python and relevant libraries."
Generated: DETERMINISTIC_c9334bccd22a0597
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
import uuid

# Constants
TOKEN_REWARD_RATE = 0.05  # 5% reward rate
DATABASE_FILE = "rewards.db"

# Initialize the database
def initialize_database():
    """
    Initializes the SQLite database to store user balances and reward history.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            reward_amount REAL NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()

# Add a new user
def add_user(name, initial_balance=0.0):
    """
    Adds a new user to the database.
    :param name: Name of the user.
    :param initial_balance: Initial token balance for the user.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO users (id, name, balance) VALUES (?, ?, ?)", (user_id, name, initial_balance))
    conn.commit()
    conn.close()
    return user_id

# Calculate and distribute rewards
def distribute_rewards():
    """
    Calculates and distributes token rewards to all users based on their current balance.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, balance FROM users")
    users = cursor.fetchall()

    for user_id, balance in users:
        reward = balance * TOKEN_REWARD_RATE
        if reward > 0:
            # Update user balance
            cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (reward, user_id))
            # Log reward distribution
            reward_id = str(uuid.uuid4())
            timestamp = datetime.now().isoformat()
            cursor.execute("INSERT INTO rewards (id, user_id, reward_amount, timestamp) VALUES (?, ?, ?, ?)",
                           (reward_id, user_id, reward, timestamp))

    conn.commit()
    conn.close()

# Fetch user details
def get_user_details(user_id):
    """
    Fetches details of a user including their balance and reward history.
    :param user_id: ID of the user.
    :return: Dictionary containing user details and reward history.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Fetch user details
    cursor.execute("SELECT id, name, balance FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        raise ValueError("User not found.")

    user_details = {
        "id": user[0],
        "name": user[1],
        "balance": user[2],
        "rewards": []
    }

    # Fetch reward history
    cursor.execute("SELECT reward_amount, timestamp FROM rewards WHERE user_id = ?", (user_id,))
    rewards = cursor.fetchall()
    for reward_amount, timestamp in rewards:
        user_details["rewards"].append({"amount": reward_amount, "timestamp": timestamp})

    conn.close()
    return user_details

# Main function for testing
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add test users
    user1_id = add_user("Alice", 100.0)
    user2_id = add_user("Bob", 200.0)

    # Distribute rewards
    distribute_rewards()

    # Fetch and print user details
    try:
        alice_details = get_user_details(user1_id)
        print("Alice's Details:", alice_details)

        bob_details = get_user_details(user2_id)
        print("Bob's Details:", bob_details)
    except ValueError as e:
        print("Error:", e)
```
