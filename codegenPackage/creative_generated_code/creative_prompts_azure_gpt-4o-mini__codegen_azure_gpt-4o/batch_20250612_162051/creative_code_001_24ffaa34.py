"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Write a code snippet for a web application that allows users to take the "Teste do Perfil de Dependência Emocional" and receive personalized feedback.
Generated: DETERMINISTIC_24ffaa343c634ada
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Question and possible answers for the quiz
quiz_questions = [
    {"question": "Do you find yourself constantly seeking approval from others?", "answers": ["Yes", "No"]},
    {"question": "Do you feel anxious or insecure when you're alone?", "answers": ["Yes", "No"]},
    {"question": "Do you prioritize others' happiness over your own?", "answers": ["Yes", "No"]},
    {"question": "Do you often fear abandonment or rejection?", "answers": ["Yes", "No"]},
    {"question": "Do you struggle to set boundaries with others?", "answers": ["Yes", "No"]},
]

# Home route to display the quiz
@app.route('/')
def home():
    return render_template('quiz.html', questions=quiz_questions)

# Process user responses and provide feedback
@app.route('/submit', methods=['POST'])
def submit_quiz():
    try:
        # Extracting user responses from the request form
        user_responses = request.form.to_dict()

        # Calculate emotional dependency score (basic example: count "Yes" responses)
        score = sum(1 for key, answer in user_responses.items() if answer.lower() == "yes")

        # Generate personalized feedback based on score
        feedback = ""
        if score <= 2:
            feedback = "You seem to have a healthy level of independence and emotional balance."
        elif score <= 4:
            feedback = "You may have some tendencies towards emotional dependency. Consider reflecting on your relationships and boundaries."
        else:
            feedback = "You might be experiencing significant emotional dependency. It could be helpful to explore this further with a professional."

        # Respond with feedback as JSON
        return jsonify({"score": score, "feedback": feedback})

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your quiz responses."}), 500


# Main entry point to run the app
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Notes for setup:
1. Ensure you have Flask installed (`pip install flask`).
2. Create a `templates` folder in the project directory.
3. Add a `quiz.html` file under `templates` with the HTML form to display the quiz and collect user responses.
Example HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form action="/submit" method="POST">
        {% for question in questions %}
        <div>
            <p>{{ question['question'] }}</p>
            {% for answer in question['answers'] %}
            <label>
                <input type="radio" name="{{ loop.index }}" value="{{ answer }}" required> {{ answer }}
            </label>
            {% endfor %}
        </div>
        {% endfor %}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
