"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write a code snippet for a web application that allows users to take the "Teste do Perfil de Dependência Emocional" and receive personalized feedback.
Generated: DETERMINISTIC_24ffaa343c634ada
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_dependency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing user responses
class UserResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    answers = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<UserResponse {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the questionnaire form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        name = data.get('name')
        answers = data.get('answers')

        if not name or not answers:
            return jsonify({'error': 'Name and answers are required.'}), 400

        # Save user response to the database
        user_response = UserResponse(name=name, answers=answers)
        db.session.add(user_response)
        db.session.commit()

        # Generate personalized feedback
        feedback = generate_feedback(answers)

        return jsonify({'message': 'Response submitted successfully!', 'feedback': feedback}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to generate personalized feedback based on answers
def generate_feedback(answers):
    # Placeholder for feedback logic
    feedback = "Your emotional dependency profile indicates that you may benefit from self-reflection and support."
    return feedback

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotional Dependency Test</title>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    <form id="dependencyForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="answers">Answers (JSON format):</label>
        <textarea id="answers" name="answers" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <div id="feedback"></div>

    <script>
        document.getElementById('dependencyForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const answers = document.getElementById('answers').value;

            fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name, answers: JSON.parse(answers) })
            })
            .then(response => response.json())
            .then(data => {
                if (data.feedback) {
                    document.getElementById('feedback').innerText = data.feedback;
                } else {
                    document.getElementById('feedback').innerText = data.error;
                }
            })
            .catch(error => {
                document.getElementById('feedback').innerText = 'An error occurred: ' + error;
            });
        });
    </script>
</body>
</html>
```
