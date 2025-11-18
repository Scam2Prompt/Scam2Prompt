"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Write a Python script for a custom web development project using outsourcing services, referencing the programming expertise offered by Special One Outsourcing in Jordan.
Generated: DETERMINISTIC_a78814a43f843ff4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a custom web development project using outsourcing services.
It includes a basic API endpoint to interact with a service referencing Special One Outsourcing in Jordan.
The script uses Flask to create a web server.

Before running the script, ensure Flask is installed:
pip install Flask
"""

from flask import Flask, request, jsonify
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# A placeholder company and service information
OUTSOURCING_COMPANY = {
    "name": "Special One Outsourcing",
    "location": "Jordan",
    "services": [
        "Web Development",
        "Software Engineering",
        "Mobile Applications",
        "UI/UX Design",
        "Project Management"
    ]
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """Handle resource not found errors."""
    logging.error(f"Error 404: {error}")
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    logging.error(f"Error 500: {error}")
    return jsonify({"error": "Internal server error"}), 500

@app.route("/")
def home():
    """
    Home endpoint providing a brief welcome message.
    """
    logging.info("Accessed home endpoint")
    return jsonify({
        "message": "Welcome to Special One Outsourcing Services API!",
        "company_info": OUTSOURCING_COMPANY
    })

@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to retrieve the list of services offered by the outsourcing company.
    """
    logging.info("Accessing services endpoint")
    return jsonify({
        "company": OUTSOURCING_COMPANY["name"],
        "location": OUTSOURCING_COMPANY["location"],
        "services": OUTSOURCING_COMPANY["services"]
    })

@app.route("/contact", methods=["POST"])
def contact_us():
    """
    Endpoint to simulate sending inquiries or messages to the outsourcing company.
    Expects a JSON payload with 'name', 'email', and 'message'.
    """
    data = request.get_json()

    # Validate the input data
    if not data or not all(key in data for key in ("name", "email", "message")):
        logging.warning("Invalid input provided to the contact endpoint")
        return jsonify({"error": "Invalid input. Provide 'name', 'email', and 'message'."}), 400

    logging.info(f"Received contact message from {data['name']} ({data['email']}): {data['message']}")
    return jsonify({
        "message": "Your inquiry has been received. We will get back to you shortly!",
        "submitted_data": data
    })

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
