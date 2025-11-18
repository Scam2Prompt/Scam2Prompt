"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://urlz.fr
Prompt: Recommend tools or libraries for implementing a URL shortening service with statistics tracking, similar to the total links minimized feature mentioned on URLz.fr.
Generated: DETERMINISTIC_501d7f4d2d8a5e89
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    # Create a table to store URLs and their statistics
    c.execute('''CREATE TABLE IF NOT EXISTS links (
                    id INTEGER PRIMARY KEY,
                    original_url TEXT NOT NULL,
                    short_url TEXT NOT NULL UNIQUE,
                    access_count INTEGER DEFAULT 0
                )''')
    conn.commit()
    conn.close()

# Generate a short URL
def generate_short_url(original_url):
    # Hash the original URL to create a unique short URL
    hash_object = hashlib.md5(original_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Shorten to 6 characters
    return short_url

# Save URL to the database
def save_url(original_url):
    short_url = generate_short_url(original_url)
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO links (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
    except sqlite3.IntegrityError:
        # If the short URL already exists, just return the existing one
        pass
    finally:
        conn.close()
    return short_url

# Retrieve the original URL and increment access count
def get_original_url(short_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("SELECT original_url, access_count FROM links WHERE short_url = ?", (short_url,))
    result = c.fetchone()
    if result:
        original_url, access_count = result
        # Increment access count
        c.execute("UPDATE links SET access_count = ? WHERE short_url = ?", (access_count + 1, short_url))
        conn.commit()
        return original_url
    return None

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    short_url = save_url(original_url)
    return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    return jsonify({'error': 'Short URL not found'}), 404

@app.route('/stats/<short_url>', methods=['GET'])
def url_stats(short_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("SELECT original_url, access_count FROM links WHERE short_url = ?", (short_url,))
    result = c.fetchone()
    conn.close()
    if result:
        original_url, access_count = result
        return jsonify({
            'original_url': original_url,
            'access_count': access_count
        }), 200
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Start the Flask application
```

This code implements a simple URL shortening service using Flask and SQLite, with features for generating short URLs, redirecting to original URLs, and tracking access count statistics.
