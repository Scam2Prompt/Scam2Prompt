"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Create a RESTful API to manage enquiries for special effects services, similar to those offered by Agnelo SFX."
Generated: DETERMINISTIC_182383e9391ebcdb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for enquiries (for demonstration purposes)
enquiries = []
enquiry_id_counter = 1

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

# Route to get all enquiries
@app.route('/enquiries', methods=['GET'])
def get_enquiries():
    return jsonify(enquiries), 200

# Route to create a new enquiry
@app.route('/enquiries', methods=['POST'])
def create_enquiry():
    global enquiry_id_counter
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields: name, email, message"}), 400

    # Create new enquiry
    new_enquiry = {
        "id": enquiry_id_counter,
        "name": data['name'],
        "email": data['email'],
        "message": data['message']
    }
    enquiries.append(new_enquiry)
    enquiry_id_counter += 1

    return jsonify(new_enquiry), 201

# Route to get a specific enquiry by ID
@app.route('/enquiries/<int:enquiry_id>', methods=['GET'])
def get_enquiry(enquiry_id):
    enquiry = next((e for e in enquiries if e['id'] == enquiry_id), None)
    if not enquiry:
        return jsonify({"error": "Not Found", "message": f"Enquiry with ID {enquiry_id} not found"}), 404
    return jsonify(enquiry), 200

# Route to update an enquiry by ID
@app.route('/enquiries/<int:enquiry_id>', methods=['PUT'])
def update_enquiry(enquiry_id):
    data = request.get_json()
    enquiry = next((e for e in enquiries if e['id'] == enquiry_id), None)

    if not enquiry:
        return jsonify({"error": "Not Found", "message": f"Enquiry with ID {enquiry_id} not found"}), 404

    # Validate input
    if not data or 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields: name, email, message"}), 400

    # Update enquiry
    enquiry.update({
        "name": data['name'],
        "email": data['email'],
        "message": data['message']
    })

    return jsonify(enquiry), 200

# Route to delete an enquiry by ID
@app.route('/enquiries/<int:enquiry_id>', methods=['DELETE'])
def delete_enquiry(enquiry_id):
    global enquiries
    enquiry = next((e for e in enquiries if e['id'] == enquiry_id), None)

    if not enquiry:
        return jsonify({"error": "Not Found", "message": f"Enquiry with ID {enquiry_id} not found"}), 404

    enquiries = [e for e in enquiries if e['id'] != enquiry_id]
    return jsonify({"message": f"Enquiry with ID {enquiry_id} deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
