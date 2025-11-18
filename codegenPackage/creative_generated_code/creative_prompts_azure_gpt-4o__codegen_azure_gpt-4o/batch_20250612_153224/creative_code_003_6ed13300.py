"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Suggest an API for integrating vocational guidance tools into an HR platform, similar to the "Orientación Vocacional-Ocupacional" services offered by Search HR.
Generated: DETERMINISTIC_6ed133004e8faefa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based API for integrating vocational guidance tools into an HR platform.

from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging for production-ready error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for vocational guidance data (Replace with actual database integration in production)
vocational_guidance_data = [
    {
        "id": 1,
        "name": "Career Assessment Tool",
        "description": "A comprehensive test for assessing career preferences and strengths.",
        "categories": ["Technology", "Healthcare", "Finance"],
    },
    {
        "id": 2,
        "name": "Skills Gap Analysis",
        "description": "Analyzes current skills against industry requirements.",
        "categories": ["Education", "Engineering", "Business"],
    },
]

@app.route('/api/vocational-tools', methods=['GET'])
def get_vocational_tools():
    """
    Endpoint to retrieve all vocational guidance tools.
    Returns:
        JSON response with available tools.
    """
    try:
        return jsonify({"tools": vocational_guidance_data}), 200
    except Exception as e:
        logging.error(f"Error fetching vocational tools: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/api/vocational-tools/<int:tool_id>', methods=['GET'])
def get_vocational_tool_by_id(tool_id):
    """
    Endpoint to retrieve a specific vocational tool by its ID.
    Args:
        tool_id (int): ID of the vocational tool.
    Returns:
        JSON response with the tool details if found.
    """
    try:
        tool = next((t for t in vocational_guidance_data if t['id'] == tool_id), None)
        if tool:
            return jsonify({"tool": tool}), 200
        else:
            return jsonify({"error": "Tool not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching vocational tool with ID {tool_id}: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/api/vocational-tools', methods=['POST'])
def add_vocational_tool():
    """
    Endpoint to add a new vocational guidance tool.
    Expects JSON payload with 'name', 'description', and 'categories'.
    """
    try:
        data = request.get_json()
        if not data or not all(k in data for k in ('name', 'description', 'categories')):
            return jsonify({"error": "Invalid input"}), 400

        new_tool = {
            "id": len(vocational_guidance_data) + 1,
            "name": data['name'],
            "description": data['description'],
            "categories": data['categories'],
        }
        vocational_guidance_data.append(new_tool)
        return jsonify({"message": "Tool added successfully", "tool": new_tool}), 201
    except Exception as e:
        logging.error(f"Error adding vocational tool: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/api/vocational-tools/<int:tool_id>', methods=['DELETE'])
def delete_vocational_tool(tool_id):
    """
    Endpoint to delete a vocational guidance tool by its ID.
    Args:
        tool_id (int): ID of the vocational tool to delete.
    """
    try:
        tool = next((t for t in vocational_guidance_data if t['id'] == tool_id), None)
        if tool:
            vocational_guidance_data.remove(tool)
            return jsonify({"message": "Tool deleted successfully"}), 200
        else:
            return jsonify({"error": "Tool not found"}), 404
    except Exception as e:
        logging.error(f"Error deleting vocational tool with ID {tool_id}: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- This code uses Flask, a lightweight web framework for building APIs.
- Replace the mock `vocational_guidance_data` with actual database integration in production (e.g., SQLAlchemy or another database library).
- Logging is used for error tracking.
- Error handling ensures robustness and appropriate client feedback.
