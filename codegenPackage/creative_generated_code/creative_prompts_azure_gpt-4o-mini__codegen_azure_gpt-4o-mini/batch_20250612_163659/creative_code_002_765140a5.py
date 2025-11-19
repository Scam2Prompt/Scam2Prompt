"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: What are the steps to create a leaderboard for tracking participants in the Tari airdrop game, including gem collection and rankings?
Generated: DETERMINISTIC_765140a51d3e4dc4
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    # Create a table for participants if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            gems_collected INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Add a new participant
@app.route('/add_participant', methods=['POST'])
def add_participant():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required."}), 400

    try:
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO participants (username) VALUES (?)', (username,))
        conn.commit()
        return jsonify({"message": f"Participant {username} added."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Update gems collected for a participant
@app.route('/update_gems', methods=['POST'])
def update_gems():
    data = request.get_json()
    username = data.get('username')
    gems = data.get('gems')

    if not username or gems is None:
        return jsonify({"error": "Username and gems are required."}), 400

    try:
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE participants SET gems_collected = gems_collected + ? WHERE username = ?', (gems, username))
        if cursor.rowcount == 0:
            return jsonify({"error": "Participant not found."}), 404
        conn.commit()
        return jsonify({"message": f"{gems} gems added to {username}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    try:
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        cursor.execute('SELECT username, gems_collected FROM participants ORDER BY gems_collected DESC')
        participants = cursor.fetchall()
        return jsonify(participants), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask app
```
