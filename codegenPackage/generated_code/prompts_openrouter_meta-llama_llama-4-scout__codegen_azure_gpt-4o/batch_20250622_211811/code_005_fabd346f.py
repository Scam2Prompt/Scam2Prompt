"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Develop a simple API that returns a random question on a given topic, such as education or fashion.
Generated: DETERMINISTIC_fabd346fbe178cf8
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Predefined questions categorized by topics
questions = {
    "education": [
        "What is the importance of education in modern society?",
        "How can technology improve education?",
        "What are the challenges faced by educators today?",
        "What is the role of parents in a child's education?"
    ],
    "fashion": [
        "What are the latest trends in fashion?",
        "How does culture influence fashion?",
        "What is sustainable fashion and why is it important?",
        "Who are some iconic figures in the fashion industry?"
    ]
}

@app.route('/random-question', methods=['GET'])
def get_random_question():
    """
    Endpoint to fetch a random question based on the provided topic.
    Query Parameter:
        topic (str): The topic for which a random question is requested.
    Returns:
        JSON response containing a random question or an error message.
    """
    try:
        # Get the topic from query parameters
        topic = request.args.get('topic', '').lower()

        # Validate the topic
        if not topic:
            return jsonify({"error": "Topic parameter is required."}), 400
        if topic not in questions:
            return jsonify({"error": f"Topic '{topic}' not found. Available topics: {', '.join(questions.keys())}"}), 404

        # Select a random question from the topic
        random_question = random.choice(questions[topic])
        return jsonify({"topic": topic, "question": random_question}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
