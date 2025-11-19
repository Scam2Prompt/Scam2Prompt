"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Generate a code snippet for a social networking app that allows users to create group chats and share inspirational posts, similar to the features on HopefulMe.
Generated: DETERMINISTIC_e090c255d45cb1bb
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hopefulme.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    group_chats = db.relationship('GroupChat', backref='owner', lazy=True)

# Define the GroupChat model
class GroupChat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    messages = db.relationship('Message', backref='group_chat', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    group_chat_id = db.Column(db.Integer, db.ForeignKey('group_chat.id'), nullable=False)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new group chat
@app.route('/group_chat', methods=['POST'])
def create_group_chat():
    data = request.get_json()
    
    # Error handling for missing fields
    if 'title' not in data or 'user_id' not in data:
        abort(400, description="Missing title or user_id")
    
    # Create and save the new group chat
    new_chat = GroupChat(title=data['title'], user_id=data['user_id'])
    db.session.add(new_chat)
    db.session.commit()
    
    return jsonify({"message": "Group chat created", "chat_id": new_chat.id}), 201

# Endpoint to share an inspirational post in a group chat
@app.route('/group_chat/<int:chat_id>/message', methods=['POST'])
def share_inspirational_post(chat_id):
    data = request.get_json()
    
    # Error handling for missing fields
    if 'content' not in data:
        abort(400, description="Missing content")
    
    # Validate group chat existence
    group_chat = GroupChat.query.get(chat_id)
    if not group_chat:
        abort(404, description="Group chat not found")

    # Create and save the new message
    new_message = Message(content=data['content'], group_chat_id=chat_id)
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({"message": "Inspirational post shared", "message_id": new_message.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
