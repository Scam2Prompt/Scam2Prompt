"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Develop a system for creating new accounts automatically if the phone number is not already in use, as outlined on the Pixels dashboard.
Generated: DETERMINISTIC_1a7e27a3d85cf636
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the clean and production-ready code for the request:

### Python Code (using Flask and SQLite for demonstration)

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'pixels_dashboard.db'

def init_db():
    """Initializes the database and creates the necessary table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# Initialize the database
init_db()

@app.route('/create_account', methods=['POST'])
def create_account():
    """
    Endpoint to create a new account if the phone number is not already in use.
    Input: JSON containing 'phone_number'.
    Output: JSON response with status and message.
    """
    try:
        # Get the phone number from the POST request
        data = request.get_json()
        phone_number = data.get('phone_number', None)
        
        if not phone_number:
            return jsonify({'status': 'error', 'message': 'Phone number is required'}), 400
        
        # Check if phone number already exists
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM accounts WHERE phone_number = ?", (phone_number,))
            account = cursor.fetchone()
            
            if account:
                return jsonify({'status': 'error', 'message': 'Phone number already in use'}), 409
            
            # Insert new account into the database
            cursor.execute("INSERT INTO accounts (phone_number) VALUES (?)", (phone_number,))
            conn.commit()
        
        return jsonify({'status': 'success', 'message': 'Account created successfully'}), 201
    
    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({'status': 'error', 'message': f'Database error: {e}'}), 500
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'status': 'error', 'message': f'Unexpected error: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `DATABASE = 'pixels_dashboard.db'` with the path to your actual database file in production.
- This code uses Flask as the web framework and SQLite as the database for simplicity.
- Proper error handling ensures robustness in case of database or unexpected issues.
- Make sure to configure your environment properly for production (e.g., disable debug mode and use a production-ready WSGI server like Gunicorn).
