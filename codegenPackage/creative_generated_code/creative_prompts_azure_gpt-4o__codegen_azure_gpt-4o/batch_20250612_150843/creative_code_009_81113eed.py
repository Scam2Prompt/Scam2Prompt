"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.org
Prompt: Write code to create a financial literacy quiz that users can take after registering with LucraBot GPT, with questions tailored to topics like savings, investments, and market trends.
Generated: DETERMINISTIC_81113eed07331e3e
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

# Flask app for web-based financial literacy quiz
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for registered users
users_db = {}

# Financial literacy questions pool
questions_pool = [
    {
        "question": "What is the recommended percentage of income to save for emergencies?",
        "options": ["5%", "20%", "50%", "10%"],
        "answer": "20%"
    },
    {
        "question": "Which of the following is a low-risk investment option?",
        "options": ["Stocks", "Government Bonds", "Cryptocurrency", "Real Estate"],
        "answer": "Government Bonds"
    },
    {
        "question": "What does diversification in investments mean?",
        "options": [
            "Investing in one asset type",
            "Spreading investments across multiple asset types",
            "Avoiding risky investments entirely",
            "Selling assets frequently"
        ],
        "answer": "Spreading investments across multiple asset types"
    },
    {
        "question": "What is a bull market?",
        "options": [
            "A market in decline",
            "A market experiencing strong growth",
            "A market with high inflation",
            "A market controlled by central banks"
        ],
        "answer": "A market experiencing strong growth"
    },
    {
        "question": "What is the primary purpose of a retirement fund?",
        "options": [
            "To invest in high-risk assets",
            "To provide financial security after retirement",
            "To save for short-term goals",
            "To avoid paying taxes"
        ],
        "answer": "To provide financial security after retirement"
    }
]

# Error response utility
def error_response(message):
    return jsonify({"error": message}), 400


@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a user for LucraBot GPT.
    Expects JSON input with 'username' and 'email'.
    """
    data = request.json

    # Basic input validation
    if 'username' not in data or 'email' not in data:
        return error_response("Missing 'username' or 'email' in request.")

    username = data['username']
    email = data['email']

    # Check if the user already exists
    if username in users_db:
        return error_response(f"User '{username}' is already registered.")

    # Store user in the database
    users_db[username] = {"email": email, "quiz_attempts": []}
    return jsonify({"message": f"User '{username}' registered successfully."})


@app.route('/quiz', methods=['GET'])
def take_quiz():
    """
    Endpoint to take the financial literacy quiz.
    Expects 'username' as a query parameter.
    Returns a random set of 3 questions for the quiz.
    """
    username = request.args.get('username')

    if not username:
        return error_response("Missing 'username' query parameter.")

    if username not in users_db:
        return error_response(f"User '{username}' not found. Please register first.")

    # Select a random subset of questions (3 questions)
    selected_questions = random.sample(questions_pool, 3)

    # Save the selected questions for the user's session
    users_db[username]["quiz_attempts"].append({
        "questions": selected_questions,
        "score": None
    })

    return jsonify({"quiz": selected_questions})


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """
    Endpoint to submit answers for the quiz.
    Expects JSON input with 'username' and 'answers'.
    Calculates score and stores it in the user's session.
    """
    data = request.json

    # Basic input validation
    if 'username' not in data or 'answers' not in data:
        return error_response("Missing 'username' or 'answers' in request.")

    username = data['username']
    answers = data['answers']

    if username not in users_db or not users_db[username]["quiz_attempts"]:
        return error_response("No active quiz found for the user. Please start a quiz first.")

    # Get the most recent quiz attempt
    quiz_attempt = users_db[username]["quiz_attempts"][-1]
    questions = quiz_attempt["questions"]

    # Calculate score
    score = 0
    for i, question in enumerate(questions):
        if i < len(answers) and answers[i].strip().lower() == question["answer"].strip().lower():
            score += 1

    # Save score
    quiz_attempt["score"] = score

    return jsonify({"message": f"Quiz submitted successfully. Your score: {score}/3"})


if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True)
```
