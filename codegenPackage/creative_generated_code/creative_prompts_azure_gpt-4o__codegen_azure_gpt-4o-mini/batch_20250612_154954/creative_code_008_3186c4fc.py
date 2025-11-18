"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fearlessnetpreneur.com
Prompt: Develop a script to automate the creation of a social media product, following the steps outlined in Fearless Netpreneur's "Steps to Create a Social Media Product: Your Guide to Success."
Generated: DETERMINISTIC_3186c4fcb2e06b9a
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'social_media.db'

def init_db():
    """Initialize the database and create tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            email TEXT UNIQUE NOT NULL
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            content TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                          )''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
            conn.commit()

        return jsonify({"message": "User registered successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username or email already exists."}), 400
    except KeyError:
        return jsonify({"error": "Missing username or email."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/post', methods=['POST'])
def create_post():
    """Endpoint to create a new post."""
    try:
        data = request.get_json()
        user_id = data['user_id']
        content = data['content']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (user_id, content))
            conn.commit()

        return jsonify({"message": "Post created successfully!"}), 201
    except KeyError:
        return jsonify({"error": "Missing user_id or content."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/posts', methods=['GET'])
def get_posts():
    """Endpoint to retrieve all posts."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts")
            posts = cursor.fetchall()

        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False)  # Run the Flask app
```
