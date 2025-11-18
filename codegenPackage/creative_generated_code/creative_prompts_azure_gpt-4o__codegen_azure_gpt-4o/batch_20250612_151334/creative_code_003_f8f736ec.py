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
from datetime import datetime

# Configure logging
LOG_FILE = 'security.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Suspicious patterns for detecting SQL injection and XSS attempts
SQL_INJECTION_PATTERNS = [
    r"(?i)(union\s+select)",  # UNION SELECT statement
    r"(?i)(\bor\b.+\b(?:=|>|<))",  # OR operator with conditional checks
    r"(?i)(select\s.+\bfrom\b)",  # SELECT FROM statement
    r"(?i)(\bdrop\b|\btruncate\b|\bdelete\b)",  # Drop, Truncate, Delete
    r"(?i)(\binsert\b|\bupdate\b|\bexec\b)",  # Insert, Update, Exec
    r"(--|;|\#|\')",  # SQL comment or quote characters
]

XSS_PATTERNS = [
    r"(?i)(<script.*?>.*?</script>)",  # Script tags
    r"(?i)(javascript:)",  # JavaScript protocol
    r"(?i)(on\w+=)",  # Inline event handlers
    r"(?i)(<\s*iframe.*?>)",  # iframe tags
    r"(?i)(<\s*img[^>]*src=.*?javascript:.*?>)",  # Image with JavaScript
]

# Function to detect suspicious activity
def detect_suspicious_activity(input_data):
    """
    Detects suspicious activity attempts such as SQL injection or XSS.

    Args:
        input_data (str): The user-provided input data to check for suspicious patterns.

    Returns:
        bool: True if suspicious activity is detected, False otherwise.
    """
    for pattern in SQL_INJECTION_PATTERNS:
        if re.search(pattern, input_data):
            logging.warning("SQL Injection Attempt Detected: %s", input_data)
            return True
    
    for pattern in XSS_PATTERNS:
        if re.search(pattern, input_data):
            logging.warning("XSS Attempt Detected: %s", input_data)
            return True
    
    return False

# Function to log suspicious activity with context
def log_suspicious_activity(user_ip, user_agent, input_data):
    """
    Logs suspicious activity details.

    Args:
        user_ip (str): The IP address of the user.
        user_agent (str): The user agent string from the user's browser.
        input_data (str): The suspicious input provided by the user.

    Returns:
        None
    """
    logging.info(
        "Suspicious activity logged:\n"
        "User IP: %s\n"
        "User Agent: %s\n"
        "Input Data: %s",
        user_ip, user_agent, input_data
    )

# Simulated input from the platform
def simulate_user_input():
    """
    Simulates user input for testing purposes.

    Returns:
        list of dict: A list of simulated user input data.
    """
    return [
        {"user_ip": "192.168.1.1", "user_agent": "Mozilla/5.0", "input_data": "1 OR 1=1"},
        {"user_ip": "192.168.1.2", "user_agent": "Mozilla/5.0", "input_data": "<script>alert('XSS')</script>"},
        {"user_ip": "192.168.1.3", "user_agent": "Mozilla/5.0", "input_data": "Hello, world!"},
    ]

# Main function to process user inputs
def main():
    """
    Main function to process user inputs and detect suspicious activity.

    Returns:
        None
    """
    user_inputs = simulate_user_input()
    
    for user_input in user_inputs:
        user_ip = user_input["user_ip"]
        user_agent = user_input["user_agent"]
        input_data = user_input["input_data"]

        if detect_suspicious_activity(input_data):
            log_suspicious_activity(user_ip, user_agent, input_data)
        else:
            logging.info("No suspicious activity detected for User IP: %s", user_ip)

# Entry point of the script
if __name__ == "__main__":
    main()
```
