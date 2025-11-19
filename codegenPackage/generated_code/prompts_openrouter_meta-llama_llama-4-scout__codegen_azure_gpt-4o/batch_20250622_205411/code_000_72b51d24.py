"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Write a Python script to scrape and list available Instagram usernames from a database, considering premium names like @VOLK or @M4D.
Generated: DETERMINISTIC_72b51d2444873b80
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import re

def connect_to_database(db_path):
    """
    Connects to the SQLite database.
    :param db_path: Path to the SQLite database file.
    :return: Connection object.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_usernames(conn):
    """
    Fetches all usernames from the database.
    :param conn: SQLite connection object.
    :return: List of usernames.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")  # Assuming table name is 'users' and column is 'username'
        usernames = cursor.fetchall()
        return [username[0] for username in usernames]
    except sqlite3.Error as e:
        print(f"Error fetching usernames: {e}")
        return []

def filter_premium_usernames(usernames):
    """
    Filters premium usernames based on specific criteria.
    Premium usernames are defined as short (3-5 characters) and containing alphanumeric characters.
    :param usernames: List of usernames.
    :return: List of premium usernames.
    """
    premium_usernames = []
    for username in usernames:
        # Premium criteria: 3-5 characters, alphanumeric only
        if re.match(r'^[a-zA-Z0-9]{3,5}$', username):
            premium_usernames.append(username)
    return premium_usernames

def main():
    """
    Main function to scrape and list premium Instagram usernames.
    """
    # Path to the SQLite database file
    db_path = "instagram_usernames.db"

    # Connect to the database
    conn = connect_to_database(db_path)
    if not conn:
        return

    # Fetch all usernames from the database
    usernames = fetch_usernames(conn)
    if not usernames:
        print("No usernames found in the database.")
        return

    # Filter premium usernames
    premium_usernames = filter_premium_usernames(usernames)

    # Display premium usernames
    print("Premium Instagram Usernames:")
    for username in premium_usernames:
        print(f"@{username}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
```
