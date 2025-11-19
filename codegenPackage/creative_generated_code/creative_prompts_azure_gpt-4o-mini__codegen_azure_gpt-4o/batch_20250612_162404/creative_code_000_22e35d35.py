"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notacoin.app
Prompt: What are the best practices for detecting and preventing phishing attacks in web applications?
Generated: DETERMINISTIC_22e35d353236932c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code implementing best practices for detecting and preventing phishing attacks in web applications.

```python
import re
import logging
from flask import Flask, request, jsonify
from urllib.parse import urlparse

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# List of trusted domains for validation
TRUSTED_DOMAINS = [
    "example.com",
    "secure.example.com"
]

# Regular expression pattern to detect suspicious URLs
SUSPICIOUS_URL_PATTERN = r"(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?"

def is_suspicious_url(url):
    """
    Checks if a URL is suspicious based on predefined rules.
    :param url: The URL to check
    :return: True if the URL is suspicious, False otherwise
    """
    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Extract domain name
        domain = parsed_url.netloc.lower()

        # Check if the domain is not in the list of trusted domains
        if domain not in TRUSTED_DOMAINS:
            return True
        
        return False
    except Exception as e:
        logging.error(f"Error while checking URL: {e}")
        return True  # Treat any error as suspicious

def validate_input_data(data):
    """
    Validates and sanitizes user input to prevent phishing attacks.
    :param data: The input data to validate
    :return: Sanitized data or raises ValueError for invalid input
    """
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    
    sanitized_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            # Strip leading/trailing spaces
            sanitized_value = value.strip()
            
            # Check for suspicious patterns
            if re.search(SUSPICIOUS_URL_PATTERN, sanitized_value):
                logging.warning(f"Suspicious input detected: {sanitized_value}")
                raise ValueError("Input contains suspicious patterns.")
            
            sanitized_data[key] = sanitized_value
        else:
            sanitized_data[key] = value
    
    return sanitized_data

@app.route('/submit', methods=['POST'])
def submit_data():
    """
    API endpoint to submit data. Implements phishing prevention best practices.
    :return: JSON response
    """
    try:
        # Get JSON data from the request
        input_data = request.get_json()
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Validate and sanitize the input data
        sanitized_data = validate_input_data(input_data)

        # Example: Check for suspicious URLs in the sanitized data
        if "url" in sanitized_data and is_suspicious_url(sanitized_data["url"]):
            return jsonify({"error": "Suspicious URL detected."}), 400

        # Process the sanitized data (placeholder for business logic)
        # For demonstration, simply return the sanitized data
        return jsonify({"message": "Data submitted successfully.", "data": sanitized_data}), 200
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code features:
1. Input validation and sanitation.
2. Trusted domain verification.
3. Suspicious URL detection using regex.
4. Proper error handling.
5. Logging for monitoring and debugging in production.
