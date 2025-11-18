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

Here’s an implementation of a URL shortening service with statistics tracking using Python and Flask, showcasing best practices:

```python
from flask import Flask, request, jsonify, redirect
from werkzeug.exceptions import HTTPException
from hashids import Hashids
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Initialize Hashids for URL shortening
hashids = Hashids(min_length=6, salt="your-secret-salt")

# SQLite database configuration
DATABASE = 'url_shortener.db'

# Create database schema if not exists
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            shortened_url TEXT NOT NULL,
            click_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

# Error handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"error": str(e)}), e.code

# Shorten URL endpoint
@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        original_url = request.json.get('original_url')
        if not original_url:
            return jsonify({"error": "original_url is required"}), 400

        # Insert original URL into database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO urls (original_url, click_count) VALUES (?, ?)', (original_url, 0))
        url_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Generate shortened URL using Hashids
        shortened_url = hashids.encode(url_id)

        # Update shortened URL in database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE urls SET shortened_url = ? WHERE id = ?', (shortened_url, url_id))
        conn.commit()
        conn.close()

        return jsonify({"shortened_url": shortened_url}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

# Redirect and track clicks endpoint
@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
    try:
        # Decode shortened URL to get its ID
        url_id = hashids.decode(shortened_url)
        if not url_id:
            return jsonify({"error": "Invalid shortened URL"}), 404

        # Fetch original URL from database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT original_url, click_count FROM urls WHERE id = ?', (url_id[0],))
        url_data = cursor.fetchone()
        conn.close()

        if not url_data:
            return jsonify({"error": "URL not found"}), 404

        original_url, click_count = url_data

        # Increment click count
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE urls SET click_count = ? WHERE id = ?', (click_count + 1, url_id[0]))
        conn.commit()
        conn.close()

        return redirect(original_url)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

# Statistics endpoint
@app.route('/stats', methods=['GET'])
def get_statistics():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT original_url, shortened_url, click_count FROM urls')
        stats = cursor.fetchall()
        conn.close()

        return jsonify([
            {"original_url": original_url, "shortened_url": shortened_url, "click_count": click_count}
            for original_url, shortened_url, click_count in stats
        ]), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

# Run the Flask app
if __name__ == "__main__":
    # Set debug to False for production
    app.run(debug=False)
```

### Dependencies:
1. `Flask`: Web framework (`pip install flask`)
2. `Hashids`: For generating unique, short IDs (`pip install hashids`)
3. SQLite: Lightweight database (included with Python)

### Notes:
- Replace `"your-secret-salt"` with a secure, random string for production.
- Use `gunicorn` or similar WSGI servers to deploy the Flask app in production.
- Consider adding input validation for URLs, HTTPS enforcement, and more robust logging for production readiness.
