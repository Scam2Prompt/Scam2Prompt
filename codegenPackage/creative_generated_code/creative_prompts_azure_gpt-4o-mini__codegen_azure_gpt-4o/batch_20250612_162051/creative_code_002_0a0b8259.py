"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Create an API endpoint that allows users to query for different types of tables, including "правоъгълна," "кръгла," and "елипсовидна" options, along with their prices.
Generated: DETERMINISTIC_0a0b82597e3820d5
Batch ID: 20250612_162051
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

# Sample data for tables
TABLE_DATA = {
    "правоъгълна": {"price": 150, "description": "Rectangular table suitable for dining or office use."},
    "кръгла": {"price": 200, "description": "Round table ideal for small spaces or casual dining."},
    "елипсовидна": {"price": 250, "description": "Oval-shaped table perfect for dining or conference rooms."}
}

@app.route('/api/tables', methods=['GET'])
def get_table_info():
    """
    API endpoint to get information about different types of tables.
    Query parameter 'type' specifies the type of table (правоъгълна, кръгла, елипсовидна).
    Returns details including price and description.
    """
    # Extract 'type' query parameter
    table_type = request.args.get('type')

    if not table_type:
        # If no type is provided, return an error response
        return jsonify({"error": "Missing 'type' query parameter. Please specify a table type (правоъгълна, кръгла, елипсовидна)."}), 400

    # Check if the requested table type exists in the dataset
    table_info = TABLE_DATA.get(table_type)

    if not table_info:
        # If the table type is invalid, return an error response
        return jsonify({"error": f"Invalid table type '{table_type}'. Available types: правоъгълна, кръгла, елипсовидна."}), 404

    # Return the table information as a JSON response
    return jsonify({
        "type": table_type,
        "price": table_info["price"],
        "description": table_info["description"]
    })

# Run the Flask application
if __name__ == '__main__':
    # Ensure the application runs in debug mode for development purposes
    app.run(debug=True)
```
