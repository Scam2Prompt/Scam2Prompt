"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Create a step-by-step guide for implementing password-protected self-destructing notes in a web application, including encryption and link generation, inspired by privnote.co.
Generated: DETERMINISTIC_cd3c97f550bc34b9
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, send_file
from cryptography.fernet import Fernet
import os
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# Decrypt the message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

# In-memory storage for our notes (for demonstration purposes only)
notes_storage = {}

# Create a note
@app.route('/create_note', methods=['POST'])
def create_note():
    try:
        # Retrieve data from request
        data = request.json
        message = data['message']
        password = data['password']
        duration = data.get('duration', 60)  # Default to 60 seconds

        # Generate a key and encrypt the message
        key = generate_key()
        encrypted_message = encrypt_message(message, key)

        # Store the note with an expiry timestamp
        expiry_time = datetime.now() + timedelta(seconds=duration)
        note_id = len(notes_storage) + 1  # Simple incremental ID
        notes_storage[note_id] = {
            'message': encrypted_message,
            'key': key,
            'expiry_time': expiry_time,
            'password': password
        }

        # Return the note ID for retrieval
        return jsonify({"note_id": note_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Retrieve a note
@app.route('/retrieve_note/<int:note_id>', methods=['POST'])
def retrieve_note(note_id):
    try:
        # Retrieve password from request
        data = request.json
        password = data['password']

        # Check if note exists
        if note_id not in notes_storage:
            return jsonify({"error": "Note not found"}), 404

        note = notes_storage[note_id]

        # Check if note has expired
        if datetime.now() > note['expiry_time']:
            del notes_storage[note_id]  # Remove expired note
            return jsonify({"error": "Note has expired"}), 410

        # Validate password
        if note['password'] != password:
            return jsonify({"error": "Invalid password"}), 403

        # Decrypt the message and return it
        decrypted_message = decrypt_message(note['message'], note['key'])
        return jsonify({"message": decrypted_message}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Main function to run the Flask app
if __name__ == '__main__':
    # Run the app on localhost with debug mode enabled
    app.run(debug=True, port=5000)
```

This code implements a simple web application using Flask, which allows users to create password-protected self-destructing notes. Each note is encrypted and stored in memory, with a specified duration after which it expires. Proper error handling and comments are included to ensure clarity and robustness.
