"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Create a governance mechanism for the Base Mafia platform that incorporates community feedback and voting to optimize platform functionality.
Generated: DETERMINISTIC_1b76fa3f9fd0ab0d
Batch ID: 20250612_145924
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
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for the application

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///governance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for community feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    votes = db.relationship('Vote', backref='feedback', lazy=True)

# Database model for voting
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'), nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    vote_type = db.Column(db.Boolean, nullable=False)  # True for upvote, False for downvote

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.get_json()
        new_feedback = Feedback(user_id=data['user_id'], content=data['content'])
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to vote on feedback
@app.route('/vote', methods=['POST'])
def vote_feedback():
    try:
        data = request.get_json()
        existing_vote = Vote.query.filter_by(feedback_id=data['feedback_id'], user_id=data['user_id']).first()

        if existing_vote:
            # Update vote if it already exists
            existing_vote.vote_type = data['vote_type']
        else:
            # Create a new vote
            new_vote = Vote(feedback_id=data['feedback_id'], user_id=data['user_id'], vote_type=data['vote_type'])
            db.session.add(new_vote)

        db.session.commit()
        return jsonify({"message": "Vote recorded successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to fetch feedback and votes
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedback_list = Feedback.query.all()
        results = []
        for feedback in feedback_list:
            votes_count = len(feedback.votes)
            upvotes = sum(1 for vote in feedback.votes if vote.vote_type)
            downvotes = votes_count - upvotes
            results.append({
                "id": feedback.id,
                "user_id": feedback.user_id,
                "content": feedback.content,
                "upvotes": upvotes,
                "downvotes": downvotes
            })
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
