"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Write Python code to integrate a membership management system for organizations like the Idaho Association of Commerce & Industry, including features for member login and event registration.
Generated: DETERMINISTIC_449ef7135ba70ddd
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Database setup
def init_db():
    with sqlite3.connect('membership.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY,
                member_id INTEGER,
                event_id INTEGER,
                FOREIGN KEY(member_id) REFERENCES members(id),
                FOREIGN KEY(event_id) REFERENCES events(id)
            )
        ''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register_member():
    """Register a new member."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)
    try:
        with sqlite3.connect('membership.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO members (username, password) VALUES (?, ?)', 
                           (username, hashed_password))
            conn.commit()
        return jsonify({'message': 'Member registered successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 409

@app.route('/login', methods=['POST'])
def login_member():
    """Log in an existing member."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    with sqlite3.connect('membership.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM members WHERE username = ?', (username,))
        member = cursor.fetchone()

    if member and check_password_hash(member[1], password):
        session['member_id'] = member[0]
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new event."""
    if 'member_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403

    name = request.json.get('name')
    date = request.json.get('date')
    description = request.json.get('description')

    if not name or not date:
        return jsonify({'error': 'Event name and date are required.'}), 400

    with sqlite3.connect('membership.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO events (name, date, description) VALUES (?, ?, ?)',
                       (name, date, description))
        conn.commit()
    return jsonify({'message': 'Event created successfully.'}), 201

@app.route('/register_event', methods=['POST'])
def register_event():
    """Register a member for an event."""
    if 'member_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403

    event_id = request.json.get('event_id')
    
    with sqlite3.connect('membership.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM events WHERE id = ?', (event_id,))
        event = cursor.fetchone()

    if not event:
        return jsonify({'error': 'Event not found.'}), 404

    member_id = session['member_id']
    try:
        with sqlite3.connect('membership.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO registrations (member_id, event_id) VALUES (?, ?)', 
                           (member_id, event_id))
            conn.commit()
        return jsonify({'message': 'Registered for event successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Already registered for this event.'}), 409

@app.route('/logout', methods=['POST'])
def logout_member():
    """Log out the current member."""
    session.pop('member_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

if __name__ == '__main__':
    init_db()  # Initialize the database at startup
    app.run(debug=True)  # Set debug to False in production
```

Make sure to change `your_secret_key` to a strong random key in production and set `debug` to `False` before deploying the application.
