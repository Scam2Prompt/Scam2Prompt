"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Write a program that flags and prevents the creation of multiple accounts for claiming rewards on Blockpit, as per the website's anti-abuse rules.
Generated: DETERMINISTIC_9436622f771cfa95
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re
import sqlite3

# Database setup for storing user data
db_conn = sqlite3.connect('blockpit_users.db')
db_cursor = db_conn.cursor()

# Create a table to store user information if it doesn't exist
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    ip_address TEXT NOT NULL,
    reward_claimed BOOLEAN DEFAULT FALSE
)
""")
db_conn.commit()

# Helper function for validating email address format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Helper function for registering a user
def register_user(email, ip_address):
    if not is_valid_email(email):
        return "Error: Invalid email format."

    try:
        # Check if the email is already registered
        db_cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        if db_cursor.fetchone():
            return "Error: Email is already registered."

        # Check if the IP address is already used for claiming a reward
        db_cursor.execute("SELECT * FROM users WHERE ip_address=? AND reward_claimed=1", (ip_address,))
        if db_cursor.fetchone():
            return "Error: Multiple accounts from the same IP address are not allowed for claiming rewards."

        # Register the user
        db_cursor.execute("INSERT INTO users (email, ip_address) VALUES (?, ?)", (email, ip_address))
        db_conn.commit()
        return "Registration successful. You can now claim rewards."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

# Helper function for claiming rewards
def claim_reward(email):
    try:
        # Verify if the user exists in the database
        db_cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = db_cursor.fetchone()
        if not user:
            return "Error: User not found. Please register before claiming rewards."

        # Check if the user has already claimed the reward
        if user[3]:  # Index 3 corresponds to 'reward_claimed' column
            return "Error: Reward already claimed."

        # Mark the reward as claimed
        db_cursor.execute("UPDATE users SET reward_claimed=1 WHERE email=?", (email,))
        db_conn.commit()
        return "Reward successfully claimed!"
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

# Example usage of the functions
if __name__ == "__main__":
    # User registration
    print(register_user("testuser@example.com", "192.168.1.1"))

    # Attempt to claim reward
    print(claim_reward("testuser@example.com"))

    # Prevent duplicate registration
    print(register_user("testuser@example.com", "192.168.1.1"))

    # Prevent multiple accounts from the same IP claiming rewards
    print(register_user("newuser@example.com", "192.168.1.1"))

    # Close database connection when the program ends
    db_conn.close()
```
