"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
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

app = Flask(__name__)

# In-memory database to store training programs
training_programs = []

# API Endpoints

@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Retrieve all training programs.
    """
    return jsonify({"programs": training_programs}), 200


@app.route('/programs', methods=['POST'])
def create_program():
    """
    Create a new training program.
    Request JSON should include:
        - name: str (name of the program)
        - description: str (description of the program)
        - duration: int (duration of the program in weeks)
        - objectives: list[str] (objectives of the program)
    """
    try:
        data = request.get_json()
        
        # Validate request data
        if not all(key in data for key in ('name', 'description', 'duration', 'objectives')):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate data types
        if not isinstance(data['name'], str) or not isinstance(data['description'], str) \
           or not isinstance(data['duration'], int) or not isinstance(data['objectives'], list):
            return jsonify({"error": "Invalid data types"}), 400
        
        # Create the program and save it
        program = {
            "id": len(training_programs) + 1,
            "name": data['name'],
            "description": data['description'],
            "duration": data['duration'],
            "objectives": data['objectives']
        }
        training_programs.append(program)
        
        return jsonify({"message": "Program created successfully", "program": program}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program_by_id(program_id):
    """
    Retrieve a specific training program by ID.
    """
    program = next((p for p in training_programs if p['id'] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404
    return jsonify({"program": program}), 200


@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """
    Update an existing training program by ID.
    Request JSON should include any of the following fields:
        - name: str (name of the program)
        - description: str (description of the program)
        - duration: int (duration of the program in weeks)
        - objectives: list[str] (objectives of the program)
    """
    program = next((p for p in training_programs if p['id'] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    try:
        data = request.get_json()

        # Validate data types if fields are provided
        if 'name' in data and not isinstance(data['name'], str):
            return jsonify({"error": "Invalid data type for 'name'"}), 400
        if 'description' in data and not isinstance(data['description'], str):
            return jsonify({"error": "Invalid data type for 'description'"}), 400
        if 'duration' in data and not isinstance(data['duration'], int):
            return jsonify({"error": "Invalid data type for 'duration'"}), 400
        if 'objectives' in data and not isinstance(data['objectives'], list):
            return jsonify({"error": "Invalid data type for 'objectives'"}), 400

        # Update the program
        program.update({key: data[key] for key in data if key in program})
        return jsonify({"message": "Program updated successfully", "program": program}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """
    Delete a specific training program by ID.
    """
    global training_programs
    program = next((p for p in training_programs if p['id'] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    training_programs = [p for p in training_programs if p['id'] != program_id]
    return jsonify({"message": "Program deleted successfully"}), 200


# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
