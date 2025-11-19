"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmonyrecycle.net
Prompt: What are the best practices for developing a mobile app that educates users about recycling and waste management?
Generated: DETERMINISTIC_04e8bf92421e8396
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a mobile app
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data: List of recycling facts
recycling_facts = [
    {"id": 1, "fact": "Recycling one aluminum can saves enough energy to run a TV for three hours."},
    {"id": 2, "fact": "Plastic bottles can take up to 450 years to decompose."},
    {"id": 3, "fact": "Recycling paper uses 70% less energy than making new paper from trees."}
]

@app.route('/facts', methods=['GET'])
def get_facts():
    """
    Endpoint to retrieve recycling facts.
    Returns a JSON list of recycling facts.
    """
    return jsonify(recycling_facts), 200

@app.route('/facts/<int:fact_id>', methods=['GET'])
def get_fact(fact_id):
    """
    Endpoint to retrieve a specific recycling fact by ID.
    :param fact_id: ID of the recycling fact
    :return: JSON object of the recycling fact or 404 if not found
    """
    # Search for the recycling fact by ID
    fact = next((fact for fact in recycling_facts if fact["id"] == fact_id), None)
    if fact is None:
        return jsonify({"error": "Fact not found"}), 404
    return jsonify(fact), 200

@app.route('/facts', methods=['POST'])
def add_fact():
    """
    Endpoint to add a new recycling fact.
    :return: JSON object of the added fact with 201 status code
    """
    try:
        # Get the fact from the request body
        new_fact = request.json.get('fact', '')
        if not new_fact:
            return jsonify({"error": "Fact is required"}), 400

        # Create a new fact object and add it to the facts list
        new_id = max(fact["id"] for fact in recycling_facts) + 1
        recycling_facts.append({"id": new_id, "fact": new_fact})
        return jsonify({"id": new_id, "fact": new_fact}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/facts/<int:fact_id>', methods=['DELETE'])
def delete_fact(fact_id):
    """
    Endpoint to delete a specific recycling fact by ID.
    :param fact_id: ID of the recycling fact
    :return: JSON object confirming deletion or 404 if not found
    """
    global recycling_facts
    recycling_facts = [fact for fact in recycling_facts if fact["id"] != fact_id]
    return jsonify({"message": "Fact deleted"}), 200

if __name__ == '__main__':
    try:
        # Run the app on localhost with debug enabled
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the application: {str(e)}")
```
