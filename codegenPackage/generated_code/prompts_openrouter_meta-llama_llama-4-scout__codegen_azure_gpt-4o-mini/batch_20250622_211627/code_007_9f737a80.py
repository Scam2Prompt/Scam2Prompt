"""
Generated Code Metadata:
========================
Original URL: https://iplis.ru
Prompt: Design a URL shortener and IP tracker tool using IPLogger's features, including a simple user interface for analytics.
Generated: DETERMINISTIC_9f737a80bba07b7d
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, redirect, render_template, jsonify
import sqlite3
import uuid
import datetime

app = Flask(__name__)

# Database setup
DATABASE = 'url_shortener.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id TEXT PRIMARY KEY,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ip_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short_url TEXT NOT NULL,
                ip_address TEXT NOT NULL,
                accessed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (short_url) REFERENCES urls (short_url)
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def index():
    """Render the main page for URL shortening."""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a given URL and store it in the database."""
    original_url = request.form.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_url = str(uuid.uuid4())[:8]  # Generate a short URL
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO urls (id, original_url, short_url) VALUES (?, ?, ?)',
                           (str(uuid.uuid4()), original_url, short_url))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Short URL already exists'}), 400

    return jsonify({'short_url': request.host_url + short_url}), 201

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirect to the original URL and log the IP address."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
            row = cursor.fetchone()
            if row is None:
                return jsonify({'error': 'Short URL not found'}), 404
            
            original_url = row[0]
            ip_address = request.remote_addr
            
            # Log the IP address
            cursor.execute('INSERT INTO ip_logs (short_url, ip_address) VALUES (?, ?)',
                           (short_url, ip_address))
            conn.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return redirect(original_url)

@app.route('/analytics/<short_url>')
def analytics(short_url):
    """Provide analytics for a given short URL."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
            url_row = cursor.fetchone()
            if url_row is None:
                return jsonify({'error': 'Short URL not found'}), 404
            
            cursor.execute('SELECT ip_address, accessed_at FROM ip_logs WHERE short_url = ?', (short_url,))
            logs = cursor.fetchall()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    analytics_data = {
        'original_url': url_row[0],
        'access_logs': [{'ip_address': log[0], 'accessed_at': log[1]} for log in logs]
    }
    return jsonify(analytics_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Shortener</title>
</head>
<body>
    <h1>URL Shortener</h1>
    <form id="urlForm">
        <input type="text" name="url" placeholder="Enter URL to shorten" required>
        <button type="submit">Shorten</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('urlForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/shorten', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            document.getElementById('result').innerText = response.ok ? 
                `Short URL: ${result.short_url}` : `Error: ${result.error}`;
        };
    </script>
</body>
</html>
```

### Notes
- Ensure you have Flask installed (`pip install Flask`).
- The database file `url_shortener.db` will be created in the same directory as the script.
- The HTML template should be saved in a folder named `templates` in the same directory as the Python script.
