"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonsol.net
Prompt: Construct a web application feature that allows users to submit feedback on Authentic Oil's product ideas, integrating their commitment to customer insights and collaboration.
Generated: DETERMINISTIC_5046d47ffac771c7
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_app.py
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'feedback.db'

def init_db():
    """Initialize the database if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            product_idea TEXT NOT NULL,
            feedback TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()  # Ensure the database is initialized when the app starts

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback.
    Expects JSON payload with 'name', 'email', 'product_idea', and 'feedback'.
    """
    try:
        # Extract data from request
        data = request.get_json()

        # Validate input
        name = data.get('name')
        email = data.get('email')
        product_idea = data.get('product_idea')
        feedback = data.get('feedback')

        if not name or not email or not product_idea or not feedback:
            return jsonify({"error": "All fields are required"}), 400  # Bad request

        # Save feedback to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        timestamp = datetime.utcnow().isoformat()
        cursor.execute("""
            INSERT INTO feedback (name, email, product_idea, feedback, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, product_idea, feedback, timestamp))
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully"}), 201  # Created

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500  # Internal server error

@app.route('/view-feedback', methods=['GET'])
def view_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedback_list = cursor.fetchall()
        conn.close()

        # Format results
        feedback_data = [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "product_idea": row[3],
                "feedback": row[4],
                "timestamp": row[5]
            }
            for row in feedback_list
        ]

        return jsonify({"feedback": feedback_data}), 200  # OK

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500  # Internal server error

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
