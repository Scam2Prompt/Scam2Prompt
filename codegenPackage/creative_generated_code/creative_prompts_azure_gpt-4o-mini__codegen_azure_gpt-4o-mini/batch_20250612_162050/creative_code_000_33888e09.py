"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: How can I implement a text-based counselling service similar to the one offered at Text Counselling Online, focusing on user preferences for written communication?
Generated: DETERMINISTIC_33888e098fee5b52
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counseling_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.Column(db.JSON, nullable=True)  # Store user preferences as JSON

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user for the counseling service."""
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400

    new_user = User(name=data['name'], email=data['email'], preferences=data.get('preferences'))
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already registered"}), 400

@app.route('/send_message', methods=['POST'])
def send_message():
    """Send a message from a registered user."""
    data = request.get_json()

    if not data or 'user_id' not in data or 'content' not in data:
        return jsonify({"error": "User ID and message content are required"}), 400

    new_message = Message(user_id=data['user_id'], content=data['content'])
    
    try:
        db.session.add(new_message)
        db.session.commit()
        return jsonify({"message": "Message sent successfully", "message_id": new_message.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/get_messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    """Fetch all messages for a specific user."""
    messages = Message.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": msg.id, "content": msg.content, "timestamp": msg.timestamp} for msg in messages]), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
