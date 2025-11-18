"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimunstake-prosper.pages.dev
Prompt: Develop a tool to enable token holders to vote and contribute ideas on the Prosper platform, integrating community-driven features into the code.
Generated: DETERMINISTIC_757727d3f5250ca1
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prosper.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model to represent a token holder
class TokenHolder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.Column(db.Integer, default=0)
    votes = db.relationship('Vote', backref='holder', lazy=True)

# Model to represent a voting idea
class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    votes = db.relationship('Vote', backref='idea', lazy=True)

# Model to represent a vote
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holder_id = db.Column(db.Integer, db.ForeignKey('token_holder.id'), nullable=False)
    idea_id = db.Column(db.Integer, db.ForeignKey('idea.id'), nullable=False)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to register a new token holder
@app.route('/api/token-holders', methods=['POST'])
def register_token_holder():
    data = request.json
    if not data or 'username' not in data:
        abort(400, 'Username is required')
    
    new_holder = TokenHolder(username=data['username'])
    db.session.add(new_holder)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Username already exists')

    return jsonify({'id': new_holder.id, 'username': new_holder.username}), 201

# Route to create a new idea
@app.route('/api/ideas', methods=['POST'])
def create_idea():
    data = request.json
    if not data or 'title' not in data or 'description' not in data:
        abort(400, 'Title and description are required')
    
    new_idea = Idea(title=data['title'], description=data['description'])
    db.session.add(new_idea)
    db.session.commit()

    return jsonify({'id': new_idea.id, 'title': new_idea.title}), 201

# Route to vote on an idea
@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.json
    if not data or 'holder_id' not in data or 'idea_id' not in data:
        abort(400, 'Holder ID and Idea ID are required')
    
    vote_record = Vote(holder_id=data['holder_id'], idea_id=data['idea_id'])
    db.session.add(vote_record)
    db.session.commit()

    return jsonify({'message': 'Vote recorded successfully'}), 201

# Route to get all ideas
@app.route('/api/ideas', methods=['GET'])
def get_ideas():
    ideas = Idea.query.all()
    return jsonify([{'id': idea.id, 'title': idea.title, 'description': idea.description} for idea in ideas]), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
