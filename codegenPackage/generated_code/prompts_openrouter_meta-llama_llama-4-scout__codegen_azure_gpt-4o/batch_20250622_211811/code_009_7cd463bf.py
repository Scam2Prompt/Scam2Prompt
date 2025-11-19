"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Create a simple web application that displays a random question on a given topic, such as sports or video games.
Generated: DETERMINISTIC_7cd463bf543ffa67
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import random

# Initialize the Flask application
app = Flask(__name__)

# Sample questions categorized by topics
questions = {
    "sports": [
        "What is the national sport of Japan?",
        "Who won the FIFA World Cup in 2018?",
        "Which sport uses the term 'love' for scoring?",
    ],
    "video_games": [
        "What year was the first Call of Duty game released?",
        "Which video game features the character 'Master Chief'?",
        "What is the best-selling video game of all time?",
    ],
}

@app.route('/random-question', methods=['GET'])
def get_random_question():
    """
    Endpoint to fetch a random question based on the topic provided as a query parameter.
    Example: /random-question?topic=sports
    """
    try:
        # Get the topic from query parameters
        topic = request.args.get('topic', '').lower()

        # Validate the topic
        if topic not in questions:
            return jsonify({"error": "Invalid topic. Available topics are: sports, video_games"}), 400

        # Select a random question from the topic
        question = random.choice(questions[topic])

        # Return the question as a JSON response
        return jsonify({"topic": topic, "question": question}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/')
def home():
    """
    Home endpoint to provide basic information about the API.
    """
    return jsonify({
        "message": "Welcome to the Random Question API!",
        "endpoints": {
            "/random-question": "GET a random question by providing a topic as a query parameter (e.g., ?topic=sports)"
        },
        "available_topics": list(questions.keys())
    }), 200

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable it in production
    app.run(debug=True)
```
