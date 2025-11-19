"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Create an API recommendation for a legal consultation service that aligns with the ethical standards and client dedication highlighted on the CAAG website.
Generated: DETERMINISTIC_040ac18971345389
Batch ID: 20250612_162051
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

# In-memory data store for simplicity (use a database in production)
consultations = []

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP-specific exceptions."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "message": e.description
        }
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle generic exceptions."""
    return jsonify({
        "error": {
            "code": 500,
            "message": "An unexpected error occurred."
        }
    }), 500

@app.route("/api/v1/consultations", methods=["POST"])
def create_consultation():
    """
    Create a new legal consultation request.
    Endpoint: POST /api/v1/consultations
    Request Body:
        {
            "name": "Client Name",
            "email": "Client Email",
            "issue": "Brief description of the legal issue"
        }
    Response:
        {
            "id": 1,
            "name": "Client Name",
            "email": "Client Email",
            "issue": "Brief description of the legal issue",
            "status": "Pending"
        }
    """
    try:
        data = request.json

        # Validate input
        if not data or not all(k in data for k in ("name", "email", "issue")):
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "Invalid input. 'name', 'email' and 'issue' are required."
                }
            }), 400

        # Create consultation
        consultation = {
            "id": len(consultations) + 1,
            "name": data["name"],
            "email": data["email"],
            "issue": data["issue"],
            "status": "Pending"  # Default status
        }
        consultations.append(consultation)
        return jsonify(consultation), 201
    except Exception as e:
        # Unexpected error
        return handle_generic_exception(e)

@app.route("/api/v1/consultations", methods=["GET"])
def list_consultations():
    """
    List all legal consultation requests.
    Endpoint: GET /api/v1/consultations
    Response:
        [
            {
                "id": 1,
                "name": "Client Name",
                "email": "Client Email",
                "issue": "Brief description of the legal issue",
                "status": "Pending"
            },
            ...
        ]
    """
    return jsonify(consultations), 200

@app.route("/api/v1/consultations/<int:consultation_id>", methods=["GET"])
def get_consultation(consultation_id):
    """
    Retrieve a specific legal consultation request by ID.
    Endpoint: GET /api/v1/consultations/<consultation_id>
    Response:
        {
            "id": 1,
            "name": "Client Name",
            "email": "Client Email",
            "issue": "Brief description of the legal issue",
            "status": "Pending"
        }
    """
    consultation = next((c for c in consultations if c["id"] == consultation_id), None)
    if not consultation:
        return jsonify({
            "error": {
                "code": 404,
                "message": "Consultation not found."
            }
        }), 404
    return jsonify(consultation), 200

@app.route("/api/v1/consultations/<int:consultation_id>", methods=["PUT"])
def update_consultation(consultation_id):
    """
    Update the status of a legal consultation request.
    Endpoint: PUT /api/v1/consultations/<consultation_id>
    Request Body:
        {
            "status": "Updated status"
        }
    Response:
        {
            "id": 1,
            "name": "Client Name",
            "email": "Client Email",
            "issue": "Brief description of the legal issue",
            "status": "Updated status"
        }
    """
    try:
        data = request.json

        # Validate input
        if not data or "status" not in data:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "Invalid input. 'status' is required."
                }
            }), 400

        consultation = next((c for c in consultations if c["id"] == consultation_id), None)
        if not consultation:
            return jsonify({
                "error": {
                    "code": 404,
                    "message": "Consultation not found."
                }
            }), 404

        # Update consultation status
        consultation["status"] = data["status"]
        return jsonify(consultation), 200
    except Exception as e:
        # Unexpected error
        return handle_generic_exception(e)

@app.route("/api/v1/consultations/<int:consultation_id>", methods=["DELETE"])
def delete_consultation(consultation_id):
    """
    Delete a legal consultation request.
    Endpoint: DELETE /api/v1/consultations/<consultation_id>
    Response:
        {
            "message": "Consultation deleted successfully."
        }
    """
    consultation = next((c for c in consultations if c["id"] == consultation_id), None)
    if not consultation:
        return jsonify({
            "error": {
                "code": 404,
                "message": "Consultation not found."
            }
        }), 404

    consultations.remove(consultation)
    return jsonify({
        "message": "Consultation deleted successfully."
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
```
