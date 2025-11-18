"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Recommend libraries or APIs for implementing a feature where encrypted notes can be shared via unique links and automatically deleted after being read, as described on privnote.co.
Generated: DETERMINISTIC_c60f13cef76d5b14
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os
from datetime import datetime, timedelta
import threading

app = Flask(__name__)

# In-memory storage for notes and expiration times
notes_storage = {}
notes_expiration = {}

# Generate a new encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a note
def encrypt_note(note, key):
    fernet = Fernet(key)
    encrypted_note = fernet.encrypt(note.encode())
    return encrypted_note

# Decrypt a note
def decrypt_note(encrypted_note, key):
    fernet = Fernet(key)
    decrypted_note = fernet.decrypt(encrypted_note).decode()
    return decrypted_note

# Start a thread to delete a note after a certain period
def schedule_note_deletion(note_id, expiration_time):
    def delete_note():
        # Wait for the expiration time
        threading.Event().wait(expiration_time)
        # Remove note from storage
        if note_id in notes_storage:
            del notes_storage[note_id]
            del notes_expiration[note_id]

    threading.Thread(target=delete_note).start()

@app.route('/create_note', methods=['POST'])
def create_note():
    """
    Endpoint to create an encrypted note.
    Expects JSON with 'note' field.
    Returns a unique link to the encrypted note.
    """
    try:
        data = request.get_json()
        if 'note' not in data:
            return jsonify({'error': 'No note provided'}), 400
        
        note = data['note']
        key = generate_key()
        encrypted_note = encrypt_note(note, key)
        
        # Generate a unique note ID
        note_id = os.urandom(16).hex()
        
        # Store the note and its expiration (set to 10 minutes)
        notes_storage[note_id] = (encrypted_note, key)
        notes_expiration[note_id] = datetime.now() + timedelta(minutes=10)
        
        # Schedule note deletion
        schedule_note_deletion(note_id, 600)  # 600 seconds = 10 minutes

        return jsonify({'link': f'/read_note/{note_id}'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/read_note/<note_id>', methods=['GET'])
def read_note(note_id):
    """
    Endpoint to read an encrypted note.
    Deletes the note after it has been read.
    """
    try:
        if note_id not in notes_storage:
            return jsonify({'error': 'Note not found or has expired'}), 404
        
        encrypted_note, key = notes_storage[note_id]
        # Decrypt and return the note
        decrypted_note = decrypt_note(encrypted_note, key)

        # Delete the note after it has been read
        del notes_storage[note_id]
        del notes_expiration[note_id]

        return jsonify({'note': decrypted_note}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
