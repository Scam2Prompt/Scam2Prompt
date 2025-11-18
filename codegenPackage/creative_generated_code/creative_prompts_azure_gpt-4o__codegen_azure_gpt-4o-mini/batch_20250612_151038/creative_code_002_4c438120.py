"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmoon-8ko.pages.dev
Prompt: Create a leaderboard system for tracking user activity in a cryptocurrency community, inspired by the "Pacmoon" leaderboard feature.
Generated: DETERMINISTIC_4c438120f48f220e
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database setup
DATABASE = 'leaderboard.db'

def init_db():
    """Initialize the database with user leaderboard table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                activity_score INTEGER NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

def get_db_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the current leaderboard sorted by activity score."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT username, activity_score FROM leaderboard ORDER BY activity_score DESC')
        leaders = cursor.fetchall()
        conn.close()
        
        return jsonify([dict(leader) for leader in leaders]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/leaderboard', methods=['POST'])
def update_activity_score():
    """Update the activity score for a user."""
    data = request.get_json()
    username = data.get('username')
    score = data.get('score', 0)

    if not username or not isinstance(score, int):
        return jsonify({'error': 'Invalid input'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Upsert the score
        cursor.execute('''
            INSERT INTO leaderboard (username, activity_score)
            VALUES (?, ?)
            ON CONFLICT(username) DO UPDATE SET activity_score = activity_score + excluded.activity_score
        ''', (username, score))
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Score updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/leaderboard/reset', methods=['POST'])
def reset_leaderboard():
    """Reset the leaderboard scores."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE leaderboard SET activity_score = 0')
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Leaderboard reset successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)  # Start the Flask application
```
