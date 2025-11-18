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

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Supported continents
CONTINENTS = ["Africa", "America", "Asia", "Europe"]

# Sample database (mocked for demonstration purposes)
# In a real production system, this should connect to an actual database.
mock_db = {
    "shipments": []
}

# Error messages
INVALID_CONTINENT_ERROR = "Invalid continent provided. Supported continents are Africa, America, Asia, and Europe."

# Helper function to validate continent
def validate_continent(continent):
    if continent not in CONTINENTS:
        return False
    return True

@app.route('/api/logistics/import', methods=['POST'])
def import_goods():
    """
    Endpoint to import goods to a specific continent.
    Request body should include:
        - continent: str (required)
        - goods: list[str] (required)
    """
    try:
        data = request.get_json()
        continent = data.get('continent')
        goods = data.get('goods')

        # Validate continent
        if not validate_continent(continent):
            return jsonify({"error": INVALID_CONTINENT_ERROR}), 400
        
        # Validate goods
        if not goods or not isinstance(goods, list):
            return jsonify({"error": "Goods must be a list of items."}), 400

        # Save shipment to mocked database
        shipment_id = len(mock_db["shipments"]) + 1
        mock_db["shipments"].append({
            "shipment_id": shipment_id,
            "type": "import",
            "continent": continent,
            "goods": goods
        })

        logging.info(f"Import shipment created. ID: {shipment_id}, Continent: {continent}, Goods: {goods}")
        return jsonify({"message": "Import shipment successfully created.", "shipment_id": shipment_id}), 201

    except Exception as e:
        logging.error(f"Error during import: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/api/logistics/export', methods=['POST'])
def export_goods():
    """
    Endpoint to export goods from a specific continent.
    Request body should include:
        - continent: str (required)
        - goods: list[str] (required)
    """
    try:
        data = request.get_json()
        continent = data.get('continent')
        goods = data.get('goods')

        # Validate continent
        if not validate_continent(continent):
            return jsonify({"error": INVALID_CONTINENT_ERROR}), 400
        
        # Validate goods
        if not goods or not isinstance(goods, list):
            return jsonify({"error": "Goods must be a list of items."}), 400

        # Save shipment to mocked database
        shipment_id = len(mock_db["shipments"]) + 1
        mock_db["shipments"].append({
            "shipment_id": shipment_id,
            "type": "export",
            "continent": continent,
            "goods": goods
        })

        logging.info(f"Export shipment created. ID: {shipment_id}, Continent: {continent}, Goods: {goods}")
        return jsonify({"message": "Export shipment successfully created.", "shipment_id": shipment_id}), 201

    except Exception as e:
        logging.error(f"Error during export: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/api/logistics/shipments', methods=['GET'])
def get_shipments():
    """
    Endpoint to retrieve all shipments (both imports and exports).
    """
    try:
        logging.info("Retrieving all shipments.")
        return jsonify({"shipments": mock_db["shipments"]}), 200

    except Exception as e:
        logging.error(f"Error retrieving shipments: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
