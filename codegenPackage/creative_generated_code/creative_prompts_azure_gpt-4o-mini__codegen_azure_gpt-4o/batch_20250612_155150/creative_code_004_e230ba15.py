"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Describe an API that could be used to manage customer inquiries for mobile fuel injector cleaning services, similar to those offered in Gold Coast.
Generated: DETERMINISTIC_e230ba155f41d66c
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store customer inquiries (for demonstration purposes)
customer_inquiries = []


@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """
    Endpoint to retrieve all customer inquiries.
    Returns:
        JSON response containing a list of all customer inquiries.
    """
    return jsonify({"status": "success", "data": customer_inquiries}), 200


@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """
    Endpoint to create a new customer inquiry.
    Expects:
        JSON payload with keys: 'name', 'email', 'phone', and 'message'.
    Returns:
        JSON response with the created inquiry and status.
    """
    try:
        # Parse and validate request data
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Ensure all fields are provided
        if not all([name, email, phone, message]):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        # Create a new inquiry object
        inquiry = {
            "id": len(customer_inquiries) + 1,  # Auto-incrementing ID
            "name": name,
            "email": email,
            "phone": phone,
            "message": message
        }
        customer_inquiries.append(inquiry)

        return jsonify({"status": "success", "data": inquiry}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500


@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry_by_id(inquiry_id):
    """
    Endpoint to retrieve a specific inquiry by ID.
    Args:
        inquiry_id (int): ID of the inquiry to retrieve.
    Returns:
        JSON response with the requested inquiry or error message.
    """
    inquiry = next((i for i in customer_inquiries if i['id'] == inquiry_id), None)
    if inquiry:
        return jsonify({"status": "success", "data": inquiry}), 200
    else:
        return jsonify({"status": "error", "message": "Inquiry not found"}), 404


@app.route('/api/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    """
    Endpoint to delete a specific inquiry by ID.
    Args:
        inquiry_id (int): ID of the inquiry to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    global customer_inquiries
    inquiry = next((i for i in customer_inquiries if i['id'] == inquiry_id), None)
    if inquiry:
        customer_inquiries = [i for i in customer_inquiries if i['id'] != inquiry_id]
        return jsonify({"status": "success", "message": "Inquiry deleted successfully"}), 200
    else:
        return jsonify({"status": "error", "message": "Inquiry not found"}), 404


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
