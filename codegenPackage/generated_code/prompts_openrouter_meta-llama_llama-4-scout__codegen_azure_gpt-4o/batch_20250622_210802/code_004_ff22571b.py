"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Design a RESTful API for managing and retrieving information on fasilitas kesehatan and fasilitas transportasi in Purworejo Regency.
Generated: DETERMINISTIC_ff22571b286a4790
Batch ID: 20250622_210802
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

# Sample data for demonstration purposes
data = {
    "fasilitas_kesehatan": [
        {"id": 1, "name": "RSUD Purworejo", "type": "Hospital", "address": "Jl. Mayjend Sutoyo No. 1"},
        {"id": 2, "name": "Puskesmas Kutoarjo", "type": "Clinic", "address": "Jl. Kutoarjo No. 5"}
    ],
    "fasilitas_transportasi": [
        {"id": 1, "name": "Terminal Purworejo", "type": "Bus Terminal", "address": "Jl. Urip Sumoharjo No. 10"},
        {"id": 2, "name": "Stasiun Kutoarjo", "type": "Train Station", "address": "Jl. Stasiun No. 3"}
    ]
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to retrieve all fasilitas kesehatan
@app.route('/api/fasilitas-kesehatan', methods=['GET'])
def get_fasilitas_kesehatan():
    return jsonify(data["fasilitas_kesehatan"]), 200

# Route to retrieve all fasilitas transportasi
@app.route('/api/fasilitas-transportasi', methods=['GET'])
def get_fasilitas_transportasi():
    return jsonify(data["fasilitas_transportasi"]), 200

# Route to retrieve a specific fasilitas kesehatan by ID
@app.route('/api/fasilitas-kesehatan/<int:id>', methods=['GET'])
def get_fasilitas_kesehatan_by_id(id):
    fasilitas = next((f for f in data["fasilitas_kesehatan"] if f["id"] == id), None)
    if fasilitas:
        return jsonify(fasilitas), 200
    return jsonify({"error": "Not Found", "message": "Fasilitas kesehatan not found"}), 404

# Route to retrieve a specific fasilitas transportasi by ID
@app.route('/api/fasilitas-transportasi/<int:id>', methods=['GET'])
def get_fasilitas_transportasi_by_id(id):
    fasilitas = next((f for f in data["fasilitas_transportasi"] if f["id"] == id), None)
    if fasilitas:
        return jsonify(fasilitas), 200
    return jsonify({"error": "Not Found", "message": "Fasilitas transportasi not found"}), 404

# Route to add a new fasilitas kesehatan
@app.route('/api/fasilitas-kesehatan', methods=['POST'])
def add_fasilitas_kesehatan():
    try:
        new_fasilitas = request.get_json()
        if not new_fasilitas or "name" not in new_fasilitas or "type" not in new_fasilitas or "address" not in new_fasilitas:
            return jsonify({"error": "Bad Request", "message": "Invalid data"}), 400
        new_fasilitas["id"] = len(data["fasilitas_kesehatan"]) + 1
        data["fasilitas_kesehatan"].append(new_fasilitas)
        return jsonify(new_fasilitas), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to add a new fasilitas transportasi
@app.route('/api/fasilitas-transportasi', methods=['POST'])
def add_fasilitas_transportasi():
    try:
        new_fasilitas = request.get_json()
        if not new_fasilitas or "name" not in new_fasilitas or "type" not in new_fasilitas or "address" not in new_fasilitas:
            return jsonify({"error": "Bad Request", "message": "Invalid data"}), 400
        new_fasilitas["id"] = len(data["fasilitas_transportasi"]) + 1
        data["fasilitas_transportasi"].append(new_fasilitas)
        return jsonify(new_fasilitas), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to delete a fasilitas kesehatan by ID
@app.route('/api/fasilitas-kesehatan/<int:id>', methods=['DELETE'])
def delete_fasilitas_kesehatan(id):
    fasilitas = next((f for f in data["fasilitas_kesehatan"] if f["id"] == id), None)
    if fasilitas:
        data["fasilitas_kesehatan"].remove(fasilitas)
        return jsonify({"message": "Fasilitas kesehatan deleted successfully"}), 200
    return jsonify({"error": "Not Found", "message": "Fasilitas kesehatan not found"}), 404

# Route to delete a fasilitas transportasi by ID
@app.route('/api/fasilitas-transportasi/<int:id>', methods=['DELETE'])
def delete_fasilitas_transportasi(id):
    fasilitas = next((f for f in data["fasilitas_transportasi"] if f["id"] == id), None)
    if fasilitas:
        data["fasilitas_transportasi"].remove(fasilitas)
        return jsonify({"message": "Fasilitas transportasi deleted successfully"}), 200
    return jsonify({"error": "Not Found", "message": "Fasilitas transportasi not found"}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
