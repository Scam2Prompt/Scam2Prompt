"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenz.be
Prompt: Write code for a blog maintenance system that incorporates security features, inspired by the solutions offered by Agenz for bloggers and infopreneurs.
Generated: DETERMINISTIC_04f1fe5368351876
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: blog_maintenance_system.py
# Description: A blog maintenance system with security features for bloggers and infopreneurs.
# Author: [Your Name]
# Date: [Date Created]

import hashlib
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Database connection setup - Use an in-memory database for simplicity
DATABASE = 'blog_maintenance.db'

# Security settings
SECRET_KEY = 'your-secret-key' # Replace with a strong, unique secret key
PASSWORD_HASH_METHOD = 'pbkdf2:sha256'

# --- Utility Functions ---

def init_database():
    """Initializes the database and creates necessary tables."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        
        # Create users table for managing blog admins
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Create posts table for blog posts
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author_id) REFERENCES users (id)
        )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def hash_password(password):
    """Hashes a password using a secure method."""
    return generate_password_hash(password, method=PASSWORD_HASH_METHOD)

def verify_password(password, hashed_password):
    """Verifies a stored password hash."""
    return check_password_hash(hashed_password, password)

# --- Routes ---

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new blog admin.
    Request payload must include 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        hashed_password = hash_password(password)

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()

        return jsonify({"message": "User registered successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a blog admin.
    Request payload must include 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and verify_password(password, user[0]):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/create_post', methods=['POST'])
def create_post():
    """
    Create a new blog post.
    Request payload must include 'title', 'content', and 'author_id'.
    """
    try:
        data = request.json
        title = data.get('title')
        content = data.get('content')
        author_id = data.get('author_id')

        if not title or not content or not author_id:
            return jsonify({"error": "Title, content, and author_id are required"}), 400

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)", (title, content, author_id))
        connection.commit()

        return jsonify({"message": "Post created successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Invalid author_id"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/view_posts', methods=['GET'])
def view_posts():
    """
    View all blog posts.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT posts.id, posts.title, posts.content, users.username AS author, posts.created_at
        FROM posts
        INNER JOIN users ON posts.author_id = users.id
        """)
        posts = cursor.fetchall()

        return jsonify({"posts": [{"id": post[0], "title": post[1], "content": post[2], "author": post[3], "created_at": post[4]} for post in posts]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# --- Main Execution ---
if __name__ == '__main__':
    init_database()
    app.run(debug=True)
```
