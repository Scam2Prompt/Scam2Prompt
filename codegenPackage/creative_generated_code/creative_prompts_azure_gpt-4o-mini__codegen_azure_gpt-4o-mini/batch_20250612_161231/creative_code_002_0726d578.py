"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afunabb.cl
Prompt: Create an API endpoint that retrieves information about labor rights and support services for non-academic staff at universities, inspired by the offerings of AFUNABB Chillán.
Generated: DETERMINISTIC_0726d578f95df28f
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross Origin Resource Sharing for all domains

# Sample data simulating a database for the API
LABOR_RIGHTS_DATA = {
    "labor_rights": [
        {
            "title": "Right to Fair Wages",
            "description": "All staff should receive fair compensation for their work.",
            "contact": "HR Department"
        },
        {
            "title": "Right to Safe Working Conditions",
            "description": "Staff are entitled to a safe and healthy work environment.",
            "contact": "Safety Office"
        }
    ],
    "support_services": [
        {
            "title": "Counseling Services",
            "description": "Free and confidential counseling for staff.",
            "contact": "Counseling Center"
        },
        {
            "title": "Legal Assistance",
            "description": "Access to legal advice and representation for employment disputes.",
            "contact": "Legal Aid Office"
        }
    ]
}

@app.route('/api/labor-rights', methods=['GET'])
def get_labor_rights():
    """
    Retrieve information about labor rights for non-academic staff.
    
    Returns:
        JSON: A JSON object containing labor rights information.
    """
    try:
        return jsonify(LABOR_RIGHTS_DATA["labor_rights"]), 200
    except Exception as e:
        # Log the error for debugging purposes (in a real app, use logging)
        print(f"Error retrieving labor rights: {e}")
        abort(500)  # Internal server error

@app.route('/api/support-services', methods=['GET'])
def get_support_services():
    """
    Retrieve information about support services for non-academic staff.
    
    Returns:
        JSON: A JSON object containing support services information.
    """
    try:
        return jsonify(LABOR_RIGHTS_DATA["support_services"]), 200
    except Exception as e:
        # Log the error for debugging purposes (in a real app, use logging)
        print(f"Error retrieving support services: {e}")
        abort(500)  # Internal server error

if __name__ == '__main__':
    # Run the app on the default Flask port
    app.run(host='0.0.0.0', port=5000)
```
