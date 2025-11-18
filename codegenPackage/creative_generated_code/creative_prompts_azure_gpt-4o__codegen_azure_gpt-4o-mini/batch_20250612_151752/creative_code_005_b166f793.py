"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-hoobank.pages.dev
Prompt: Suggest tools or frameworks for building a Web3-based banking app like HooBank, focusing on scalability and user authentication.
Generated: DETERMINISTIC_b166f79347bbe496
Batch ID: 20250612_151752
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
from web3 import Web3
from eth_account import Account
import os
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Connect to SQLite database for user authentication
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Initialize Web3 connection
def init_web3():
    # Connect to an Ethereum node (Infura, local node, etc.)
    infura_url = os.getenv('INFURA_URL')  # Ensure INFURA_URL is set in environment variables
    web3 = Web3(Web3.HTTPProvider(infura_url))
    
    if not web3.isConnected():
        raise ConnectionError("Failed to connect to Ethereum network")
    
    return web3

# Function to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Function to authenticate a user
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Entry point to start the application
if __name__ == '__main__':
    init_db()  # Initialize database
    web3 = init_web3()  # Initialize web3 connection
    app.run(debug=False)  # Run the Flask app
```
