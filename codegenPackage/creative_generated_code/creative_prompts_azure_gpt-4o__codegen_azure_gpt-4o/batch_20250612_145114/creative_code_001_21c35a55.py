"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Develop a web application using Flask that allows users to request roofing estimates, incorporating King Roofing's specific services like skylight installation and SWR underlayments.
Generated: DETERMINISTIC_21c35a55e56de578
Batch ID: 20250612_145114
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

# Sample services offered by King Roofing
SERVICES = {
    "roof_replacement": 5000,
    "skylight_installation": 1500,
    "SWR_underlayment": 800,
    "roof_inspection": 200
}

# Home route
@app.route("/")
def home():
    """
    Home page route. Provides a welcome message.
    """
    return "Welcome to King Roofing's Estimate Request Portal!"

# Route to list available services
@app.route("/services", methods=["GET"])
def list_services():
    """
    Endpoint to list all roofing services offered by King Roofing.
    """
    return jsonify({"services": SERVICES})

# Route to request an estimate
@app.route("/estimate", methods=["POST"])
def request_estimate():
    """
    Endpoint to request a roofing estimate based on selected services.
    Expects a JSON payload with a list of desired services.
    """
    try:
        # Retrieve the JSON payload from the request
        data = request.get_json()
        
        if not data or "services" not in data:
            return jsonify({"error": "Invalid request. 'services' field is required."}), 400
        
        selected_services = data["services"]
        if not isinstance(selected_services, list):
            return jsonify({"error": "'services' should be a list of service names."}), 400

        # Calculate the total estimate
        total_estimate = 0
        invalid_services = []

        for service in selected_services:
            if service in SERVICES:
                total_estimate += SERVICES[service]
            else:
                invalid_services.append(service)

        # Prepare the response
        response = {
            "selected_services": selected_services,
            "invalid_services": invalid_services,
            "total_estimate": total_estimate
        }

        return jsonify(response)

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Start the Flask application
if __name__ == "__main__":
    """
    Main entry point for the application.
    Runs the Flask development server.
    """
    app.run(debug=True)
```
