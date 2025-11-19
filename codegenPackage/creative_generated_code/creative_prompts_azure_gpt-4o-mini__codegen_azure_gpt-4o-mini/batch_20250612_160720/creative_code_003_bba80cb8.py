"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bom.so
Prompt: Generate code to track user clicks on a shortened URL created with Bom.so and analyze the data.
Generated: DETERMINISTIC_bba80cb81146fba5
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Database setup
DATABASE = 'url_clicks.db'

def init_db():
    """Initialize the SQLite database with a table for tracking clicks."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/track_click', methods=['POST'])
def track_click():
    """Endpoint to track click on a shortened URL created with Bom.so."""
    # Get the URL from the request
    data = request.get_json()
    url = data.get('url')

    # Validate the input
    if not url:
        return jsonify({"error": "Missing URL parameter."}), 400

    # Store the click data in the database
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clicks (url) VALUES (?)', (url,))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        conn.close()

    return jsonify({"message": "Click tracked successfully."}), 200

@app.route('/analytics', methods=['GET'])
def analytics():
    """Endpoint to retrieve click analytics for tracked URLs."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT url, COUNT(*) as click_count FROM clicks GROUP BY url')
        results = cursor.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        conn.close()

    # Build the response data
    analytics_data = [{"url": row[0], "click_count": row[1]} for row in results]

    return jsonify(analytics_data), 200

if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True)  # Run the Flask app
```
