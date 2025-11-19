"""
Generated Code Metadata:
========================
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Implement a Learn-to-Earn platform using the 99Bitcoins token, integrating interactive learning modules, quizzes, and tutorials for users.
Generated: DETERMINISTIC_f1b4a7d000d56afe
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learn_to_earn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    earned_tokens = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Module model
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Module {self.title}>'

# Define the Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(255), nullable=False)

    module = db.relationship('Module', backref=db.backref('quizzes', lazy=True))

    def __repr__(self):
        return f'<Quiz {self.question}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e)), e.code

# Route to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id}), 201

# Route to get user information
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"username": user.username, "earned_tokens": user.earned_tokens})

# Route to create a new learning module
@app.route('/api/modules', methods=['POST'])
def create_module():
    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    new_module = Module(title=title, content=content)
    db.session.add(new_module)
    db.session.commit()
    return jsonify({"message": "Module created", "module_id": new_module.id}), 201

# Route to create a quiz for a module
@app.route('/api/quizzes', methods=['POST'])
def create_quiz():
    data = request.json
    module_id = data.get('module_id')
    question = data.get('question')
    correct_answer = data.get('correct_answer')

    if not module_id or not question or not correct_answer:
        return jsonify({"error": "Module ID, question, and correct answer are required"}), 400

    new_quiz = Quiz(module_id=module_id, question=question, correct_answer=correct_answer)
    db.session.add(new_quiz)
    db.session.commit()
    return jsonify({"message": "Quiz created", "quiz_id": new_quiz.id}), 201

# Route to take a quiz and earn tokens
@app.route('/api/quizzes/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    data = request.json
    user_id = data.get('user_id')
    answer = data.get('answer')

    quiz = Quiz.query.get(quiz_id)
    user = User.query.get(user_id)

    if not quiz or not user:
        return jsonify({"error": "Quiz or User not found"}), 404

    if answer == quiz.correct_answer:
        user.earned_tokens += 1  # Increment tokens for correct answer
        db.session.commit()
        return jsonify({"message": "Correct answer! Tokens earned.", "earned_tokens": user.earned_tokens}), 200
    else:
        return jsonify({"message": "Incorrect answer."}), 200

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```
