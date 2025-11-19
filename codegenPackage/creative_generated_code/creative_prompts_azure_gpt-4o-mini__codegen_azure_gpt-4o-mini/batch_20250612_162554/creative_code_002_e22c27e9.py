"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Can you provide a code snippet for integrating a feedback system for UMKM using the guidelines from leprettystellar.com?
Generated: DETERMINISTIC_e22c27e90b35ce2b
Batch ID: 20250612_162554
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

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'feedback.db'

def init_db():
    """Initializes the database and creates the feedback table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Submits feedback from the user."""
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('name', 'email', 'message')):
            return jsonify({'error': 'Invalid input. Name, email, and message are required.'}), 400
        
        # Insert feedback into the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO feedback (name, email, message)
                VALUES (?, ?, ?)
            ''', (data['name'], data['email'], data['message']))
            conn.commit()

        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred: ' + str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Retrieves all feedback entries."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM feedback ORDER BY created_at DESC')
            feedbacks = cursor.fetchall()

        # Format feedback data
        feedback_list = [{'id': fb[0], 'name': fb[1], 'email': fb[2], 'message': fb[3], 'created_at': fb[4]} for fb in feedbacks]

        return jsonify(feedback_list), 200

    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred: ' + str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize database and create table if it doesn't exist
    app.run(debug=True)  # Run the Flask application
```
