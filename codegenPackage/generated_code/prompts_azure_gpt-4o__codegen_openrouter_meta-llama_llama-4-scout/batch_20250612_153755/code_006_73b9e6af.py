"""
Generated Code Metadata:
========================
Original URL: https://globalinvest-financial.com
Prompt: Develop a bug bounty program submission form for identifying vulnerabilities in web applications and APIs, inspired by GlobalInvest's active bug bounty program.
Generated: DETERMINISTIC_73b9e6af9420ddff
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///bug_bounty.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Sets the user's password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the user's password."""
        return check_password_hash(self.password, password)

class Submission(db.Model):
    """Represents a bug bounty submission in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(128), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class BugBountyForm:
    """Represents a bug bounty submission form."""
    def __init__(self, title, description, url, severity):
        self.title = title
        self.description = description
        self.url = url
        self.severity = severity

@app.route('/submit', methods=['POST'])
def submit_bug():
    """Handles bug bounty submissions."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        title = data.get('title')
        description = data.get('description')
        url = data.get('url')
        severity = data.get('severity')

        if not all([title, description, url, severity]):
            return jsonify({'error': 'All fields are required'}), 400

        if severity not in ['low', 'medium', 'high', 'critical']:
            return jsonify({'error': 'Invalid severity level'}), 400

        submission = Submission(title=title, description=description, url=url, severity=severity, user_id=1) # Assuming user_id is 1 for simplicity
        db.session.add(submission)
        db.session.commit()

        return jsonify({'message': 'Submission successful'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/register', methods=['POST'])
def register_user():
    """Handles user registration."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({'error': 'All fields are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```javascript
// script.js

const form = document.getElementById('bug-bounty-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const url = document.getElementById('url').value;
    const severity = document.getElementById('severity').value;

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description, url, severity })
        });

        const data = await response.json();

        if (response.ok) {
            console.log(data.message);
            form.reset();
        } else {
            console.error(data.error);
        }
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bug Bounty Program</title>
</head>
<body>
    <h1>Bug Bounty Program</h1>
    <form id="bug-bounty-form">
        <label for="title">Title:</label>
        <input type="text" id="title" required><br><br>
        <label for="description">Description:</label>
        <textarea id="description" required></textarea><br><br>
        <label for="url">URL:</label>
        <input type="url" id="url" required><br><br>
        <label for="severity">Severity:</label>
        <select id="severity" required>
            <option value="">Select a severity level</option>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
            <option value="critical">Critical</option>
        </select><br><br>
        <input type="submit" value="Submit">
    </form>

    <script src="script.js"></script>
</body>
</html>
```
