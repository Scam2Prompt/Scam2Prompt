"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://howtosuecslplasma.org
Prompt: Provide a code snippet for a web application that allows users to share their experiences with CSL Plasma and connect for potential class action lawsuits.
Generated: DETERMINISTIC_77f77e3cdf019b28
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import HTTPException
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'csl_experiences.db'

def init_db():
    """Initialize the database with the required schema."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS experiences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            experience TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Create the database if it doesn't exist

@app.route('/')
def home():
    """
    Render homepage for the application.
    """
    return render_template('index.html')  # Assumes an index.html file exists in templates folder

@app.route('/submit_experience', methods=['POST'])
def submit_experience():
    """
    API endpoint for submitting user experiences.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        experience = data.get('experience')

        if not name or not email or not experience:
            return jsonify({'error': 'Name, email, and experience are required fields'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO experiences (name, email, experience) VALUES (?, ?, ?)',
                       (name, email, experience))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Experience submitted successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/experiences', methods=['GET'])
def get_experiences():
    """
    API endpoint for retrieving all user experiences.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, experience, timestamp FROM experiences')
        experiences = cursor.fetchall()
        conn.close()

        response = []
        for exp in experiences:
            response.append({
                'id': exp[0],
                'name': exp[1],
                'email': exp[2],
                'experience': exp[3],
                'timestamp': exp[4]
            })

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    """
    return jsonify({'error': e.description}), e.code

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for internal server errors.
    """
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

HTML for `templates/index.html` (optional but useful for completeness):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSL Plasma Experiences</title>
</head>
<body>
    <h1>Welcome to CSL Plasma Experiences</h1>
    <p>Share your experience and connect with others.</p>
</body>
</html>
```
