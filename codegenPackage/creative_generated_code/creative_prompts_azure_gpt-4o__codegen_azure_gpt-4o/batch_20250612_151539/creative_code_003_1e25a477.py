"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Develop a script to implement a "Call Me Back" feature for an e-commerce site, similar to the callback request functionality on the Joss Home website.
Generated: DETERMINISTIC_1e25a477f8883f61
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
call_me_back.py

This script implements a "Call Me Back" feature for an e-commerce site. 
Users can request a callback by entering their name, phone number, and preferred time. 
The data is validated and stored for processing by customer service.

Dependencies:
- Flask: Web framework for Python
- SQLite: Lightweight database for storing callback requests
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database file name
DATABASE = "callback_requests.db"

# Initialize the database with a table for callback requests
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CallbackRequests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        preferred_time TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the script starts
init_db()

@app.route('/request-callback', methods=['POST'])
def request_callback():
    """
    Endpoint for users to request a callback.

    Expects JSON payload with:
    - name: User's name (string)
    - phone: User's phone number (string)
    - preferred_time: Preferred callback time (string, in 'YYYY-MM-DD HH:MM:SS' format)

    Returns:
    - Success or error message.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        preferred_time = data.get('preferred_time')

        # Validate input
        if not name or not phone or not preferred_time:
            return jsonify({"error": "All fields (name, phone, preferred_time) are required."}), 400

        try:
            # Validate preferred_time format
            datetime.strptime(preferred_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({"error": "preferred_time must be in 'YYYY-MM-DD HH:MM:SS' format."}), 400

        # Store the request in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO CallbackRequests (name, phone, preferred_time, created_at)
        VALUES (?, ?, ?, ?)
        """, (name, phone, preferred_time, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()

        return jsonify({"message": "Callback request successfully submitted."}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/callback-requests', methods=['GET'])
def get_callback_requests():
    """
    Endpoint to fetch all callback requests.

    Returns:
    - JSON list of callback requests.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, preferred_time, created_at FROM CallbackRequests")
        rows = cursor.fetchall()
        conn.close()

        # Format the rows as a list of dictionaries
        callback_requests = [
            {
                "id": row[0],
                "name": row[1],
                "phone": row[2],
                "preferred_time": row[3],
                "created_at": row[4]
            }
            for row in rows
        ]

        return jsonify(callback_requests), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
