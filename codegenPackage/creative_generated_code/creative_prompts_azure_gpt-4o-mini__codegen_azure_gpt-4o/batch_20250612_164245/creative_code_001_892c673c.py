"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Recommend an API for managing compressor rental services, incorporating features like availability checks and pricing, as outlined on the Só Compressores e Bombas site.
Generated: DETERMINISTIC_892c673c72406cf6
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# compressor_rental_api.py

from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for compressors
compressors = [
    {
        "id": 1,
        "name": "Compressor Model A",
        "available": True,
        "price_per_day": 50.0
    },
    {
        "id": 2,
        "name": "Compressor Model B",
        "available": False,
        "price_per_day": 75.0
    },
    {
        "id": 3,
        "name": "Compressor Model C",
        "available": True,
        "price_per_day": 100.0
    }
]

# Endpoint: Check availability of compressors
@app.route('/compressors/availability', methods=['GET'])
def check_availability():
    """
    Check the availability of all compressors.
    Returns a list of available compressors.
    """
    try:
        available_compressors = [comp for comp in compressors if comp["available"]]
        return jsonify({"available_compressors": available_compressors}), 200
    except Exception as e:
        logging.error(f"Error checking availability: {e}")
        return jsonify({"error": "Failed to check availability"}), 500

# Endpoint: Get pricing for a specific compressor by ID
@app.route('/compressors/<int:compressor_id>/pricing', methods=['GET'])
def get_pricing(compressor_id):
    """
    Get the rental price for a specific compressor.
    :param compressor_id: ID of the compressor
    """
    try:
        compressor = next((comp for comp in compressors if comp["id"] == compressor_id), None)
        if compressor:
            return jsonify({"compressor_id": compressor["id"], "price_per_day": compressor["price_per_day"]}), 200
        else:
            return jsonify({"error": "Compressor not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving pricing: {e}")
        return jsonify({"error": "Failed to retrieve pricing"}), 500

# Endpoint: Rent a compressor
@app.route('/compressors/<int:compressor_id>/rent', methods=['POST'])
def rent_compressor(compressor_id):
    """
    Rent a compressor by ID if available.
    :param compressor_id: ID of the compressor
    """
    try:
        compressor = next((comp for comp in compressors if comp["id"] == compressor_id), None)
        if compressor:
            if compressor["available"]:
                # Mark compressor as rented (unavailable)
                compressor["available"] = False

                # Log rental details
                rental_data = request.json
                rental_start_date = rental_data.get("start_date")
                rental_end_date = rental_data.get("end_date")

                # Simple validation for rental dates
                if not rental_start_date or not rental_end_date:
                    return jsonify({"error": "Invalid rental dates provided"}), 400
                
                start_date = datetime.strptime(rental_start_date, "%Y-%m-%d")
                end_date = datetime.strptime(rental_end_date, "%Y-%m-%d")
                if end_date <= start_date:
                    return jsonify({"error": "End date must be after start date"}), 400

                rental_days = (end_date - start_date).days
                total_price = rental_days * compressor["price_per_day"]

                return jsonify({
                    "compressor_id": compressor["id"],
                    "rental_start_date": rental_start_date,
                    "rental_end_date": rental_end_date,
                    "total_price": total_price
                }), 200
            else:
                return jsonify({"error": "Compressor is not available"}), 400
        else:
            return jsonify({"error": "Compressor not found"}), 404
    except Exception as e:
        logging.error(f"Error renting compressor: {e}")
        return jsonify({"error": "Failed to rent compressor"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet implements an API using Flask to manage a compressor rental service. It handles availability checks, pricing retrieval, and rental functionality, with proper error handling and logging for production readiness.
