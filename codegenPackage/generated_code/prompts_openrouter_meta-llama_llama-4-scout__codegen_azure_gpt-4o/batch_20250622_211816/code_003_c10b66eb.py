"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Design an API for a property management system that integrates with financial planners, mortgage brokers, accountants, and solicitors, similar to Bebold Properties' network of trusted experts.
Generated: DETERMINISTIC_c10b66eb564f7240
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for storing expert information
experts_db = {
    "financial_planners": [],
    "mortgage_brokers": [],
    "accountants": [],
    "solicitors": []
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to get all experts by category
@app.route('/api/experts/<category>', methods=['GET'])
def get_experts(category):
    """
    Retrieve all experts in a given category.
    :param category: The category of experts (financial_planners, mortgage_brokers, accountants, solicitors)
    :return: JSON response with the list of experts
    """
    if category not in experts_db:
        return jsonify({"error": "Invalid category"}), 400
    return jsonify({"experts": experts_db[category]}), 200

# Route to add a new expert to a category
@app.route('/api/experts/<category>', methods=['POST'])
def add_expert(category):
    """
    Add a new expert to a given category.
    :param category: The category of experts (financial_planners, mortgage_brokers, accountants, solicitors)
    :return: JSON response with the status of the operation
    """
    if category not in experts_db:
        return jsonify({"error": "Invalid category"}), 400

    data = request.get_json()
    if not data or "name" not in data or "contact_info" not in data:
        return jsonify({"error": "Invalid input"}), 400

    expert = {
        "name": data["name"],
        "contact_info": data["contact_info"]
    }
    experts_db[category].append(expert)
    return jsonify({"message": "Expert added successfully"}), 201

# Route to delete an expert from a category
@app.route('/api/experts/<category>/<expert_name>', methods=['DELETE'])
def delete_expert(category, expert_name):
    """
    Delete an expert from a given category.
    :param category: The category of experts (financial_planners, mortgage_brokers, accountants, solicitors)
    :param expert_name: The name of the expert to delete
    :return: JSON response with the status of the operation
    """
    if category not in experts_db:
        return jsonify({"error": "Invalid category"}), 400

    experts = experts_db[category]
    for expert in experts:
        if expert["name"] == expert_name:
            experts.remove(expert)
            return jsonify({"message": "Expert deleted successfully"}), 200

    return jsonify({"error": "Expert not found"}), 404

# Route to update an expert's information
@app.route('/api/experts/<category>/<expert_name>', methods=['PUT'])
def update_expert(category, expert_name):
    """
    Update an expert's information in a given category.
    :param category: The category of experts (financial_planners, mortgage_brokers, accountants, solicitors)
    :param expert_name: The name of the expert to update
    :return: JSON response with the status of the operation
    """
    if category not in experts_db:
        return jsonify({"error": "Invalid category"}), 400

    data = request.get_json()
    if not data or "name" not in data or "contact_info" not in data:
        return jsonify({"error": "Invalid input"}), 400

    experts = experts_db[category]
    for expert in experts:
        if expert["name"] == expert_name:
            expert["name"] = data["name"]
            expert["contact_info"] = data["contact_info"]
            return jsonify({"message": "Expert updated successfully"}), 200

    return jsonify({"error": "Expert not found"}), 404

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    :return: JSON response with the status of the API
    """
    return jsonify({"status": "API is running"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
