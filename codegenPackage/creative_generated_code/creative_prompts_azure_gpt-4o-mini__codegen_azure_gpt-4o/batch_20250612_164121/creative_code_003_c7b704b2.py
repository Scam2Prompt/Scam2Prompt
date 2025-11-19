"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Develop an API endpoint that returns random questions categorized by topics such as weird/funny and personality, similar to the features on dex.chat.
Generated: DETERMINISTIC_c7b704b22efdbfb4
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample question database categorized by topics
QUESTION_DATABASE = {
    "weird/funny": [
        "If animals could talk, which would be the rudest?",
        "What's the strangest thing you've ever eaten?",
        "If you were a chair, who would you want to sit on you?"
    ],
    "personality": [
        "What motivates you the most?",
        "How do you handle failure?",
        "If you could change one thing about yourself, what would it be?"
    ]
}

@app.route('/api/questions', methods=['GET'])
def get_random_question():
    """
    API endpoint to fetch a random question based on the specified topic.

    Query Parameters:
        topic (str): The topic to fetch questions from.
                     Valid topics: "weird/funny", "personality".

    Returns:
        JSON response containing a random question from the specified topic.
        If the topic is invalid or missing, returns an error message.
    """
    try:
        # Get the topic from query parameters
        topic = request.args.get('topic')

        if not topic:
            return jsonify({"error": "Topic parameter is required."}), 400

        if topic not in QUESTION_DATABASE:
            return jsonify({"error": f"Invalid topic. Valid topics are: {', '.join(QUESTION_DATABASE.keys())}"}), 400

        # Fetch a random question from the specified topic
        random_question = random.choice(QUESTION_DATABASE[topic])
        return jsonify({"question": random_question}), 200

    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    # Use debug=True for development purposes. Set to False in production.
    app.run(debug=True)
```
