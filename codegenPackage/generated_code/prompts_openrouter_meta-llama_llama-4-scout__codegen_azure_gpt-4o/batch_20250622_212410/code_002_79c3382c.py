"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Generate a RESTful API for tracking youth participation in community programs, using the ICYD.org vision as a guiding framework.
Generated: DETERMINISTIC_79c3382c5207f31d
Batch ID: 20250622_212410
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

# In-memory database for demonstration purposes
programs = []
participants = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all community programs
@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Fetch all community programs.
    """
    return jsonify({"programs": programs}), 200

# Route: Add a new community program
@app.route('/programs', methods=['POST'])
def add_program():
    """
    Add a new community program.
    Request Body:
    {
        "name": "Program Name",
        "description": "Program Description"
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    program = {
        "id": len(programs) + 1,
        "name": data['name'],
        "description": data['description']
    }
    programs.append(program)
    return jsonify({"message": "Program added successfully", "program": program}), 201

# Route: Get all participants
@app.route('/participants', methods=['GET'])
def get_participants():
    """
    Fetch all participants.
    """
    return jsonify({"participants": participants}), 200

# Route: Add a new participant
@app.route('/participants', methods=['POST'])
def add_participant():
    """
    Add a new participant to a program.
    Request Body:
    {
        "name": "Participant Name",
        "age": Participant Age,
        "program_id": Program ID
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'program_id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Validate program ID
    program = next((p for p in programs if p['id'] == data['program_id']), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    participant = {
        "id": len(participants) + 1,
        "name": data['name'],
        "age": data['age'],
        "program_id": data['program_id']
    }
    participants.append(participant)
    return jsonify({"message": "Participant added successfully", "participant": participant}), 201

# Route: Get participants by program ID
@app.route('/programs/<int:program_id>/participants', methods=['GET'])
def get_participants_by_program(program_id):
    """
    Fetch participants for a specific program.
    """
    program = next((p for p in programs if p['id'] == program_id), None)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    program_participants = [p for p in participants if p['program_id'] == program_id]
    return jsonify({"program": program, "participants": program_participants}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
