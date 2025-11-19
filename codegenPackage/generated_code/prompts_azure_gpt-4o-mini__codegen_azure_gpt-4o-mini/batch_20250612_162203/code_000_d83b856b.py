"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a code snippet for a multipurpose CMS that integrates with a cooperative management system, similar to Nexelit.
Generated: DETERMINISTIC_d83b856b3545ca3f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('contents', lazy=True))

    def __repr__(self):
        return f'<Content {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        raise BadRequest("Missing 'username' or 'email' in request data.")
    
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id}), 201

# Route to create new content
@app.route('/content', methods=['POST'])
def create_content():
    data = request.get_json()
    if not data or 'title' not in data or 'body' not in data or 'user_id' not in data:
        raise BadRequest("Missing 'title', 'body', or 'user_id' in request data.")
    
    new_content = Content(title=data['title'], body=data['body'], user_id=data['user_id'])
    db.session.add(new_content)
    db.session.commit()
    return jsonify({"message": "Content created", "content_id": new_content.id}), 201

# Route to get all content for a user
@app.route('/users/<int:user_id>/content', methods=['GET'])
def get_user_content(user_id):
    user = User.query.get(user_id)
    if not user:
        raise NotFound("User not found.")
    
    contents = Content.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": content.id, "title": content.title, "body": content.body} for content in contents]), 200

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
