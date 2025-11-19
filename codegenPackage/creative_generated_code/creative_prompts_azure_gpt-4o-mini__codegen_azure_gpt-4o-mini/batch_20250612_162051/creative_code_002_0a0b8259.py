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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for tables and their prices
TABLES_DATA = {
    "правоъгълна": {"price": 200},
    "кръгла": {"price": 150},
    "елипсовидна": {"price": 180}
}

@app.route('/api/tables', methods=['GET'])
def get_tables():
    """
    API endpoint to retrieve table types and their prices.
    Query parameter 'type' can be used to filter specific table types.
    If 'type' is not provided, all table types will be returned.
    """
    try:
        table_type = request.args.get('type')
        
        # If a specific table type is requested
        if table_type:
            table_info = TABLES_DATA.get(table_type)
            if table_info:
                return jsonify({table_type: table_info}), 200
            else:
                return jsonify({"error": "Table type not found."}), 404
        else:
            # Return all table types if no filter is applied
            return jsonify(TABLES_DATA), 200
    
    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install Flask before running this code:
```bash
pip install Flask
```
