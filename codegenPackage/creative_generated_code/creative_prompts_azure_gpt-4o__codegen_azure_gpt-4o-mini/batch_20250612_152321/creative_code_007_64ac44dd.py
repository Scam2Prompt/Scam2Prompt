"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Write code to implement a secure registration system for a platform like Claim-Bits, ensuring stability and user data protection.
Generated: DETERMINISTIC_64ac44dd7b735a2d
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize Flask app, Bcrypt for password hashing, and JWT for authentication
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_here')  # Change this in production
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Connect to SQLite database (or create it if it doesn't exist)
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate request data
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"msg": "Missing required fields"}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the username or email exists
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
    if cursor.fetchone():
        return jsonify({"msg": "Username or email already exists"}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Insert new user into the database
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                   (username, email, hashed_password))
    conn.commit()
    conn.close()

    return jsonify({"msg": "User registered successfully"}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate request data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    # Fetch the user from the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    # Check if user exists and password is correct
    if user and bcrypt.check_password_hash(user[3], password):  # user[3] is the hashed password
        access_token = create_access_token(identity=user[0])  # user[0] is the user_id
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Initialize database on startup
@app.before_first_request
def create_db():
    init_db()

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

### Notes:
- This code utilizes Flask for the web framework, SQLite for the database, Bcrypt for password hashing, and JWT for user authentication.
- Ensure to set the `JWT_SECRET_KEY` in a secure manner in the production environment.
- Modify database handling to use a more robust database like PostgreSQL or MySQL for production purposes.
- Always sanitize inputs and consider additional security measures based on your specific use case.
