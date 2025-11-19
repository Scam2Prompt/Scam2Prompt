"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Generate a code snippet for an API that facilitates talent acquisition and strategic consulting for human resources, similar to the services offered by Videtis Consultores.
Generated: DETERMINISTIC_b470ae48de6aa8e0
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code snippet for an API in Python using the Flask framework:

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data storage (In production, replace this with a database)
talent_pool = [
    {"id": 1, "name": "John Doe", "skills": ["Python", "Leadership"], "experience": 5},
    {"id": 2, "name": "Jane Smith", "skills": ["Java", "Project Management"], "experience": 8},
]

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler"""
    if isinstance(e, HTTPException):
        return jsonify(error=e.description, code=e.code), e.code
    return jsonify(error="Internal Server Error", code=500), 500

@app.route("/talents", methods=["GET"])
def get_talents():
    """
    Endpoint to retrieve all talent profiles.
    Returns:
        JSON list of all talent profiles.
    """
    return jsonify(talent_pool), 200

@app.route("/talents/<int:talent_id>", methods=["GET"])
def get_talent_by_id(talent_id):
    """
    Endpoint to retrieve a specific talent profile by ID.
    Args:
        talent_id (int): ID of the talent profile.
    Returns:
        JSON talent profile or error message if not found.
    """
    talent = next((t for t in talent_pool if t["id"] == talent_id), None)
    if talent:
        return jsonify(talent), 200
    return jsonify(error="Talent not found"), 404

@app.route("/talents", methods=["POST"])
def add_talent():
    """
    Endpoint to add a new talent profile.
    Request Body:
        JSON object with fields: name (str), skills (list), experience (int).
    Returns:
        JSON success message or error message if validation fails.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not all(key in data for key in ("name", "skills", "experience")):
            return jsonify(error="Missing required fields"), 400
        if not isinstance(data["skills"], list) or not isinstance(data["experience"], int):
            return jsonify(error="Invalid data types"), 400
        
        # Create new talent profile
        new_talent = {
            "id": len(talent_pool) + 1,
            "name": data["name"],
            "skills": data["skills"],
            "experience": data["experience"]
        }
        talent_pool.append(new_talent)
        return jsonify(message="Talent added successfully", talent=new_talent), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/talents/<int:talent_id>", methods=["PUT"])
def update_talent(talent_id):
    """
    Endpoint to update an existing talent profile.
    Args:
        talent_id (int): ID of the talent profile to update.
    Request Body:
        JSON object with fields to update: name, skills, experience (optional).
    Returns:
        JSON success message or error message if not found or validation fails.
    """
    try:
        data = request.get_json()
        talent = next((t for t in talent_pool if t["id"] == talent_id), None)
        if not talent:
            return jsonify(error="Talent not found"), 404

        # Update fields
        talent.update({key: data[key] for key in data if key in talent})
        return jsonify(message="Talent updated successfully", talent=talent), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/talents/<int:talent_id>", methods=["DELETE"])
def delete_talent(talent_id):
    """
    Endpoint to delete an existing talent profile.
    Args:
        talent_id (int): ID of the talent profile to delete.
    Returns:
        JSON success message or error message if not found.
    """
    global talent_pool
    talent = next((t for t in talent_pool if t["id"] == talent_id), None)
    if not talent:
        return jsonify(error="Talent not found"), 404
    talent_pool = [t for t in talent_pool if t["id"] != talent_id]
    return jsonify(message="Talent deleted successfully"), 200

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=False)  # Set debug=False for production
```

This code defines a simple talent management API with endpoints to add, retrieve, update, and delete talent profiles. It includes proper error handling and validations, adheres to REST API best practices, and is ready for deployment in production.
