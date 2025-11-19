"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbss.ru
Prompt: What are the best practices for implementing a click fraud detection API mentioned on wbss.ru?
Generated: DETERMINISTIC_3f0ae98f7d53f16a
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('clicks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database table
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS clicks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ad_id TEXT NOT NULL,
                        user_id TEXT NOT NULL,
                        ip_address TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

# Function to log a click
def log_click(ad_id, user_id, ip_address):
    try:
        conn = get_db_connection()
        conn.execute('INSERT INTO clicks (ad_id, user_id, ip_address) VALUES (?, ?, ?)',
                     (ad_id, user_id, ip_address))
        conn.commit()
    except Exception as e:
        logging.error(f"Error logging click: {e}")
    finally:
        conn.close()

# Function to detect click fraud based on simple rules
def detect_fraud(ad_id):
    conn = get_db_connection()
    # Simple rule: if more than 5 clicks from the same IP in a minute, flag as fraud
    fraud_threshold = 5
    fraud_timeframe = 60  # in seconds

    query = '''SELECT COUNT(*) as click_count FROM clicks 
               WHERE ad_id = ? AND timestamp >= datetime('now', '-1 minute')
               GROUP BY ip_address'''
    cursor = conn.execute(query, (ad_id,))
    click_counts = cursor.fetchall()
    conn.close()

    # Check if any IP exceeded the threshold
    for row in click_counts:
        if row['click_count'] > fraud_threshold:
            return True  # Fraud detected
    return False  # No fraud detected

@app.route('/click', methods=['POST'])
def click_handler():
    data = request.json
    
    # Validate incoming data
    if not data or 'ad_id' not in data or 'user_id' not in data or 'ip_address' not in data:
        logging.warning("Missing parameters in request")
        return jsonify({'error': 'Missing parameters'}), 400

    ad_id = data['ad_id']
    user_id = data['user_id']
    ip_address = data['ip_address']

    # Log the click
    log_click(ad_id, user_id, ip_address)

    # Check for fraud
    if detect_fraud(ad_id):
        logging.warning(f"Fraud detected for ad_id {ad_id} from IP {ip_address}")
        return jsonify({'status': 'fraud detected'}), 403

    return jsonify({'status': 'click logged successfully'}), 200

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```
