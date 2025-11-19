"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://let-talks.live
Prompt: Provide an example of a RESTful API endpoint for managing chat messages in a live chat system like let-talks.live.
Generated: DETERMINISTIC_236e8c6c8a32d0f3
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for chat messages
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)

# Schema for input validation
class ChatMessageSchema(Schema):
    username = fields.Str(required=True)
    message = fields.Str(required=True)

message_schema = ChatMessageSchema()
messages_schema = ChatMessageSchema(many=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/messages', methods=['POST'])
def create_message():
    """
    Create a new chat message.
    Expects a JSON body with 'username' and 'message'.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = message_schema.load(data)
        
        # Create a new chat message object
        new_message = ChatMessage(**validated_data)
        db.session.add(new_message)
        db.session.commit()
        
        return jsonify(message_schema.dump(new_message)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """
    Retrieve all chat messages.
    Returns a list of messages in JSON format.
    """
    try:
        messages = ChatMessage.query.all()
        return jsonify(messages_schema.dump(messages)), 200
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    """
    Delete a chat message by ID.
    """
    try:
        message = ChatMessage.query.get(message_id)
        if message is None:
            abort(404, description="Message not found")
        
        db.session.delete(message)
        db.session.commit()
        return jsonify({"message": "Message deleted"}), 204
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
```
