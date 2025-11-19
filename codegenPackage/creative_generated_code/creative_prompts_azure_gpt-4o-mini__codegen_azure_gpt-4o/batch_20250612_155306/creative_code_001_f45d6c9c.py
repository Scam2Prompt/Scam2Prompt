"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defivalidation.com
Prompt: Write a code snippet to implement a domain inquiry form that captures user information like country codes as seen on Defivalidation.com.
Generated: DETERMINISTIC_f45d6c9ca47ee37a
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Allowed country codes for validation (can be extended)
ALLOWED_COUNTRY_CODES = ["US", "CA", "GB", "AU", "DE", "FR"]

def is_valid_country_code(country_code):
    """
    Validate the country code.
    :param country_code: str - The country code to validate.
    :return: bool - True if valid, False otherwise.
    """
    return country_code.upper() in ALLOWED_COUNTRY_CODES

@app.route('/domain-inquiry', methods=['POST'])
def domain_inquiry():
    """
    Handle domain inquiry form submission.
    Expects JSON input with 'name', 'email', 'domain', and 'country_code'.
    Responds with validation errors or success message.
    """
    data = request.get_json()

    # Validate input fields
    errors = {}

    # Validate name
    name = data.get("name")
    if not name or not name.strip():
        errors["name"] = "Name is required."
    
    # Validate email
    email = data.get("email")
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors["email"] = "A valid email address is required."
    
    # Validate domain
    domain = data.get("domain")
    if not domain or not re.match(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$", domain):  # Basic domain check
        errors["domain"] = "A valid domain name is required."
    
    # Validate country code
    country_code = data.get("country_code")
    if not country_code or not is_valid_country_code(country_code):
        errors["country_code"] = f"Country code must be one of: {', '.join(ALLOWED_COUNTRY_CODES)}."

    # Return errors if any validations failed
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    # Success response
    return jsonify({
        "success": True,
        "message": "Domain inquiry submitted successfully!",
        "data": {
            "name": name,
            "email": email,
            "domain": domain,
            "country_code": country_code.upper()
        }
    }), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
