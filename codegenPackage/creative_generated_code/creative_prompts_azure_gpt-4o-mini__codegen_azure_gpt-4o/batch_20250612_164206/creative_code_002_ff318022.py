"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Create a REST API endpoint for managing academic programs at SMKN 1 Kadipaten, including features for adding, updating, and retrieving program details.
Generated: DETERMINISTIC_ff31802238eb700d
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

app = Flask(__name__)

# In-memory database for storing academic programs
academic_programs = {}

# API endpoint to add a new academic program
@app.route('/api/programs', methods=['POST'])
def add_program():
    """
    Adds a new academic program.
    Expects JSON data: {"id": <int>, "name": <str>, "description": <str>}
    """
    try:
        data = request.get_json()
        if not data or 'id' not in data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        program_id = data['id']
        if program_id in academic_programs:
            return jsonify({"error": "Program ID already exists"}), 400
        
        academic_programs[program_id] = {
            "name": data['name'],
            "description": data['description']
        }
        return jsonify({"message": "Academic program added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an existing academic program
@app.route('/api/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """
    Updates an existing academic program.
    Expects JSON data: {"name": <str>, "description": <str>}
    """
    try:
        if program_id not in academic_programs:
            return jsonify({"error": "Program not found"}), 404
        
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        academic_programs[program_id].update({
            "name": data['name'],
            "description": data['description']
        })
        return jsonify({"message": "Academic program updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all academic programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    Retrieves all academic programs.
    """
    try:
        return jsonify({"programs": academic_programs}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific academic program by ID
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program_by_id(program_id):
    """
    Retrieves a specific academic program by ID.
    """
    try:
        if program_id not in academic_programs:
            return jsonify({"error": "Program not found"}), 404
        
        return jsonify({"program": academic_programs[program_id]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
