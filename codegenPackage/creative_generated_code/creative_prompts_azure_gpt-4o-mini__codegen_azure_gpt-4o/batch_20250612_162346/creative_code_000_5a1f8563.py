"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaptadtours.com
Prompt: Generate a code snippet for a travel booking API that includes options for trekking the Everest Base Camp, highlighting its challenging nature and stunning views.
Generated: DETERMINISTIC_5a1f8563453214e8
Batch ID: 20250612_162346
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

# Sample data for trekking packages
trekking_packages = [
    {
        "id": 1,
        "name": "Everest Base Camp Trek",
        "duration": "14 days",
        "difficulty": "Challenging",
        "description": "A breathtaking trek to Everest Base Camp with stunning views of the Himalayas.",
        "price": 1500,
        "available": True
    },
    {
        "id": 2,
        "name": "Annapurna Circuit Trek",
        "duration": "10 days",
        "difficulty": "Moderate",
        "description": "Explore the diverse landscapes and culture of the Annapurna region.",
        "price": 1200,
        "available": True
    }
]

# Error handling for invalid package ID
def find_package_by_id(package_id):
    for package in trekking_packages:
        if package["id"] == package_id:
            return package
    return None

@app.route('/api/trekking_packages', methods=['GET'])
def get_trekking_packages():
    """
    Endpoint to retrieve all trekking packages.
    """
    return jsonify({"success": True, "data": trekking_packages}), 200

@app.route('/api/trekking_packages/<int:package_id>', methods=['GET'])
def get_trekking_package_by_id(package_id):
    """
    Endpoint to retrieve a specific trekking package by ID.
    """
    package = find_package_by_id(package_id)
    if package:
        return jsonify({"success": True, "data": package}), 200
    else:
        return jsonify({"success": False, "error": "Package not found"}), 404

@app.route('/api/book', methods=['POST'])
def book_trekking_package():
    """
    Endpoint to book a trekking package.
    """
    try:
        data = request.get_json()
        package_id = data.get("package_id")
        user_name = data.get("user_name")
        user_email = data.get("user_email")

        if not package_id or not user_name or not user_email:
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        package = find_package_by_id(package_id)
        if not package:
            return jsonify({"success": False, "error": "Package not found"}), 404

        if not package["available"]:
            return jsonify({"success": False, "error": "Package is currently unavailable"}), 400

        # Simulate successful booking
        return jsonify({
            "success": True,
            "message": f"Successfully booked {package['name']} for {user_name} ({user_email})!"
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # App runs on localhost:5000 by default
    app.run(debug=True)
```
