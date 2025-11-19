"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Generate a code snippet for a tenant smart app that includes features like digital rent payment and faster complaint resolution, as described on the Moms PG website.
Generated: DETERMINISTIC_d66b08bf6216fe4d
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from typing import List, Dict

app = Flask(__name__)

# In-memory storage for tenants and complaints (for demonstration purposes)
tenants = {}
complaints = {}

@app.route('/api/tenants', methods=['POST'])
def register_tenant():
    """
    Register a new tenant with their details.
    Expected JSON payload:
    {
        "name": "Tenant Name",
        "email": "tenant@example.com",
        "apartment_number": "101"
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["name", "email", "apartment_number"]):
            raise BadRequest("Missing required tenant information.")

        tenant_id = str(len(tenants) + 1)
        tenants[tenant_id] = {
            "name": data["name"],
            "email": data["email"],
            "apartment_number": data["apartment_number"],
            "rent_paid": False
        }
        return jsonify({"tenant_id": tenant_id}), 201

    except BadRequest as err:
        return jsonify({"error": str(err)}), 400

@app.route('/api/rent/<tenant_id>', methods=['POST'])
def pay_rent(tenant_id):
    """
    Process rent payment for a tenant.
    Expected JSON payload:
    {
        "amount": 1000
    }
    """
    try:
        if tenant_id not in tenants:
            raise NotFound("Tenant not found.")

        data = request.get_json()
        if not data or "amount" not in data:
            raise BadRequest("Amount is required for payment.")

        tenants[tenant_id]['rent_paid'] = True  # Simulate rent payment
        return jsonify({"message": "Rent payment successful."}), 200

    except (BadRequest, NotFound) as err:
        return jsonify({"error": str(err)}), err.code

@app.route('/api/complaints', methods=['POST'])
def create_complaint():
    """
    Create a new complaint.
    Expected JSON payload:
    {
        "tenant_id": "1",
        "description": "Description of the complaint."
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["tenant_id", "description"]):
            raise BadRequest("Missing required complaint information.")

        if data['tenant_id'] not in tenants:
            raise NotFound("Tenant not found.")

        complaint_id = str(len(complaints) + 1)
        complaints[complaint_id] = {
            "tenant_id": data["tenant_id"],
            "description": data["description"],
            "timestamp": datetime.now().isoformat(),
            "status": "Pending"
        }
        return jsonify({"complaint_id": complaint_id}), 201

    except (BadRequest, NotFound) as err:
        return jsonify({"error": str(err)}), err.code

@app.route('/api/complaints/<complaint_id>', methods=['GET'])
def resolve_complaint(complaint_id):
    """
    Resolve a specific complaint by complaint ID.
    """
    try:
        if complaint_id not in complaints:
            raise NotFound("Complaint not found.")

        # Simulate complaint resolution
        complaints[complaint_id]['status'] = "Resolved"
        return jsonify({"message": "Complaint resolved successfully."}), 200

    except NotFound as err:
        return jsonify({"error": str(err)}), 404

if __name__ == '__main__':
    app.run(debug=False)
```
