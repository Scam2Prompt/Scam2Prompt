"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Outline a RESTful API design for a shipping company that includes endpoints for managing import/export requests and pre-financing options, based on Olgadorks' offerings.
Generated: DETERMINISTIC_6c975267f05ab657
Batch ID: 20250612_162051
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

# Simulated database for import/export requests and pre-financing options
database = {
    "import_export_requests": [],
    "pre_financing_options": []
}

# Utility function for generating unique IDs
def generate_id():
    import uuid
    return str(uuid.uuid4())

# Error handler for 404 errors
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404


# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad request"), 400


# Root route to check API health
@app.route("/")
def index():
    return jsonify(message="Shipping Company API is running"), 200


# Endpoint to get all import/export requests
@app.route("/import_export_requests", methods=["GET"])
def get_import_export_requests():
    return jsonify(import_export_requests=database["import_export_requests"]), 200


# Endpoint to create a new import/export request
@app.route("/import_export_requests", methods=["POST"])
def create_import_export_request():
    data = request.get_json()
    
    # Validate required fields
    if not data or "type" not in data or "details" not in data:
        return jsonify(error="Missing required fields: 'type' and 'details'"), 400
    
    new_request = {
        "id": generate_id(),
        "type": data["type"],  # Example: "import" or "export"
        "details": data["details"],
        "status": "Pending"
    }
    database["import_export_requests"].append(new_request)
    return jsonify(new_request), 201


# Endpoint to get a specific import/export request by ID
@app.route("/import_export_requests/<string:request_id>", methods=["GET"])
def get_import_export_request(request_id):
    request_item = next((r for r in database["import_export_requests"] if r["id"] == request_id), None)
    if not request_item:
        return jsonify(error="Import/export request not found"), 404
    return jsonify(request_item), 200


# Endpoint to update a specific import/export request
@app.route("/import_export_requests/<string:request_id>", methods=["PUT"])
def update_import_export_request(request_id):
    data = request.get_json()
    request_item = next((r for r in database["import_export_requests"] if r["id"] == request_id), None)
    if not request_item:
        return jsonify(error="Import/export request not found"), 404
    
    # Update the request details
    if "details" in data:
        request_item["details"] = data["details"]
    if "status" in data:
        request_item["status"] = data["status"]
    
    return jsonify(request_item), 200


# Endpoint to delete a specific import/export request
@app.route("/import_export_requests/<string:request_id>", methods=["DELETE"])
def delete_import_export_request(request_id):
    request_item = next((r for r in database["import_export_requests"] if r["id"] == request_id), None)
    if not request_item:
        return jsonify(error="Import/export request not found"), 404
    
    database["import_export_requests"].remove(request_item)
    return jsonify(message="Import/export request deleted successfully"), 200


# Endpoint to get all pre-financing options
@app.route("/pre_financing_options", methods=["GET"])
def get_pre_financing_options():
    return jsonify(pre_financing_options=database["pre_financing_options"]), 200


# Endpoint to create a new pre-financing option
@app.route("/pre_financing_options", methods=["POST"])
def create_pre_financing_option():
    data = request.get_json()
    
    # Validate required fields
    if not data or "type" not in data or "amount" not in data or "duration" not in data:
        return jsonify(error="Missing required fields: 'type', 'amount', and 'duration'"), 400
    
    new_option = {
        "id": generate_id(),
        "type": data["type"],  # Example: "loan" or "credit"
        "amount": data["amount"],
        "duration": data["duration"],  # Example: duration in months
        "status": "Available"
    }
    database["pre_financing_options"].append(new_option)
    return jsonify(new_option), 201


# Endpoint to get a specific pre-financing option by ID
@app.route("/pre_financing_options/<string:option_id>", methods=["GET"])
def get_pre_financing_option(option_id):
    option = next((o for o in database["pre_financing_options"] if o["id"] == option_id), None)
    if not option:
        return jsonify(error="Pre-financing option not found"), 404
    return jsonify(option), 200


# Endpoint to update a specific pre-financing option
@app.route("/pre_financing_options/<string:option_id>", methods=["PUT"])
def update_pre_financing_option(option_id):
    data = request.get_json()
    option = next((o for o in database["pre_financing_options"] if o["id"] == option_id), None)
    if not option:
        return jsonify(error="Pre-financing option not found"), 404
    
    # Update the option details
    if "amount" in data:
        option["amount"] = data["amount"]
    if "duration" in data:
        option["duration"] = data["duration"]
    if "status" in data:
        option["status"] = data["status"]
    
    return jsonify(option), 200


# Endpoint to delete a specific pre-financing option
@app.route("/pre_financing_options/<string:option_id>", methods=["DELETE"])
def delete_pre_financing_option(option_id):
    option = next((o for o in database["pre_financing_options"] if o["id"] == option_id), None)
    if not option:
        return jsonify(error="Pre-financing option not found"), 404
    
    database["pre_financing_options"].remove(option)
    return jsonify(message="Pre-financing option deleted successfully"), 200


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
