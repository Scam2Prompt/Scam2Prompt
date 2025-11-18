"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Develop a customer support chatbot for MARUF ONLINE BD that integrates hotline numbers and email support for package inquiries.
Generated: DETERMINISTIC_aa62e2fe7245dfc9
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define hotline numbers and email support
support_info = {
    "hotline_numbers": ["+8801XXXXXXXXX", "+8801XXXXXXXXY"],  # Example hotline numbers
    "email_support": "support@marufonlinebd.com"
}

# Function to validate user input
def validate_input(user_input):
    if not user_input:
        return False, "Input cannot be empty."
    return True, ""

# Function to handle customer inquiries
def handle_inquiry(inquiry):
    inquiry = inquiry.lower()
    
    if re.search(r'\bpackage inquiry\b', inquiry):
        response = (
            "For package inquiries, you can reach our hotline at: "
            f"{', '.join(support_info['hotline_numbers'])} "
            f"or email us at {support_info['email_support']}."
        )
    else:
        response = "I'm sorry, I can assist with package inquiries only."
    
    return response

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get user input from request
        user_input = request.json.get('message', '').strip()
        
        # Validate input
        is_valid, error_message = validate_input(user_input)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Handle the inquiry and generate a response
        response_message = handle_inquiry(user_input)
        
        return jsonify({"response": response_message}), 200
    
    except Exception as e:
        # Return a generic error message for any uncaught exceptions
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=False)
```

This Flask application defines a simple customer support chatbot that handles inquiries related to package information and provides hotline and email support.
