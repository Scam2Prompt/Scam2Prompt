"""
Generated Code Metadata:
========================
Original URL: https://lol-hser2bio.vercel.app
Prompt: Develop a simple full-stack application using Flask (Python) and SQLite to store and display spiritual or motivational messages, with user capabilities to submit new messages.
Generated: DETERMINISTIC_813ab7f460c9dcdc
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Database file name
DATABASE = 'messages.db'

# Ensure the database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE messages (id INTEGER PRIMARY KEY, content TEXT NOT NULL)')
    conn.close()

# Helper function to interact with the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    """
    Render the homepage with all motivational messages.
    """
    messages = query_db('SELECT * FROM messages')
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit_message():
    """
    Endpoint to submit a new motivational message.
    """
    try:
        content = request.form.get('content')
        if not content:
            return jsonify({'error': 'Message content cannot be empty'}), 400
        query_db('INSERT INTO messages (content) VALUES (?)', [content])
        return jsonify({'success': 'Message added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """
    API endpoint to fetch all motivational messages.
    """
    try:
        messages = query_db('SELECT * FROM messages')
        return jsonify([dict(message) for message in messages]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Motivational Messages</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        form {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Motivational Messages</h1>
    <div id="messages">
        {% for message in messages %}
        <div class="message">
            <p>{{ message['content'] }}</p>
        </div>
        {% endfor %}
    </div>
    <form id="messageForm" method="POST" action="/submit">
        <textarea name="content" rows="4" cols="50" placeholder="Write your motivational message here..." required></textarea><br>
        <button type="submit">Submit</button>
    </form>
    <script>
        const form = document.getElementById('messageForm');
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/submit', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
                alert(result.success);
                location.reload();
            } else {
                alert(result.error);
            }
        });
    </script>
</body>
</html>
```
