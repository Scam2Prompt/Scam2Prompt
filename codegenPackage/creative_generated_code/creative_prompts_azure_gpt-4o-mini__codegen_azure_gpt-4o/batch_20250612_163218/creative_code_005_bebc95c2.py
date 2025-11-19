"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxlogy.com
Prompt: Suggest an API that can be used for social media marketing automation, reflecting the diverse services of a leading digital marketing agency in Dhaka.
Generated: DETERMINISTIC_bebc95c27b2515fe
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging for debugging and production readiness
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Available services offered by the digital marketing agency
SERVICES = [
    {"id": 1, "name": "Content Creation", "description": "Professional content for posts, blogs, and ads."},
    {"id": 2, "name": "Social Media Management", "description": "Automation and performance tracking for social media accounts."},
    {"id": 3, "name": "SEO Optimization", "description": "Boost traffic and visibility with search engine optimization."},
    {"id": 4, "name": "PPC Campaigns", "description": "Targeted pay-per-click advertising strategies."},
    {"id": 5, "name": "Analytics and Reporting", "description": "Insightful metrics to optimize marketing strategies."},
]

# Error Messages
ERROR_MESSAGES = {
    "not_found": "The requested service was not found.",
    "invalid_request": "Invalid request. Please check your input.",
    "server_error": "An unexpected error occurred. Please try again later."
}

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all available marketing services.
    Example: GET /api/services
    """
    try:
        return jsonify({"success": True, "services": SERVICES}), 200
    except Exception as e:
        logging.error(f"Error fetching services: {str(e)}")
        return jsonify({"success": False, "message": ERROR_MESSAGES["server_error"]}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Endpoint to retrieve details of a specific service by ID.
    Example: GET /api/services/1
    """
    try:
        service = next((s for s in SERVICES if s["id"] == service_id), None)
        if service:
            return jsonify({"success": True, "service": service}), 200
        else:
            return jsonify({"success": False, "message": ERROR_MESSAGES["not_found"]}), 404
    except Exception as e:
        logging.error(f"Error fetching service by ID: {str(e)}")
        return jsonify({"success": False, "message": ERROR_MESSAGES["server_error"]}), 500

@app.route('/api/contact', methods=['POST'])
def contact_agency():
    """
    Endpoint to handle inquiries from clients.
    Example: POST /api/contact
    Payload: {"name": "John Doe", "email": "john@example.com", "message": "Interested in your PPC campaigns"}
    """
    try:
        data = request.get_json()

        # Validate request payload
        if not data or not all(k in data for k in ("name", "email", "message")):
            return jsonify({"success": False, "message": ERROR_MESSAGES["invalid_request"]}), 400

        # Simulate storing the contact inquiry (e.g., save to database or send email)
        logging.info(f"New inquiry received: {data}")

        return jsonify({"success": True, "message": "Thank you for reaching out! We will respond shortly."}), 200
    except Exception as e:
        logging.error(f"Error handling contact request: {str(e)}")
        return jsonify({"success": False, "message": ERROR_MESSAGES["server_error"]}), 500

# Run Flask app (use production-ready server like Gunicorn in deployment)
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
