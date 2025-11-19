"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pegasus-usual-dao.vercel.app
Prompt: What are the best practices for handling restricted regions in API responses, as seen on the Usual Interface?
Generated: DETERMINISTIC_dfcfd8b32624dc65
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Mock data representing restricted and unrestricted regions
API_RESPONSE = {
    "name": "Sample Data",
    "global_info": "This information is available globally.",
    "restricted_info": "This information is restricted to specific regions."
}

# List of allowed regions
ALLOWED_REGIONS = ["US", "EU", "APAC"]

def region_restriction(func):
    """
    Decorator to handle restricted regions in API responses.
    Verifies if the request originates from an allowed region.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Extract region from query params (mocked here)
            region = request.args.get('region', '').upper()

            if region not in ALLOWED_REGIONS:
                # Restrict access if the region is not allowed
                return jsonify({
                    "error": "Access denied",
                    "message": f"Your region '{region}' is not authorized to access restricted content."
                }), 403
            
            # If region is allowed, proceed with the API response
            return func(*args, **kwargs)
        except Exception as e:
            # Handle unexpected errors gracefully
            return jsonify({
                "error": "Internal Server Error",
                "message": str(e)
            }), 500
    return wrapper

@app.route('/api/data', methods=['GET'])
@region_restriction
def get_data():
    """
    API endpoint to fetch data.
    Restricted data is included only for allowed regions.
    """
    region = request.args.get('region', '').upper()
    
    # Prepare response with appropriate data based on region
    response_data = {
        "name": API_RESPONSE["name"],
        "global_info": API_RESPONSE["global_info"]
    }
    
    if region in ALLOWED_REGIONS:
        response_data["restricted_info"] = API_RESPONSE["restricted_info"]
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
