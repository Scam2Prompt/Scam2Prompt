"""
Generated Code Metadata:
========================
Original URL: https://privnote.icu
Prompt: Write a Python script to create a self-destructing note service with encryption, allowing users to set an expiration date for the note.
Generated: DETERMINISTIC_31671a16dfab7492
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the note using the provided key
def encrypt_note(note, key):
    fernet = Fernet(key)
    encrypted_note = fernet.encrypt(note.encode())
    return encrypted_note

# Decrypt the note using the provided key
def decrypt_note(encrypted_note, key):
    fernet = Fernet(key)
    decrypted_note = fernet.decrypt(encrypted_note).decode()
    return decrypted_note

# Store notes in a JSON file
def store_note(note_data):
    if not os.path.exists('notes.json'):
        with open('notes.json', 'w') as f:
            json.dump([], f)

    with open('notes.json', 'r+') as f:
        notes = json.load(f)
        notes.append(note_data)
        f.seek(0)
        json.dump(notes, f)

# Load notes from the JSON file
def load_notes():
    if not os.path.exists('notes.json'):
        return []
    with open('notes.json', 'r') as f:
        return json.load(f)

# API endpoint to create a self-destructing note
@app.route('/create_note', methods=['POST'])
def create_note():
    try:
        data = request.json
        note = data.get('note')
        expiration_minutes = data.get('expiration_minutes', 10)

        if not note or expiration_minutes <= 0:
            return jsonify({'error': 'Invalid note or expiration time'}), 400

        key = generate_key()
        encrypted_note = encrypt_note(note, key)
        expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)

        note_data = {
            'encrypted_note': base64.urlsafe_b64encode(encrypted_note).decode(),
            'key': base64.urlsafe_b64encode(key).decode(),
            'expiration_time': expiration_time.isoformat()
        }

        store_note(note_data)

        return jsonify({'message': 'Note created successfully', 'expiration_time': expiration_time.isoformat()}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve a note
@app.route('/get_note', methods=['GET'])
def get_note():
    try:
        current_time = datetime.now()
        notes = load_notes()
        note_id = request.args.get('id')

        if note_id is None or not note_id.isdigit() or int(note_id) >= len(notes):
            return jsonify({'error': 'Invalid note ID'}), 400

        note_data = notes[int(note_id)]
        expiration_time = datetime.fromisoformat(note_data['expiration_time'])

        if current_time > expiration_time:
            return jsonify({'error': 'This note has expired'}), 410

        key = base64.urlsafe_b64decode(note_data['key'])
        encrypted_note = base64.urlsafe_b64decode(note_data['encrypted_note'])
        decrypted_note = decrypt_note(encrypted_note, key)

        return jsonify({'note': decrypted_note}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, you need to install Flask and cryptography. You can do this using pip:

```bash
pip install Flask cryptography
```

### Usage
1. Start the Flask server by running the script.
2. Use a tool like Postman or curl to send POST requests to `/create_note` with a JSON body containing the note and expiration time.
3. Retrieve the note using a GET request to `/get_note` with the note ID as a query parameter.
