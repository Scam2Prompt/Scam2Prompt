"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Create an API endpoint for Jiomart Digital that handles product returns and refunds, including tracking the status of the return process.
Generated: DETERMINISTIC_32211ef15a306b3a
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory storage for demonstration purposes
returns_db = {}

# Possible statuses for a return/refund
RETURN_STATUSES = ['Initiated', 'In Progress', 'Completed', 'Rejected']

@app.route('/product-return', methods=['POST'])
def initiate_product_return():
    """
    Endpoint to initiate a product return/refund process.
    Expects parameters: product_id, user_id, reason
    """
    try:
        data = request.json
        product_id = data.get('product_id')
        user_id = data.get('user_id')
        reason = data.get('reason')

        # Validate input
        if not product_id or not user_id or not reason:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a unique return ID
        return_id = str(uuid.uuid4())

        # Create a return entry
        return_entry = {
            "return_id": return_id,
            "product_id": product_id,
            "user_id": user_id,
            "reason": reason,
            "status": "Initiated",
            "created_at": datetime.utcnow().isoformat()
        }

        # Store the return entry
        returns_db[return_id] = return_entry

        return jsonify({"message": "Return initiated successfully", "return_id": return_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/product-return/<return_id>', methods=['GET'])
def get_return_status(return_id):
    """
    Endpoint to track the status of a product return/refund process.
    Expects: return_id in the URL path.
    """
    try:
        # Lookup the return entry
        return_entry = returns_db.get(return_id)

        if not return_entry:
            return jsonify({"error": "Return ID not found"}), 404

        return jsonify({"return_id": return_id, "status": return_entry["status"], "details": return_entry}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/product-return/<return_id>', methods=['PATCH'])
def update_return_status(return_id):
    """
    Endpoint to update the status of a product return/refund process.
    Expects: return_id in the URL path, and new_status in the request body.
    """
    try:
        data = request.json
        new_status = data.get('new_status')

        # Validate input
        if new_status not in RETURN_STATUSES:
            return jsonify({"error": f"Invalid status. Valid statuses are: {', '.join(RETURN_STATUSES)}"}), 400

        # Lookup the return entry
        return_entry = returns_db.get(return_id)

        if not return_entry:
            return jsonify({"error": "Return ID not found"}), 404

        # Update the status
        return_entry["status"] = new_status
        return_entry["updated_at"] = datetime.utcnow().isoformat()

        return jsonify({"message": "Return status updated successfully", "return_id": return_id, "new_status": new_status}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/product-return/<return_id>', methods=['DELETE'])
def cancel_product_return(return_id):
    """
    Endpoint to cancel a product return/refund process.
    Expects: return_id in the URL path.
    """
    try:
        # Lookup the return entry
        return_entry = returns_db.get(return_id)

        if not return_entry:
            return jsonify({"error": "Return ID not found"}), 404

        # Remove the return entry from the database
        del returns_db[return_id]

        return jsonify({"message": "Return canceled successfully", "return_id": return_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
