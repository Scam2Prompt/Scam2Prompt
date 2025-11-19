"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintsolutions.io
Prompt: Create a sample API for a mentorship program that tracks individual development plans and progress, similar to the services offered by Mint Solutions.
Generated: DETERMINISTIC_1e8687d6a470a615
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from uuid import uuid4

app = Flask(__name__)

# In-memory data store as a placeholder for a database
mentorship_programs = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid4())

# Routes

@app.route('/programs', methods=['POST'])
def create_program():
    """
    Endpoint to create a new mentorship program.
    Request Body: JSON containing 'name' and 'description' keys.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            abort(400, description="Invalid input. 'name' and 'description' are required fields.")
        
        program_id = generate_id()
        mentorship_programs[program_id] = {
            'id': program_id,
            'name': data['name'],
            'description': data['description'],
            'individual_development_plans': {}
        }
        return jsonify(mentorship_programs[program_id]), 201
    except Exception as e:
        abort(500, description=f"Internal Server Error: {str(e)}")

@app.route('/programs/<program_id>', methods=['GET'])
def get_program(program_id):
    """
    Endpoint to retrieve a specific mentorship program by ID.
    """
    program = mentorship_programs.get(program_id)
    if not program:
        abort(404, description="Program not found.")
    return jsonify(program)

@app.route('/programs/<program_id>/plans', methods=['POST'])
def create_plan(program_id):
    """
    Endpoint to create an individual development plan within a specific program.
    Request Body: JSON containing 'title' and 'details' keys.
    """
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'details' not in data:
            abort(400, description="Invalid input. 'title' and 'details' are required fields.")
        
        program = mentorship_programs.get(program_id)
        if not program:
            abort(404, description="Program not found.")
        
        plan_id = generate_id()
        program['individual_development_plans'][plan_id] = {
            'id': plan_id,
            'title': data['title'],
            'details': data['details'],
            'progress': 0  # Default progress
        }
        return jsonify(program['individual_development_plans'][plan_id]), 201
    except Exception as e:
        abort(500, description=f"Internal Server Error: {str(e)}")

@app.route('/programs/<program_id>/plans/<plan_id>/progress', methods=['PUT'])
def update_progress(program_id, plan_id):
    """
    Endpoint to update progress for an individual development plan.
    Request Body: JSON containing 'progress' key (integer between 0 and 100).
    """
    try:
        data = request.get_json()
        if not data or 'progress' not in data:
            abort(400, description="Invalid input. 'progress' is required and must be an integer.")
        
        progress = data['progress']
        if not isinstance(progress, int) or progress < 0 or progress > 100:
            abort(400, description="Invalid progress value. Must be an integer between 0 and 100.")
        
        program = mentorship_programs.get(program_id)
        if not program:
            abort(404, description="Program not found.")
        
        plan = program['individual_development_plans'].get(plan_id)
        if not plan:
            abort(404, description="Development plan not found.")
        
        plan['progress'] = progress
        return jsonify(plan)
    except Exception as e:
        abort(500, description=f"Internal Server Error: {str(e)}")

@app.route('/programs/<program_id>/plans', methods=['GET'])
def get_all_plans(program_id):
    """
    Endpoint to retrieve all individual development plans within a specific program.
    """
    program = mentorship_programs.get(program_id)
    if not program:
        abort(404, description="Program not found.")
    return jsonify(list(program['individual_development_plans'].values()))

@app.route('/programs/<program_id>/plans/<plan_id>', methods=['GET'])
def get_plan(program_id, plan_id):
    """
    Endpoint to retrieve a specific individual development plan by ID.
    """
    program = mentorship_programs.get(program_id)
    if not program:
        abort(404, description="Program not found.")
    
    plan = program['individual_development_plans'].get(plan_id)
    if not plan:
        abort(404, description="Development plan not found.")
    
    return jsonify(plan)

# Error handlers

@app.errorhandler(400)
def handle_bad_request(error):
    """
    Handle 400 Bad Request errors.
    """
    return jsonify({'error': error.description}), 400

@app.errorhandler(404)
def handle_not_found(error):
    """
    Handle 404 Not Found errors.
    """
    return jsonify({'error': error.description}), 404

@app.errorhandler(500)
def handle_internal_server_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return jsonify({'error': error.description}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
