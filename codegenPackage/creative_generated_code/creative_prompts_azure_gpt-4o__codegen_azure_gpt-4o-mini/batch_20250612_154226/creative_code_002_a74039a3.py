"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Create Python code to automate the intake process for legal leads, ensuring thorough vetting and live transfer functionality, as described on ClaimLink Legal Solutions.
Generated: DETERMINISTIC_a74039a31115c1ed
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Setting up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory storage for leads (Consider using a database in production)
leads_db = []

class Lead:
    """Class to represent a legal lead."""
    def __init__(self, name, email, phone, details):
        self.name = name
        self.email = email
        self.phone = phone
        self.details = details

    def to_dict(self):
        """Convert Lead instance to dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'details': self.details
        }

def validate_lead_data(data):
    """Validate incoming lead data."""
    required_fields = ['name', 'email', 'phone', 'details']
    
    for field in required_fields:
        if field not in data:
            logger.error(f'Missing field: {field}')
            raise ValueError(f'Missing field: {field}')
    
    # Additional validations can be added here (e.g., email format)

@app.route('/intake', methods=['POST'])
def intake_lead():
    """Endpoint to intake a new legal lead."""
    try:
        data = request.get_json()
        logger.info(f'Received data: {data}')

        # Validate the incoming data
        validate_lead_data(data)

        # Create a new lead and add it to the database
        new_lead = Lead(data['name'], data['email'], data['phone'], data['details'])
        leads_db.append(new_lead)
        logger.info(f'New lead added: {new_lead.to_dict()}')

        # Here you would add functionality for live transfer if applicable

        return jsonify(new_lead.to_dict()), 201

    except ValueError as ve:
        logger.error(f'Validation error: {str(ve)}')
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'An internal error occurred'}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    response = e.get_response()
    response.data = json.dumps({
        'error': e.description
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Ensure to install Flask: `pip install Flask`
- This code is designed for a basic Flask web application to intake leads.
- For production, consider persistent storage (like a database) instead of in-memory lists.
- Security measures and further validations should be included based on specific requirements.
