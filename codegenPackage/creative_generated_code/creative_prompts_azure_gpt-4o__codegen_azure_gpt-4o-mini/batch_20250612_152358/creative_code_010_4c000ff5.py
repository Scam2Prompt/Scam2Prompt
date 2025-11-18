"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Develop a dashboard to monitor affiliate earnings and referral activity, incorporating Lite Trade's promotional tools and banners.
Generated: DETERMINISTIC_4c000ff5d5888296
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('affiliate_dashboard.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        return None

# Route to render the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API endpoint to get affiliate earnings
@app.route('/api/earnings', methods=['GET'])
def get_earnings():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        # Query to retrieve earnings data
        earnings = conn.execute('SELECT * FROM earnings').fetchall()
        return jsonify([dict(row) for row in earnings]), 200
    except sqlite3.Error as e:
        logging.error(f"Error querying earnings: {e}")
        return jsonify({'error': 'Query failed'}), 500
    finally:
        conn.close()

# API endpoint to get referral activity
@app.route('/api/referrals', methods=['GET'])
def get_referrals():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        # Query to retrieve referral data
        referrals = conn.execute('SELECT * FROM referrals').fetchall()
        return jsonify([dict(row) for row in referrals]), 200
    except sqlite3.Error as e:
        logging.error(f"Error querying referrals: {e}")
        return jsonify({'error': 'Query failed'}), 500
    finally:
        conn.close()

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found'}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affiliate Dashboard</title>
    <script>
        // Function to fetch and display earnings
        async function fetchEarnings() {
            const response = await fetch('/api/earnings');
            const data = await response.json();
            if (response.ok) {
                // Render earnings data in the dashboard
                console.log(data);
            } else {
                console.error(data.error);
            }
        }

        // Function to fetch and display referrals
        async function fetchReferrals() {
            const response = await fetch('/api/referrals');
            const data = await response.json();
            if (response.ok) {
                // Render referral data in the dashboard
                console.log(data);
            } else {
                console.error(data.error);
            }
        }

        // Initialize dashboard
        document.addEventListener('DOMContentLoaded', () => {
            fetchEarnings();
            fetchReferrals();
        });
    </script>
</head>
<body>
    <h1>Affiliate Earnings and Referral Activity</h1>
    <div id="earnings"></div>
    <div id="referrals"></div>
</body>
</html>
```

### Notes:
- Ensure you create a SQLite database named `affiliate_dashboard.db` with the appropriate tables (`earnings` and `referrals`) before running the application.
- Replace the queries in the API endpoints with your actual table schema and requirements.
- The HTML file is basic and should be enhanced for production use with proper styling and layout.
