"""
Generated Code Metadata:
========================
Original URL: https://sonicolab.com
Prompt: Generate a list of sustainable practices for a travel company like Soniclabs, and provide code snippets for implementing these practices in a web application.
Generated: DETERMINISTIC_eaffbab3a90d27e6
Batch ID: 20250622_212626
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

# Initialize Flask application
app = Flask(__name__)

# List of sustainable practices
sustainable_practices = [
    {
        "id": 1,
        "practice": "Promote eco-friendly accommodations",
        "description": "Partner with hotels and lodges that use renewable energy and follow sustainable practices."
    },
    {
        "id": 2,
        "practice": "Encourage carbon offset programs",
        "description": "Offer customers the option to offset their carbon footprint for flights and travel."
    },
    {
        "id": 3,
        "practice": "Support local communities",
        "description": "Collaborate with local businesses and artisans to boost the local economy."
    },
    {
        "id": 4,
        "practice": "Reduce single-use plastics",
        "description": "Provide reusable water bottles and encourage travelers to avoid single-use plastics."
    },
    {
        "id": 5,
        "practice": "Promote sustainable transportation",
        "description": "Encourage the use of public transport, biking, and walking for local travel."
    }
]

# Route to get all sustainable practices
@app.route('/practices', methods=['GET'])
def get_practices():
    """
    Endpoint to retrieve all sustainable practices.
    Returns:
        JSON response containing the list of practices.
    """
    return jsonify({"practices": sustainable_practices}), 200

# Route to get a specific practice by ID
@app.route('/practices/<int:practice_id>', methods=['GET'])
def get_practice_by_id(practice_id):
    """
    Endpoint to retrieve a specific sustainable practice by ID.
    Args:
        practice_id (int): ID of the practice to retrieve.
    Returns:
        JSON response containing the practice details or an error message.
    """
    practice = next((p for p in sustainable_practices if p["id"] == practice_id), None)
    if practice:
        return jsonify({"practice": practice}), 200
    else:
        return jsonify({"error": "Practice not found"}), 404

# Route to add a new sustainable practice
@app.route('/practices', methods=['POST'])
def add_practice():
    """
    Endpoint to add a new sustainable practice.
    Expects JSON payload with 'practice' and 'description' fields.
    Returns:
        JSON response containing the newly added practice or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'practice' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400

        new_practice = {
            "id": len(sustainable_practices) + 1,
            "practice": data['practice'],
            "description": data['description']
        }
        sustainable_practices.append(new_practice)
        return jsonify({"message": "Practice added successfully", "practice": new_practice}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to delete a sustainable practice by ID
@app.route('/practices/<int:practice_id>', methods=['DELETE'])
def delete_practice(practice_id):
    """
    Endpoint to delete a sustainable practice by ID.
    Args:
        practice_id (int): ID of the practice to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global sustainable_practices
    practice = next((p for p in sustainable_practices if p["id"] == practice_id), None)
    if practice:
        sustainable_practices = [p for p in sustainable_practices if p["id"] != practice_id]
        return jsonify({"message": "Practice deleted successfully"}), 200
    else:
        return jsonify({"error": "Practice not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
