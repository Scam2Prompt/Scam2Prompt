"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Write a RESTful API endpoint that allows users to submit feedback on HVAC services, ensuring it captures details about the service quality and technician performance as highlighted by RJW Mechanical.
Generated: DETERMINISTIC_442dd3dd65b253c5
Batch ID: 20250612_163935
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

app = Flask(__name__)

# Sample structure for feedback storage (could be replaced with a real database in production)
feedback_store = []

# Exception handler for better error responses
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "success": False,
        "error": str(e)
    }
    if isinstance(e, HTTPException):
        response["status_code"] = e.code
    else:
        response["status_code"] = 500
    return jsonify(response), response["status_code"]

# Route to submit feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback about HVAC services.
    Expects a JSON payload with the following structure:
    {
        "service_quality": int,  # Rating from 1-5
        "technician_performance": int,  # Rating from 1-5
        "comments": str,  # Optional free-text feedback
        "customer_name": str  # Optional name of the customer
    }
    """
    try:
        # Parse JSON payload
        feedback_data = request.get_json()
        if not feedback_data:
            return jsonify({
                "success": False,
                "message": "Invalid request body. Expected JSON payload."
            }), 400

        # Validate required fields
        service_quality = feedback_data.get('service_quality')
        technician_performance = feedback_data.get('technician_performance')
        comments = feedback_data.get('comments', '')
        customer_name = feedback_data.get('customer_name', 'Anonymous')

        if service_quality is None or technician_performance is None:
            return jsonify({
                "success": False,
                "message": "Fields 'service_quality' and 'technician_performance' are required."
            }), 400
        if not (1 <= service_quality <= 5):
            return jsonify({
                "success": False,
                "message": "'service_quality' must be an integer between 1 and 5."
            }), 400
        if not (1 <= technician_performance <= 5):
            return jsonify({
                "success": False,
                "message": "'technician_performance' must be an integer between 1 and 5."
            }), 400

        # Save feedback (replace with database logic in production)
        feedback_store.append({
            "service_quality": service_quality,
            "technician_performance": technician_performance,
            "comments": comments,
            "customer_name": customer_name
        })

        return jsonify({
            "success": True,
            "message": "Feedback submitted successfully."
        }), 201
    except Exception as e:
        return handle_exception(e)

# Route to retrieve all feedbacks (for demonstration purposes)
@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    Returns a list of feedback entries.
    """
    return jsonify({
        "success": True,
        "feedbacks": feedback_store
    }), 200

if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```
