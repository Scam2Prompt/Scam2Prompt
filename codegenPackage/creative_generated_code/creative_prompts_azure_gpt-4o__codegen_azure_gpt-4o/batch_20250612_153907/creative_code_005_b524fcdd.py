"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest an API for managing and displaying testimonials on a community-focused website like "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_b524fcdd7454c73e
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for testimonials
# In production, use a database instead
testimonials = []

# Helper function to validate testimonial data
def validate_testimonial(data):
    required_fields = ["name", "message", "date"]
    for field in required_fields:
        if field not in data:
            return False
    return True

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint to fetch all testimonials.
    Returns:
        JSON response containing a list of testimonials.
    """
    return jsonify({"testimonials": testimonials}), 200

@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    """
    Endpoint to add a new testimonial.
    Expects:
        JSON payload with 'name', 'message', and 'date'.
    Returns:
        JSON response with the added testimonial or error message.
    """
    if not request.json or not validate_testimonial(request.json):
        abort(400, description="Invalid testimonial data. Ensure 'name', 'message', and 'date' are provided.")

    new_testimonial = {
        "id": len(testimonials) + 1,
        "name": request.json["name"],
        "message": request.json["message"],
        "date": request.json["date"]
    }
    testimonials.append(new_testimonial)
    return jsonify(new_testimonial), 201

@app.route('/api/testimonials/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """
    Endpoint to fetch a specific testimonial by ID.
    Args:
        testimonial_id (int): ID of the testimonial to fetch.
    Returns:
        JSON response containing the testimonial or error message.
    """
    testimonial = next((t for t in testimonials if t["id"] == testimonial_id), None)
    if testimonial is None:
        abort(404, description="Testimonial not found.")
    return jsonify(testimonial), 200

@app.route('/api/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """
    Endpoint to update an existing testimonial by ID.
    Expects:
        JSON payload with 'name', 'message', and/or 'date'.
    Args:
        testimonial_id (int): ID of the testimonial to update.
    Returns:
        JSON response with the updated testimonial or error message.
    """
    testimonial = next((t for t in testimonials if t["id"] == testimonial_id), None)
    if testimonial is None:
        abort(404, description="Testimonial not found.")
    
    if not request.json:
        abort(400, description="Invalid data provided for update.")

    testimonial["name"] = request.json.get("name", testimonial["name"])
    testimonial["message"] = request.json.get("message", testimonial["message"])
    testimonial["date"] = request.json.get("date", testimonial["date"])

    return jsonify(testimonial), 200

@app.route('/api/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """
    Endpoint to delete a testimonial by ID.
    Args:
        testimonial_id (int): ID of the testimonial to delete.
    Returns:
        JSON response confirming deletion or error message.
    """
    testimonial = next((t for t in testimonials if t["id"] == testimonial_id), None)
    if testimonial is None:
        abort(404, description="Testimonial not found.")
    
    testimonials.remove(testimonial)
    return jsonify({"message": "Testimonial deleted successfully."}), 200

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": error.description}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": error.description}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
```
