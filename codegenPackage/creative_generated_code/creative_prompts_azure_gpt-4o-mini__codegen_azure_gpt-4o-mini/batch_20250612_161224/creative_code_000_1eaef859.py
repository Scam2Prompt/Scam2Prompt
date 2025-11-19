"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: How can I implement a voting system for questions similar to the QnA3 platform's airdrop campaign in a crypto application?
Generated: DETERMINISTIC_1eaef8590411540d
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Questions
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0)

# Schema for validating input data
class QuestionSchema(Schema):
    content = fields.Str(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new question
@app.route('/questions', methods=['POST'])
def create_question():
    data = request.json
    schema = QuestionSchema()

    # Validate input data
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create and save the new question
    new_question = Question(content=validated_data['content'])
    db.session.add(new_question)
    db.session.commit()
    
    return jsonify({"id": new_question.id, "content": new_question.content, "votes": new_question.votes}), 201

# Route to vote for a question
@app.route('/questions/<int:question_id>/vote', methods=['POST'])
def vote_question(question_id):
    # Retrieve the question by ID
    question = Question.query.get(question_id)
    
    # Check if the question exists
    if not question:
        return jsonify({"error": "Question not found"}), 404

    # Increment the vote count
    question.votes += 1
    db.session.commit()
    
    return jsonify({"id": question.id, "votes": question.votes}), 200

# Route to retrieve all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    # Prepare the response data
    questions_data = [{"id": q.id, "content": q.content, "votes": q.votes} for q in questions]
    
    return jsonify(questions_data), 200

# Error handling for unexpected situations
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
