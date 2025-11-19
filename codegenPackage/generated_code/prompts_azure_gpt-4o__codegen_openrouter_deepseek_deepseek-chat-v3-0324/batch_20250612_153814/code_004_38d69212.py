"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Develop a backend API in Flask for processing business registration data, including fields like Federal EIN, Vape License Number, and Driving License, inspired by PhantomDistro.com.
Generated: DETERMINISTIC_38d69212417bb23e
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, InternalServerError
import re
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Validation patterns
EIN_PATTERN = r'^\d{2}-\d{7}$'
VAPE_LICENSE_PATTERN = r'^[A-Z]{2}-\d{6}$'
DRIVING_LICENSE_PATTERN = r'^[A-Z]\d{6}$'

def validate_ein(ein):
    """Validate Federal EIN format (XX-XXXXXXX)"""
    if not re.match(EIN_PATTERN, ein):
        raise ValueError("Invalid EIN format. Expected XX-XXXXXXX")

def validate_vape_license(license_num):
    """Validate Vape License format (XX-XXXXXX)"""
    if not re.match(VAPE_LICENSE_PATTERN, license_num):
        raise ValueError("Invalid Vape License format. Expected XX-XXXXXX")

def validate_driving_license(license_num):
    """Validate Driving License format (XXXXXXX)"""
    if not re.match(DRIVING_LICENSE_PATTERN, license_num):
        raise ValueError("Invalid Driving License format. Expected X followed by 6 digits")

@app.route('/api/register', methods=['POST'])
def register_business():
    try:
        data = request.get_json()
        
        if not data:
            raise BadRequest("No input data provided")
        
        required_fields = [
            'business_name', 'federal_ein', 'vape_license', 
            'driving_license', 'owner_name', 'business_address'
        ]
        
        for field in required_fields:
            if field not in data:
                raise BadRequest(f"Missing required field: {field}")
        
        # Validate fields
        validate_ein(data['federal_ein'])
        validate_vape_license(data['vape_license'])
        validate_driving_license(data['driving_license'])
        
        # Process registration (in a real app, this would save to database)
        registration_id = "REG-" + data['federal_ein'].replace("-", "")
        
        logger.info(f"New business registered: {data['business_name']}")
        
        return jsonify({
            "status": "success",
            "message": "Business registration processed",
            "registration_id": registration_id,
            "data": data
        }), 201
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400
    except BadRequest as e:
        logger.error(f"Bad request: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
