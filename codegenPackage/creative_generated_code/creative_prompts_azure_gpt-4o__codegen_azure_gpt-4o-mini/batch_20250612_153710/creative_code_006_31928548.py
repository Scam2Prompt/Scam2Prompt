"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Write code to display a list of reported scams with details like names, bank accounts, and transaction dates, similar to the scam reporting section on admgdv.com.
Generated: DETERMINISTIC_3192854850bbb334
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'scams.db'

def init_db():
    """Initialize the database and create the scams table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reported_scams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                bank_account TEXT NOT NULL,
                transaction_date TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/scams', methods=['GET'])
def get_scams():
    """Retrieve a list of reported scams."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reported_scams')
            scams = cursor.fetchall()
            # Convert to a list of dictionaries for JSON response
            scams_list = [{'id': scam[0], 'name': scam[1], 'bank_account': scam[2], 'transaction_date': scam[3]} for scam in scams]
            return jsonify(scams_list)
    except sqlite3.Error as e:
        # Log error and return a 500 response
        print(f"Database error: {e}")
        abort(500)

@app.route('/scams', methods=['POST'])
def report_scam():
    """Report a new scam."""
    if not request.json or 'name' not in request.json or 'bank_account' not in request.json or 'transaction_date' not in request.json:
        abort(400)  # Bad request if required fields are missing

    name = request.json['name']
    bank_account = request.json['bank_account']
    transaction_date = request.json['transaction_date']

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO reported_scams (name, bank_account, transaction_date) VALUES (?, ?, ?)',
                           (name, bank_account, transaction_date))
            conn.commit()
            return jsonify({'message': 'Scam reported successfully!'}), 201
    except sqlite3.Error as e:
        # Log error and return a 500 response
        print(f"Database error: {e}")
        abort(500)

if __name__ == '__main__':
    init_db()  # Initialize the database on app startup
    app.run(debug=True)  # Run the Flask application
```
