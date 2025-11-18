"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Suggest an API for integrating patient feedback collection into a medical clinic website, specifically for gathering opinions on services like endoscopia digestiva alta and pesquisa de intolerâncias alimentares.
Generated: DETERMINISTIC_a583750cf192f06b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for feedback (for production, use a database)
feedback_storage = []

# API Endpoint: Submit feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to collect patient feedback on medical services.
    Expects a JSON object with patient name, service name, and feedback message.
    """
    try:
        # Parse JSON request data
        data = request.json
        
        # Validate required fields
        if not data or 'patient_name' not in data or 'service_name' not in data or 'feedback_message' not in data:
            return jsonify({"error": "Missing required fields: patient_name, service_name, feedback_message"}), 400
        
        # Store feedback
        feedback = {
            "patient_name": data['patient_name'],
            "service_name": data['service_name'],
            "feedback_message": data['feedback_message']
        }
        feedback_storage.append(feedback)
        
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# API Endpoint: Retrieve feedback
@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all submitted feedback.
    """
    try:
        return jsonify({"feedback": feedback_storage}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while fetching feedback", "details": str(e)}), 500

# API Endpoint: Retrieve feedback for a specific service
@app.route('/api/feedback/<service_name>', methods=['GET'])
def get_feedback_for_service(service_name):
    """
    Endpoint to retrieve feedback for a specific service.
    """
    try:
        # Filter feedback by service name
        filtered_feedback = [fb for fb in feedback_storage if fb['service_name'].lower() == service_name.lower()]
        
        if not filtered_feedback:
            return jsonify({"message": f"No feedback found for service: {service_name}"}), 404
        
        return jsonify({"feedback": filtered_feedback}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while fetching feedback", "details": str(e)}), 500

# Run the Flask app (for development; use a production-ready WSGI server for production)
if __name__ == '__main__':
    app.run(debug=True)
```
