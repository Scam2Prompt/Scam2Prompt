"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cryptophonesupport.com
Prompt: What are the best practices for implementing cryptographic protocols in API development as discussed on cryptophonesupport.com?
Generated: DETERMINISTIC_85a5457f0579e285
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import os
import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Constants for HMAC
SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')  # Should be set in environment variables
HMAC_ALGORITHM = 'sha256'

def generate_hmac(data: str) -> str:
    """
    Generate a HMAC for the given data using the specified secret key.

    :param data: The data to be hashed.
    :return: The HMAC as a hexadecimal string.
    """
    return hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.new(HMAC_ALGORITHM)).hexdigest()

def verify_hmac(data: str, provided_hmac: str) -> bool:
    """
    Verify the HMAC for the given data against the provided HMAC.

    :param data: The data that was hashed.
    :param provided_hmac: The HMAC to verify.
    :return: True if the HMAC is valid, False otherwise.
    """
    expected_hmac = generate_hmac(data)
    return hmac.compare_digest(expected_hmac, provided_hmac)

@app.route('/api/data', methods=['POST'])
def receive_data():
    """
    API endpoint to receive data and verify its HMAC.

    The request should include JSON data with the format:
    {
        "data": "<data_string>",
        "hmac": "<hmac_string>"
    }

    :return: JSON response indicating success or failure.
    """
    try:
        # Parse JSON data from the request
        request_data = request.get_json()
        if not request_data or 'data' not in request_data or 'hmac' not in request_data:
            abort(400, description="Invalid input data. Must include 'data' and 'hmac'.")

        data = request_data['data']
        provided_hmac = request_data['hmac']

        # Verify the HMAC
        if verify_hmac(data, provided_hmac):
            return jsonify({"message": "HMAC verified successfully", "status": "success"}), 200
        else:
            abort(403, description="HMAC verification failed.")

    except json.JSONDecodeError:
        abort(400, description="Invalid JSON format.")
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

### Note:
Make sure to set the `SECRET_KEY` environment variable in your production environment for secure HMAC generation.
