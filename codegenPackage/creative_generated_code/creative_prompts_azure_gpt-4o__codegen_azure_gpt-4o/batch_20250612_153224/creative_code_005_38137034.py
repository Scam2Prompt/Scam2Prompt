"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Design a REST API that enables manufacturers to submit inquiries to PRGMEA about sourcing processes and receive automated responses.
Generated: DETERMINISTIC_381370342eceab6b
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
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for automated responses
AUTOMATED_RESPONSES = {
    "fabric sourcing": "We provide assistance with fabric sourcing from trusted suppliers.",
    "pricing": "Please specify quantities and details for a custom pricing estimate.",
    "shipping processes": "Our shipping department offers global delivery services.",
    "minimum order quantities": "The minimum order quantity depends on the product requested. Contact us for details.",
}

@app.route('/api/inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint for manufacturers to submit inquiries.
    Accepts JSON payload with 'manufacturer_name', 'email', and 'query'.
    Example JSON payload:
        {
            "manufacturer_name": "ABC Textiles",
            "email": "contact@abc.com",
            "query": "fabric sourcing"
        }
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Request body must be JSON."}), 400

        # Validate required fields
        manufacturer_name = data.get("manufacturer_name")
        email = data.get("email")
        query = data.get("query")

        if not manufacturer_name or not email or not query:
            return jsonify({"error": "Missing required fields: 'manufacturer_name', 'email', 'query'"}), 400

        # Generate automated response based on the query
        response_message = AUTOMATED_RESPONSES.get(query.lower(), "Your query has been received. We will respond shortly.")
        
        # Log the inquiry
        logging.info(f"Inquiry received: Manufacturer: {manufacturer_name}, Email: {email}, Query: {query}")

        # Return response
        return jsonify({
            "manufacturer_name": manufacturer_name,
            "email": email,
            "query": query,
            "response": response_message
        }), 200

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error processing inquiry: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    """
    Handle 405 errors gracefully.
    """
    return jsonify({"error": "Method not allowed."}), 405

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```
