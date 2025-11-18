"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Generate code to create a multilingual job posting system for recruiting Latin American talent in European markets, as discussed in Management en Red's blog.
Generated: DETERMINISTIC_da3f5be57263ee2b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
from flask_babel import Babel, _
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure Flask-Babel for multilingual support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'pt', 'fr']
babel = Babel(app)

# Database setup
DATABASE = 'job_postings.db'

# Initialize database (run once)
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_postings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            location TEXT,
            language TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to connect to the database
def connect_db():
    return sqlite3.connect(DATABASE)

# Retrieve the user's preferred language
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Endpoint to create a job posting
@app.route('/create_job_posting', methods=['POST'])
def create_job_posting():
    try:
        # Parse the request data
        data = request.json
        title = data.get('title')
        description = data.get('description')
        location = data.get('location')
        language = data.get('language', 'en')

        # Validate input
        if not title or not description or not location:
            return jsonify({'error': _('Title, description, and location are required')}), 400

        # Insert job posting into the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO job_postings (title, description, location, language, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, location, language, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        return jsonify({'message': _('Job posting created successfully')}), 201
    except Exception as e:
        return jsonify({'error': _('An error occurred while creating the job posting: {}').format(str(e))}), 500

# Endpoint to retrieve all job postings
@app.route('/job_postings', methods=['GET'])
def get_job_postings():
    try:
        # Fetch job postings from the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM job_postings')
        rows = cursor.fetchall()
        conn.close()

        # Format the result
        job_postings = []
        for row in rows:
            job_postings.append({
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'location': row[3],
                'language': row[4],
                'created_at': row[5]
            })

        return jsonify(job_postings), 200
    except Exception as e:
        return jsonify({'error': _('An error occurred while retrieving job postings: {}').format(str(e))}), 500

# Endpoint to retrieve job postings filtered by language
@app.route('/job_postings/<language>', methods=['GET'])
def get_job_postings_by_language(language):
    try:
        # Fetch job postings by language from the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM job_postings WHERE language = ?', (language,))
        rows = cursor.fetchall()
        conn.close()

        # Format the result
        job_postings = []
        for row in rows:
            job_postings.append({
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'location': row[3],
                'language': row[4],
                'created_at': row[5]
            })

        return jsonify(job_postings), 200
    except Exception as e:
        return jsonify({'error': _('An error occurred while retrieving job postings: {}').format(str(e))}), 500

# Initialize the application
if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()
    app.run(host='0.0.0.0', port=5000)
```
