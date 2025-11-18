"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Write code to create a collaborative pool maintenance logging system similar to the features described on Pooltyme, including user invitations and shared log history.
Generated: DETERMINISTIC_95d3c69ed2dfebea
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for a collaborative pool maintenance logging system using Flask and SQLite:

```python
from flask import Flask, request, jsonify, g
import sqlite3
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE = 'pool_maintenance.db'


def get_db():
    """Connect to the database."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection when the app context is torn down."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    """Initialize the database schema."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pool_users (
                pool_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(pool_id) REFERENCES pools(id),
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pool_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY(pool_id) REFERENCES pools(id),
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        db.commit()


@app.route('/create_user', methods=['POST'])
def create_user():
    """Endpoint to create a new user."""
    try:
        email = request.json.get('email')
        if not email:
            return jsonify({'error': 'Email is required'}), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (email) VALUES (?)', (email,))
        db.commit()
        return jsonify({'message': 'User created successfully'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/create_pool', methods=['POST'])
def create_pool():
    """Endpoint to create a new pool."""
    try:
        name = request.json.get('name')
        if not name:
            return jsonify({'error': 'Pool name is required'}), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO pools (name) VALUES (?)', (name,))
        db.commit()
        return jsonify({'message': 'Pool created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/invite_user', methods=['POST'])
def invite_user():
    """Endpoint to invite a user to a pool."""
    try:
        pool_id = request.json.get('pool_id')
        user_id = request.json.get('user_id')
        if not pool_id or not user_id:
            return jsonify({'error': 'Pool ID and User ID are required'}), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO pool_users (pool_id, user_id) VALUES (?, ?)', (pool_id, user_id))
        db.commit()
        return jsonify({'message': 'User invited to pool successfully'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'User is already in the pool'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add_log', methods=['POST'])
def add_log():
    """Endpoint to add a maintenance log to a pool."""
    try:
        pool_id = request.json.get('pool_id')
        user_id = request.json.get('user_id')
        description = request.json.get('description')
        if not pool_id or not user_id or not description:
            return jsonify({'error': 'Pool ID, User ID, and Description are required'}), 400

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO logs (pool_id, user_id, date, description) VALUES (?, ?, ?, ?)',
                       (pool_id, user_id, date, description))
        db.commit()
        return jsonify({'message': 'Log added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/view_logs/<int:pool_id>', methods=['GET'])
def view_logs(pool_id):
    """Endpoint to view all logs for a specific pool."""
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            SELECT logs.id, logs.date, logs.description, users.email
            FROM logs
            JOIN users ON logs.user_id = users.id
            WHERE logs.pool_id = ?
            ORDER BY logs.date DESC
        ''', (pool_id,))
        logs = cursor.fetchall()
        return jsonify({
            'logs': [{'id': log[0], 'date': log[1], 'description': log[2], 'user': log[3]} for log in logs]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def home():
    """Simple home endpoint to confirm the API is running."""
    return jsonify({'message': 'Welcome to the Pool Maintenance Logging System API'})


if __name__ == '__main__':
    init_db()  # Initialize database schema on startup
    app.run(debug=True)
```
