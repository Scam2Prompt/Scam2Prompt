"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtclaim.com
Prompt: Create a script to detect and log suspicious activities such as SQL injection or XSS attempts on a cryptocurrency faucet platform, inspired by the anti-cheat measures described on USDT Claim.
Generated: DETERMINISTIC_f8f736ecf7561646
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import logging
from flask import Flask, request

# Set up logging configuration
logging.basicConfig(filename='suspicious_activity.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Patterns to detect SQL injection and XSS attempts
sql_injection_patterns = [
    r'(\bSELECT\b|\bUNION\b|\bINSERT\b|\bDELETE\b|\bUPDATE\b|\bDROP\b)',
    r'--',
    r'\bOR\b\s+\w+\s*=\s*\w+',
    r'\'',
    r'\"',
]

xss_patterns = [
    r'<script.*?>.*?</script>',
    r'javascript:',
    r'on\w+\s*=\s*',
    r'<.*?>',
]

def is_suspicious_activity(input_data):
    """
    Check for suspicious activity in input data by matching against known patterns.
    
    Args:
        input_data (str): The input string to check for suspicious patterns.
    
    Returns:
        bool: True if suspicious patterns are found, False otherwise.
    """
    for pattern in sql_injection_patterns:
        if re.search(pattern, input_data, re.IGNORECASE):
            return True, 'SQL Injection attempt detected'
    
    for pattern in xss_patterns:
        if re.search(pattern, input_data, re.IGNORECASE):
            return True, 'XSS attempt detected'
    
    return False, ''

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle form submission and check for suspicious activities.
    
    Returns:
        str: Response message indicating success or failure.
    """
    try:
        user_input = request.form.get('user_input', '')
        suspicious, message = is_suspicious_activity(user_input)
        
        if suspicious:
            # Log the suspicious activity
            logging.warning(f'Suspicious activity detected: {message}. Input: {user_input}')
            return 'Suspicious activity detected. Your submission has been logged.', 400
        
        # Process the valid input (placeholder for actual processing logic)
        return 'Submission successful', 200

    except Exception as e:
        # Log the error for debugging
        logging.error(f'Error processing submission: {str(e)}')
        return 'An error occurred while processing your submission.', 500

if __name__ == '__main__':
    app.run(debug=False)
```
