"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: Write a code snippet for a web application that allows users to submit inquiries about health product regulations and guidelines based on the services offered by the Consumer Protection and Public Health Division.
Generated: DETERMINISTIC_8bd136fa1ecbc360
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'inquiries.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        inquiry TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to allow users to submit inquiries about health product regulations and guidelines.
    """
    try:
        # Get data from the request
        data = request.get_json()

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        inquiry = data.get('inquiry')

        if not name or not email or not inquiry:
            return jsonify({"error": "Name, email, and inquiry are required fields."}), 400

        # Save inquiry to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO inquiries (name, email, inquiry) 
        VALUES (?, ?, ?)
        """, (name, email, inquiry))
        conn.commit()
        conn.close()

        return jsonify({"message": "Inquiry submitted successfully."}), 201
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/inquiries', methods=['GET'])
def list_inquiries():
    """
    Endpoint to retrieve all submitted inquiries.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, inquiry, timestamp FROM inquiries")
        inquiries = cursor.fetchall()
        conn.close()

        # Format the results
        inquiry_list = [
            {"id": row[0], "name": row[1], "email": row[2], "inquiry": row[3], "timestamp": row[4]}
            for row in inquiries
        ]

        return jsonify({"inquiries": inquiry_list}), 200
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```
