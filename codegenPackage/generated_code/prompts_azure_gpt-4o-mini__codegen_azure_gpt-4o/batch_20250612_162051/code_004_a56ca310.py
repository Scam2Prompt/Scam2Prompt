"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
Batch ID: 20250612_162051
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

# In-memory database simulation
training_programs = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).data
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Route to get all training programs
@app.route('/api/training-programs', methods=['GET'])
def get_training_programs():
    """
    Fetch all training programs.
    """
    return jsonify(training_programs), 200

# Route to add a new training program
@app.route('/api/training-programs', methods=['POST'])
def add_training_program():
    """
    Add a new training program.
    Request body should include:
    - name: Name of the training program (string)
    - description: Description of the training program (string)
    - duration: Duration of the training program in weeks (integer)
    """
    try:
        data = request.get_json()
        # Validate input
        if not data or 'name' not in data or 'description' not in data or 'duration' not in data:
            return jsonify({"error": "Invalid input. 'name', 'description', and 'duration' are required."}), 400
        
        # Create a new training program
        new_program = {
            "id": len(training_programs) + 1,
            "name": data['name'],
            "description": data['description'],
            "duration": data['duration']
        }
        training_programs.append(new_program)
        return jsonify(new_program), 201
    except Exception as e:
        return handle_generic_exception(e)

# Route to update an existing training program
@app.route('/api/training-programs/<int:program_id>', methods=['PUT'])
def update_training_program(program_id):
    """
    Update an existing training program by ID.
    Request body should include:
    - name: Updated name of the training program (string, optional)
    - description: Updated description of the training program (string, optional)
    - duration: Updated duration of the training program in weeks (integer, optional)
    """
    try:
        data = request.get_json()
        # Find the program by ID
        program = next((p for p in training_programs if p['id'] == program_id), None)
        if not program:
            return jsonify({"error": "Training program not found."}), 404
        
        # Update fields if provided
        program['name'] = data.get('name', program['name'])
        program['description'] = data.get('description', program['description'])
        program['duration'] = data.get('duration', program['duration'])
        return jsonify(program), 200
    except Exception as e:
        return handle_generic_exception(e)

# Route to delete a training program
@app.route('/api/training-programs/<int:program_id>', methods=['DELETE'])
def delete_training_program(program_id):
    """
    Delete a training program by ID.
    """
    try:
        global training_programs
        # Filter out the program to delete
        training_programs = [p for p in training_programs if p['id'] != program_id]
        return jsonify({"message": "Training program deleted successfully."}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
