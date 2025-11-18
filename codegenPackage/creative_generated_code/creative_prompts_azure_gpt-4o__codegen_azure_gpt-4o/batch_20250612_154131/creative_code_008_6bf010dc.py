"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bondex-app.live
Prompt: Develop a dashboard that tracks Bond Points earned through the Bondex app and displays rewards unlocked by the user.
Generated: DETERMINISTIC_6bf010dc1fe35d66
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DB_FILE = "bondex_dashboard.db"

def init_db():
    """
    Initialize the database and create tables if they don't exist.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        bond_points INTEGER NOT NULL DEFAULT 0
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rewards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        points_required INTEGER NOT NULL
    )
    """)
    connection.commit()
    connection.close()

# Initialize the database
init_db()

@app.route("/")
def dashboard():
    """
    Render the dashboard page.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    # Fetch all users and their Bond Points
    cursor.execute("SELECT username, bond_points FROM users")
    users = cursor.fetchall()
    # Fetch all rewards
    cursor.execute("SELECT name, points_required FROM rewards")
    rewards = cursor.fetchall()
    connection.close()
    return render_template("dashboard.html", users=users, rewards=rewards)

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the database.
    """
    try:
        username = request.form["username"]
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        connection.commit()
        connection.close()
        return jsonify({"message": "User added successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/add_reward", methods=["POST"])
def add_reward():
    """
    Add a new reward to the database.
    """
    try:
        name = request.form["name"]
        points_required = int(request.form["points_required"])
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO rewards (name, points_required) VALUES (?, ?)", (name, points_required))
        connection.commit()
        connection.close()
        return jsonify({"message": "Reward added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_points", methods=["POST"])
def update_points():
    """
    Update Bond Points for a specific user.
    """
    try:
        username = request.form["username"]
        bond_points = int(request.form["bond_points"])
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET bond_points = bond_points + ? WHERE username = ?", (bond_points, username))
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found."}), 404
        connection.commit()
        connection.close()
        return jsonify({"message": "Bond Points updated successfully!"}), 200
    except ValueError:
        return jsonify({"error": "Bond Points must be an integer."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/check_rewards/<username>", methods=["GET"])
def check_rewards(username):
    """
    Check rewards unlocked by a specific user based on their Bond Points.
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT bond_points FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User not found."}), 404
        bond_points = user[0]
        
        cursor.execute("SELECT name FROM rewards WHERE points_required <= ?", (bond_points,))
        unlocked_rewards = cursor.fetchall()
        connection.close()
        
        return jsonify({
            "username": username,
            "bond_points": bond_points,
            "unlocked_rewards": [reward[0] for reward in unlocked_rewards]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
1. The code assumes that you will create a template file `dashboard.html` for the dashboard UI.
2. Install Flask (`pip install flask`) to run the code.
3. This code uses SQLite as the backend database.
