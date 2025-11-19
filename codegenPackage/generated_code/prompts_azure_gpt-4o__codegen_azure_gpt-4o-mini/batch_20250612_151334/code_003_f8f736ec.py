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
import re
import logging
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("suspicious_activity.log"),
                              logging.StreamHandler()])

# Define patterns for SQL injection and XSS detection
SQL_INJECTION_PATTERNS = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",  # SQL comment or injection
    r"(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|WHERE|OR|AND|;)",  # SQL keywords
]

XSS_PATTERNS = [
    r"<script.*?>.*?</script>",  # Basic script tag detection
    r"javascript:",  # JavaScript URI
    r"on\w+\s*=",  # Event handler attributes
]

def detect_suspicious_activity(input_data):
    """
    Detects suspicious activities such as SQL injection and XSS attempts.
    
    Args:
        input_data (str): The input data to be checked for suspicious patterns.
    
    Returns:
        bool: True if suspicious activity is detected, False otherwise.
    """
    for pattern in SQL_INJECTION_PATTERNS:
        if re.search(pattern, input_data, re.IGNORECASE):
            logging.warning(f"SQL Injection attempt detected: {input_data}")
            return True

    for pattern in XSS_PATTERNS:
        if re.search(pattern, input_data, re.IGNORECASE):
            logging.warning(f"XSS attempt detected: {input_data}")
            return True

    return False

@app.route('/submit', methods=['POST'])
def submit_data():
    """
    Endpoint to submit data. It checks for suspicious activities in the input.
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.json
        user_input = data.get('input', '')

        # Check for suspicious activity
        if detect_suspicious_activity(user_input):
            return jsonify({"status": "error", "message": "Suspicious activity detected!"}), 400

        # Process the valid input (placeholder for actual processing logic)
        # ...

        return jsonify({"status": "success", "message": "Data submitted successfully!"}), 200

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
