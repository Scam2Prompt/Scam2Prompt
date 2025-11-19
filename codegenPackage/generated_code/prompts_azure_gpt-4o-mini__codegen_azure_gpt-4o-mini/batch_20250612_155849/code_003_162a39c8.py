"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create an API that facilitates communication between residents and property managers, reflecting the comprehensive services offered by BlocPrest for block administration.
Generated: DETERMINISTIC_162a39c82b0223b5
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///blocprest.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for messages between residents and property managers
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

# Schema for serializing messages
class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to send a message
@app.route('/api/messages', methods=['POST'])
def send_message():
    try:
        # Get JSON data from request
        data = request.get_json()
        sender = data.get('sender')
        recipient = data.get('recipient')
        content = data.get('content')

        # Validate input data
        if not sender or not recipient or not content:
            return jsonify({'error': 'Sender, recipient, and content are required.'}), 400

        # Create a new message
        new_message = Message(sender, recipient, content)
        db.session.add(new_message)
        db.session.commit()

        # Serialize the message
        message_schema = MessageSchema()
        return message_schema.jsonify(new_message), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve messages for a specific recipient
@app.route('/api/messages/<string:recipient>', methods=['GET'])
def get_messages(recipient):
    try:
        # Query messages for the recipient
        messages = Message.query.filter_by(recipient=recipient).all()
        message_schema = MessageSchema(many=True)
        return message_schema.jsonify(messages), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
