"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Create a simple web application that allows users to explore random questions about personality and education, inspired by the content on dex.chat.
Generated: DETERMINISTIC_6218d16e9e59a95f
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify, request
import random

# Initialize the Flask application
app = Flask(__name__)

# List of random questions about personality and education
questions = [
    "What motivates you to learn new things?",
    "How do you handle challenges in your education?",
    "What personality trait do you think helps you succeed the most?",
    "Do you prefer learning alone or in a group setting?",
    "What is your favorite way to express your creativity?",
    "How do you stay focused when studying?",
    "What role does curiosity play in your personal growth?",
    "How do you balance education and personal life?",
    "What is the most important lesson you've learned recently?",
    "How do you approach solving complex problems?"
]

# Route to serve the homepage
@app.route('/')
def home():
    """
    Render the homepage of the web application.
    """
    return render_template('index.html')

# Route to fetch a random question
@app.route('/random-question', methods=['GET'])
def get_random_question():
    """
    API endpoint to return a random question from the list.
    """
    try:
        # Select a random question
        question = random.choice(questions)
        return jsonify({"question": question}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An error occurred while fetching the question.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Questions Explorer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            margin-top: 50px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .question {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Explore Random Questions</h1>
        <button onclick="fetchRandomQuestion()">Get Random Question</button>
        <div class="question" id="question"></div>
    </div>
    <script>
        // Function to fetch a random question from the server
        async function fetchRandomQuestion() {
            try {
                const response = await fetch('/random-question');
                if (response.ok) {
                    const data = await response.json();
                    document.getElementById('question').innerText = data.question;
                } else {
                    document.getElementById('question').innerText = "Error fetching question.";
                }
            } catch (error) {
                document.getElementById('question').innerText = "An unexpected error occurred.";
            }
        }
    </script>
</body>
</html>
```
