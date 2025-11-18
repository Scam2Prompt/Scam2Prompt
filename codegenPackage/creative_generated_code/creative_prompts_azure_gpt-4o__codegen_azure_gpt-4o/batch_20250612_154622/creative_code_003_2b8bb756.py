"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Create a secure web application for managing investment portfolios based on Tradetoearnoption's investment plans, incorporating AES encryption for transactions.
Generated: DETERMINISTIC_2b8bb75695136fdf
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, secure, production-ready implementation for the requested web application using Python and Flask. For AES encryption, the `cryptography` library is used. The application assumes a basic REST API structure.

```python
from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os
import base64

app = Flask(__name__)

# AES encryption setup
SECRET_KEY = b'your_very_secure_key'  # Replace with your own secure key
SALT = os.urandom(16)  # Random salt for key derivation

def generate_aes_key(secret_key, salt):
    """Generates AES key using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(secret_key)

def encrypt(data, key):
    """Encrypts the data using AES."""
    iv = os.urandom(16)  # Random initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data).decode('utf-8')  # Combine IV and encrypted data

def decrypt(encrypted_data, key):
    """Decrypts the data using AES."""
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    cipher_text = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = PKCS7(128).unpadder()
    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()
    return unpadder.update(decrypted_data) + unpadder.finalize()

# In-memory database (for demonstration purposes)
investment_portfolios = {}

@app.route('/api/portfolio', methods=['POST'])
def create_portfolio():
    """
    Endpoint to create a new investment portfolio.
    Payload format:
    {
        "name": "Portfolio Name",
        "amount": 1000
    }
    """
    try:
        data = request.json
        if not data or 'name' not in data or 'amount' not in data:
            return jsonify({"error": "Invalid input"}), 400

        portfolio_name = data['name']
        amount = data['amount']

        # Encrypt transaction details
        key = generate_aes_key(SECRET_KEY, SALT)
        encrypted_amount = encrypt(str(amount), key)

        # Save encrypted data
        investment_portfolios[portfolio_name] = encrypted_amount
        return jsonify({"message": "Portfolio created successfully", "portfolio": portfolio_name}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/portfolio/<name>', methods=['GET'])
def get_portfolio(name):
    """
    Endpoint to retrieve an investment portfolio by name.
    Decrypted data is returned to the client.
    """
    try:
        if name not in investment_portfolios:
            return jsonify({"error": "Portfolio not found"}), 404

        # Decrypt transaction details
        key = generate_aes_key(SECRET_KEY, SALT)
        encrypted_amount = investment_portfolios[name]
        decrypted_amount = decrypt(encrypted_amount, key)

        return jsonify({"portfolio": name, "amount": int(decrypted_amount.decode())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/portfolio/<name>', methods=['DELETE'])
def delete_portfolio(name):
    """
    Endpoint to delete an investment portfolio by name.
    """
    try:
        if name not in investment_portfolios:
            return jsonify({"error": "Portfolio not found"}), 404

        del investment_portfolios[name]
        return jsonify({"message": "Portfolio deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Install dependencies:
Ensure you have Python installed, then install Flask and cryptography:
```bash
pip install flask cryptography
```

### Notes:
1. Replace `SECRET_KEY` with a secure key, and manage the salt securely (avoid hardcoding it in production).
2. This implementation uses an in-memory database for demonstration. Replace it with a persistent database (e.g., PostgreSQL, MongoDB) for production use.
3. Disable `debug=True` in production to avoid exposing sensitive information. Use a proper deployment server like Gunicorn or uWSGI.
