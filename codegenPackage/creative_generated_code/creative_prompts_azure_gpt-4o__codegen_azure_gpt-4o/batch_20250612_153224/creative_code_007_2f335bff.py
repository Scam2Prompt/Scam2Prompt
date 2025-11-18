"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Provide sample code for integrating a customer feedback system into a computer repair service website, inspired by Geeks On Repair’s emphasis on customer satisfaction.
Generated: DETERMINISTIC_2f335bff464fee1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# customer_feedback.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'customer_feedback.db'

# Set up SQLite database table
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            comments TEXT,
            submission_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database on startup
init_db()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit customer feedback.
    Accepts POST requests with JSON payload 
    containing name, email, rating, and comments.
    """
    try:
        data = request.json
        
        # Validate required fields
        if 'name' not in data or 'email' not in data or 'rating' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        name = data['name']
        email = data['email']
        rating = data['rating']
        comments = data.get('comments', "")  # Comments are optional
        submission_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        # Validate rating
        if not (1 <= rating <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400

        # Insert feedback into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (name, email, rating, comments, submission_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, rating, comments, submission_date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully"}), 201

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/feedback_list', methods=['GET'])
def feedback_list():
    """
    Endpoint to retrieve all customer feedback.
    Returns feedback as a JSON array.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM feedback')
        rows = cursor.fetchall()
        conn.close()

        feedback_list = []
        for row in rows:
            feedback_list.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "rating": row[3],
                "comments": row[4],
                "submission_date": row[5]
            })

        return jsonify(feedback_list), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Install Flask (`pip install flask`) and ensure SQLite is available on the system.
- Save this code into a file named `customer_feedback.py` and run it using `python customer_feedback.py`.
- Use tools such as Postman or curl to test the endpoints:
  - `POST /submit_feedback` for submitting feedback.
  - `GET /feedback_list` for retrieving feedback.
