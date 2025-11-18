"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Suggest an API for handling secure communication between lawyers and clients in a family law firm, emphasizing confidentiality and client support, as highlighted by Majeli Avocat.
Generated: DETERMINISTIC_acde3065a27db281
Batch ID: 20250612_151912
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
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging
from cryptography.fernet import Fernet

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_communications.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Model for storing messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(50), nullable=False)
    recipient = db.Column(db.String(50), nullable=False)
    content = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f"<Message {self.id} from {self.sender} to {self.recipient}>"

# User authentication data (in production, use another storage like OAuth2)
users = {
    "client": generate_password_hash("client_password"),
    "lawyer": generate_password_hash("lawyer_password")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None

@app.route('/send_message', methods=['POST'])
@auth.login_required
def send_message():
    """Endpoint to send an encrypted message."""
    data = request.get_json()
    if not data or 'recipient' not in data or 'content' not in data:
        logging.error("Invalid data received for sending message.")
        return jsonify({'error': 'Please provide recipient and content.'}), 400

    try:
        # Encrypt the message content
        encrypted_content = cipher.encrypt(data['content'].encode())

        # Save the message to the database
        new_message = Message(sender=auth.current_user(), recipient=data['recipient'], content=encrypted_content)
        db.session.add(new_message)
        db.session.commit()
        logging.info(f"Message sent from {new_message.sender} to {new_message.recipient}.")
        
        return jsonify({'message': 'Message sent successfully!'}), 201
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")
        return jsonify({'error': 'Failed to send message.'}), 500

@app.route('/receive_messages', methods=['GET'])
@auth.login_required
def receive_messages():
    """Endpoint to retrieve messages for the authenticated user."""
    try:
        received_messages = Message.query.filter_by(recipient=auth.current_user()).all()
        messages = []

        for message in received_messages:
            # Decrypt the message content
            decrypted_content = cipher.decrypt(message.content).decode()
            messages.append({
                'sender': message.sender,
                'content': decrypted_content
            })

        return jsonify({'messages': messages}), 200
    except Exception as e:
        logging.error(f"Error retrieving messages: {str(e)}")
        return jsonify({'error': 'Failed to retrieve messages.'}), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

Make sure to install the necessary libraries using:
```bash
pip install Flask Flask-SQLAlchemy Flask-HTTPAuth cryptography
```
