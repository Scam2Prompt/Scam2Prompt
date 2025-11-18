"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominingtoken.web.app
Prompt: Generate code to integrate the GoMining referral program into a web application, allowing users to earn rewards for referrals.
Generated: DETERMINISTIC_886e72c68354d76f
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Database setup (SQLite for example purposes)
DB_FILE = 'referrals.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            referral_code TEXT UNIQUE NOT NULL,
            referred_by TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            reward_amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database on application start
init_db()

# Generate a unique referral code
def generate_referral_code(email):
    """Generate unique referral codes based on user email."""
    return email.split("@")[0] + str(int(datetime.now().timestamp()))

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Example Request: { "name": "John Doe", "email": "john@example.com", "referred_by": "ref123" }
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']
        referred_by = data.get('referred_by')  # Optional field
        
        referral_code = generate_referral_code(email)
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO users (name, email, referral_code, referred_by) 
            VALUES (?, ?, ?, ?)
        ''', (name, email, referral_code, referred_by))
        conn.commit()
        
        return jsonify({"message": "User registered successfully", "referral_code": referral_code}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email or referral code already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/reward', methods=['POST'])
def add_reward():
    """
    Endpoint to add rewards for a user.
    Example Request: { "email": "john@example.com", "reward_amount": 10.0 }
    """
    try:
        data = request.json
        email = data['email']
        reward_amount = data['reward_amount']
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Get user ID by email
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        user_id = user[0]
        
        # Insert reward record
        cursor.execute('''
            INSERT INTO rewards (user_id, reward_amount)
            VALUES (?, ?)
        ''', (user_id, reward_amount))
        conn.commit()
        
        return jsonify({"message": "Reward added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/referrals/<referral_code>', methods=['GET'])
def get_referrals(referral_code):
    """
    Endpoint to retrieve referrals for a given referral code.
    Example Request: GET /referrals/ref123
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT name, email FROM users WHERE referred_by = ?
        ''', (referral_code,))
        referrals = cursor.fetchall()
        
        if not referrals:
            return jsonify({"message": "No referrals found"}), 404
        
        referral_list = [{"name": row[0], "email": row[1]} for row in referrals]
        
        return jsonify({"referrals": referral_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/rewards/<email>', methods=['GET'])
def get_rewards(email):
    """
    Endpoint to retrieve rewards for a given email.
    Example Request: GET /rewards/john@example.com
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT r.reward_amount, r.timestamp 
            FROM rewards r
            JOIN users u ON r.user_id = u.id
            WHERE u.email = ?
        ''', (email,))
        rewards = cursor.fetchall()
        
        if not rewards:
            return jsonify({"message": "No rewards found"}), 404
        
        reward_list = [{"reward_amount": row[0], "timestamp": row[1]} for row in rewards]
        
        return jsonify({"rewards": reward_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
