"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappextension.com
Prompt: What API can I use to manage user account statuses, including suspension?
Generated: DETERMINISTIC_f448bbc9c76aa31e
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify, request, abort

# Initialize Flask application
app = Flask(__name__)

# Initialize SQLite database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the users table if it doesn't exist
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('active', 'suspended'))
            )
        ''')
        conn.commit()

# API endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'username' not in data:
        abort(400, description='Invalid input: username is required.')

    username = data['username']

    with get_db_connection() as conn:
        conn.execute('INSERT INTO users (username, status) VALUES (?, ?)', (username, 'active'))
        conn.commit()
    
    return jsonify({'message': 'User created successfully!'}), 201

# API endpoint to update user status
@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def update_user_status(user_id):
    data = request.get_json()
    
    if not data or 'status' not in data or data['status'] not in ['active', 'suspended']:
        abort(400, description='Invalid input: status must be "active" or "suspended".')

    new_status = data['status']

    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        
        if user is None:
            abort(404, description='User not found.')
        
        conn.execute('UPDATE users SET status = ? WHERE id = ?', (new_status, user_id))
        conn.commit()

    return jsonify({'message': 'User status updated successfully!'}), 200

# API endpoint to get user status
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_status(user_id):
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        
        if user is None:
            abort(404, description='User not found.')
        
        return jsonify({
            'id': user['id'],
            'username': user['username'],
            'status': user['status']
        }), 200

# API endpoint to delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        
        if user is None:
            abort(404, description='User not found.')
        
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()

    return jsonify({'message': 'User deleted successfully!'}), 200

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Run the application
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)
```
