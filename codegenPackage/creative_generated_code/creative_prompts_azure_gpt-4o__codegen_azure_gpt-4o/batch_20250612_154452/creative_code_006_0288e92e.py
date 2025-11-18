"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Suggest APIs or libraries for integrating live video classes and interactive quizzes into an online coaching platform inspired by Retina's medical admission preparation programs.
Generated: DETERMINISTIC_0288e92eaaa58395
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and frameworks
from flask import Flask, request, jsonify
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
import sqlite3

# App Initialization
app = Flask(__name__)

# Twilio API Credentials (Replace these with your actual credentials)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_API_KEY = "your_api_key_sid"
TWILIO_API_SECRET = "your_api_key_secret"

# Database Initialization (SQLite for simplicity)
DATABASE = 'quiz.db'

# Function to initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route for generating Twilio access tokens for video
@app.route('/generate-token', methods=['POST'])
def generate_token():
    try:
        # Extract participant data
        data = request.json
        identity = data.get('identity', 'guest')  # Default identity to 'guest'

        # Create Twilio video access token
        token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=identity)
        video_grant = VideoGrant()
        token.add_grant(video_grant)

        # Return the generated token
        return jsonify({'token': token.to_jwt().decode('utf-8')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for adding a quiz question
@app.route('/add-quiz', methods=['POST'])
def add_quiz():
    try:
        # Extract quiz data
        data = request.json
        question = data['question']
        options = data['options']  # List of options
        correct_option = data['correct_option']  # Index of the correct option

        # Validate inputs
        if not question or not options or correct_option is None or not isinstance(options, list):
            return jsonify({'error': 'Invalid input provided'}), 400

        # Save to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO quizzes (question, options, correct_option) VALUES (?, ?, ?)', 
                       (question, str(options), correct_option))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Quiz added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for fetching a quiz question
@app.route('/get-quiz/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    try:
        # Retrieve quiz from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quizzes WHERE id = ?', (quiz_id,))
        quiz = cursor.fetchone()
        conn.close()

        if quiz:
            # Convert options back to a list
            quiz_data = {
                'id': quiz[0],
                'question': quiz[1],
                'options': eval(quiz[2]),
                'correct_option': quiz[3]
            }
            return jsonify(quiz_data)
        else:
            return jsonify({'error': 'Quiz not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. Replace Twilio credentials (`TWILIO_ACCOUNT_SID`, `TWILIO_API_KEY`, `TWILIO_API_SECRET`) with actual values from your Twilio account.
2. Ensure the SQLite database (`quiz.db`) is accessible and writable by the application.
3. Host this Flask application on a production-grade server for deployment.
4. Use HTTPS for secure communication during the integration process.
