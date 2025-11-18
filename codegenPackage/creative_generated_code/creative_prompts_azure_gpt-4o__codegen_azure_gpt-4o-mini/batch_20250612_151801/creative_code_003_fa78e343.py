"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Recommend libraries or APIs for handling phone number validation and country code selection, similar to the functionality provided on the Pixels dashboard.
Generated: DETERMINISTIC_fa78e343066eb960
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# phone_number_validator.py

import phonenumbers
from phonenumbers import geocoder, carrier
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/validate_phone', methods=['POST'])
def validate_phone():
    """
    Validate a phone number and get its details including the country code and carrier.
    
    Request JSON Format:
    {
        "phone_number": "+14155552671"
    }

    Returns:
    - status: "valid" or "invalid"
    - country_code: The country code of the number (if valid)
    - carrier: The carrier of the number (if valid)
    """
    try:
        # Extract phone number from the request
        data = request.get_json()
        phone_number = data.get('phone_number')
        
        # Validate phone number using the phonenumbers library
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Check if the number is valid
        if phonenumbers.is_valid_number(parsed_number):
            country_code = geocoder.region_code_for_number(parsed_number)
            carrier_name = carrier.name_for_number(parsed_number, "en")
            return jsonify({
                "status": "valid",
                "country_code": country_code,
                "carrier": carrier_name
            }), 200
        else:
            return jsonify({
                "status": "invalid",
                "message": "The phone number is not valid."
            }), 400

    except phonenumbers.NumberParseException:
        return jsonify({
            "status": "invalid",
            "message": "The phone number provided is not in a recognized format."
        }), 400
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, you need to install Flask and phonenumbers libraries. You can do this via pip:

```bash
pip install Flask phonenumbers
```

### Usage
- Start the Flask application by running the script.
- Send a POST request to the `/validate_phone` endpoint with a JSON payload containing the phone number to be validated.
