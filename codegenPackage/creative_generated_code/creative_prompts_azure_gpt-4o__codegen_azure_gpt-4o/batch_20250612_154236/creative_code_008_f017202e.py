"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Design an API endpoint to fetch genuine aftermarket replacement parts for BPL appliances, including details like part type, availability, and pricing.
Generated: DETERMINISTIC_f017202eb40eab33
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing aftermarket replacement parts for BPL appliances
replacement_parts = [
    {"part_id": 1, "type": "Compressor", "availability": True, "price": 150.00},
    {"part_id": 2, "type": "Thermostat", "availability": True, "price": 25.00},
    {"part_id": 3, "type": "Fan Motor", "availability": False, "price": 75.00},
    {"part_id": 4, "type": "Water Filter", "availability": True, "price": 30.00},
]

@app.route('/api/replacement_parts', methods=['GET'])
def get_replacement_parts():
    """
    API endpoint to fetch aftermarket replacement parts for BPL appliances.
    Query parameters (optional):
    - type: Filter parts by type (e.g., Compressor, Thermostat).
    - availability: Filter parts based on availability (True/False).

    Returns:
        JSON response containing the filtered list of replacement parts.
    """
    try:
        # Get query parameters
        part_type = request.args.get('type')
        availability = request.args.get('availability')

        # Filter replacement parts based on query parameters
        filtered_parts = replacement_parts

        if part_type:
            filtered_parts = [part for part in filtered_parts if part['type'].lower() == part_type.lower()]
        
        if availability:
            try:
                availability_bool = availability.lower() in ['true', '1']
                filtered_parts = [part for part in filtered_parts if part['availability'] == availability_bool]
            except ValueError:
                logging.error(f"Invalid availability value: {availability}")
                return jsonify({"error": "Invalid availability parameter. Must be true or false."}), 400

        # Return the filtered parts as a JSON response
        return jsonify(filtered_parts)

    except Exception as e:
        logging.error(f"Error fetching replacement parts: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
