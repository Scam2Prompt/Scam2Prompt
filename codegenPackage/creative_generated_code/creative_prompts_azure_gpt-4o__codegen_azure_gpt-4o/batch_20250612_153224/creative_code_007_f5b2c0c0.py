"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.greenaapples.com
Prompt: Suggest an API for implementing a virtual consultation system that provides advice on therapies like "De-addiction Therapy," "Anger Management," and "Anxiety Management," based on the Green Apples e-Rx Clinic's services.
Generated: DETERMINISTIC_f5b2c0c032ab8cca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing available therapies at Green Apples e-Rx Clinic
THERAPIES = {
    "de-addiction": "De-addiction Therapy helps individuals overcome substance dependence through counseling and behavioral techniques.",
    "anger-management": "Anger Management Therapy focuses on identifying triggers and learning strategies to manage anger constructively.",
    "anxiety-management": "Anxiety Management Therapy provides tools like cognitive behavioral therapy to address anxiety symptoms effectively."
}

@app.route('/api/consultation', methods=['POST'])
def virtual_consultation():
    """
    Endpoint to provide virtual consultation based on the requested therapy type.

    Request format (JSON):
    {
        "therapy_type": "de-addiction" // Supported values: 'de-addiction', 'anger-management', 'anxiety-management'
    }

    Response format (JSON):
    {
        "success": true,
        "therapy_description": "Description of the requested therapy"
    }
    """
    try:
        # Parse the JSON request
        data = request.get_json()
        if not data or 'therapy_type' not in data:
            return jsonify({"success": False, "message": "Invalid request. Please specify 'therapy_type' in JSON format."}), 400
        
        therapy_type = data['therapy_type'].strip().lower()
        
        # Validate the therapy type and provide information
        if therapy_type in THERAPIES:
            return jsonify({
                "success": True,
                "therapy_description": THERAPIES[therapy_type]
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": f"Therapy type '{therapy_type}' is not supported. Available options are: {', '.join(THERAPIES.keys())}."
            }), 400
    except Exception as e:
        # Catch unexpected errors and log them (log statement omitted for simplicity)
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500

@app.route('/api/therapies', methods=['GET'])
def list_therapies():
    """
    Endpoint to list all available therapy types.

    Response format (JSON):
    {
        "success": true,
        "available_therapies": {
            "de-addiction": "Description",
            "anger-management": "Description",
            "anxiety-management": "Description"
        }
    }
    """
    try:
        return jsonify({
            "success": True,
            "available_therapies": THERAPIES
        }), 200
    except Exception as e:
        # Catch unexpected errors and log them
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    # Start the server on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```
