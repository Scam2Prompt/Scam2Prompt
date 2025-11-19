"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Create a simple web application that allows users to explore random questions about personality and education, inspired by the content on dex.chat.
Generated: DETERMINISTIC_6218d16e9e59a95f
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to display random questions about personality and education

from flask import Flask, render_template, jsonify
import random

# Initialize the Flask app
app = Flask(__name__)

# Define the questions dataset
questions = {
    "personality": [
        "What are your biggest strengths?",
        "How do you usually deal with stress?",
        "What motivates you in life?",
        "How do you handle feedback?",
        "What is your favorite hobby and why?"
    ],
    "education": [
        "What subjects do you enjoy studying?",
        "What learning methods work best for you?",
        "How do you approach solving difficult problems?",
        "Do you prefer group projects or individual assignments?",
        "What skills do you think are most important to learn today?"
    ]
}

@app.route('/')
def home():
    """
    This route serves the homepage with basic instructions.
    """
    return render_template('index.html')

@app.route('/question/<category>', methods=['GET'])
def get_random_question(category):
    """
    This route serves a random question based on the specified category.
    :param category: The category of questions (e.g., 'personality' or 'education').
    :return: JSON response with a random question.
    """
    try:
        if category not in questions:
            # Return error if category is not valid
            return jsonify({"error": "Invalid category. Choose 'personality' or 'education'."}), 400

        # Select a random question from the category
        question = random.choice(questions[category])
        return jsonify({"category": category, "question": question})

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (`templates/index.html`):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Questions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2rem;
            text-align: center;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
        #question {
            margin-top: 2rem;
            font-size: 1.5rem;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Explore Random Questions</h1>
    <p>Click a button below to get a random question about personality or education.</p>
    <button onclick="fetchQuestion('personality')">Personality</button>
    <button onclick="fetchQuestion('education')">Education</button>
    <p id="question"></p>

    <script>
        async function fetchQuestion(category) {
            try {
                // Make a GET request to the Flask API
                const response = await fetch(`/question/${category}`);
                const data = await response.json();

                // Handle errors from the API
                if (response.status !== 200) {
                    document.getElementById('question').innerText = data.error || "An error occurred.";
                    return;
                }

                // Display the random question
                document.getElementById('question').innerText = data.question;
            } catch (error) {
                // Handle unexpected errors
                document.getElementById('question').innerText = "Failed to fetch question. Please try again.";
            }
        }
    </script>
</body>
</html>
```
