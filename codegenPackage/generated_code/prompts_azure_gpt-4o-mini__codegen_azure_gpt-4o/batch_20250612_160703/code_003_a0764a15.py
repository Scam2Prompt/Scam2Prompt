"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Describe an API that could facilitate outreach programs for children with special education needs, taking cues from the ICON Foundation's community connect initiatives.
Generated: DETERMINISTIC_a0764a150bd66474
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store outreach program data
programs = []
participants = []

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# API Endpoint: Get all outreach programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    """
    Fetch all outreach programs.
    Returns:
        JSON response containing a list of all programs.
    """
    return jsonify({"programs": programs}), 200

# API Endpoint: Create a new outreach program
@app.route('/api/programs', methods=['POST'])
def create_program():
    """
    Create a new outreach program.
    Request Body:
        - name (str): Name of the program.
        - description (str): Description of the program.
        - target_age_group (str): Target age group for the program.
    Returns:
        JSON response containing the created program.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'target_age_group' not in data:
        return error_response("Missing required fields: name, description, target_age_group")
    
    program = {
        "id": len(programs) + 1,
        "name": data['name'],
        "description": data['description'],
        "target_age_group": data['target_age_group']
    }
    programs.append(program)
    return jsonify({"program": program}), 201

# API Endpoint: Register a participant for a program
@app.route('/api/programs/<int:program_id>/participants', methods=['POST'])
def register_participant(program_id):
    """
    Register a participant for a specific outreach program.
    Request Body:
        - name (str): Name of the participant.
        - age (int): Age of the participant.
        - special_needs (str): Description of special education needs.
    Returns:
        JSON response containing the registered participant.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'special_needs' not in data:
        return error_response("Missing required fields: name, age, special_needs")
    
    program = next((p for p in programs if p['id'] == program_id), None)
    if not program:
        return error_response("Program not found", 404)
    
    participant = {
        "id": len(participants) + 1,
        "program_id": program_id,
        "name": data['name'],
        "age": data['age'],
        "special_needs": data['special_needs']
    }
    participants.append(participant)
    return jsonify({"participant": participant}), 201

# API Endpoint: Get participants for a specific program
@app.route('/api/programs/<int:program_id>/participants', methods=['GET'])
def get_participants(program_id):
    """
    Fetch all participants registered for a specific outreach program.
    Returns:
        JSON response containing a list of participants for the program.
    """
    program = next((p for p in programs if p['id'] == program_id), None)
    if not program:
        return error_response("Program not found", 404)
    
    program_participants = [p for p in participants if p['program_id'] == program_id]
    return jsonify({"participants": program_participants}), 200

# API Endpoint: Delete a program
@app.route('/api/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """
    Delete an outreach program.
    Returns:
        JSON response confirming deletion.
    """
    global programs
    program = next((p for p in programs if p['id'] == program_id), None)
    if not program:
        return error_response("Program not found", 404)
    
    programs = [p for p in programs if p['id'] != program_id]
    return jsonify({"message": "Program deleted successfully"}), 200

# API Endpoint: Delete a participant
@app.route('/api/participants/<int:participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    """
    Delete a participant from the system.
    Returns:
        JSON response confirming deletion.
    """
    global participants
    participant = next((p for p in participants if p['id'] == participant_id), None)
    if not participant:
        return error_response("Participant not found", 404)
    
    participants = [p for p in participants if p['id'] != participant_id]
    return jsonify({"message": "Participant deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
