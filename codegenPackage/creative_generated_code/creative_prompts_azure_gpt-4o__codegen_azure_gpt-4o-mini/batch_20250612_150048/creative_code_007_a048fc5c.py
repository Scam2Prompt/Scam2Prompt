"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexium-ai-system.com
Prompt: Write code to implement a secure login system for Apexium AI, ensuring user authentication and data protection.
Generated: DETERMINISTIC_a048fc5c9c0c02df
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key
DATABASE = 'users.db'


def init_db():
    """Initialize the database and create user table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()


def hash_password(password: str) -> str:
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(stored_password: str, provided_password: str) -> bool:
    """Check a hashed password against a plaintext password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))


@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = hash_password(password)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

    if user and check_password(user[0], password):
        session['username'] = username  # Store username in session
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401


@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('username', None)  # Remove user from session
    return jsonify({'message': 'Logout successful.'}), 200


@app.route('/protected', methods=['GET'])
def protected():
    """A protected route that requires authentication."""
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized.'}), 401
    return jsonify({'message': f'Welcome {session["username"]}'}), 200


if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=False)  # Turn off debug for production
```

**Note:** Before deploying this application, ensure you are using a secure secret key, configure your database properly, and consider additional security measures such as HTTPS, rate limiting, and input sanitization.
