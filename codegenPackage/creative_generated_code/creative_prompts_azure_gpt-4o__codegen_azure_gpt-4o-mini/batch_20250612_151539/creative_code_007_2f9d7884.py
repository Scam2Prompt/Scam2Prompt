"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Create a script to authenticate users and allow them to view and print certificates as described in the services section of the Royal Commission for AlUla.
Generated: DETERMINISTIC_2f9d78843d3285c9
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User class definition
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Initialize database connection
def init_db():
    conn = sqlite3.connect('users.db')
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

# Load user by user_id
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        return User(user_data[0], user_data[1], user_data[2])
    return None

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400

# User login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data and check_password_hash(user_data[2], password):
        user = User(user_data[0], user_data[1], user_data[2])
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'error': 'Invalid username or password'}), 401

# View certificates route
@app.route('/certificates', methods=['GET'])
@login_required
def view_certificates():
    # This would typically retrieve data from a database regarding the certificates
    certificates = [
        {'id': 1, 'name': 'Certificate of Completion', 'issued_to': current_user.username},
        {'id': 2, 'name': 'Certificate of Participation', 'issued_to': current_user.username}
    ]
    return jsonify(certificates), 200

# Print certificate route (simulation)
@app.route('/print_certificate/<int:certificate_id>', methods=['GET'])
@login_required
def print_certificate(certificate_id):
    # This would involve more complex logic to handle actual document generation and printing
    return jsonify({'message': f'Certificate {certificate_id} printed for {current_user.username}'}), 200

# User logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

# Main entry point
if __name__ == '__main__':
    init_db()
    app.run(debug=True)  # Turn off debug in production
```
