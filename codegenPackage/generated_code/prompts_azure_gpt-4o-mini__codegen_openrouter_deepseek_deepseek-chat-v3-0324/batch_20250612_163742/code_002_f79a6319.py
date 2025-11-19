"""
Generated Code Metadata:
========================
Original URL: https://dropcoin.lol
Prompt: Generate a code snippet for a web application that helps users reclaim their time from social media, inspired by the solutions proposed on Dropcoin.
Generated: DETERMINISTIC_f79a63199480280f
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import sqlite3
import json
from typing import Dict, List, Optional

app = Flask(__name__)

# Database setup
DATABASE = 'time_reclaimer.db'

def get_db():
    """Get a connection to the SQLite database."""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """Initialize the database with required tables."""
    with get_db() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        db.execute("""
        CREATE TABLE IF NOT EXISTS social_media_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            platform TEXT NOT NULL,
            duration_minutes INTEGER NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)
        
        db.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            target_minutes INTEGER NOT NULL,
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Username and email are required'}), 400
    
    try:
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (?, ?)",
                (data['username'], data['email'])
            )
            db.commit()
            return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/log-usage', methods=['POST'])
def log_usage():
    """Log social media usage for a user."""
    data = request.get_json()
    required_fields = ['user_id', 'platform', 'duration_minutes']
    if not data or any(field not in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        with get_db() as db:
            db.execute(
                "INSERT INTO social_media_usage (user_id, platform, duration_minutes) VALUES (?, ?, ?)",
                (data['user_id'], data['platform'], data['duration_minutes'])
            )
            db.commit()
            return jsonify({'message': 'Usage logged successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/set-goal', methods=['POST'])
def set_goal():
    """Set a time reduction goal for a user."""
    data = request.get_json()
    required_fields = ['user_id', 'target_minutes', 'start_date', 'end_date']
    if not data or any(field not in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        with get_db() as db:
            db.execute(
                """INSERT INTO goals (user_id, target_minutes, start_date, end_date)
                VALUES (?, ?, ?, ?)""",
                (data['user_id'], data['target_minutes'], data['start_date'], data['end_date'])
            )
            db.commit()
            return jsonify({'message': 'Goal set successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/usage-stats/<int:user_id>')
def get_usage_stats(user_id: int):
    """Get usage statistics for a user."""
    try:
        with get_db() as db:
            # Get total usage
            total_usage = db.execute(
                "SELECT SUM(duration_minutes) as total FROM social_media_usage WHERE user_id = ?",
                (user_id,)
            ).fetchone()['total'] or 0
            
            # Get usage by platform
            by_platform = db.execute(
                "SELECT platform, SUM(duration_minutes) as total FROM social_media_usage WHERE user_id = ? GROUP BY platform",
                (user_id,)
            ).fetchall()
            
            # Get current goal if exists
            current_goal = db.execute(
                "SELECT * FROM goals WHERE user_id = ? AND end_date > datetime('now') ORDER BY end_date DESC LIMIT 1",
                (user_id,)
            ).fetchone()
            
            return jsonify({
                'total_usage_minutes': total_usage,
                'by_platform': [dict(row) for row in by_platform],
                'current_goal': dict(current_goal) if current_goal else None
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
