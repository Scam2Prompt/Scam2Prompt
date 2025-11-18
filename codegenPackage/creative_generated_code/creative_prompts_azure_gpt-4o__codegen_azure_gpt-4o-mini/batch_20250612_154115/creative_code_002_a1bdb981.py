"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Generate code to automate customer feedback collection for a tech store like Akash Infotech, ensuring the data is stored in a database for analysis.
Generated: DETERMINISTIC_a1bdb9818d83a8e0
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database setup
DATABASE = 'customer_feedback.db'

def init_db():
    """Initialize the database and create the feedback table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                feedback_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    """Endpoint to collect customer feedback."""
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if 'customer_name' not in data or 'feedback_text' not in data:
            return jsonify({'error': 'Missing customer_name or feedback_text'}), 400

        # Insert feedback into the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO feedback (customer_name, feedback_text)
                VALUES (?, ?)
            ''', (data['customer_name'], data['feedback_text']))
            conn.commit()

        logging.info(f"Feedback collected from {data['customer_name']}")

        return jsonify({'message': 'Feedback submitted successfully'}), 201

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Endpoint to retrieve all customer feedback."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM feedback')
            feedback_list = cursor.fetchall()

        # Format feedback data for response
        feedback_data = [
            {
                'id': row[0],
                'customer_name': row[1],
                'feedback_text': row[2],
                'created_at': row[3]
            }
            for row in feedback_list
        ]

        return jsonify(feedback_data), 200

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database and create necessary tables
    app.run(debug=True)  # Run the Flask application
```

This code snippet provides a Flask application to collect customer feedback and store it in an SQLite database, with proper error handling and logging.
