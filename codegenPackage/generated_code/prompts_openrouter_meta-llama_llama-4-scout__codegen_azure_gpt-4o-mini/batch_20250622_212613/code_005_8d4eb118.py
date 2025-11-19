"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Design a secure note-sharing system using a programming language of your choice, incorporating features like encryption, password protection, and automated note destruction, similar to Privnote.
Generated: DETERMINISTIC_8d4eb1187b0466e5
Batch ID: 20250622_212613
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
import secrets
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for encryption
def generate_key():
    return base64.urlsafe_b64encode(secrets.token_bytes(32))

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

# Retrieve notes from the JSON file
def retrieve_notes():
    if not os.path.exists('notes.json'):
        return []
    
    with open('notes.json', 'r') as f:
        return json.load(f)

# Delete expired notes
def delete_expired_notes():
    notes = retrieve_notes()
    current_time = datetime.now()
    valid_notes = [note for note in notes if note['expiry'] > current_time]
    
    with open('notes.json', 'w') as f:
        json.dump(valid_notes, f)

@app.route('/create_note', methods=['POST'])
def create_note():
    data = request.json
    note = data.get('note')
    password = data.get('password')
    expiry_minutes = data.get('expiry_minutes', 60)

    if not note or not password:
        return jsonify({'error': 'Note and password are required.'}), 400

    # Generate a key based on the password
    key = hashlib.sha256(password.encode()).digest()
    encrypted_note = encrypt_note(note, key)

    expiry_time = datetime.now() + timedelta(minutes=expiry_minutes)
    note_data = {
        'note': encrypted_note.decode(),
        'expiry': expiry_time
    }

    store_note(note_data)
    return jsonify({'message': 'Note created successfully.', 'expiry': expiry_time.isoformat()}), 201

@app.route('/retrieve_note', methods=['POST'])
def retrieve_note():
    data = request.json
    password = data.get('password')
    note_id = data.get('note_id')

    if not password or not note_id:
        return jsonify({'error': 'Password and note ID are required.'}), 400

    delete_expired_notes()
    notes = retrieve_notes()

    if note_id < 0 or note_id >= len(notes):
        return jsonify({'error': 'Invalid note ID.'}), 404

    note_data = notes[note_id]
    if note_data['expiry'] < datetime.now():
        return jsonify({'error': 'This note has expired.'}), 410

    key = hashlib.sha256(password.encode()).digest()
    try:
        decrypted_note = decrypt_note(note_data['note'].encode(), key)
        return jsonify({'note': decrypted_note}), 200
    except Exception as e:
        return jsonify({'error': 'Invalid password or note could not be decrypted.'}), 403

if __name__ == '__main__':
    app.run(debug=False)
```

### Requirements
- Install Flask and cryptography libraries:
```bash
pip install Flask cryptography
```

### Usage
- Start the server:
```bash
python your_script_name.py
```
- Use a tool like Postman or curl to interact with the API.
