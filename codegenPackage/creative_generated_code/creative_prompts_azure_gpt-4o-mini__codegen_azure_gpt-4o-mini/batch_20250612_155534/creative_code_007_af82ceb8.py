"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-beamtoken.net
Prompt: Recommend a framework for building an interactive quiz based on IKEA icons and collections.
Generated: DETERMINISTIC_af82ceb82c8a4b50
Batch ID: 20250612_155534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# Sample data for IKEA icons and collections
QUIZ_DATA = [
    {"question": "What does this icon represent?", "icon": "icon1.png", "answer": "Assembly Required"},
    {"question": "What does this icon represent?", "icon": "icon2.png", "answer": "Keep Dry"},
    {"question": "What does this icon represent?", "icon": "icon3.png", "answer": "Recyclable"},
    {"question": "What does this icon represent?", "icon": "icon4.png", "answer": "Fragile"},
    {"question": "What does this icon represent?", "icon": "icon5.png", "answer": "Keep Away from Fire"}
]

@app.route('/')
def index():
    """Render the main quiz page."""
    return render_template('index.html', title='IKEA Icon Quiz')

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    """Return a random quiz question."""
    try:
        question_data = random.choice(QUIZ_DATA)
        return jsonify(question_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    """Handle answer submission and return the result."""
    try:
        data = request.json
        user_answer = data.get('answer')
        correct_answer = data.get('correct_answer')

        # Validate the input
        if not user_answer or not correct_answer:
            return jsonify({"error": "Both answer and correct_answer are required."}), 400

        is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
        return jsonify({"is_correct": is_correct}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <script>
        async function fetchQuiz() {
            const response = await fetch('/api/quiz');
            const data = await response.json();
            if (response.ok) {
                document.getElementById('quiz-question').innerText = data.question;
                document.getElementById('quiz-icon').src = data.icon;
                document.getElementById('correct-answer').value = data.answer;
            } else {
                alert(data.error);
            }
        }

        async function submitAnswer() {
            const userAnswer = document.getElementById('user-answer').value;
            const correctAnswer = document.getElementById('correct-answer').value;

            const response = await fetch('/api/submit_answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ answer: userAnswer, correct_answer: correctAnswer })
            });

            const data = await response.json();
            if (response.ok) {
                alert(data.is_correct ? 'Correct!' : 'Wrong answer. Try again!');
            } else {
                alert(data.error);
            }

            // Reset user answer input
            document.getElementById('user-answer').value = '';
            fetchQuiz();
        }

        // Fetch a quiz question on page load
        window.onload = fetchQuiz;
    </script>
</head>
<body>
    <h1>IKEA Icon Quiz</h1>
    <div>
        <img id="quiz-icon" alt="IKEA Icon" />
        <p id="quiz-question"></p>
        <input type="text" id="user-answer" placeholder="Your answer" />
        <input type="hidden" id="correct-answer" />
        <button onclick="submitAnswer()">Submit Answer</button>
    </div>
</body>
</html>
```
