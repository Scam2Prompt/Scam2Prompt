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
# Click Fraud Detection API Implementation
# This API detects potential click fraud based on incoming requests from advertisers.
# It uses rules and patterns to identify fraudulent clicks.

from flask import Flask, request, jsonify
import logging
import re
from datetime import datetime, timedelta

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# In-memory storage for tracking click occurrences
click_tracking = {}

# Define thresholds for fraud detection (can be dynamically tuned)
MAX_CLICKS_PER_IP = 100  # Threshold for max clicks per IP per hour
SUSPICIOUS_USER_AGENTS = ['curl', 'bot', 'spider']  # Patterns in User-Agent strings indicating bots

# Helper function to check if User-Agent is suspicious
def is_suspicious_user_agent(user_agent):
    return any(re.search(pattern, user_agent, re.IGNORECASE) for pattern in SUSPICIOUS_USER_AGENTS)

# Helper function to clean up old click data (hourly cleanup)
def cleanup_old_clicks():
    cutoff_time = datetime.now() - timedelta(hours=1)
    to_delete = [
        ip for ip, records in click_tracking.items()
        if all(click_time < cutoff_time for click_time in records)
    ]
    for ip in to_delete:
        del click_tracking[ip]

# Endpoint for detecting click fraud
@app.route('/detect', methods=['POST'])
def detect_fraud():
    """
    Detects potential click fraud based on incoming request data.
    Expects JSON payload with 'ip' and 'user_agent' fields.
    """
    try:
        # Parse JSON request payload
        data = request.get_json()
        if not data or 'ip' not in data or 'user_agent' not in data:
            return jsonify({'error': 'Invalid request. Missing required fields: ip, user_agent'}), 400

        ip = data['ip']
        user_agent = data['user_agent']

        # Validate input fields
        if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):  # Simple IP address validation
            return jsonify({'error': 'Invalid IP address format'}), 400

        # Check User-Agent for suspicious patterns
        if is_suspicious_user_agent(user_agent):
            logging.warning(f"Suspicious User-Agent detected: {user_agent}")
            return jsonify({'fraud': True, 'reason': 'Suspicious User-Agent'}), 200

        # Track clicks per IP
        now = datetime.now()
        if ip not in click_tracking:
            click_tracking[ip] = []
        click_tracking[ip].append(now)

        # Remove stale click records
        cleanup_old_clicks()

        # Check if IP exceeds the threshold
        recent_clicks = [click_time for click_time in click_tracking[ip] if click_time >= now - timedelta(hours=1)]
        if len(recent_clicks) > MAX_CLICKS_PER_IP:
            logging.warning(f"Click fraud detected for IP: {ip}")
            return jsonify({'fraud': True, 'reason': 'Excessive clicks from single IP'}), 200

        # No fraud detected
        return jsonify({'fraud': False}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
