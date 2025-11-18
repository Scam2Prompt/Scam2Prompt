"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Create a RESTful API in Flask to handle customer inquiries for machinery parts and technical assistance, referencing the brands and services offered by Track Diesel Peru.
Generated: DETERMINISTIC_d61c0f7cffc9c240
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for brands and services offered by Track Diesel Peru
BRANDS = ["Caterpillar", "Komatsu", "John Deere", "Hitachi"]
SERVICES = ["Machinery Parts", "Technical Assistance"]

# Mock storage for customer inquiries
customer_inquiries = []

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 Not Found errors."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors."""
    return jsonify({"error": "Internal server error"}), 500


@app.route("/brands", methods=["GET"])
def get_brands():
    """
    Endpoint to retrieve the list of brands offered by Track Diesel Peru.
    :return: JSON response containing the list of brands.
    """
    return jsonify({"brands": BRANDS})


@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to retrieve the list of services offered by Track Diesel Peru.
    :return: JSON response containing the list of services.
    """
    return jsonify({"services": SERVICES})


@app.route("/inquiries", methods=["POST"])
def create_inquiry():
    """
    Endpoint to create a new customer inquiry.
    Expects JSON payload with 'name', 'email', 'brand', 'service', and 'message'.
    :return: JSON response with the created inquiry or error message.
    """
    try:
        data = request.get_json()

        # Validate input data
        name = data.get("name")
        email = data.get("email")
        brand = data.get("brand")
        service = data.get("service")
        message = data.get("message")

        if not name or not email or not brand or not service or not message:
            return jsonify({"error": "All fields are required"}), 400

        if brand not in BRANDS:
            return jsonify({"error": f"Brand '{brand}' not offered"}), 400

        if service not in SERVICES:
            return jsonify({"error": f"Service '{service}' not offered"}), 400

        # Create inquiry
        inquiry = {
            "id": len(customer_inquiries) + 1,
            "name": name,
            "email": email,
            "brand": brand,
            "service": service,
            "message": message,
        }
        customer_inquiries.append(inquiry)

        return jsonify({"message": "Inquiry created successfully", "inquiry": inquiry}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/inquiries", methods=["GET"])
def get_inquiries():
    """
    Endpoint to retrieve all customer inquiries.
    :return: JSON response containing the list of inquiries.
    """
    return jsonify({"inquiries": customer_inquiries})


if __name__ == "__main__":
    # Running the Flask app
    app.run(debug=True)
```
