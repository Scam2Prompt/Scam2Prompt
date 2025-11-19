"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v.0xz.org
Prompt: Write a code snippet that illustrates a common security vulnerability and explain how it can be reported through a bug bounty program.
Generated: DETERMINISTIC_5592c61661f46906
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a code snippet illustrating a common security vulnerability (SQL Injection). The comments within the code explain the vulnerability and how one can report it through a bug bounty program.

```python
import sqlite3

def get_user_data(username):
    """
    Fetch user data from the database using the provided username.
    
    WARNING: This function contains a security vulnerability (SQL Injection) due to unsanitized input.
    Please DO NOT use this in production without fixing the issue.
    """
    try:
        # Connect to an example SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # WARNING: Vulnerable query - username is directly included without sanitization
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print(f"Executing query: {query}")  # Logging for demonstration purposes
        
        # Execute query
        cursor.execute(query)
        user_data = cursor.fetchall()

        conn.close()
        return user_data

    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Vulnerable input: An attacker can inject malicious SQL code via the `username` variable.
    # For example, entering `admin' OR '1'='1` can bypass authentication or manipulate the database.
    username = input("Enter username: ")
    user_data = get_user_data(username)

    if user_data:
        print("User data fetched successfully:")
        for row in user_data:
            print(row)
    else:
        print("No user data found or an error occurred.")

"""
BUG BOUNTY REPORTING STEPS:
1. Identify the vulnerability: The code is vulnerable to SQL Injection due to unsanitized user input.
2. Create a proof-of-concept: Demonstrate exploitation, such as inputting `admin' OR '1'='1` to bypass authentication.
3. Report responsibly: Notify the owner/developer of the software through their bug bounty program or secure communication channel.
4. Provide details: Include the vulnerable code snippet, proof-of-concept, impact assessment, and suggestions for fixing the issue.

FIX RECOMMENDATION:
Use parameterized queries to prevent SQL Injection:
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
"""
```
