"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvestbank.finance.blog
Prompt: Implement a feature in a web app that tracks customer satisfaction ratings for an organic vegetable delivery service, using a database to store feedback.
Generated: DETERMINISTIC_c4deee4a015f77f7
Batch ID: 20250612_140120
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
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database file path
DATABASE = 'feedback.db'

# Function to initialize the database
def init_db():
    """
    Initialize the database if it doesn't exist.
    Creates a table named 'feedback' with columns for id, customer name, rating, and comments.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            comments TEXT
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route to submit feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit customer feedback.
    Expects JSON data with 'customer_name', 'rating', and optional 'comments'.
    """
    try:
        # Parse incoming JSON data
        data = request.json
        customer_name = data.get('customer_name')
        rating = data.get('rating')
        comments = data.get('comments', '')

        # Validate input
        if not customer_name or not rating:
            return jsonify({'error': 'Customer name and rating are required.'}), 400
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({'error': 'Rating must be an integer between 1 and 5.'}), 400

        # Insert feedback into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO feedback (customer_name, rating, comments)
            VALUES (?, ?, ?)
        """, (customer_name, rating, comments))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Feedback submitted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to retrieve feedback
@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all customer feedback.
    Returns a JSON array of feedback records.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, customer_name, rating, comments FROM feedback")
        feedback_data = cursor.fetchall()
        conn.close()

        # Convert feedback data to a list of dictionaries
        feedback_list = [
            {'id': row[0], 'customer_name': row[1], 'rating': row[2], 'comments': row[3]}
            for row in feedback_data
        ]

        return jsonify({'feedback': feedback_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
