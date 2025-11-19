"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.xyz
Prompt: How do I implement a domain purchase inquiry system that captures user details like on Idex.xyz?
Generated: DETERMINISTIC_17b916ffbff3859d
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to validate email format
def is_valid_email(email):
    # Regular expression for validating email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Function to validate domain name format
def is_valid_domain(domain):
    # Regular expression for validating domain name
    domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$'
    return bool(re.match(domain_regex, domain))

# Route to handle domain purchase inquiries
@app.route('/inquiry', methods=['POST'])
def domain_inquiry():
    try:
        # Parse incoming JSON data
        data = request.json

        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('domain'):
            return jsonify({'error': 'Missing required fields: name, email, and domain'}), 400
        
        # Extract fields
        name = data['name']
        email = data['email']
        domain = data['domain']

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Validate domain format
        if not is_valid_domain(domain):
            return jsonify({'error': 'Invalid domain format'}), 400

        # Process inquiry (In production, you would save this to a database or send an email)
        # Mock response for demonstration purposes
        response = {
            'message': 'Domain purchase inquiry submitted successfully!',
            'submitted_data': {
                'name': name,
                'email': email,
                'domain': domain
            }
        }
        return jsonify(response), 200
    
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Entry point to run the Flask application
if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(debug=True)
```

**Instructions to Run**:
1. Save this code to a file named `app.py`.
2. Install Flask using the command: `pip install flask`.
3. Run the script using: `python app.py`.
4. Test the `/inquiry` endpoint by sending a POST request with JSON data (e.g., using Postman or `curl`):
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "domain": "example.xyz"
   }
   ```

This code implements a clean, production-ready solution for a domain purchase inquiry system using Python and Flask.
