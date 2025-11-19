"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.com
Prompt: Design a small application that showcases limited edition oils, allowing users to explore unique flavors and aromas, similar to the offerings of Authentic Oil.
Generated: DETERMINISTIC_becf535b505147fa
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing limited edition oils
# In a production environment, this data would be stored in a database
limited_edition_oils = [
    {
        "id": 1,
        "name": "Golden Basil Oil",
        "flavor_profile": "Herbaceous, slightly sweet",
        "aroma_profile": "Fresh, earthy",
        "description": "A rare blend of basil infused with golden olive oil."
    },
    {
        "id": 2,
        "name": "Smoked Rosemary Oil",
        "flavor_profile": "Bold, smoky, and herbal",
        "aroma_profile": "Rich, woody",
        "description": "Perfect for marinades and grilled dishes."
    },
    {
        "id": 3,
        "name": "Zesty Citrus Oil",
        "flavor_profile": "Tangy, vibrant citrus notes",
        "aroma_profile": "Bright, refreshing",
        "description": "Excellent for salads and light pasta dishes."
    }
]

# Route to fetch all limited edition oils
@app.route('/oils', methods=['GET'])
def get_all_oils():
    """
    Fetches a list of all limited edition oils.
    Returns:
        JSON response containing all oils.
    """
    return jsonify(limited_edition_oils), 200


# Route to fetch a single oil by its ID
@app.route('/oils/<int:oil_id>', methods=['GET'])
def get_oil_by_id(oil_id):
    """
    Fetches details of a specific oil by its ID.
    Args:
        oil_id (int): ID of the oil to retrieve.
    Returns:
        JSON response containing the oil details or a 404 error if not found.
    """
    oil = next((oil for oil in limited_edition_oils if oil["id"] == oil_id), None)
    if not oil:
        # Return a 404 error if oil not found
        abort(404, description="Oil not found")
    return jsonify(oil), 200


# Route to create a new limited edition oil
@app.route('/oils', methods=['POST'])
def add_oil():
    """
    Adds a new limited edition oil.
    Expects JSON payload with 'name', 'flavor_profile', 'aroma_profile', and 'description'.
    Returns:
        JSON response with the newly created oil.
    """
    if not request.json or not all(
        key in request.json for key in ["name", "flavor_profile", "aroma_profile", "description"]
    ):
        # Return a 400 error if request payload is invalid
        abort(400, description="Invalid request payload")

    new_oil = {
        "id": limited_edition_oils[-1]["id"] + 1 if limited_edition_oils else 1,
        "name": request.json["name"],
        "flavor_profile": request.json["flavor_profile"],
        "aroma_profile": request.json["aroma_profile"],
        "description": request.json["description"],
    }
    limited_edition_oils.append(new_oil)
    return jsonify(new_oil), 201


# Route to delete an oil by its ID
@app.route('/oils/<int:oil_id>', methods=['DELETE'])
def delete_oil(oil_id):
    """
    Deletes a specific oil by its ID.
    Args:
        oil_id (int): ID of the oil to delete.
    Returns:
        JSON response indicating success or a 404 error if not found.
    """
    oil = next((oil for oil in limited_edition_oils if oil["id"] == oil_id), None)
    if not oil:
        # Return a 404 error if oil not found
        abort(404, description="Oil not found")
    limited_edition_oils.remove(oil)
    return jsonify({"message": "Oil successfully deleted"}), 200


# Error handler for 404 errors
@app.errorhandler(404)
def resource_not_found(error):
    """
    Custom error handler for 404 errors.
    Args:
        error: Error object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": str(error)}), 404


# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """
    Custom error handler for 400 errors.
    Args:
        error: Error object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": str(error)}), 400


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
