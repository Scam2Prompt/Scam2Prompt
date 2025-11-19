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
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the request
    username = request.form['username']
    password = request.form['password']

    # Vulnerable SQL query - susceptible to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        conn = get_db_connection()
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            return jsonify({"message": "Login successful!"}), 200
        else:
            return jsonify({"message": "Invalid credentials."}), 401

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

# Explanation of the Vulnerability:
# The above code snippet demonstrates a SQL Injection vulnerability in the login function.
# An attacker can manipulate the `username` or `password` fields to execute arbitrary SQL code.
# For example, by sending a request with `username=admin' --` and any password, the attacker can bypass authentication.

# Reporting through a Bug Bounty Program:
# To report this vulnerability through a bug bounty program, follow these steps:
# 1. Identify the target application and ensure it is part of the bug bounty program.
# 2. Reproduce the vulnerability in a controlled environment.
# 3. Document the steps to reproduce the issue, including the payload used.
# 4. Provide a detailed explanation of the impact of the vulnerability.
# 5. Submit your report through the bug bounty platform, adhering to their guidelines.
