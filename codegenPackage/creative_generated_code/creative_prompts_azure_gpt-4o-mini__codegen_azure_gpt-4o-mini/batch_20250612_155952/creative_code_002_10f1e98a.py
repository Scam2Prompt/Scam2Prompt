"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liquideth-gift.org
Prompt: Can you provide a code example for integrating a voting feature similar to the one used in "오늘의유머" for user-generated content?
Generated: DETERMINISTIC_10f1e98ae69a38d5
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing user-generated content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0)

# Model for storing user votes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)  # Unique user identifier

    # Relationship to link to content
    content = db.relationship('Content', backref=db.backref('votes', lazy=True))

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/content', methods=['POST'])
def create_content():
    """Endpoint to create new user-generated content."""
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, description="Bad Request: Title is required.")
    
    new_content = Content(title=data['title'])
    db.session.add(new_content)
    db.session.commit()
    return jsonify({"id": new_content.id, "title": new_content.title, "votes": new_content.votes}), 201

@app.route('/vote/<int:content_id>', methods=['POST'])
def vote(content_id):
    """Endpoint to vote on user-generated content."""
    user_id = request.json.get('user_id')
    if not user_id:
        abort(400, description="Bad Request: User ID is required.")
    
    # Check if content exists
    content = Content.query.get(content_id)
    if content is None:
        abort(404, description="Not Found: Content does not exist.")
    
    # Check if user has already voted
    existing_vote = Vote.query.filter_by(content_id=content_id, user_id=user_id).first()
    if existing_vote:
        abort(409, description="Conflict: User has already voted on this content.")
    
    # Record the vote
    new_vote = Vote(content_id=content_id, user_id=user_id)
    db.session.add(new_vote)
    content.votes += 1  # Increment vote count
    db.session.commit()
    
    return jsonify({"message": "Vote recorded.", "total_votes": content.votes}), 200

@app.route('/content/<int:content_id>', methods=['GET'])
def get_content(content_id):
    """Endpoint to retrieve content and its vote count."""
    content = Content.query.get(content_id)
    if content is None:
        abort(404, description="Not Found: Content does not exist.")
    
    return jsonify({"id": content.id, "title": content.title, "votes": content.votes}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** This code is a simple implementation of a voting feature and should be tested and refined according to your specific requirements, including security considerations such as user authentication and validation.
