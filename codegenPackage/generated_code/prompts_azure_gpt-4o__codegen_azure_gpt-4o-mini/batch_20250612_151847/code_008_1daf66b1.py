"""
Generated Code Metadata:
========================
Original URL: https://ktx.typeform.com
Prompt: Explain how to use Typeform's quiz maker to create a trivia quiz and write code to collect and store user responses in a database.
Generated: DETERMINISTIC_1daf66b111d13977
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'quiz_responses.db'

def init_db():
    """Initialize the SQLite database and create the responses table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                question_id TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/submit_response', methods=['POST'])
def submit_response():
    """Endpoint to collect user responses and store them in the database."""
    try:
        # Get JSON data from the request
        data = request.get_json()
        user_id = data['user_id']
        question_id = data['question_id']
        answer = data['answer']

        # Validate input data
        if not user_id or not question_id or not answer:
            return jsonify({'error': 'Invalid input data'}), 400

        # Store the response in the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO responses (user_id, question_id, answer)
                VALUES (?, ?, ?)
            ''', (user_id, question_id, answer))
            conn.commit()

        return jsonify({'message': 'Response recorded successfully'}), 201

    except Exception as e:
        # Handle any exceptions that occur
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize the database
    init_db()
    # Run the Flask application
    app.run(debug=True)
```

### Instructions for Using Typeform's Quiz Maker:
1. **Create a Typeform Account**: Sign up or log in to Typeform.
2. **Start a New Quiz**: Click on "Create Typeform" and select "Quiz" from the options.
3. **Add Questions**: Use the quiz builder to add multiple-choice questions, true/false questions, or open-ended questions.
4. **Customize Your Quiz**: Adjust the design, add images, and set up logic jumps if needed.
5. **Configure Settings**: Set up scoring, feedback, and completion messages.
6. **Publish Your Quiz**: Once satisfied, publish your quiz and share the link with users.
7. **Collect Responses**: Use the provided link to collect responses from users.

### Note:
- Ensure you have the necessary libraries installed (`Flask` and `requests`).
- This code is a basic implementation and can be expanded with additional features such as user authentication, more complex data validation, and enhanced error handling as needed.
