"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Provide an example of how to integrate customer satisfaction tracking in a web application, drawing on the principles highlighted by EnergiaKert's commitment to quality and service.
Generated: DETERMINISTIC_51092f6e1f3e5920
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Flask application to track customer satisfaction ratings and feedback.
# This script demonstrates how to implement a customer satisfaction tracking feature in a web app.

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'customer_feedback.db'

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            satisfaction_rating INTEGER NOT NULL CHECK(satisfaction_rating BETWEEN 1 AND 5),
            comments TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def health_check():
    """Health check endpoint to verify the service is running."""
    return "Customer Satisfaction Tracking API is running!", 200

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit customer feedback.
    Expects JSON payload with keys: customer_name, satisfaction_rating, and comments.
    """
    try:
        data = request.get_json()

        # Validate input
        customer_name = data.get('customer_name')
        satisfaction_rating = data.get('satisfaction_rating')
        comments = data.get('comments')

        if not customer_name or not satisfaction_rating:
            return jsonify({'error': 'customer_name and satisfaction_rating are required'}), 400

        if not isinstance(satisfaction_rating, int) or satisfaction_rating < 1 or satisfaction_rating > 5:
            return jsonify({'error': 'satisfaction_rating must be an integer between 1 and 5'}), 400

        # Save feedback to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (customer_name, satisfaction_rating, comments)
            VALUES (?, ?, ?)
        ''', (customer_name, satisfaction_rating, comments))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Feedback submitted successfully'}), 201
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An error occurred while processing your feedback', 'details': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to fetch all customer feedback.
    Returns a JSON array of all feedback entries.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, customer_name, satisfaction_rating, comments FROM feedback')
        feedback = cursor.fetchall()
        conn.close()

        # Convert feedback data to JSON format
        feedback_list = [
            {
                'id': row[0],
                'customer_name': row[1],
                'satisfaction_rating': row[2],
                'comments': row[3]
            } for row in feedback
        ]

        return jsonify(feedback_list), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An error occurred while fetching feedback', 'details': str(e)}), 500

if __name__ == '__main__':
    # Ensure the database is initialized before starting the server
    init_db()
    app.run(debug=True)
```

### Notes:
1. Install dependencies:
   ```
   pip install flask
   ```

2. Run the script:
   ```
   python app.py
   ```

3. Use tools like Postman or curl to test the `/feedback` endpoints for submitting (`POST`) and retrieving (`GET`) feedback.
