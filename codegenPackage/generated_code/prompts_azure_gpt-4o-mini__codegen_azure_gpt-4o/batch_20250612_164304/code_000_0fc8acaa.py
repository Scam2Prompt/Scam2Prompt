"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Generate a code snippet for a web application that allows users to find the best optical solutions based on their lifestyle and vision needs, similar to the services offered by Optic Alizé.
Generated: DETERMINISTIC_0fc8acaad5c26260
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for optical solutions
optical_solutions = [
    {
        "id": 1,
        "name": "Daily Contact Lenses",
        "description": "Convenient and hygienic lenses for daily use.",
        "lifestyle": ["active", "traveling"],
        "vision_needs": ["nearsighted", "farsighted"]
    },
    {
        "id": 2,
        "name": "Blue Light Glasses",
        "description": "Protect your eyes from digital screens.",
        "lifestyle": ["office", "gaming"],
        "vision_needs": ["eye strain"]
    },
    {
        "id": 3,
        "name": "Progressive Lenses",
        "description": "Seamless vision correction for all distances.",
        "lifestyle": ["reading", "driving"],
        "vision_needs": ["presbyopia"]
    }
]

# Endpoint to find the best optical solutions based on user input
@app.route('/find-optical-solutions', methods=['POST'])
def find_optical_solutions():
    """
    Endpoint to find the best optical solutions based on lifestyle and vision needs.
    Expects a JSON payload with 'lifestyle' and 'vision_needs' fields.
    """
    try:
        # Parse the JSON request data
        data = request.get_json()
        lifestyle = data.get('lifestyle', [])
        vision_needs = data.get('vision_needs', [])

        # Validate input
        if not lifestyle or not vision_needs:
            return jsonify({"error": "Both 'lifestyle' and 'vision_needs' fields are required."}), 400

        # Filter optical solutions based on user input
        matching_solutions = [
            solution for solution in optical_solutions
            if any(life in solution['lifestyle'] for life in lifestyle) and
               any(need in solution['vision_needs'] for need in vision_needs)
        ]

        # Return matching solutions
        return jsonify({"matching_solutions": matching_solutions}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to list all available optical solutions
@app.route('/optical-solutions', methods=['GET'])
def list_optical_solutions():
    """
    Endpoint to list all available optical solutions.
    """
    return jsonify({"optical_solutions": optical_solutions}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
