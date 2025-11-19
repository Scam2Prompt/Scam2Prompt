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

Here is an implementation of a voting system for questions in a crypto application written in Python using Flask and SQLAlchemy:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)  # Question content
    votes = db.Column(db.Integer, nullable=False, default=0)  # Vote count

# Initialize database
with app.app_context():
    db.create_all()

# Error handling middleware
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Endpoint to create a new question
@app.route('/questions', methods=['POST'])
def create_question():
    try:
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({"error": "Invalid request. 'content' is required."}), 400
        
        question = Question(content=data['content'])
        db.session.add(question)
        db.session.commit()
        
        return jsonify({"message": "Question created successfully", "question": {"id": question.id, "content": question.content, "votes": question.votes}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to upvote a question
@app.route('/questions/<int:question_id>/vote', methods=['POST'])
def vote_question(question_id):
    try:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        
        question.votes += 1
        db.session.commit()
        
        return jsonify({"message": "Question voted successfully", "question": {"id": question.id, "content": question.content, "votes": question.votes}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all questions
@app.route('/questions', methods=['GET'])
def list_questions():
    try:
        questions = Question.query.all()
        question_list = [{"id": q.id, "content": q.content, "votes": q.votes} for q in questions]
        
        return jsonify({"questions": question_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get details of a specific question
@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    try:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        
        return jsonify({"question": {"id": question.id, "content": question.content, "votes": question.votes}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
