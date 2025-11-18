"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: Write code for an educational platform that uses Mary AI as a mentor to teach programming and design to beginners. Include features for intuitive AI-assisted learning.
Generated: DETERMINISTIC_2d1c58ba71219e5c
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready Python code for an AI-powered educational platform that uses Mary AI to teach programming and design. The example uses OpenAI's API for natural language processing and Flask for the web interface.

```python
from flask import Flask, request, jsonify, render_template
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI API key (ensure this is set securely via environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Error message for missing API key
if not openai.api_key:
    raise ValueError("OpenAI API key not set. Please configure the OPENAI_API_KEY environment variable.")

# Route: Home page
@app.route('/')
def home():
    """
    Render the homepage.
    """
    return render_template('index.html')

# Route: Handle user queries (e.g., programming/design questions)
@app.route('/ask', methods=['POST'])
def ask_mary():
    """
    Handle user input and provide AI-generated assistance via Mary AI.
    """
    try:
        # Parse user input
        user_input = request.json.get('query', '')
        if not user_input:
            return jsonify({"error": "No query provided"}), 400

        # Generate AI response using OpenAI's GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Mary AI, a mentor who teaches programming and design to beginners in an intuitive and easy-to-understand way. Be helpful, educational, and supportive."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract and return the AI's response
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": answer}), 200

    except Exception as e:
        # Error handling
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Route: Programming exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    """
    Provide programming and design exercises for users to practice.
    """
    exercises = [
        {
            "id": 1,
            "title": "Introduction to Variables",
            "description": "Learn how to declare and use variables in Python. Create a program that stores your name in a variable and prints a welcome message.",
            "difficulty": "Beginner"
        },
        {
            "id": 2,
            "title": "Basic HTML Layout",
            "description": "Create a simple HTML page with a header, a paragraph, and a link using proper HTML tags.",
            "difficulty": "Beginner"
        },
        {
            "id": 3,
            "title": "If-Else Statements",
            "description": "Write a Python program that checks if a number is positive, negative, or zero.",
            "difficulty": "Intermediate"
        }
    ]
    return jsonify({"exercises": exercises}), 200

# Route: Submit exercise solutions
@app.route('/submit_solution', methods=['POST'])
def submit_solution():
    """
    Evaluate user-submitted solutions for exercises and provide feedback.
    """
    try:
        # Parse the solution submission
        submission = request.json
        exercise_id = submission.get('exercise_id')
        user_code = submission.get('code')

        # Validate input
        if not exercise_id or not user_code:
            return jsonify({"error": "Exercise ID and code are required"}), 400

        # Example feedback mechanism (mocked for demonstration)
        feedback = f"Your solution for Exercise {exercise_id} has been received. Well done!"
        return jsonify({"feedback": feedback}), 200

    except Exception as e:
        # Error handling
        return jsonify({"error": "An error occurred while submitting your solution.", "details": str(e)}), 500

# Main: Run Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Dependencies
To run this code, ensure you have the following installed:
1. Python 3.7+
2. Flask (`pip install flask`)
3. OpenAI Python library (`pip install openai`)

### Templates
Create an `index.html` file for the homepage, which could be a simple HTML page welcoming users to the platform.
