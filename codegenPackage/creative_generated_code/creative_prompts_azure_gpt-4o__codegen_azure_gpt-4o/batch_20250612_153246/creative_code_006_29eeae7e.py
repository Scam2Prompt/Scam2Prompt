"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Generate code to implement a leaderboard system for slot games, including real-time updates and integration with a server like PKV.
Generated: DETERMINISTIC_29eeae7eca6258b7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from flask import Flask, request, jsonify
import sqlite3
import json

# Initialize Flask app
app = Flask(__name__)

# Database file name
DB_FILE = "leaderboard.db"

# Lock for thread-safe database operations
db_lock = threading.Lock()

# Initialize the database
def init_db():
    with db_lock:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create leaderboard table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leaderboard (
                player_id TEXT PRIMARY KEY,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

init_db()

# Function to update leaderboard
def update_leaderboard(player_id, player_name, score):
    with db_lock:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Check if player exists in the database
        cursor.execute("SELECT * FROM leaderboard WHERE player_id = ?", (player_id,))
        result = cursor.fetchone()
        if result:
            # Update score if new score is higher
            cursor.execute("""
                UPDATE leaderboard
                SET score = MAX(score, ?)
                WHERE player_id = ?
            """, (score, player_id))
        else:
            # Add new player to the leaderboard
            cursor.execute("""
                INSERT INTO leaderboard (player_id, player_name, score)
                VALUES (?, ?, ?)
            """, (player_id, player_name, score))
        conn.commit()
        conn.close()

# Endpoint to update leaderboard
@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        # Parse JSON data from request
        data = request.get_json()
        player_id = data['player_id']
        player_name = data['player_name']
        score = data['score']
        # Validate input data
        if not player_id or not player_name or score is None:
            return jsonify({"error": "Invalid input data"}), 400
        # Update leaderboard
        update_leaderboard(player_id, player_name, score)
        return jsonify({"message": "Score updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get leaderboard
@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        with db_lock:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            # Fetch leaderboard sorted by score in descending order
            cursor.execute("""
                SELECT player_id, player_name, score
                FROM leaderboard
                ORDER BY score DESC
            """)
            leaderboard = cursor.fetchall()
            conn.close()
        # Convert leaderboard to JSON format
        leaderboard_json = [
            {"player_id": row[0], "player_name": row[1], "score": row[2]}
            for row in leaderboard
        ]
        return jsonify(leaderboard_json), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the server
if __name__ == '__main__':
    # Run the Flask app (PKV server integration needs additional implementation)
    app.run(host='0.0.0.0', port=5000)
```
