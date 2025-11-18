"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasesupport.help
Prompt: Provide code examples for handling security questions and concerns in a cryptocurrency platform, inspired by the Coinbase Support page.
Generated: DETERMINISTIC_31af2b839a3ee945
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Generate a new key for encryption/decryption
def generate_key() -> bytes:
    """Generate a new encryption key."""
    return Fernet.generate_key()

# Encrypt a security question answer
def encrypt_answer(answer: str, key: bytes) -> str:
    """Encrypt the security question answer using a symmetric key."""
    fernet = Fernet(key)
    encrypted_answer = fernet.encrypt(answer.encode())
    return encrypted_answer.decode()

# Decrypt a security question answer
def decrypt_answer(encrypted_answer: str, key: bytes) -> str:
    """Decrypt the security question answer using a symmetric key."""
    try:
        fernet = Fernet(key)
        decrypted_answer = fernet.decrypt(encrypted_answer.encode())
        return decrypted_answer.decode()
    except Exception as e:
        raise ValueError("Invalid encryption key or data.") from e

# Store the user data securely (for demonstration purposes, this uses an in-memory store)
USER_DATA_STORE = {}

# API endpoint to set a security question and answer
@app.route('/set_security_question', methods=['POST'])
def set_security_question():
    """API to set a user's security question and answer."""
    data = request.json
    user_id = data.get('user_id')
    question = data.get('question')
    answer = data.get('answer')

    if not user_id or not question or not answer:
        abort(400, 'Missing user_id, question, or answer.')

    # Generate a key for this user (in practice, this should be securely stored)
    key = generate_key()
    
    # Encrypt the answer
    encrypted_answer = encrypt_answer(answer, key)

    # Store the data (in a production system, use a secure database)
    USER_DATA_STORE[user_id] = {
        'question': question,
        'encrypted_answer': encrypted_answer,
        'key': key.decode()  # Store the key, but it should be managed securely
    }

    return jsonify({'message': 'Security question set successfully.'}), 201

# API endpoint to verify a security question answer
@app.route('/verify_security_answer', methods=['POST'])
def verify_security_answer():
    """API to verify a user's answer to their security question."""
    data = request.json
    user_id = data.get('user_id')
    answer = data.get('answer')

    if not user_id or not answer:
        abort(400, 'Missing user_id or answer.')

    user_data = USER_DATA_STORE.get(user_id)
    if not user_data:
        abort(404, 'User not found.')

    try:
        # Decrypt the stored answer
        key = user_data['key'].encode()
        decrypted_answer = decrypt_answer(user_data['encrypted_answer'], key)

        # Check if the answer matches
        if decrypted_answer == answer:
            return jsonify({'message': 'Verification successful.'}), 200
        else:
            return jsonify({'message': 'Incorrect answer.'}), 403

    except ValueError as e:
        return jsonify({'message': str(e)}), 403

if __name__ == '__main__':
    app.run(debug=True)
```
