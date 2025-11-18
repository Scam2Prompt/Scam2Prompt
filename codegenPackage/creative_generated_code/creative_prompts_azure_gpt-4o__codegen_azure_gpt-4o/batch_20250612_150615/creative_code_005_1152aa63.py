"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Design an API that allows users to retrieve library archives information, such as the Women & Leadership Archives and University Archives mentioned on the Flagship webpage.
Generated: DETERMINISTIC_1152aa636a7e8045
Batch ID: 20250612_150615
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

# Initialize Flask application
app = Flask(__name__)

# Sample archive data
ARCHIVES = [
    {"id": 1, "name": "Women & Leadership Archives", "description": "Preserves records documenting women's leadership and contributions.", "location": "Flagship Campus, Building A"},
    {"id": 2, "name": "University Archives", "description": "Preserves records related to the history of the university.", "location": "Flagship Campus, Building B"}
]

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle unexpected errors and HTTP exceptions.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route: Get list of all archives
@app.route('/api/archives', methods=['GET'])
def get_archives():
    """
    Retrieve the list of all archives.
    Returns:
        JSON response with the archive data.
    """
    return jsonify({"archives": ARCHIVES}), 200

# Route: Get archive by ID
@app.route('/api/archives/<int:archive_id>', methods=['GET'])
def get_archive_by_id(archive_id):
    """
    Retrieve archive details by ID.
    Args:
        archive_id (int): The ID of the archive to retrieve.
    Returns:
        JSON response with the archive data, or 404 if not found.
    """
    archive = next((arch for arch in ARCHIVES if arch["id"] == archive_id), None)
    if not archive:
        return jsonify({"error": "Archive not found"}), 404
    return jsonify({"archive": archive}), 200

# Route: Search archives by name
@app.route('/api/archives/search', methods=['GET'])
def search_archives():
    """
    Search archives by name query parameter.
    Args:
        name (str): Query parameter specifying the name to search for.
    Returns:
        JSON response with matching archive data.
    """
    name_query = request.args.get('name', '').lower()
    matching_archives = [arch for arch in ARCHIVES if name_query in arch["name"].lower()]
    if not matching_archives:
        return jsonify({"message": "No archives found matching the search criteria"}), 404
    return jsonify({"archives": matching_archives}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
