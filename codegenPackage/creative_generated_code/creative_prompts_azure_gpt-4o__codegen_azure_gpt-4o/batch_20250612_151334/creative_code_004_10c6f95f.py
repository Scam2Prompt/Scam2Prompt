"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtclaim.com
Prompt: Provide a solution for securely managing user accounts on a cryptocurrency faucet platform, ensuring compliance with rules against multiple accounts, proxy usage, and public computer access as outlined by USDT Claim.
Generated: DETERMINISTIC_10c6f95fe7e31830
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import re
import uuid
import sqlite3
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Database initialization
DATABASE = 'user_accounts.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            user_agent TEXT NOT NULL,
            registration_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper functions
def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Validate email format."""
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

def detect_proxy(ip_address):
    """Detect proxy usage based on IP address."""
    # Placeholder for actual proxy detection logic
    # In production, integrate a proper proxy detection service/API
    return ip_address.startswith('192.') or ip_address.startswith('10.')

def detect_public_computer(user_agent):
    """Detect public computer usage based on User-Agent."""
    # Example heuristic: User-Agent indicates kiosks or public browsers
    return 'kiosk' in user_agent.lower() or 'public' in user_agent.lower()

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user account.

    Expected JSON format:
    {
        "email": "user@example.com",
        "password": "securepassword"
    }
    """
    data = request.json

    if not data or 'email' not in data or 'password' not in data:
        return make_response(jsonify({"error": "Invalid request format"}), 400)

    email = data['email']
    password = data['password']
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent', '')

    if not is_valid_email(email):
        return make_response(jsonify({"error": "Invalid email format"}), 400)

    if detect_proxy(ip_address):
        return make_response(jsonify({"error": "Proxy usage detected. Registration denied"}), 403)

    if detect_public_computer(user_agent):
        return make_response(jsonify({"error": "Public computer usage detected. Registration denied"}), 403)

    hashed_password = hash_password(password)

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        user_id = str(uuid.uuid4())
        cursor.execute('''
            INSERT INTO users (id, email, password_hash, ip_address, user_agent)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, email, hashed_password, ip_address, user_agent))
        conn.commit()
        return jsonify({"message": "User registered successfully", "user_id": user_id})
    except sqlite3.IntegrityError:
        return make_response(jsonify({"error": "Email is already registered"}), 409)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), 500)
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    """
    Log in a user account.

    Expected JSON format:
    {
        "email": "user@example.com",
        "password": "securepassword"
    }
    """
    data = request.json

    if not data or 'email' not in data or 'password' not in data:
        return make_response(jsonify({"error": "Invalid request format"}), 400)

    email = data['email']
    password = data['password']
    hashed_password = hash_password(password)

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, email FROM users WHERE email = ? AND password_hash = ?', (email, hashed_password))
        user = cursor.fetchone()

        if user is None:
            return make_response(jsonify({"error": "Invalid email or password"}), 401)

        return jsonify({"message": "Login successful", "user_id": user[0]})
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), 500)
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
```
