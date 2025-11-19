"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I create a nutritional education program for schools that incorporates the guidelines provided by It's Cool Foods for promoting healthy eating among children?
Generated: DETERMINISTIC_6d997ddd58d34489
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for nutritional guidelines
NUTRITIONAL_GUIDELINES = {
    "fruits": "Aim for at least 1-2 servings of fruits each day.",
    "vegetables": "Include a variety of vegetables in your meals.",
    "whole_grains": "Choose whole grains over refined grains.",
    "dairy": "Opt for low-fat or fat-free dairy options.",
    "protein": "Incorporate lean proteins such as chicken, fish, beans, and nuts."
}

# Error handling for invalid requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

@app.route('/guidelines', methods=['GET'])
def get_guidelines():
    """
    Endpoint to retrieve nutritional guidelines.
    Returns a JSON object containing the guidelines for healthy eating.
    """
    return jsonify(NUTRITIONAL_GUIDELINES)

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback on the nutritional education program.
    Expects a JSON payload with 'name' and 'comments'.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'comments' not in data:
            raise ValueError("Missing 'name' or 'comments' in request data.")
        
        # Here you would typically save the feedback to a database
        # For demonstration, we will just print it
        print(f"Feedback received from {data['name']}: {data['comments']}")
        
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except ValueError as ve:
        return bad_request(ve)
    except Exception as e:
        return internal_error(e)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
