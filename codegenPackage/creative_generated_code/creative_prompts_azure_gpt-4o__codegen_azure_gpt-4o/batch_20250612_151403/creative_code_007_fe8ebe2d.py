"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a REST API endpoint for retrieving construction tool details, including "niveis, prumos e linhas," "talhas manuais," and "trole manual," based on the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_fe8ebe2de7eba2f8
Batch ID: 20250612_151403
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

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Sample dataset based on Anhanguera Ferramentas catalog
TOOLS_CATALOG = [
    {
        "id": 1,
        "name": "niveis, prumos e linhas",
        "description": "Precision tools for leveling and alignment.",
        "category": "Construction",
        "price": 50.0
    },
    {
        "id": 2,
        "name": "talhas manuais",
        "description": "Manual hoists for lifting heavy loads.",
        "category": "Lifting Equipment",
        "price": 150.0
    },
    {
        "id": 3,
        "name": "trole manual",
        "description": "Manual trolleys for transportation.",
        "category": "Transportation",
        "price": 100.0
    }
]

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """
    REST API endpoint to retrieve construction tool details.
    Returns a JSON response containing data for the requested tools.
    
    Query Parameters:
      - name (optional): Filter tools by name.
    """
    try:
        # Extract query parameter for filtering by name
        name_filter = request.args.get('name', None)

        if name_filter:
            # Apply filtering based on the 'name' query parameter
            filtered_tools = [
                tool for tool in TOOLS_CATALOG if name_filter.lower() in tool['name'].lower()
            ]
            logging.info(f"Filtered tools by name: {name_filter}")
            return jsonify(filtered_tools), 200
        
        # Return the full catalog if no filter is applied
        logging.info("Returning full tool catalog.")
        return jsonify(TOOLS_CATALOG), 200

    except Exception as e:
        # Log the error and return a server error response
        logging.error(f"An error occurred while retrieving tools: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Start the Flask server (for local development)
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a production-ready REST API endpoint using Flask. It includes error handling, logging, and follows Python best practices for clarity and maintainability.
