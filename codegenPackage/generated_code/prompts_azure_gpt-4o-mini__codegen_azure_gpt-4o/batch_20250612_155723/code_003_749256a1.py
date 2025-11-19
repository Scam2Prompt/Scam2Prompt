"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Create an API endpoint that retrieves and categorizes testimonials from various professionals in Sedona, based on the structure used in The Faces of Sedona and the Verde Valley.
Generated: DETERMINISTIC_749256a1d2ad6b43
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data structure for testimonials
testimonials = [
    {
        "id": 1,
        "name": "John Doe",
        "profession": "Photographer",
        "testimonial": "Sedona's beauty inspires my work every day.",
        "category": "Creative Arts"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "profession": "Chef",
        "testimonial": "The local ingredients here are unmatched.",
        "category": "Culinary"
    },
    {
        "id": 3,
        "name": "Emily Johnson",
        "profession": "Yoga Instructor",
        "testimonial": "Sedona's energy is perfect for mindfulness and yoga.",
        "category": "Wellness"
    }
]

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the API.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    API endpoint to retrieve and categorize testimonials.
    Query Parameters:
        - category (optional): Filter testimonials by category.
    Returns:
        - JSON response with testimonials, optionally filtered by category.
    """
    try:
        # Get the 'category' query parameter if provided
        category = request.args.get('category', None)

        # Filter testimonials by category if specified
        if category:
            filtered_testimonials = [
                t for t in testimonials if t['category'].lower() == category.lower()
            ]
            return jsonify({"testimonials": filtered_testimonials}), 200

        # Return all testimonials if no category is specified
        return jsonify({"testimonials": testimonials}), 200

    except Exception as e:
        # Log the error (in production, use a proper logging framework)
        print(f"Error occurred: {e}")
        return jsonify({"error": "Failed to retrieve testimonials"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
