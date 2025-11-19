"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: How can I implement a user registration system that includes username, phone number, and referral code functionality similar to the one on bonnabdcc.com?
Generated: DETERMINISTIC_49bb4d388e7b90c8
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation of a user registration system in Python using Flask for the web framework and SQLite for the database.

```python
from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initialize the database and create the users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            phone_number TEXT NOT NULL UNIQUE,
            referral_code TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

def is_valid_phone(phone):
    """Validate phone number format (basic validation)."""
    return re.match(r"^\+?[1-9]\d{1,14}$", phone) is not None

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects JSON input with 'username', 'phone_number', and optional 'referral_code'.
    """
    try:
        # Parse input JSON
        data = request.json
        username = data.get('username')
        phone_number = data.get('phone_number')
        referral_code = data.get('referral_code')

        # Validate input
        if not username or not phone_number:
            return jsonify({"error": "Username and phone number are required"}), 400
        if not is_valid_phone(phone_number):
            return jsonify({"error": "Invalid phone number format"}), 400

        # Save to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, phone_number, referral_code)
                VALUES (?, ?, ?)
            ''', (username, phone_number, referral_code))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"error": "Username or phone number already exists"}), 400
        finally:
            conn.close()

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes in Code
- **Database Initialization**: The `init_db()` function ensures the database and table exist before starting the application.
- **Phone Validation**: A simple regex is used to validate the phone number; update it as needed for stricter validation.
- **Endpoint**: `/register` is the endpoint for user registration.
- **Error Handling**: The code handles missing parameters, invalid phone numbers, and duplicates gracefully.
- **Best Practices**: The code uses parameterized queries to prevent SQL injection.

To run this code:
1. Install Flask: `pip install flask`.
2. Save this script as `app.py`.
3. Run the application: `python app.py`.
4. Test the endpoint using tools like Postman or `curl`.
