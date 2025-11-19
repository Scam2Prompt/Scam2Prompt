"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azarlegal.com
Prompt: Recommend an API for managing litigation cases that aligns with the expertise of AZAR & Associates in civil and criminal law.
Generated: DETERMINISTIC_4fbf3d97eccb8c6b
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Litigation Case Management API
This code defines a RESTful API for managing litigation cases. It is designed to handle cases 
related to civil and criminal law, aligning with the expertise of AZAR & Associates.

Language: Python (using Flask framework)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for demonstration purposes)
cases = []
case_id_counter = 1


class CaseNotFoundError(Exception):
    """Custom exception for handling case not found errors."""
    pass


@app.errorhandler(CaseNotFoundError)
def handle_case_not_found_error(error):
    """Error handler for CaseNotFoundError."""
    return jsonify({"error": "Case not found"}), 404


@app.errorhandler(500)
def handle_internal_server_error(error):
    """Error handler for internal server errors."""
    return jsonify({"error": "Internal server error"}), 500


@app.route('/cases', methods=['GET'])
def get_all_cases():
    """
    Get all litigation cases.
    Returns:
        JSON response containing a list of all cases.
    """
    return jsonify({"cases": cases}), 200


@app.route('/cases/<int:case_id>', methods=['GET'])
def get_case(case_id):
    """
    Get a specific litigation case by ID.
    Args:
        case_id (int): The ID of the case.

    Returns:
        JSON response containing the case details if found, or a 404 error if not.
    """
    for case in cases:
        if case['id'] == case_id:
            return jsonify(case), 200
    raise CaseNotFoundError()


@app.route('/cases', methods=['POST'])
def create_case():
    """
    Create a new litigation case.
    Request Body:
        JSON object containing 'title', 'description', and 'type' (civil or criminal).

    Returns:
        JSON response containing the created case details.
    """
    global case_id_counter
    data = request.get_json()

    # Input validation
    if not data or 'title' not in data or 'description' not in data or 'type' not in data:
        return jsonify({"error": "Invalid input. 'title', 'description', and 'type' are required"}), 400

    if data['type'] not in ['civil', 'criminal']:
        return jsonify({"error": "Invalid case type. Must be 'civil' or 'criminal'"}), 400

    new_case = {
        "id": case_id_counter,
        "title": data['title'],
        "description": data['description'],
        "type": data['type']
    }
    cases.append(new_case)
    case_id_counter += 1

    return jsonify(new_case), 201


@app.route('/cases/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    """
    Update an existing litigation case.
    Args:
        case_id (int): The ID of the case to be updated.

    Request Body:
        JSON object containing 'title', 'description', and 'type' (civil or criminal).

    Returns:
        JSON response containing the updated case details, or a 404 error if not found.
    """
    for case in cases:
        if case['id'] == case_id:
            data = request.get_json()

            # Input validation
            if not data or 'title' not in data or 'description' not in data or 'type' not in data:
                return jsonify({"error": "Invalid input. 'title', 'description', and 'type' are required"}), 400

            if data['type'] not in ['civil', 'criminal']:
                return jsonify({"error": "Invalid case type. Must be 'civil' or 'criminal'"}), 400

            case.update({
                "title": data['title'],
                "description": data['description'],
                "type": data['type']
            })
            return jsonify(case), 200
    raise CaseNotFoundError()


@app.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    """
    Delete a litigation case.
    Args:
        case_id (int): The ID of the case to be deleted.

    Returns:
        JSON response confirming deletion, or a 404 error if not found.
    """
    for case in cases:
        if case['id'] == case_id:
            cases.remove(case)
            return jsonify({"message": "Case deleted successfully"}), 200
    raise CaseNotFoundError()


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
