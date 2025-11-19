"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Create an API endpoint that allows law firms to receive live-transferred leads, similar to the services offered by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7ed9477d62da31a8
Batch ID: 20250612_163546
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

# Set up logging to output errors and other relevant information
logging.basicConfig(level=logging.INFO)

# In-memory storage for leads (for demonstration purposes)
leads_storage = []

@app.route('/api/v1/leads', methods=['POST'])
def receive_lead():
    """
    API endpoint to receive live-transferred leads for law firms.
    Expects a JSON payload with lead details.
    """
    try:
        # Validate that JSON content is sent
        if not request.is_json:
            return jsonify({"error": "Invalid request. Expected JSON payload."}), 400
        
        # Parse JSON payload
        lead_data = request.get_json()

        # Required fields for a lead
        required_fields = ["name", "phone_number", "email", "case_type", "timestamp"]

        # Validate all required fields are present
        missing_fields = [field for field in required_fields if field not in lead_data]
        if missing_fields:
            return jsonify({"error": "Missing required fields.", "missing_fields": missing_fields}), 400

        # Validate phone number format (simple length check for demonstration)
        if len(lead_data["phone_number"]) < 10 or not lead_data["phone_number"].isdigit():
            return jsonify({"error": "Invalid phone number format."}), 400

        # Example: Verify email format using a basic check
        if "@" not in lead_data["email"]:
            return jsonify({"error": "Invalid email format."}), 400

        # Store the lead (in-memory for now, or integrate with a database in production)
        leads_storage.append(lead_data)

        # Log the received lead for auditing
        logging.info(f"New lead received: {lead_data}")

        return jsonify({"message": "Lead successfully received.", "data": lead_data}), 201
    
    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"Error receiving lead: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
```

To use this API, send a POST request to `/api/v1/leads` with a JSON payload containing the lead details. For production environments, ensure `debug=True` is turned off and integrate with a secure database instead of in-memory storage.
