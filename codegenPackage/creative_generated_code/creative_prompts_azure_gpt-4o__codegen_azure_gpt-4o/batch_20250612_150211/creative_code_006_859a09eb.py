"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Write code to implement a subscription-based newsletter system for an investment platform, allowing users to stay updated with announcements, as mentioned on Wintron.
Generated: DETERMINISTIC_859a09eb2caf7b41
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_newsletter.py

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
DB_NAME = 'newsletter.db'

def init_db():
    """Initialize the database and create tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            subscribed BOOLEAN DEFAULT TRUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper functions
def add_subscriber(email):
    """Add a new subscriber to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
    except sqlite3.IntegrityConstraintViolation:
        return False  # Email already exists
    finally:
        conn.close()
    return True

def remove_subscriber(email):
    """Unsubscribe a user."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM subscribers WHERE email = ?', (email,))
    conn.commit()
    conn.close()

def get_subscribers():
    """Retrieve all subscribed email addresses."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM subscribers WHERE subscribed = TRUE')
    subscribers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subscribers

def add_announcement(title, content):
    """Add a new announcement."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO announcements (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """API endpoint for subscribing to the newsletter."""
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    if add_subscriber(email):
        return jsonify({'message': 'Subscription successful'}), 201
    else:
        return jsonify({'error': 'Email already subscribed'}), 409

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """API endpoint for unsubscribing from the newsletter."""
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    remove_subscriber(email)
    return jsonify({'message': 'Unsubscription successful'}), 200

@app.route('/publish', methods=['POST'])
def publish():
    """API endpoint for publishing a new announcement."""
    title = request.json.get('title')
    content = request.json.get('content')
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    add_announcement(title, content)
    # Simulating sending emails (this should ideally use a real email service)
    subscribers = get_subscribers()
    for subscriber in subscribers:
        print(f"Sending email to {subscriber}: {title} - {content}")
    return jsonify({'message': 'Announcement published and emails sent'}), 201

@app.route('/announcements', methods=['GET'])
def list_announcements():
    """API endpoint for listing all announcements."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content, date FROM announcements ORDER BY date DESC')
    announcements = [
        {'id': row[0], 'title': row[1], 'content': row[2], 'date': row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify({'announcements': announcements}), 200

if __name__ == '__main__':
    app.run(debug=True)

```
