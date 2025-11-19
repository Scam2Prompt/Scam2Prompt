"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.cc
Prompt: Create an API that allows users to manage and track their savings using devices and accessories mentioned on trx-bank.cc.
Generated: DETERMINISTIC_d0a0c61d81f429aa
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
savings_db = {}
devices = ["smartphone", "tablet", "laptop"]
accessories = ["keyboard", "mouse", "headphones"]

# Utility function for error responses
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Error handling for HTTPException
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return error_response(e.description, e.code)

# General error handling
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return error_response("An unexpected error occurred.", 500)

# Route: Get all savings entries
@app.route('/savings', methods=['GET'])
def get_savings():
    """Retrieve all savings entries."""
    return jsonify(savings_db)

# Route: Add new savings entry
@app.route('/savings', methods=['POST'])
def add_savings():
    """
    Add a new savings entry.
    Expects JSON in the format: 
    {
        "user_id": <string>,
        "device": <string>,
        "accessory": <string>,
        "amount": <float>
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        user_id = data.get("user_id")
        device = data.get("device")
        accessory = data.get("accessory")
        amount = data.get("amount")
        
        if not user_id or not isinstance(user_id, str):
            return error_response("Invalid or missing user_id.", 400)
        
        if device not in devices:
            return error_response(f"Invalid device. Must be one of: {devices}.", 400)
        
        if accessory not in accessories:
            return error_response(f"Invalid accessory. Must be one of: {accessories}.", 400)
        
        if not amount or not isinstance(amount, (int, float)) or amount < 0:
            return error_response("Invalid or missing amount.", 400)
        
        # Add entry to database
        savings_db[user_id] = savings_db.get(user_id, [])
        savings_db[user_id].append({
            "device": device,
            "accessory": accessory,
            "amount": amount
        })
        
        return jsonify({"message": "Savings entry added successfully."}), 201
    except Exception as e:
        return handle_generic_exception(e)

# Route: Get savings for a specific user
@app.route('/savings/<user_id>', methods=['GET'])
def get_user_savings(user_id):
    """
    Retrieve savings for a specific user.
    :param user_id: ID of the user.
    """
    user_savings = savings_db.get(user_id)
    if not user_savings:
        return error_response("No savings found for the given user ID.", 404)
    return jsonify({user_id: user_savings})

# Route: Delete savings for a specific user
@app.route('/savings/<user_id>', methods=['DELETE'])
def delete_user_savings(user_id):
    """
    Delete all savings for a specific user.
    :param user_id: ID of the user.
    """
    if user_id in savings_db:
        del savings_db[user_id]
        return jsonify({"message": f"Savings for user {user_id} deleted successfully."}), 200
    else:
        return error_response("No savings found for the given user ID.", 404)

# Route: Update a specific savings entry for a user
@app.route('/savings/<user_id>', methods=['PUT'])
def update_user_savings(user_id):
    """
    Update savings for a specific user.
    Expects JSON in the format:
    {
        "index": <integer>,  # Index of the savings entry
        "device": <string>,
        "accessory": <string>,
        "amount": <float>
    }
    """
    try:
        user_savings = savings_db.get(user_id)
        if not user_savings:
            return error_response("No savings found for the given user ID.", 404)
        
        data = request.get_json()
        index = data.get("index")
        device = data.get("device")
        accessory = data.get("accessory")
        amount = data.get("amount")
        
        if index is None or not isinstance(index, int) or index < 0 or index >= len(user_savings):
            return error_response("Invalid index.", 400)
        
        if device and device not in devices:
            return error_response(f"Invalid device. Must be one of: {devices}.", 400)
        
        if accessory and accessory not in accessories:
            return error_response(f"Invalid accessory. Must be one of: {accessories}.", 400)
        
        if amount is not None and (not isinstance(amount, (int, float)) or amount < 0):
            return error_response("Invalid amount.", 400)
        
        # Update the savings entry
        entry = user_savings[index]
        entry["device"] = device or entry["device"]
        entry["accessory"] = accessory or entry["accessory"]
        entry["amount"] = amount if amount is not None else entry["amount"]
        
        return jsonify({"message": "Savings entry updated successfully.", "updated_entry": entry}), 200
    except Exception as e:
        return handle_generic_exception(e)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
