"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Create a script to detect and log suspicious activities such as SQL injection or XSS attempts on a cryptocurrency faucet platform, inspired by the anti-cheat measures described on USDT Claim.
Generated: DETERMINISTIC_f8f736ecf7561646
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import re
from flask import request, jsonify

# Configure logging
logging.basicConfig(filename='suspicious_activities.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to detect SQL injection attempts
def detect_sql_injection(input_string):
    """
    Detects SQL injection attempts in a given input string.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if SQL injection is detected, False otherwise.
    """
    sql_injection_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "CREATE", "ALTER", "TRUNCATE"]
    sql_injection_patterns = [r"UNION\s+SELECT", r"OR\s+1\s*=\s*1", r"AND\s+1\s*=\s*1"]

    # Check for SQL injection keywords
    for keyword in sql_injection_keywords:
        if keyword in input_string.upper():
            logging.warning(f"SQL injection keyword detected: {keyword}")
            return True

    # Check for SQL injection patterns
    for pattern in sql_injection_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            logging.warning(f"SQL injection pattern detected: {pattern}")
            return True

    return False

# Define a function to detect XSS attempts
def detect_xss_attempts(input_string):
    """
    Detects XSS attempts in a given input string.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if XSS is detected, False otherwise.
    """
    xss_patterns = [r"<script>", r"</script>", r"javascript:", r"alert\(", r"eval\("]

    # Check for XSS patterns
    for pattern in xss_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            logging.warning(f"XSS pattern detected: {pattern}")
            return True

    return False

# Define a function to log suspicious activities
def log_suspicious_activity(ip_address, user_agent, input_string, activity_type):
    """
    Logs suspicious activities.

    Args:
        ip_address (str): The IP address of the user.
        user_agent (str): The user agent of the user.
        input_string (str): The input string that triggered the detection.
        activity_type (str): The type of suspicious activity (SQL injection or XSS).
    """
    logging.info(f"Suspicious {activity_type} activity detected from {ip_address} with user agent {user_agent}: {input_string}")

# Define a Flask API endpoint to test the detection functions
from flask import Flask
app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test_detection():
    try:
        data = request.get_json()
        input_string = data.get('input_string')

        if detect_sql_injection(input_string):
            log_suspicious_activity(request.remote_addr, request.user_agent, input_string, 'SQL injection')
            return jsonify({'message': 'SQL injection detected'}), 403

        if detect_xss_attempts(input_string):
            log_suspicious_activity(request.remote_addr, request.user_agent, input_string, 'XSS')
            return jsonify({'message': 'XSS detected'}), 403

        return jsonify({'message': 'No suspicious activity detected'}), 200

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
