"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: How can I implement a user feedback system for a course platform that mirrors the experiential learning approach described on Virtual5?
Generated: DETERMINISTIC_5e43179771f51600
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the implementation of a user feedback system for a course platform. The code is written in Python using Flask for the backend:

```python
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database initialization
DATABASE = 'feedback.db'


def init_db():
    """
    Initialize the database and create the feedback table if it doesn't exist.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating >= 1 AND rating <= 5),
            comments TEXT,
            timestamp DATETIME NOT NULL
        )
    """)
    connection.commit()
    connection.close()


# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback.
    Expects JSON payload with course_id, user_id, rating, and optional comments.
    """
    try:
        data = request.json

        # Validate required fields
        if not all(key in data for key in ('course_id', 'user_id', 'rating')):
            return jsonify({'error': 'Missing required fields'}), 400

        course_id = data['course_id']
        user_id = data['user_id']
        rating = data['rating']
        comments = data.get('comments', '')  # Optional field

        # Validate rating is between 1 and 5
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

        # Insert feedback into the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        timestamp = datetime.utcnow()
        cursor.execute("""
            INSERT INTO feedback (course_id, user_id, rating, comments, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (course_id, user_id, rating, comments, timestamp))
        connection.commit()
        connection.close()

        return jsonify({'message': 'Feedback submitted successfully'}), 201

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Route to retrieve feedback for a course
@app.route('/feedback/<course_id>', methods=['GET'])
def get_feedback(course_id):
    """
    Endpoint to retrieve feedback for a specific course.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM feedback WHERE course_id = ?", (course_id,))
        feedback_list = cursor.fetchall()
        connection.close()

        # Transform data into a list of dictionaries
        feedback_data = [
            {
                'id': row[0],
                'course_id': row[1],
                'user_id': row[2],
                'rating': row[3],
                'comments': row[4],
                'timestamp': row[5]
            }
            for row in feedback_list
        ]

        return jsonify(feedback_data), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Route to delete feedback by ID
@app.route('/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Endpoint to delete feedback by ID.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
        connection.commit()
        rows_affected = cursor.rowcount
        connection.close()

        if rows_affected == 0:
            return jsonify({'message': 'Feedback not found'}), 404

        return jsonify({'message': 'Feedback deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()
    app.run(debug=True)
```

### Key Features:
- **Submit Feedback**: `/feedback` (POST) allows users to submit feedback along with ratings and optional comments.
- **Retrieve Feedback**: `/feedback/<course_id>` (GET) retrieves all feedback for a specific course.
- **Delete Feedback**: `/feedback/<feedback_id>` (DELETE) allows admin to delete feedback by ID.
- **Database**: SQLite is used for storing feedback data with proper schema initialization.
- **Error Handling**: Comprehensive error handling for all endpoints.

### Notes:
- Replace `DATABASE = 'feedback.db'` with your preferred database configuration in production.
- Set `debug=False` when deploying in production for security reasons.
