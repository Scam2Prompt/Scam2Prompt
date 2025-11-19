"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a REST API endpoint that allows patients to submit testimonials about their experiences with cosmetic surgery, inspired by the testimonials section on Dr. Gareth September's website.
Generated: DETERMINISTIC_7d5f1fb8ab56e649
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for testimonials (for demonstration purposes)
testimonials = []

# Define error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).get_data()
    response.content_type = "application/json"
    return response

# Define error handler for other unhandled exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": {
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e)
        }
    }), 500

# Define the endpoint for submitting testimonials
@app.route('/api/testimonials', methods=['POST'])
def submit_testimonial():
    """
    Endpoint: Submit a testimonial
    Method: POST
    Request JSON Body:
        {
            "name": <string>,
            "email": <string>,
            "testimonial": <string>
        }
    Response:
        Success: Returns a confirmation message and stores the testimonial in memory.
        Error: Returns an appropriate error message for invalid input.
    """
    try:
        # Parse and validate the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request: JSON data is required"}), 400
        
        # Required fields
        name = data.get("name")
        email = data.get("email")
        testimonial = data.get("testimonial")
        
        # Validate required fields
        if not name or not email or not testimonial:
            return jsonify({"error": "Invalid request: 'name', 'email', and 'testimonial' are required"}), 400
        
        # Store the testimonial in memory
        testimonial_entry = {
            "name": name,
            "email": email,
            "testimonial": testimonial
        }
        testimonials.append(testimonial_entry)
        
        # Return success response
        return jsonify({
            "message": "Testimonial submitted successfully!",
            "testimonial": testimonial_entry
        }), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

# Define the endpoint for retrieving all testimonials
@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint: Retrieve all testimonials
    Method: GET
    Response:
        Success: Returns a list of all submitted testimonials.
    """
    return jsonify({
        "testimonials": testimonials
    }), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
