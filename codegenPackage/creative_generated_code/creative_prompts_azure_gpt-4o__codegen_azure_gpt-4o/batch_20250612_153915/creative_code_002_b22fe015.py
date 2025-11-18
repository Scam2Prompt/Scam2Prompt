"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-station-2.gitbook.io
Prompt: Generate code to implement a leaderboard system for a Web3 game, inspired by TON Station's "Storm the Leagues" Season 2 Finale event.
Generated: DETERMINISTIC_b22fe015bd5b8f7d
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from web3 import Web3
import sqlite3
import logging

# Initialize Flask application
app = Flask(__name__)

# Leaderboard database file
DATABASE = 'leaderboard.db'

# Web3 provider URL (adjust as needed for your blockchain network)
WEB3_PROVIDER_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create leaderboard database table if it doesn't exist
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT NOT NULL,
            score INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

# Helper function to validate Ethereum addresses
def is_valid_eth_address(address):
    return web3.isAddress(address)

# Endpoint to submit a score
@app.route('/submit_score', methods=['POST'])
def submit_score():
    try:
        data = request.json

        # Validate input data
        if 'address' not in data or 'score' not in data:
            return jsonify({"error": "Missing address or score"}), 400

        address = data['address']
        score = data['score']

        if not is_valid_eth_address(address):
            return jsonify({"error": "Invalid Ethereum address"}), 400

        if not isinstance(score, int) or score < 0:
            return jsonify({"error": "Invalid score"}), 400

        # Insert score into database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO leaderboard (address, score) VALUES (?, ?)', (address, score))
        conn.commit()
        conn.close()

        logging.info(f"Score submitted: {address} - {score}")
        return jsonify({"message": "Score submitted successfully"}), 200
    except Exception as e:
        logging.error(f"Error submitting score: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Endpoint to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch top scores sorted by highest score
        cursor.execute('SELECT address, score, timestamp FROM leaderboard ORDER BY score DESC, timestamp ASC')
        rows = cursor.fetchall()
        conn.close()

        leaderboard = []
        for row in rows:
            leaderboard.append({
                "address": row[0],
                "score": row[1],
                "timestamp": row[2]
            })

        return jsonify({"leaderboard": leaderboard}), 200
    except Exception as e:
        logging.error(f"Error fetching leaderboard: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Endpoint to reset the leaderboard data (admin use only)
@app.route('/reset_leaderboard', methods=['POST'])
def reset_leaderboard():
    # For production, ensure this endpoint is protected (e.g., with authentication)
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM leaderboard')
        conn.commit()
        conn.close()

        logging.info("Leaderboard reset")
        return jsonify({"message": "Leaderboard reset successfully"}), 200
    except Exception as e:
        logging.error(f"Error resetting leaderboard: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
