"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beyond-blitz.pages.dev
Prompt: Write a code snippet to implement a feature that allows users to engage and share content to earn $BEYOND tokens.
Generated: DETERMINISTIC_bd097983596a3e08
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beyond_tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Content {self.content}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to engage with content
@app.route('/engage', methods=['POST'])
def engage_content():
    """
    Engage with content and reward user with $BEYOND tokens.

    Expected JSON payload:
    {
        "username": "user1",
        "content_id": 1
    }
    """
    data = request.json
    username = data.get('username')
    content_id = data.get('content_id')

    # Check if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check if content exists
    content = Content.query.get(content_id)
    if not content:
        return jsonify({'error': 'Content not found'}), 404

    # Reward user with tokens
    user.tokens += 10  # Rewarding 10 tokens for engaging
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to award tokens'}), 500

    return jsonify({'message': 'Engagement successful', 'tokens': user.tokens}), 200

# Route to create a user
@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Create a new user.

    Expected JSON payload:
    {
        "username": "new_user"
    }
    """
    data = request.json
    username = data.get('username')

    new_user = User(username=username)
    db.session.add(new_user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

    return jsonify({'message': 'User created', 'username': new_user.username}), 201

# Route to create content
@app.route('/create_content', methods=['POST'])
def create_content():
    """
    Create new content linked to a user.

    Expected JSON payload:
    {
        "username": "user1",
        "content": "This is some interesting content."
    }
    """
    data = request.json
    username = data.get('username')
    content_text = data.get('content')

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    new_content = Content(user_id=user.id, content=content_text)
    db.session.add(new_content)
    
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create content'}), 500

    return jsonify({'message': 'Content created', 'content_id': new_content.id}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
