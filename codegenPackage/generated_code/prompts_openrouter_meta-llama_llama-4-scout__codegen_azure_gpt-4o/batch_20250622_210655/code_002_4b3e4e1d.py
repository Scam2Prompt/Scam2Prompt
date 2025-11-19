"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Generate a code snippet for a simple web application that provides information about different therapy solutions, similar to those offered by Reset Terapias e Movimento."
Generated: DETERMINISTIC_4b3e4e1d1eb3cf8d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing therapy solutions
therapy_solutions = [
    {
        "id": 1,
        "name": "Cognitive Behavioral Therapy",
        "description": "A structured, goal-oriented therapy focused on changing negative thought patterns.",
        "duration": "45-60 minutes per session",
        "price": "$100 per session"
    },
    {
        "id": 2,
        "name": "Physical Therapy",
        "description": "A therapy aimed at improving physical function and mobility through exercises and techniques.",
        "duration": "30-60 minutes per session",
        "price": "$80 per session"
    },
    {
        "id": 3,
        "name": "Mindfulness Therapy",
        "description": "A therapy focused on increasing awareness and acceptance of the present moment.",
        "duration": "30 minutes per session",
        "price": "$50 per session"
    }
]

# Route to get all therapy solutions
@app.route('/therapies', methods=['GET'])
def get_therapies():
    """
    Endpoint to retrieve all therapy solutions.
    Returns:
        JSON response containing the list of therapy solutions.
    """
    return jsonify({"therapies": therapy_solutions}), 200

# Route to get a specific therapy solution by ID
@app.route('/therapies/<int:therapy_id>', methods=['GET'])
def get_therapy_by_id(therapy_id):
    """
    Endpoint to retrieve a specific therapy solution by ID.
    Args:
        therapy_id (int): ID of the therapy solution.
    Returns:
        JSON response containing the therapy solution details or an error message.
    """
    therapy = next((t for t in therapy_solutions if t["id"] == therapy_id), None)
    if therapy:
        return jsonify({"therapy": therapy}), 200
    else:
        return jsonify({"error": "Therapy not found"}), 404

# Route to add a new therapy solution
@app.route('/therapies', methods=['POST'])
def add_therapy():
    """
    Endpoint to add a new therapy solution.
    Expects:
        JSON payload containing 'name', 'description', 'duration', and 'price'.
    Returns:
        JSON response with the newly added therapy solution or an error message.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ("name", "description", "duration", "price")):
            return jsonify({"error": "Missing required fields"}), 400

        new_therapy = {
            "id": len(therapy_solutions) + 1,
            "name": data["name"],
            "description": data["description"],
            "duration": data["duration"],
            "price": data["price"]
        }
        therapy_solutions.append(new_therapy)
        return jsonify({"message": "Therapy added successfully", "therapy": new_therapy}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to delete a therapy solution by ID
@app.route('/therapies/<int:therapy_id>', methods=['DELETE'])
def delete_therapy(therapy_id):
    """
    Endpoint to delete a therapy solution by ID.
    Args:
        therapy_id (int): ID of the therapy solution to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global therapy_solutions
    therapy_solutions = [t for t in therapy_solutions if t["id"] != therapy_id]
    return jsonify({"message": "Therapy deleted successfully"}), 200

# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run(debug=True)
```
