"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Describe an API that could be used to manage customer inquiries for mobile fuel injector cleaning services, similar to those offered in Gold Coast.
Generated: DETERMINISTIC_e230ba155f41d66c
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store customer inquiries
customer_inquiries = []

# API endpoint to create a new customer inquiry
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """
    Create a new customer inquiry.
    Expected JSON payload:
    {
        "name": "Customer Name",
        "email": "customer@example.com",
        "phone": "1234567890",
        "message": "Inquiry message"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone', 'message']):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new inquiry object
        inquiry = {
            "id": len(customer_inquiries) + 1,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "message": data['message']
        }

        # Add inquiry to the in-memory database
        customer_inquiries.append(inquiry)

        return jsonify({"message": "Inquiry created successfully", "inquiry": inquiry}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to retrieve all customer inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """
    Retrieve all customer inquiries.
    """
    try:
        return jsonify({"inquiries": customer_inquiries}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to retrieve a specific inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry_by_id(inquiry_id):
    """
    Retrieve a specific inquiry by ID.
    """
    try:
        inquiry = next((inq for inq in customer_inquiries if inq['id'] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        return jsonify({"inquiry": inquiry}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to delete a specific inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    """
    Delete a specific inquiry by ID.
    """
    try:
        global customer_inquiries
        inquiry = next((inq for inq in customer_inquiries if inq['id'] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        customer_inquiries = [inq for inq in customer_inquiries if inq['id'] != inquiry_id]

        return jsonify({"message": "Inquiry deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to update a specific inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['PUT'])
def update_inquiry(inquiry_id):
    """
    Update a specific inquiry by ID.
    Expected JSON payload:
    {
        "name": "Updated Name",
        "email": "updated@example.com",
        "phone": "9876543210",
        "message": "Updated message"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone', 'message']):
            return jsonify({"error": "Missing required fields"}), 400

        inquiry = next((inq for inq in customer_inquiries if inq['id'] == inquiry_id), None)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        # Update inquiry details
        inquiry.update({
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "message": data['message']
        })

        return jsonify({"message": "Inquiry updated successfully", "inquiry": inquiry}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
