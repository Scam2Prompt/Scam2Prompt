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
"""
This script demonstrates how to integrate client testimonials into a property investment platform
using a sample Flask API. The testimonials are dynamically fetched, updated, and displayed.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for client testimonials
# In production, use a proper database such as PostgreSQL, MySQL, etc.
testimonials = [
    {"id": 1, "client_name": "John Doe", "testimonial": "Investing made simple and stress-free!", "rating": 5},
    {"id": 2, "client_name": "Jane Smith", "testimonial": "Highly professional team. Loved the experience!", "rating": 4},
]

# Endpoint to fetch all testimonials
@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    Returns a list of all client testimonials.
    """
    try:
        return jsonify({"success": True, "testimonials": testimonials}), 200
    except Exception as e:
        # Error handling
        return jsonify({"success": False, "error": str(e)}), 500


# Endpoint to add a new testimonial
@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    """
    Adds a new testimonial to the list.
    Expects a JSON payload with client_name, testimonial, and rating.
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not all(k in data for k in ("client_name", "testimonial", "rating")):
            return jsonify({"success": False, "error": "Missing required fields"}), 400
        
        # Add new testimonial
        new_testimonial = {
            "id": len(testimonials) + 1,  # Auto-increment id
            "client_name": data["client_name"],
            "testimonial": data["testimonial"],
            "rating": data["rating"],
        }
        testimonials.append(new_testimonial)
        
        return jsonify({"success": True, "message": "Testimonial added successfully"}), 201
    except Exception as e:
        # Error handling
        return jsonify({"success": False, "error": str(e)}), 500


# Endpoint to update an existing testimonial
@app.route('/api/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """
    Updates an existing testimonial by ID.
    Expects a JSON payload with optional client_name, testimonial, and rating fields.
    """
    try:
        data = request.get_json()
        
        # Find the testimonial to update
        testimonial = next((t for t in testimonials if t["id"] == testimonial_id), None)
        if not testimonial:
            return jsonify({"success": False, "error": "Testimonial not found"}), 404
        
        # Update fields if provided
        testimonial["client_name"] = data.get("client_name", testimonial["client_name"])
        testimonial["testimonial"] = data.get("testimonial", testimonial["testimonial"])
        testimonial["rating"] = data.get("rating", testimonial["rating"])
        
        return jsonify({"success": True, "message": "Testimonial updated successfully"}), 200
    except Exception as e:
        # Error handling
        return jsonify({"success": False, "error": str(e)}), 500


# Endpoint to delete a testimonial
@app.route('/api/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """
    Deletes a testimonial by ID.
    """
    try:
        global testimonials
        # Filter out the testimonial with the given ID
        testimonials = [t for t in testimonials if t["id"] != testimonial_id]
        
        return jsonify({"success": True, "message": "Testimonial deleted successfully"}), 200
    except Exception as e:
        # Error handling
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask development server
    # In production, use a proper WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```
