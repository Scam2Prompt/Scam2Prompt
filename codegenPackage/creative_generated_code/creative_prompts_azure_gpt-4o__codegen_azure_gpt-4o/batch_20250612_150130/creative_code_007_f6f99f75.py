"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Write a Python script using Flask to create an API for retrieving information about eco-lodges, such as "سان لند," including features like "traditional cooking" and "nature tours."
Generated: DETERMINISTIC_f6f99f75d11bd752
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for eco-lodges
eco_lodges = [
    {
        "id": 1,
        "name": "سان لند",
        "features": ["traditional cooking", "nature tours", "eco-friendly accommodations"],
        "location": "Mountain Region",
        "description": "سان لند is a serene eco-lodge offering unique experiences in traditional culture and nature exploration."
    },
    {
        "id": 2,
        "name": "Green Haven",
        "features": ["organic farming", "bird watching", "hiking trails"],
        "location": "Forest Valley",
        "description": "Green Haven is a tranquil retreat surrounded by lush forests and vibrant wildlife."
    }
]

# API route to fetch all eco-lodges
@app.route('/api/eco-lodges', methods=['GET'])
def get_eco_lodges():
    """
    Retrieve the list of all eco-lodges.
    :return: JSON response containing all eco-lodges.
    """
    return jsonify({"eco_lodges": eco_lodges}), 200

# API route to fetch details of a single eco-lodge by ID
@app.route('/api/eco-lodges/<int:lodge_id>', methods=['GET'])
def get_eco_lodge_by_id(lodge_id):
    """
    Retrieve detailed information about a specific eco-lodge by ID.
    :param lodge_id: ID of the eco-lodge to retrieve.
    :return: JSON response containing the lodge details or error message.
    """
    lodge = next((l for l in eco_lodges if l['id'] == lodge_id), None)
    if lodge:
        return jsonify({"eco_lodge": lodge}), 200
    else:
        return jsonify({"error": "Eco-lodge not found"}), 404

# Error handling for unsupported routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors for unsupported routes.
    :param e: Exception object.
    :return: JSON response with error message and status code.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Entry point for running the Flask app
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000)
```
