"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Create an API endpoint for submitting paving service requests, incorporating the unique two-step process mentioned on the Hyperswap Bedford Paving page.
Generated: DETERMINISTIC_cb8d9ef11e76a358
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for submissions
submissions = {}

# Step 1: Generate unique submission ID
@app.route('/paving-requests/step1', methods=['POST'])
def generate_submission_id():
    try:
        # Generate a unique ID for the request
        submission_id = str(uuid.uuid4())
        submissions[submission_id] = {"status": "Pending", "details": None}
        
        return jsonify({
            "success": True,
            "message": "Submission ID generated successfully.",
            "submission_id": submission_id
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to generate submission ID."
        }), 500

# Step 2: Submit service request details
@app.route('/paving-requests/step2/<submission_id>', methods=['POST'])
def submit_service_request(submission_id):
    try:
        # Ensure submission ID exists
        if submission_id not in submissions:
            return jsonify({
                "success": False,
                "message": "Invalid submission ID."
            }), 404
        
        # Get request data
        data = request.json
        if not data:
            return jsonify({
                "success": False,
                "message": "Request data is required."
            }), 400
        
        # Validate required fields
        required_fields = ['name', 'address', 'email', 'service_details']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "success": False,
                "message": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400
        
        # Update submission with details
        submissions[submission_id] = {
            "status": "Submitted",
            "details": data
        }
        
        return jsonify({
            "success": True,
            "message": "Service request submitted successfully.",
            "submission_id": submission_id,
            "submission_details": data
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to submit service request."
        }), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "success": True,
        "message": "API is running."
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
