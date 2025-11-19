"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: Recommend an API for integrating wedding photography packages and pricing into a website, inspired by the services provided by Yaisa Tangwell Photography.
Generated: DETERMINISTIC_ffbe1aa69ad2aa56
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a simple Flask-based API for integrating wedding photography packages and pricing into a website.
Inspired by services like Yaisa Tangwell Photography, the API allows users to retrieve package details and pricing.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing wedding photography packages
# In a production environment, this data would typically come from a database.
photography_packages = [
    {
        "id": 1,
        "name": "Basic Package",
        "description": "Includes 4 hours of coverage, 50 edited photos, and an online gallery.",
        "price": 1000.00
    },
    {
        "id": 2,
        "name": "Standard Package",
        "description": "Includes 8 hours of coverage, 100 edited photos, an online gallery, and a USB drive.",
        "price": 2000.00
    },
    {
        "id": 3,
        "name": "Premium Package",
        "description": "Includes full-day coverage, 200 edited photos, an online gallery, a USB drive, and a photo album.",
        "price": 3500.00
    }
]

@app.route('/api/packages', methods=['GET'])
def get_packages():
    """
    Endpoint to retrieve all wedding photography packages.
    Returns:
        JSON response containing all packages.
    """
    return jsonify({"packages": photography_packages}), 200

@app.route('/api/packages/<int:package_id>', methods=['GET'])
def get_package_by_id(package_id):
    """
    Endpoint to retrieve a specific wedding photography package by ID.
    Args:
        package_id (int): ID of the package to retrieve.
    Returns:
        JSON response containing the package details or an error message if not found.
    """
    package = next((pkg for pkg in photography_packages if pkg["id"] == package_id), None)
    if package:
        return jsonify({"package": package}), 200
    else:
        return jsonify({"error": "Package not found"}), 404

@app.route('/api/packages', methods=['POST'])
def add_package():
    """
    Endpoint to add a new wedding photography package.
    Expects JSON payload with 'name', 'description', and 'price'.
    Returns:
        JSON response with the newly added package or an error message if the input is invalid.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "price")):
            return jsonify({"error": "Invalid input. 'name', 'description', and 'price' are required."}), 400
        
        new_package = {
            "id": len(photography_packages) + 1,
            "name": data["name"],
            "description": data["description"],
            "price": float(data["price"])
        }
        photography_packages.append(new_package)
        return jsonify({"message": "Package added successfully", "package": new_package}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    """
    Endpoint to delete a wedding photography package by ID.
    Args:
        package_id (int): ID of the package to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global photography_packages
    package = next((pkg for pkg in photography_packages if pkg["id"] == package_id), None)
    if package:
        photography_packages = [pkg for pkg in photography_packages if pkg["id"] != package_id]
        return jsonify({"message": "Package deleted successfully"}), 200
    else:
        return jsonify({"error": "Package not found"}), 404

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response indicating an internal server error occurred.
    """
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
