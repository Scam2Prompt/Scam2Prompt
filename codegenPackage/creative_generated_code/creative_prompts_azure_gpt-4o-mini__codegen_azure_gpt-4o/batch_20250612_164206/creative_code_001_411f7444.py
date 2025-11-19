"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: How can I implement an API to manage the accreditation documents for water and gas meter verification services mentioned on the site?
Generated: DETERMINISTIC_411f7444669a5bcd
Batch ID: 20250612_164206
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

app = Flask(__name__)

# In-memory "database" to store accreditation documents
documents_db = {}

# Helper function to validate document data
def validate_document_data(data):
    required_fields = ["title", "description", "file_url", "verification_date"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/documents', methods=['POST'])
def create_document():
    """
    API Endpoint to create a new accreditation document.
    Expects JSON payload with title, description, file_url, and verification_date.
    """
    try:
        data = request.json
        valid, error_message = validate_document_data(data)
        if not valid:
            return jsonify({"error": error_message}), 400

        # Generate unique ID for the document
        document_id = str(uuid.uuid4())
        document = {
            "id": document_id,
            "title": data["title"],
            "description": data["description"],
            "file_url": data["file_url"],
            "verification_date": data["verification_date"],
        }
        documents_db[document_id] = document

        return jsonify({"message": "Document created successfully.", "document": document}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/documents/<document_id>', methods=['GET'])
def get_document(document_id):
    """
    API Endpoint to retrieve a specific accreditation document by ID.
    """
    try:
        document = documents_db.get(document_id)
        if not document:
            return jsonify({"error": "Document not found."}), 404
        
        return jsonify({"document": document}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/documents/<document_id>', methods=['PUT'])
def update_document(document_id):
    """
    API Endpoint to update an existing accreditation document by ID.
    Expects JSON payload with any of the fields: title, description, file_url, verification_date.
    """
    try:
        document = documents_db.get(document_id)
        if not document:
            return jsonify({"error": "Document not found."}), 404

        data = request.json
        document.update({key: value for key, value in data.items() if key in document})
        documents_db[document_id] = document

        return jsonify({"message": "Document updated successfully.", "document": document}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/documents/<document_id>', methods=['DELETE'])
def delete_document(document_id):
    """
    API Endpoint to delete an accreditation document by ID.
    """
    try:
        if document_id not in documents_db:
            return jsonify({"error": "Document not found."}), 404

        del documents_db[document_id]

        return jsonify({"message": "Document deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/documents', methods=['GET'])
def list_documents():
    """
    API Endpoint to list all accreditation documents.
    """
    try:
        return jsonify({"documents": list(documents_db.values())}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
