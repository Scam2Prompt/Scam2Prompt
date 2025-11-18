"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Write a Python script that uses an API or library to create a self-destructing note similar to the functionality described on privnote.co, including encryption and a custom expiration time.
Generated: DETERMINISTIC_18cba53b44209aa0
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import base64
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a secret key for encryption and decryption
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

# Store notes in memory for simplicity (use a database in production)
notes_store = {}


def encrypt_data(data: str) -> str:
    """
    Encrypts the given string using Fernet encryption.

    :param data: The string to be encrypted.
    :return: Encrypted string in base64 format.
    """
    encrypted_bytes = cipher_suite.encrypt(data.encode())
    return base64.urlsafe_b64encode(encrypted_bytes).decode()


def decrypt_data(data: str) -> str:
    """
    Decrypts the given base64-encoded encrypted string.

    :param data: The base64-encoded encrypted string.
    :return: Decrypted plain text.
    """
    encrypted_bytes = base64.urlsafe_b64decode(data.encode())
    return cipher_suite.decrypt(encrypted_bytes).decode()


@app.route('/create_note', methods=['POST'])
def create_note():
    """
    Endpoint to create a self-destructing note.
    Expects JSON payload with 'content' and 'expiration_time' in seconds.
    """
    try:
        payload = request.json
        note_content = payload.get('content')
        expiration_time = payload.get('expiration_time')

        if not note_content or not expiration_time:
            return jsonify({"error": "Missing 'content' or 'expiration_time'"}), 400

        # Generate a unique ID for the note
        note_id = base64.urlsafe_b64encode(cipher_suite.encrypt(str(time.time()).encode())).decode()

        # Encrypt the content and store the note with expiration metadata
        encrypted_content = encrypt_data(note_content)
        notes_store[note_id] = {
            "content": encrypted_content,
            "expires_at": time.time() + expiration_time
        }

        return jsonify({"note_id": note_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_note/<note_id>', methods=['GET'])
def get_note(note_id):
    """
    Endpoint to retrieve a self-destructing note.
    The note is deleted upon retrieval or if expired.
    """
    try:
        note = notes_store.get(note_id)

        if not note:
            return jsonify({"error": "Note not found or already destroyed"}), 404

        # Check if the note has expired
        if time.time() > note["expires_at"]:
            del notes_store[note_id]
            return jsonify({"error": "Note has expired"}), 410

        # Decrypt the note content, delete the note, and return the content
        decrypted_content = decrypt_data(note["content"])
        del notes_store[note_id]  # Destroy the note
        return jsonify({"content": decrypted_content}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Dependencies:
1. Install Flask for REST API:
   ```bash
   pip install flask
   ```
2. Install cryptography for encryption:
   ```bash
   pip install cryptography
   ```
   
### Notes:
- Use this script in a secure environment; avoid storing keys in plain text in production.
- Replace the in-memory `notes_store` with a proper database for scalability and persistence.
