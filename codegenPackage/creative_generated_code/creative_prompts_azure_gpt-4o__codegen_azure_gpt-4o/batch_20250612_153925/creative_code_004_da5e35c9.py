"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Write code to display a dynamic leaderboard for a cryptocurrency rewards campaign, showing users with the highest points earned, as referenced in AVAAI Hunt.
Generated: DETERMINISTIC_da5e35c9ed2ecdd5
Batch ID: 20250612_153925
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

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'leaderboard.db'

def init_db():
    """Initialize the database and create leaderboard table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            points INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to fetch leaderboard data
def get_leaderboard(limit=10):
    """
    Fetch top users sorted by points in descending order.
    :param limit: Maximum number of users to display (default: 10).
    :return: List of leaderboard entries.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, points
        FROM leaderboard
        ORDER BY points DESC
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{'username': row[0], 'points': row[1]} for row in rows]

# Route to view leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    """
    API endpoint to fetch the leaderboard.
    :return: JSON response with top users.
    """
    try:
        limit = int(request.args.get('limit', 10))  # Default to top 10 if no limit is provided
        leaderboard_data = get_leaderboard(limit)
        return jsonify({'status': 'success', 'data': leaderboard_data}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Route to update user points
@app.route('/update_points', methods=['POST'])
def update_points():
    """
    API endpoint to update a user's points.
    :return: JSON response indicating success or failure.
    """
    try:
        data = request.json
        username = data.get('username')
        points = data.get('points')

        # Validate input data
        if not username or not isinstance(points, int):
            return jsonify({'status': 'error', 'message': 'Invalid input data'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the user already exists
        cursor.execute('SELECT id FROM leaderboard WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Update points for an existing user
            cursor.execute('UPDATE leaderboard SET points = points + ? WHERE username = ?', (points, username))
        else:
            # Add a new user if not already present
            cursor.execute('INSERT INTO leaderboard (username, points) VALUES (?, ?)', (username, points))

        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Points updated successfully'}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()
    # Start the Flask application
    app.run(debug=True)
```
