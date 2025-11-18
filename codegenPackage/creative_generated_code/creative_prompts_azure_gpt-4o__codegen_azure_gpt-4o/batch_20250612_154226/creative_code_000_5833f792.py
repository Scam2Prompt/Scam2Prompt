"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Write code to implement a lead generation API for a law firm specializing in personal injury cases, using ClaimLink Legal Solutions' approach of pre-qualified leads and bilingual support.
Generated: DETERMINISTIC_5833f7922ff1da07
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pre-defined list of supported languages
SUPPORTED_LANGUAGES = ['en', 'es']  # English ('en') and Spanish ('es')

# Sample validation criteria for a pre-qualified lead
def is_prequalified_lead(data):
    """
    Function to validate if the lead meets pre-qualification criteria.
    Criteria can be extended based on business rules.
    """
    required_fields = ['name', 'phone', 'email', 'case_details', 'language']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    if data['language'] not in SUPPORTED_LANGUAGES:
        return False, "Unsupported language. Supported languages are: 'en', 'es'."
    
    # Additional validation criteria can be added here
    return True, None

@app.route('/leads', methods=['POST'])
def generate_lead():
    """
    API endpoint to create a new lead.
    Expects a JSON payload with the following structure:
    {
        "name": "John Doe",
        "phone": "+123456789",
        "email": "john.doe@example.com",
        "case_details": "Brief description of the case",
        "language": "en"
    }
    """
    try:
        # Parse JSON payload
        lead_data = request.get_json()
        
        if not lead_data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        # Validate lead data
        is_valid, error_message = is_prequalified_lead(lead_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # If valid, save lead to database (stubbed out for this example)
        # Normally, you would integrate with a database here.
        logging.info(f"Lead successfully created: {lead_data}")

        # Return success response
        return jsonify({"message": "Lead successfully created", "lead": lead_data}), 201
    
    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error occurred while creating lead: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
```
