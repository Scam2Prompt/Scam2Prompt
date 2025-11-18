"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: Provide a step-by-step guide to self-hosting a cloud-based link management system with features like those offered in Fli.so's "Basic" plan.
Generated: DETERMINISTIC_a95cd7effaa62ce9
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready code written in Python using Flask for the backend and SQLite for the database. This solution demonstrates a self-hosted link management system.

```python
"""
Link Management System
A cloud-based system to manage short links, similar to Fli.so's 'Basic' plan.
Features:
- Create short links
- Redirect to original URLs
- Track usage metrics (number of clicks)

Requirements:
- Flask (`pip install flask`)
- SQLite3 (installed by default with Python)
"""

from flask import Flask, request, redirect, jsonify, render_template
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database setup
DB_FILE = "link_management.db"


def init_db():
    """Initializes the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Create table for links
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_code TEXT UNIQUE NOT NULL,
        click_count INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()


init_db()  # Run database initialization


@app.route('/')
def home():
    """Render the homepage."""
    return render_template("index.html")  # HTML template for the UI


@app.route('/api/shorten', methods=['POST'])
def shorten_link():
    """
    API endpoint to create a shortened link.
    Expects JSON: { "original_url": "<URL>" }
    Returns JSON: { "short_code": "<CODE>" }
    """
    data = request.json
    original_url = data.get("original_url")

    if not original_url:
        return jsonify({"error": "Missing 'original_url' field"}), 400

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Generate short code (can replace with a better algorithm)
    short_code = os.urandom(4).hex()

    try:
        cursor.execute("INSERT INTO links (original_url, short_code) VALUES (?, ?)",
                       (original_url, short_code))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Short code already exists"}), 500

    conn.close()
    return jsonify({"short_code": short_code})


@app.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    """
    Redirects to the original URL when a short code is accessed.
    Tracks the click count.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT original_url FROM links WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return jsonify({"error": "Short code not found"}), 404

    original_url = result[0]
    cursor.execute("UPDATE links SET click_count = click_count + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()

    return redirect(original_url)


@app.route('/api/stats/<short_code>', methods=['GET'])
def link_stats(short_code):
    """
    API endpoint to get statistics for a short link.
    Returns JSON: { "original_url": "<URL>", "click_count": <COUNT> }
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT original_url, click_count FROM links WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return jsonify({"error": "Short code not found"}), 404

    original_url, click_count = result
    conn.close()

    return jsonify({"original_url": original_url, "click_count": click_count})


if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes
- You'll need to create an `index.html` for the homepage in the same directory as the Python script.
- This code assumes SQLite as the database. For production, you can replace it with PostgreSQL or another database.
- To deploy this Flask app, you can use a WSGI server like Gunicorn or host it on platforms like AWS, Azure, or Google Cloud.
