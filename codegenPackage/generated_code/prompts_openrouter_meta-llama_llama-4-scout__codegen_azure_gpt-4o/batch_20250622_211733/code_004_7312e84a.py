"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Generate a sample script for a chatbot that can be integrated into the Sardagna Poeta Advogados website to provide basic legal information and direct clients to relevant areas of the firm's services.
Generated: DETERMINISTIC_7312e84ab950e2e6
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample legal information database
LEGAL_INFO = {
    "corporate law": "Corporate law deals with the formation, operation, and dissolution of corporations.",
    "family law": "Family law covers matters such as divorce, child custody, and adoption.",
    "tax law": "Tax law involves regulations related to taxation and compliance.",
    "real estate law": "Real estate law governs property transactions, leases, and disputes.",
    "employment law": "Employment law addresses workplace rights, contracts, and disputes."
}

# Firm services mapping
FIRM_SERVICES = {
    "corporate law": "/services/corporate-law",
    "family law": "/services/family-law",
    "tax law": "/services/tax-law",
    "real estate law": "/services/real-estate-law",
    "employment law": "/services/employment-law"
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint for chatbot interaction.
    Expects a JSON payload with a 'message' field containing the user's query.
    """
    try:
        # Parse the incoming request
        data = request.get_json()
        user_message = data.get('message', '').lower()

        if not user_message:
            return jsonify({"error": "Message field is required."}), 400

        # Search for relevant legal information
        response = {}
        for key in LEGAL_INFO:
            if key in user_message:
                response['info'] = LEGAL_INFO[key]
                response['service_link'] = FIRM_SERVICES[key]
                break

        # If no match is found, provide a generic response
        if not response:
            response['info'] = "I'm sorry, I couldn't find information related to your query. Please visit our website for more details."
            response['service_link'] = "/services"

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
