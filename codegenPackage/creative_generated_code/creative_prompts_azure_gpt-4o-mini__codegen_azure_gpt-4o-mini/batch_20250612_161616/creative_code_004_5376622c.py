"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3-ai.web.app
Prompt: Suggest a library for implementing a voting system similar to the one used in QnA3, focusing on crypto questions and rewards distribution.
Generated: DETERMINISTIC_5376622c6b227d88
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Initialize Flask app and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the Questions
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Question {self.title}>'

# Define a model for the Votes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    voter_address = db.Column(db.String(100), nullable=False, unique=True)  # Assuming unique wallets

    def __repr__(self):
        return f'<Vote {self.id} for Question {self.question_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new question
@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = Question(title=data['title'])
    db.session.add(new_question)
    try:
        db.session.commit()
        return jsonify({'message': 'Question created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Error creating question!'}), 400

# Route to vote for a question
@app.route('/vote/<int:question_id>', methods=['POST'])
def vote(question_id):
    data = request.get_json()
    voter_address = data['voter_address']
    
    # Check if the voter has already voted
    existing_vote = Vote.query.filter_by(voter_address=voter_address).first()
    if existing_vote:
        return jsonify({'message': 'You have already voted!'}), 403

    # Record the vote
    new_vote = Vote(question_id=question_id, voter_address=voter_address)
    db.session.add(new_vote)
    question = Question.query.get_or_404(question_id)
    question.votes += 1

    try:
        db.session.commit()
        return jsonify({'message': 'Vote recorded successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Error saving vote!'}), 400

# Route to get all questions along with their votes
@app.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([
        {'id': q.id, 'title': q.title, 'votes': q.votes, 'created_at': q.created_at}
        for q in questions
    ]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
