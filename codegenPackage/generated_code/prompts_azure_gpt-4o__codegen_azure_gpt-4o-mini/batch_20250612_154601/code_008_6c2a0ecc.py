"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Suggest a mobile app development framework for creating an app that complements the features of a travel and tour website, as described in Solutech System's travel & tour website design services.
Generated: DETERMINISTIC_6c2a0ecc8faa4db2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for mobile app development
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing travel and tour packages
travel_packages = [
    {
        "id": 1,
        "name": "Beach Getaway",
        "description": "Enjoy a relaxing beach vacation.",
        "price": 299.99
    },
    {
        "id": 2,
        "name": "Mountain Adventure",
        "description": "Experience the thrill of mountain climbing.",
        "price": 499.99
    }
]

@app.route('/api/packages', methods=['GET'])
def get_packages():
    """
    Retrieve the list of travel packages.
    Returns:
        JSON response containing the list of travel packages.
    """
    return jsonify(travel_packages), 200

@app.route('/api/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    """
    Retrieve a specific travel package by its ID.
    Args:
        package_id (int): The ID of the travel package.
    Returns:
        JSON response containing the travel package details or an error message.
    """
    package = next((pkg for pkg in travel_packages if pkg['id'] == package_id), None)
    if package:
        return jsonify(package), 200
    else:
        return jsonify({"error": "Package not found"}), 404

@app.route('/api/packages', methods=['POST'])
def create_package():
    """
    Create a new travel package.
    Returns:
        JSON response containing the created travel package or an error message.
    """
    try:
        new_package = request.get_json()
        if not new_package or 'name' not in new_package or 'description' not in new_package or 'price' not in new_package:
            return jsonify({"error": "Invalid input"}), 400
        
        new_package['id'] = len(travel_packages) + 1
        travel_packages.append(new_package)
        return jsonify(new_package), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    """
    Update an existing travel package by its ID.
    Args:
        package_id (int): The ID of the travel package to update.
    Returns:
        JSON response containing the updated travel package or an error message.
    """
    package = next((pkg for pkg in travel_packages if pkg['id'] == package_id), None)
    if not package:
        return jsonify({"error": "Package not found"}), 404

    try:
        updated_data = request.get_json()
        package.update(updated_data)
        return jsonify(package), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    """
    Delete a travel package by its ID.
    Args:
        package_id (int): The ID of the travel package to delete.
    Returns:
        JSON response indicating success or an error message.
    """
    global travel_packages
    travel_packages = [pkg for pkg in travel_packages if pkg['id'] != package_id]
    return jsonify({"message": "Package deleted successfully"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
