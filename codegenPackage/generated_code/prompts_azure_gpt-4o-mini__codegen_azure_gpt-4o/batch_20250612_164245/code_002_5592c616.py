"""
Generated Code Metadata:
========================
Original URL: https://v.0xz.org
Prompt: Write a code snippet that illustrates a common security vulnerability and explain how it can be reported through a bug bounty program.
Generated: DETERMINISTIC_5592c61661f46906
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This Python code snippet demonstrates a common security vulnerability: SQL Injection.
# It is intentionally insecure to illustrate the issue. Do NOT use this code in production.

import sqlite3

def insecure_login(username, password):
    """
    Simulates an insecure login function vulnerable to SQL Injection.
    """
    try:
        # Connect to a sample SQLite database
        connection = sqlite3.connect("example.db")
        cursor = connection.cursor()

        # Create a users table for demonstration purposes
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)

        # Insert a sample user (username: admin, password: password123)
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'password123')")

        # Vulnerable query: User input is directly concatenated into the SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")  # Debugging purposes

        # Execute the insecure query
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            print("Login successful!")
        else:
            print("Invalid credentials.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

# Example of exploiting the vulnerability:
# Input: username = "admin' --", password = "anything"
# This input bypasses authentication by commenting out the password check.
insecure_login("admin' --", "anything")

# Reporting the vulnerability:
# If you discover this vulnerability in a real-world application, report it through a bug bounty program.
# Provide details such as:
# - Steps to reproduce the issue
# - Impact of the vulnerability (e.g., unauthorized access)
# - Suggested fix (e.g., use parameterized queries to prevent SQL Injection)
```
