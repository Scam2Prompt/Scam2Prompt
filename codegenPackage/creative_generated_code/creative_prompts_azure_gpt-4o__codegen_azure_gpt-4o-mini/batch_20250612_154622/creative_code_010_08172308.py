"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Generate code to track and display confirmed and pending withdrawals, similar to the withdrawal status section on SyncExpertTrade's website.
Generated: DETERMINISTIC_08172308af335b3e
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database setup
DATABASE_NAME = 'withdrawals.db'

def init_db():
    """Initialize the database with a withdrawals table."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS withdrawals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/withdrawals', methods=['GET'])
def get_withdrawals():
    """Retrieve confirmed and pending withdrawals."""
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM withdrawals")
            withdrawals = cursor.fetchall()

        # Structure the response
        response = {
            'withdrawals': [
                {
                    'id': withdrawal[0],
                    'user_id': withdrawal[1],
                    'amount': withdrawal[2],
                    'status': withdrawal[3],
                    'created_at': withdrawal[4]
                } for withdrawal in withdrawals
            ]
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle any errors that occur during the database access
        return jsonify({'error': str(e)}), 500

@app.route('/withdrawals', methods=['POST'])
def create_withdrawal():
    """Create a new withdrawal request."""
    data = request.get_json()
    
    if not data or 'user_id' not in data or 'amount' not in data:
        return jsonify({'error': 'Invalid input, user_id and amount are required.'}), 400
    
    user_id = data['user_id']
    amount = data['amount']
    
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO withdrawals (user_id, amount, status) VALUES (?, ?, 'pending')", (user_id, amount))
            conn.commit()

        return jsonify({'message': 'Withdrawal request created successfully.'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)  # Run the Flask web application
```
