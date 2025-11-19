"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Create an API that facilitates communication between residents and property managers, reflecting the comprehensive services offered by BlocPrest for block administration.
Generated: DETERMINISTIC_162a39c82b0223b5
Batch ID: 20250612_155849
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blocprest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for communication messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat()
        }

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to send a message
@app.route('/api/messages', methods=['POST'])
def send_message():
    data = request.get_json()
    
    # Validate request data
    if not data or 'sender_id' not in data or 'receiver_id' not in data or 'content' not in data:
        raise BadRequest("Missing required fields: sender_id, receiver_id, content.")
    
    # Create and save the message
    new_message = Message(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        content=data['content']
    )
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify(new_message.to_dict()), 201

# API endpoint to retrieve messages for a user
@app.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    messages = Message.query.filter((Message.sender_id == user_id) | (Message.receiver_id == user_id)).all()
    
    if not messages:
        raise NotFound("No messages found for the specified user.")
    
    return jsonify([message.to_dict() for message in messages]), 200

# Error handler for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
