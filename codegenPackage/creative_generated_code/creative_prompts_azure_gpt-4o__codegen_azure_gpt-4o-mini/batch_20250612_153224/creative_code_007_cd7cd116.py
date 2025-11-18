"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erpify.co
Prompt: Generate code to facilitate communication between ERP freelancers and employers using live chat functionality, as described on ERPIFY.
Generated: DETERMINISTIC_cd7cd116209b6137
Batch ID: 20250612_153224
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
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'username': self.username,
            'message': self.message,
            'timestamp': self.timestamp.isoformat()
        }

# Route to get chat history
@app.route('/messages', methods=['GET'])
def get_messages():
    """Fetches all messages from the database."""
    try:
        messages = Message.query.all()
        return jsonify([msg.to_dict() for msg in messages]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Handle new message events
@socketio.on('new_message')
def handle_new_message(data):
    """Handles incoming messages and saves them to the database."""
    username = data.get('username')
    message = data.get('message')

    if not username or not message:
        emit('error', {'error': 'Invalid message data'}, broadcast=False)
        return

    try:
        # Create and save new message
        new_message = Message(username=username, message=message)
        db.session.add(new_message)
        db.session.commit()

        # Emit the new message to all clients
        emit('message', new_message.to_dict(), broadcast=True)
    except Exception as e:
        emit('error', {'error': str(e)}, broadcast=False)

# Main entry point to run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the Flask-SocketIO server
    socketio.run(app, host='0.0.0.0', port=os.environ.get('PORT', 5000))
```

### Requirements
- Flask
- Flask-SocketIO
- Flask-SQLAlchemy

### Installation
To run this code, ensure you have the necessary libraries installed:
```bash
pip install Flask Flask-SocketIO Flask-SQLAlchemy
```
### Note
Ensure to handle database migrations and production configurations as needed when deploying this application.
