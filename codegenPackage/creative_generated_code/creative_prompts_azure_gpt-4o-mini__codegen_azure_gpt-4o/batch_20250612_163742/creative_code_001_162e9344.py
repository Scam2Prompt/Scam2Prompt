"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropcoin.lol
Prompt: How can I implement an API that tracks the impact of social media on mental health, referencing the concerns raised on Dropcoin about addiction and societal division?
Generated: DETERMINISTIC_162e93440c83b672
Batch ID: 20250612_163742
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
import logging
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Database file
DATABASE = 'mental_health_impact.db'

# Initialize the SQLite database
def init_db():
    """Initialize the database and create tables if they don't exist."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Create table to store the mental health impact data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS impact_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_feedback TEXT NOT NULL,
                addiction_score INTEGER NOT NULL,
                division_score INTEGER NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

# Initialize the database on application start
init_db()

@app.route('/')
def home():
    """API Home Endpoint."""
    return jsonify({"message": "Welcome to the Social Media Mental Health Impact API"}), 200

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback about mental health impact.
    
    Expected JSON payload:
    {
        "platform": "Twitter",
        "user_feedback": "I feel stressed using this platform.",
        "addiction_score": 8,
        "division_score": 7
    }
    """
    try:
        # Parse the JSON payload
        data = request.json
        platform = data.get('platform')
        user_feedback = data.get('user_feedback')
        addiction_score = data.get('addiction_score')
        division_score = data.get('division_score')

        # Validate inputs
        if not all([platform, user_feedback, addiction_score, division_score]):
            return jsonify({"error": "Missing required fields"}), 400
        if not isinstance(addiction_score, int) or not isinstance(division_score, int):
            return jsonify({"error": "Scores must be integers"}), 400

        # Insert data into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO impact_data (platform, user_feedback, addiction_score, division_score)
            VALUES (?, ?, ?, ?)
        ''', (platform, user_feedback, addiction_score, division_score))
        conn.commit()

        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        logging.error(f"Error submitting feedback: {e}")
        return jsonify({"error": "An error occurred while submitting feedback"}), 500
    finally:
        conn.close()

@app.route('/get-feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    Returns:
        JSON list of feedback data.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Fetch all data from the database
        cursor.execute('SELECT * FROM impact_data')
        rows = cursor.fetchall()
        
        # Format data into a JSON-friendly structure
        feedback_data = [
            {
                "id": row[0],
                "platform": row[1],
                "user_feedback": row[2],
                "addiction_score": row[3],
                "division_score": row[4]
            }
            for row in rows
        ]

        return jsonify(feedback_data), 200
    except Exception as e:
        logging.error(f"Error retrieving feedback: {e}")
        return jsonify({"error": "An error occurred while retrieving feedback"}), 500
    finally:
        conn.close()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to ensure the API is running."""
    return jsonify({"status": "OK"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
