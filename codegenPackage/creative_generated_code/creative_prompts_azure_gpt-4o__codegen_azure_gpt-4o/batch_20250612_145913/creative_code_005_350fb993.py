"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx40.com
Prompt: Suggest a library or tool to securely handle user authentication and account creation for an online gambling platform like TANTE4D.
Generated: DETERMINISTIC_350fb99350f3b852
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is production-ready Python code using the `Flask` web framework and the `Flask-JWT-Extended` library for secure user authentication and account creation:

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Configure the secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your-secure-secret-key'  # Replace with a strong secret key
jwt = JWTManager(app)

# SQLite database file
DATABASE = 'users.db'


# Function to initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Save the user to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while registering the user'}), 500


# Route to authenticate a user and generate a JWT token
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Fetch user from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            # Create a JWT token for the user
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': 'An error occurred while logging in'}), 500


# Protected route (example of JWT usage)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Retrieve the username of the currently logged-in user
    current_user = get_jwt_identity()
    return jsonify({'message': f'Welcome, {current_user}! This is a protected route.'}), 200


# Main entry point
if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Replace `'your-secure-secret-key'` with a strong, random secret key for production use.
2. Always use HTTPS in production to secure communication.
3. Consider more advanced security measures, such as rate limiting and monitoring for brute-force attempts.
4. This code uses SQLite for simplicity, but in production, use a more robust database system like PostgreSQL or MySQL.
