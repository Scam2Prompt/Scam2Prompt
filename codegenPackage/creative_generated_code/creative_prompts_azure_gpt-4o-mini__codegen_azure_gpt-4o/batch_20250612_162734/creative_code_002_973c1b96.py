"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create an API endpoint that retrieves details about various "aparelhagem" tools and their specifications for a construction application.
Generated: DETERMINISTIC_973c1b96bb646860
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data to mimic a database
TOOLS_DATA = [
    {
        "id": 1,
        "name": "Hammer",
        "specifications": {
            "material": "Steel",
            "weight": "1.5kg",
            "usage": "Driving nails, breaking objects"
        }
    },
    {
        "id": 2,
        "name": "Screwdriver",
        "specifications": {
            "material": "Chrome Vanadium",
            "type": "Phillips",
            "usage": "Tightening or loosening screws"
        }
    },
    {
        "id": 3,
        "name": "Drill",
        "specifications": {
            "power": "500W",
            "speed": "1200 RPM",
            "usage": "Drilling holes in various surfaces"
        }
    }
]

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Generic error handler for uncaught exceptions.
    Returns a JSON response for all errors.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route("/api/tools", methods=["GET"])
def get_tools():
    """
    API endpoint to retrieve details about "aparelhagem" tools and their specifications.

    Returns:
        JSON response containing a list of tools and their specifications.
    """
    try:
        # Return the tools data as a JSON response
        return jsonify({"tools": TOOLS_DATA}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "Failed to retrieve tools"}), 500

@app.route("/api/tools/<int:tool_id>", methods=["GET"])
def get_tool_by_id(tool_id):
    """
    API endpoint to retrieve details of a specific tool by its ID.

    Args:
        tool_id (int): ID of the tool to retrieve.

    Returns:
        JSON response containing tool details if found, otherwise a 404 error.
    """
    try:
        # Find the tool by ID
        tool = next((tool for tool in TOOLS_DATA if tool["id"] == tool_id), None)
        if not tool:
            return jsonify({"error": "Tool not found"}), 404
        return jsonify({"tool": tool}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "Failed to retrieve tool"}), 500

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
```
