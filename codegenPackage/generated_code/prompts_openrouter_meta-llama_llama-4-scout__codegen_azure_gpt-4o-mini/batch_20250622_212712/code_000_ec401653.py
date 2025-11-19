"""
Generated Code Metadata:
========================
Original URL: https://urlra.com
Prompt: Write a Python script to create a custom URL shortener with features like link tracking, retargeting, and custom splash pages using a service similar to URLra.com.
Generated: DETERMINISTIC_ec401653d6e135cf
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3
from flask import Flask, request, redirect, jsonify, render_template

app = Flask(__name__)

# Database setup
DATABASE = 'url_shortener.db'

def init_db():
    """Initialize the database with the required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_url TEXT UNIQUE NOT NULL,
                splash_page TEXT,
                clicks INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def generate_short_url(original_url):
    """Generate a short URL using a hash of the original URL."""
    hash_object = hashlib.md5(original_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Shorten to 6 characters
    return short_url

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to create a short URL."""
    data = request.json
    original_url = data.get('original_url')
    splash_page = data.get('splash_page', None)

    if not original_url:
        return jsonify({'error': 'Original URL is required'}), 400

    short_url = generate_short_url(original_url)

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO urls (original_url, short_url, splash_page) VALUES (?, ?, ?)',
                           (original_url, short_url, splash_page))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Short URL already exists'}), 400

    return jsonify({'short_url': request.host_url + short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    """Redirect to the original URL and track clicks."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT original_url, splash_page, clicks FROM urls WHERE short_url = ?', (short_url,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({'error': 'Short URL not found'}), 404

        original_url, splash_page, clicks = result
        clicks += 1
        cursor.execute('UPDATE urls SET clicks = ? WHERE short_url = ?', (clicks, short_url))
        conn.commit()

    if splash_page:
        return render_template('splash.html', original_url=original_url, splash_page=splash_page)
    return redirect(original_url)

@app.route('/stats/<short_url>', methods=['GET'])
def get_stats(short_url):
    """Get statistics for a short URL."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT original_url, clicks FROM urls WHERE short_url = ?', (short_url,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({'error': 'Short URL not found'}), 404

        original_url, clicks = result
        return jsonify({'original_url': original_url, 'clicks': clicks}), 200

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```

**Note:** This code requires Flask to be installed. You can install it using `pip install Flask`. Additionally, a simple HTML template named `splash.html` should be created to handle splash page rendering.
