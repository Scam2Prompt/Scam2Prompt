"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Create a REST API endpoint that provides information about the academic and cultural training programs offered by the Escuela de Suboficiales de la Fuerza Aérea del Perú.
Generated: DETERMINISTIC_be6cd65202c0f67a
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for academic and cultural training programs
training_programs = [
    {
        "id": 1,
        "name": "Aeronautical Engineering Basics",
        "type": "Academic",
        "description": "A foundational course on aeronautical engineering principles.",
        "duration": "6 months"
    },
    {
        "id": 2,
        "name": "Leadership and Ethics Training",
        "type": "Cultural",
        "description": "A program aimed at developing leadership and ethical decision-making skills.",
        "duration": "3 months"
    },
    {
        "id": 3,
        "name": "Advanced Aircraft Maintenance",
        "type": "Academic",
        "description": "An advanced course on aircraft systems and maintenance techniques.",
        "duration": "12 months"
    },
    {
        "id": 4,
        "name": "Peruvian Cultural Studies",
        "type": "Cultural",
        "description": "A program that explores the rich history and culture of Peru.",
        "duration": "2 months"
    }
]

@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    REST API endpoint to fetch information about training programs.
    Returns:
        JSON response containing the list of academic and cultural training programs.
    """
    try:
        return jsonify({"programs": training_programs}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program_by_id(program_id):
    """
    REST API endpoint to fetch details of a specific training program by ID.
    Parameters:
        program_id (int): ID of the training program
    Returns:
        JSON response containing the program details or an error message.
    """
    try:
        program = next((p for p in training_programs if p["id"] == program_id), None)
        if program:
            return jsonify({"program": program}), 200
        else:
            return jsonify({"error": "Program not found"}), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/api/programs', methods=['POST'])
def create_program():
    """
    REST API endpoint to create a new training program.
    Expects JSON payload with program details.
    Returns:
        JSON response containing the newly created program or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "type", "description", "duration")):
            return jsonify({"error": "Invalid input. Ensure 'name', 'type', 'description', and 'duration' are provided."}), 400
        
        # Generate a new ID for the program
        new_id = max(p["id"] for p in training_programs) + 1 if training_programs else 1
        new_program = {
            "id": new_id,
            **data
        }
        training_programs.append(new_program)
        return jsonify({"program": new_program}), 201
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/api/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """
    REST API endpoint to delete a specific training program by ID.
    Parameters:
        program_id (int): ID of the training program to be deleted
    Returns:
        JSON response confirming the deletion or an error message.
    """
    try:
        global training_programs
        training_programs = [p for p in training_programs if p["id"] != program_id]
        return jsonify({"message": "Program deleted successfully"}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```
