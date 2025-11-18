"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Create a logistics API integration for importing and exporting goods to and from Africa, America, Asia, and Europe, inspired by Olgadorks Shipping Company Limited's global reach.
Generated: DETERMINISTIC_193966c19b8b5640
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Sample in-memory database for demonstration purposes
shipments_db = []

# Define a shipment data model
class Shipment:
    def __init__(self, id, origin, destination, goods, quantity):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.goods = goods
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "origin": self.origin,
            "destination": self.destination,
            "goods": self.goods,
            "quantity": self.quantity,
        }


@app.route('/shipments', methods=['POST'])
def create_shipment():
    """
    Create a new shipment entry.
    Request JSON should include: origin, destination, goods, quantity
    """
    try:
        data = request.get_json()
        
        # Validate request data
        if not all(key in data for key in ['origin', 'destination', 'goods', 'quantity']):
            logging.error("Invalid request data: %s", data)
            return jsonify({"error": "Invalid request data"}), 400

        # Create a new shipment
        shipment_id = len(shipments_db) + 1
        shipment = Shipment(
            id=shipment_id,
            origin=data['origin'],
            destination=data['destination'],
            goods=data['goods'],
            quantity=data['quantity']
        )
        shipments_db.append(shipment)
        
        logging.info("Shipment created successfully: %s", shipment.to_dict())
        return jsonify(shipment.to_dict()), 201
    
    except Exception as e:
        logging.exception("Error creating shipment: %s", e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    """
    Retrieve a shipment by its ID.
    """
    try:
        shipment = next((s for s in shipments_db if s.id == shipment_id), None)
        
        if shipment is None:
            logging.warning("Shipment not found: ID %d", shipment_id)
            return jsonify({"error": "Shipment not found"}), 404
        
        return jsonify(shipment.to_dict()), 200
    
    except Exception as e:
        logging.exception("Error retrieving shipment: %s", e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/shipments', methods=['GET'])
def list_shipments():
    """
    List all shipments.
    """
    try:
        return jsonify([shipment.to_dict() for shipment in shipments_db]), 200
    except Exception as e:
        logging.exception("Error listing shipments: %s", e)
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Instructions for Running the Code
1. Ensure you have Flask installed. If not, install it using:
   ```bash
   pip install Flask
   ```

2. Save the code in a file named `logistics_api.py`.

3. Run the API using:
   ```bash
   python logistics_api.py
   ```

4. Access the API endpoints via HTTP requests (e.g., using Postman or cURL).

### API Endpoints
- `POST /shipments`: Create a shipment.
- `GET /shipments/<id>`: Retrieve a specific shipment by ID.
- `GET /shipments`: List all shipments.
