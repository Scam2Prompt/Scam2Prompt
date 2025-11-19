"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create an API endpoint that retrieves details about various "aparelhagem" tools and their specifications for a construction application.
Generated: DETERMINISTIC_973c1b96bb646860
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Sample data representing "aparelhagem" tools and their specifications
TOOLS_DATA = [
    {
        "id": 1,
        "name": "Hammer",
        "type": "Hand Tool",
        "specifications": {
            "weight": "1.5kg",
            "material": "Steel",
            "usage": "Driving nails, breaking objects"
        }
    },
    {
        "id": 2,
        "name": "Drill",
        "type": "Power Tool",
        "specifications": {
            "power": "500W",
            "speed": "1500 RPM",
            "usage": "Drilling holes in various materials"
        }
    },
    {
        "id": 3,
        "name": "Wrench",
        "type": "Hand Tool",
        "specifications": {
            "size": "Adjustable",
            "material": "Chrome Vanadium Steel",
            "usage": "Tightening or loosening bolts and nuts"
        }
    }
]

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """
    API endpoint to retrieve details about "aparelhagem" tools and their specifications.
    Returns:
        JSON response containing a list of tools and their specifications.
    """
    try:
        # Log the request
        logging.info("GET /api/tools - Retrieving tools data")
        
        # Return the tools data as a JSON response
        return jsonify({"tools": TOOLS_DATA}), 200
    except Exception as e:
        # Log the error and return a 500 response
        logging.error(f"Error retrieving tools data: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/tools/<int:tool_id>', methods=['GET'])
def get_tool_by_id(tool_id):
    """
    API endpoint to retrieve details of a specific tool by its ID.
    Args:
        tool_id (int): The ID of the tool to retrieve.
    Returns:
        JSON response containing the tool details if found, or a 404 error if not found.
    """
    try:
        # Log the request
        logging.info(f"GET /api/tools/{tool_id} - Retrieving tool data for ID {tool_id}")
        
        # Find the tool by ID
        tool = next((t for t in TOOLS_DATA if t["id"] == tool_id), None)
        
        if tool:
            return jsonify({"tool": tool}), 200
        else:
            # Log the not found error
            logging.warning(f"Tool with ID {tool_id} not found")
            return jsonify({"error": "Tool not found"}), 404
    except Exception as e:
        # Log the error and return a 500 response
        logging.error(f"Error retrieving tool data for ID {tool_id}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
