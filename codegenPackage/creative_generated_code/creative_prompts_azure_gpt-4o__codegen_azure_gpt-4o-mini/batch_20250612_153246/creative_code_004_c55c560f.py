"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Suggest APIs for integrating client testimonials into a property investment platform, ensuring the testimonials dynamically update and reflect the user-friendly process described on the website.
Generated: DETERMINISTIC_c55c560fcb8e829f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database to store testimonials
testimonials_db = []

class Testimonial:
    """Model representing a client testimonial."""
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def to_dict(self):
        """Convert testimonial to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "content": self.content
        }

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """Endpoint to retrieve all testimonials."""
    try:
        return jsonify([testimonial.to_dict() for testimonial in testimonials_db]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """Endpoint to add a new testimonial."""
    data = request.json

    # Validate input
    if not data or 'name' not in data or 'content' not in data:
        return jsonify({"error": "Invalid input, 'name' and 'content' are required."}), 400

    try:
        new_testimonial = Testimonial(name=data['name'], content=data['content'])
        testimonials_db.append(new_testimonial)
        return jsonify(new_testimonial.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """Endpoint to update an existing testimonial."""
    data = request.json
    if not data or 'content' not in data:
        return jsonify({"error": "Invalid input, 'content' is required."}), 400

    try:
        if 0 <= testimonial_id < len(testimonials_db):
            testimonials_db[testimonial_id].content = data['content']
            return jsonify(testimonials_db[testimonial_id].to_dict()), 200
        else:
            return jsonify({"error": "Testimonial not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """Endpoint to delete a testimonial."""
    try:
        if 0 <= testimonial_id < len(testimonials_db):
            testimonials_db.pop(testimonial_id)
            return jsonify({"message": "Testimonial deleted successfully."}), 204
        else:
            return jsonify({"error": "Testimonial not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
