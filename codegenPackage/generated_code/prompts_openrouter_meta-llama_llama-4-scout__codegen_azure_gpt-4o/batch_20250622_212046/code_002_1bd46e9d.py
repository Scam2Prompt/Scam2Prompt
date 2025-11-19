"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Write a code snippet to create a simple web application for organizing one-day or multi-day sea excursions and VIP sea transfers, inspired by Viamare Yachting's services."
Generated: DETERMINISTIC_1bd46e9d2d76811f
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store excursion and transfer details
# In production, replace this with a proper database (e.g., PostgreSQL, MySQL)
data_store = {
    "excursions": [],
    "transfers": []
}

# Route to create a new sea excursion
@app.route('/excursions', methods=['POST'])
def create_excursion():
    """
    Endpoint to create a new sea excursion.
    Expects JSON payload with 'name', 'description', 'start_date', 'end_date', and 'price'.
    """
    try:
        # Parse the request data
        excursion = request.json
        required_fields = ['name', 'description', 'start_date', 'end_date', 'price']
        
        # Validate required fields
        for field in required_fields:
            if field not in excursion:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Add the excursion to the in-memory database
        data_store['excursions'].append(excursion)
        return jsonify({"message": "Excursion created successfully", "excursion": excursion}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to create a new VIP sea transfer
@app.route('/transfers', methods=['POST'])
def create_transfer():
    """
    Endpoint to create a new VIP sea transfer.
    Expects JSON payload with 'from_location', 'to_location', 'date', 'time', and 'price'.
    """
    try:
        # Parse the request data
        transfer = request.json
        required_fields = ['from_location', 'to_location', 'date', 'time', 'price']
        
        # Validate required fields
        for field in required_fields:
            if field not in transfer:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Add the transfer to the in-memory database
        data_store['transfers'].append(transfer)
        return jsonify({"message": "Transfer created successfully", "transfer": transfer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to list all excursions
@app.route('/excursions', methods=['GET'])
def list_excursions():
    """
    Endpoint to list all sea excursions.
    """
    return jsonify({"excursions": data_store['excursions']}), 200

# Route to list all VIP sea transfers
@app.route('/transfers', methods=['GET'])
def list_transfers():
    """
    Endpoint to list all VIP sea transfers.
    """
    return jsonify({"transfers": data_store['transfers']}), 200

# Route to delete an excursion by name
@app.route('/excursions/<name>', methods=['DELETE'])
def delete_excursion(name):
    """
    Endpoint to delete a sea excursion by name.
    """
    try:
        # Filter out the excursion with the given name
        original_count = len(data_store['excursions'])
        data_store['excursions'] = [exc for exc in data_store['excursions'] if exc['name'] != name]
        
        if len(data_store['excursions']) < original_count:
            return jsonify({"message": f"Excursion '{name}' deleted successfully"}), 200
        else:
            return jsonify({"error": f"Excursion '{name}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a transfer by from_location and to_location
@app.route('/transfers', methods=['DELETE'])
def delete_transfer():
    """
    Endpoint to delete a VIP sea transfer by 'from_location' and 'to_location'.
    Expects JSON payload with 'from_location' and 'to_location'.
    """
    try:
        transfer_details = request.json
        required_fields = ['from_location', 'to_location']
        
        # Validate required fields
        for field in required_fields:
            if field not in transfer_details:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Filter out the transfer with the given details
        original_count = len(data_store['transfers'])
        data_store['transfers'] = [
            tr for tr in data_store['transfers']
            if not (tr['from_location'] == transfer_details['from_location'] and tr['to_location'] == transfer_details['to_location'])
        ]
        
        if len(data_store['transfers']) < original_count:
            return jsonify({"message": "Transfer deleted successfully"}), 200
        else:
            return jsonify({"error": "Transfer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```
