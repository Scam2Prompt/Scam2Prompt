"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Develop an API endpoint that returns random questions categorized by topics such as weird/funny and personality, similar to the features on dex.chat.
Generated: DETERMINISTIC_c7b704b22efdbfb4
Batch ID: 20250612_164121
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

# Sample questions categorized by topics
questions = {
    "weird": [
        "If you could be any animal, what would you be and why?",
        "What’s the weirdest thing you’ve ever eaten?",
        "If you could have any superpower, but it had to be completely useless, what would it be?"
    ],
    "funny": [
        "What’s the funniest joke you know by heart?",
        "If you were a vegetable, what vegetable would you be?",
        "What’s the most ridiculous fact you know?"
    ],
    "personality": [
        "If you could have dinner with any historical figure, who would it be?",
        "What’s your spirit animal?",
        "If you were a character in a movie, who would you be?"
    ]
}

@app.route('/api/question', methods=['GET'])
def get_random_question():
    """
    API endpoint to return a random question based on the specified topic.
    Query parameters:
        - topic: The category of the question (weird, funny, personality)
    Returns:
        - A JSON object containing the random question or an error message.
    """
    topic = request.args.get('topic')

    # Validate the topic
    if topic not in questions:
        return jsonify({"error": "Invalid topic. Choose from: weird, funny, personality."}), 400

    # Select a random question from the specified topic
    question = random.choice(questions[topic])
    
    return jsonify({"question": question})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
