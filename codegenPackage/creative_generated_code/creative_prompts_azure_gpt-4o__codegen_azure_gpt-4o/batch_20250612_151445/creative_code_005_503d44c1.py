"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Suggest APIs or frameworks to implement a virtual admission system like "Matrícula Virtual" described on the Trentino website.
Generated: DETERMINISTIC_503d44c185cce323
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-commented, production-ready Python example implementation using the Flask framework to create a basic virtual admission system API. It includes error handling, follows best practices, and is syntactically correct:

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database setup (for demonstration purposes)
admissions_db = []

# Utility function for error response
def create_error_response(message, code):
    return jsonify({"error": message, "status_code": code}), code

# Error handling for common exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return create_error_response(e.description, e.code)

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return create_error_response("An unexpected error occurred.", 500)

# API endpoint: View all admissions
@app.route('/admissions', methods=['GET'])
def get_admissions():
    return jsonify(admissions_db), 200

# API endpoint: Create a new admission
@app.route('/admissions', methods=['POST'])
def create_admission():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'course' not in data:
            return create_error_response("Invalid input data. 'name' and 'course' are required.", 400)
        
        admission_id = len(admissions_db) + 1
        new_admission = {
            "id": admission_id,
            "name": data['name'],
            "course": data['course'],
            "status": "pending"
        }
        admissions_db.append(new_admission)
        return jsonify(new_admission), 201
    except Exception as e:
        return create_error_response(str(e), 500)

# API endpoint: View a specific admission by ID
@app.route('/admissions/<int:id>', methods=['GET'])
def get_admission_by_id(id):
    admission = next((ad for ad in admissions_db if ad['id'] == id), None)
    if not admission:
        return create_error_response(f"Admission with ID {id} not found.", 404)
    return jsonify(admission), 200

# API endpoint: Update admission status
@app.route('/admissions/<int:id>/status', methods=['PUT'])
def update_admission_status(id):
    try:
        data = request.get_json()
        if not data or 'status' not in data:
            return create_error_response("Invalid input data. 'status' is required.", 400)
        
        admission = next((ad for ad in admissions_db if ad['id'] == id), None)
        if not admission:
            return create_error_response(f"Admission with ID {id} not found.", 404)
        
        admission['status'] = data['status']
        return jsonify(admission), 200
    except Exception as e:
        return create_error_response(str(e), 500)

# API endpoint: Delete an admission by ID
@app.route('/admissions/<int:id>', methods=['DELETE'])
def delete_admission(id):
    admission = next((ad for ad in admissions_db if ad['id'] == id), None)
    if not admission:
        return create_error_response(f"Admission with ID {id} not found.", 404)
    
    admissions_db.remove(admission)
    return jsonify({"message": f"Admission with ID {id} has been deleted."}), 200

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Setup Instructions:
1. Install dependencies:
   ```
   pip install flask
   ```
2. Run the application:
   ```
   python app.py
   ```
3. Use tools like Postman or curl to test the endpoints.

### Example API Endpoints:
1. `GET /admissions`: View all admissions.
2. `POST /admissions`: Add a new admission (example JSON: `{"name": "John Doe", "course": "Computer Science"}`).
3. `GET /admissions/<id>`: View admission details by ID.
4. `PUT /admissions/<id>/status`: Update admission status (example JSON: `{"status": "approved"}`).
5. `DELETE /admissions/<id>`: Delete an admission by ID.
