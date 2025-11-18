"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Develop a REST API for SKI Foundation's "Kerjasama Pendampingan Bisnis kepada Pelaku UMKM" program, allowing partners to submit business plans and track their implementation progress.
Generated: DETERMINISTIC_1f7dbdb0f82f46e9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# Mock database
business_plans = {}

# Helper function for error responses
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Endpoint: Submit a business plan
@app.route('/api/business-plans', methods=['POST'])
def submit_business_plan():
    """
    Submit a business plan.
    Request Body:
        - partner_name (str): Name of the partner.
        - business_name (str): Name of the business/UMKM.
        - plan_description (str): Detailed description of the business plan.
    Returns:
        - success message with unique ID.
    """
    try:
        data = request.json
        # Validate request data
        if not data or 'partner_name' not in data or 'business_name' not in data or 'plan_description' not in data:
            return error_response("Missing required fields: partner_name, business_name, plan_description", 400)
        
        # Generate unique ID for the business plan
        plan_id = str(uuid.uuid4())
        business_plans[plan_id] = {
            "partner_name": data['partner_name'],
            "business_name": data['business_name'],
            "plan_description": data['plan_description'],
            "status": "Submitted",  # Default status
            "progress_updates": []  # Empty progress updates
        }

        return jsonify({"message": "Business plan submitted successfully!", "plan_id": plan_id}), 201
    except Exception as ex:
        return error_response(f"An error occurred: {str(ex)}", 500)

# Endpoint: Track implementation progress
@app.route('/api/business-plans/<plan_id>', methods=['GET'])
def track_progress(plan_id):
    """
    Track the progress of a business plan.
    Path Parameter:
        - plan_id (str): Unique ID of the business plan.
    Returns:
        - Business plan details and progress updates.
    """
    try:
        # Retrieve business plan by ID
        plan = business_plans.get(plan_id)
        if not plan:
            return error_response("Business plan not found.", 404)

        return jsonify(plan), 200
    except Exception as ex:
        return error_response(f"An error occurred: {str(ex)}", 500)

# Endpoint: Add progress update to a business plan
@app.route('/api/business-plans/<plan_id>/progress', methods=['POST'])
def add_progress_update(plan_id):
    """
    Add a progress update to a business plan.
    Path Parameter:
        - plan_id (str): Unique ID of the business plan.
    Request Body:
        - update (str): Description of the progress update.
    Returns:
        - Updated progress of the business plan.
    """
    try:
        data = request.json
        # Validate request data
        if not data or 'update' not in data:
            return error_response("Missing required field: update", 400)

        # Retrieve business plan by ID
        plan = business_plans.get(plan_id)
        if not plan:
            return error_response("Business plan not found.", 404)

        # Add progress update
        plan['progress_updates'].append(data['update'])

        return jsonify({"message": "Progress update added successfully!", "progress_updates": plan['progress_updates']}), 200
    except Exception as ex:
        return error_response(f"An error occurred: {str(ex)}", 500)

# Global error handler
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    """
    Handles HTTP exceptions globally.
    """
    return error_response(error.description, error.code)

@app.errorhandler(Exception)
def handle_generic_exception(error):
    """
    Handles generic exceptions globally.
    """
    return error_response(str(error), 500)

if __name__ == '__main__':
    # Production-ready app can be run using a WSGI server like gunicorn
    app.run(debug=True)
```
