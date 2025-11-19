"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Create Python code to automate the intake process for legal leads, ensuring thorough vetting and live transfer functionality, as described on ClaimLink Legal Solutions.
Generated: DETERMINISTIC_a74039a31115c1ed
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Any, Optional
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for leads (for demonstration purposes)
leads_db: Dict[str, Dict[str, Any]] = {}

# Define a Lead data structure
class Lead:
    def __init__(self, name: str, email: str, phone: str, case_details: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.case_details = case_details

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "case_details": self.case_details
        }

# Function to validate lead data
def validate_lead_data(data: Dict[str, Any]) -> Optional[str]:
    required_fields = ['name', 'email', 'phone', 'case_details']
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    return None

# Endpoint to intake a new lead
@app.route('/intake', methods=['POST'])
def intake_lead():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        # Validate lead data
        validation_error = validate_lead_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Create a new Lead instance
        lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            case_details=data['case_details']
        )

        # Store the lead in the in-memory database
        lead_id = str(len(leads_db) + 1)  # Simple ID generation
        leads_db[lead_id] = lead.to_dict()

        logging.info(f"Lead intake successful: {lead.to_dict()}")
        return jsonify({"message": "Lead intake successful", "lead_id": lead_id}), 201

    except Exception as e:
        logging.error(f"Error during lead intake: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Endpoint to transfer lead to a legal representative
@app.route('/transfer/<lead_id>', methods=['POST'])
def transfer_lead(lead_id: str):
    try:
        # Check if the lead exists
        lead = leads_db.get(lead_id)
        if not lead:
            return jsonify({"error": "Lead not found"}), 404

        # Simulate live transfer logic (e.g., notifying a legal representative)
        # In a real application, this would involve more complex logic
        logging.info(f"Transferring lead: {lead}")
        return jsonify({"message": "Lead transferred successfully", "lead": lead}), 200

    except Exception as e:
        logging.error(f"Error during lead transfer: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
