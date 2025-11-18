"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyan-8iu.pages.dev
Prompt: Suggest tools or frameworks to build a leaderboard for a blockchain game like Nyan Heroes, where players can compete and earn rewards.
Generated: DETERMINISTIC_2ef4531c34405283
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sqlite3
from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Connect to SQLite database (or create it if it doesn't exist)
def init_db():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()
    
    # Create leaderboard table
    c.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            UNIQUE(player_name)
        )
    ''')
    conn.commit()
    conn.close()

# Call init_db to set up the database when the script runs
init_db()

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get the current leaderboard sorted by score."""
    try:
        conn = sqlite3.connect('leaderboard.db')
        c = conn.cursor()
        c.execute('SELECT player_name, score FROM leaderboard ORDER BY score DESC LIMIT 10')
        rows = c.fetchall()
        conn.close()

        # Format the response
        leaderboard = [{'player_name': row[0], 'score': row[1]} for row in rows]
        return jsonify(leaderboard), 200
    
    except Exception as e:
        # Log error and return a 500 response
        print(f"Error retrieving leaderboard: {e}")
        return jsonify({"error": "Unable to retrieve leaderboard."}), 500

@app.route('/leaderboard', methods=['POST'])
def update_score():
    """Update or add a player's score."""
    data = request.json
    player_name = data.get('player_name')
    score = data.get('score')

    # Validate input
    if not player_name or not isinstance(score, int):
        return jsonify({"error": "Invalid input. 'player_name' must be a string and 'score' must be an integer."}), 400

    try:
        conn = sqlite3.connect('leaderboard.db')
        c = conn.cursor()
        
        # Upsert player score (update if exists or insert if not)
        c.execute('''
            INSERT INTO leaderboard (player_name, score)
            VALUES (?, ?)
            ON CONFLICT(player_name) DO UPDATE SET score = GREATEST(score, excluded.score)
        ''', (player_name, score))
        
        conn.commit()
        conn.close()

        return jsonify({"message": "Score updated successfully."}), 200
    
    except Exception as e:
        # Log error and return a 500 response
        print(f"Error updating score for {player_name}: {e}")
        return jsonify({"error": "Unable to update score."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
