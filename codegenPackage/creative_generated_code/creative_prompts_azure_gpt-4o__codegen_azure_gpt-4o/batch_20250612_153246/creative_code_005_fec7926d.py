"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praiasdeminas.eng.br
Prompt: Write code to develop a customer feedback system that collects reviews about pool construction and renovation services, similar to the testimonials on the Praias de Minas website.
Generated: DETERMINISTIC_fec7926d87b0e238
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DB_NAME = "feedback.db"

# Database setup function
def init_db():
    """
    Initialize the SQLite database with the required table.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            comments TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

# Initialize the database
init_db()

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to handle customer feedback submission.
    Expects JSON input with 'name', 'email', 'rating', and 'comments'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        rating = data.get('rating')
        comments = data.get('comments')

        # Validate input
        if not name or not email or not rating:
            return jsonify({'error': 'Missing required fields: name, email, or rating'}), 400
        if not (1 <= int(rating) <= 5):
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400

        # Save feedback to database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO feedback (name, email, rating, comments)
            VALUES (?, ?, ?, ?)
        """, (name, email, rating, comments))
        connection.commit()
        connection.close()

        # Return success response
        return jsonify({'message': 'Feedback submitted successfully'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/get-feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all customer feedback.
    Returns a list of feedback entries in JSON format.
    """
    try:
        # Fetch all feedback from the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email, rating, comments, timestamp FROM feedback ORDER BY timestamp DESC")
        feedback_list = cursor.fetchall()
        connection.close()

        # Format feedback as a list of dictionaries
        formatted_feedback = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'rating': row[3],
                'comments': row[4],
                'timestamp': row[5]
            }
            for row in feedback_list
        ]

        # Return feedback data as JSON
        return jsonify({'feedback': formatted_feedback}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    """
    Simple home endpoint.
    """
    return jsonify({'message': 'Welcome to the Customer Feedback System!'}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
