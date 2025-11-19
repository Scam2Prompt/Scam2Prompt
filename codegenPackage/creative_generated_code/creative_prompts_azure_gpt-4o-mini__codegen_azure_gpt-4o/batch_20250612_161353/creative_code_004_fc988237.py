"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: How can I develop an API that provides information on the legal requirements and costs for temporary registration in Adygea?
Generated: DETERMINISTIC_fc98823783f444fd
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for legal requirements and costs
TEMPORARY_REGISTRATION_DATA = {
    "Adygea": {
        "legal_requirements": [
            "Identity document (passport).",
            "Proof of residence.",
            "Application form for temporary registration.",
            "Consent from the property owner."
        ],
        "costs": {
            "registration_fee": 500,  # Example amount in rubles
            "service_charge": 200    # Example amount in rubles
        }
    }
}

@app.route('/api/temporary-registration', methods=['GET'])
def get_temporary_registration_info():
    """
    API Endpoint to fetch temporary registration information for Adygea.

    Query Parameters:
        - region (optional): Specify a region to fetch data. Defaults to Adygea.
    
    Returns:
        JSON object containing legal requirements and costs for temporary registration.
    """
    try:
        # Get region from query parameters
        region = request.args.get('region', 'Adygea')
        
        # Check if data for the region exists
        if region in TEMPORARY_REGISTRATION_DATA:
            response_data = TEMPORARY_REGISTRATION_DATA[region]
            return jsonify({
                "region": region,
                "data": response_data
            }), 200
        else:
            # Handle case where region is not found
            return jsonify({
                "error": "Region not found. Please check the region name or contact support."
            }), 404
    except Exception as e:
        # Generic error handling
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```
