"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Create a dashboard to display user statistics for a web3 community, including raffle winners and entries, inspired by the Atlas3 MoonSeeker DAO application.
Generated: DETERMINISTIC_d3abf8608aa49a1d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)

# Database setup
DB_PATH = "web3_community.db"

def setup_database():
    """Create the required database schema for user statistics and raffle data."""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create user statistics table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_statistics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            wallet_address TEXT NOT NULL UNIQUE,
            activity_score INTEGER DEFAULT 0
        )""")
        # Create raffle entries table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS raffle_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raffle_id INTEGER NOT NULL,
            wallet_address TEXT NOT NULL,
            entry_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        # Create raffle winners table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS raffle_winners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raffle_id INTEGER NOT NULL,
            wallet_address TEXT NOT NULL,
            win_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        conn.commit()
        conn.close()

# Setup database on application start
setup_database()

# Flask routes
@app.route("/")
def dashboard():
    """
    Render the dashboard HTML page.
    """
    return render_template("dashboard.html")

@app.route("/api/user_statistics", methods=["GET"])
def get_user_statistics():
    """
    API endpoint to fetch user statistics.
    Returns:
        JSON response containing user statistics.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT username, wallet_address, activity_score FROM user_statistics")
        users = cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": users}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/api/raffle_winners", methods=["GET"])
def get_raffle_winners():
    """
    API endpoint to fetch raffle winners.
    Returns:
        JSON response containing raffle winners.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT raffle_id, wallet_address, win_timestamp FROM raffle_winners")
        winners = cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": winners}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/api/raffle_entries", methods=["GET"])
def get_raffle_entries():
    """
    API endpoint to fetch raffle entries.
    Returns:
        JSON response containing raffle entries.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT raffle_id, wallet_address, entry_timestamp FROM raffle_entries")
        entries = cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": entries}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/api/add_user", methods=["POST"])
def add_user():
    """
    API endpoint to add a new user to the database.
    Expects JSON payload: {"username": "example", "wallet_address": "0x123"}
    """
    try:
        data = request.get_json()
        username = data.get("username")
        wallet_address = data.get("wallet_address")
        if not username or not wallet_address:
            return jsonify({"success": False, "message": "Missing username or wallet address"}), 400

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_statistics (username, wallet_address) VALUES (?, ?)", (username, wallet_address))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "User added successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"success": False, "message": "Wallet address already exists"}), 409
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Error handling
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors with a custom JSON response.
    """
    return jsonify({"success": False, "message": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors with a custom JSON response.
    """
    return jsonify({"success": False, "message": "Internal server error"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
