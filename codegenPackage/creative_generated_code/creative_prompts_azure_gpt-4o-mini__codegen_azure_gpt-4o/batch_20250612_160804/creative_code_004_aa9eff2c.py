"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Suggest an API endpoint structure for accessing technical bulletins related to pest control products offered by Tấn Hưng Việt Nam.
Generated: DETERMINISTIC_aa9eff2c9546d41e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: pest_control_api.py

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database of technical bulletins for pest control products
technical_bulletins = [
    {
        "id": 1,
        "product_name": "Pest-X",
        "bulletin_title": "Effective Pest Management Tips",
        "content": "Learn how to effectively manage pests with Pest-X.",
        "date_published": "2023-10-01"
    },
    {
        "id": 2,
        "product_name": "Bug-Free",
        "bulletin_title": "Safeguarding Against Bugs",
        "content": "Bug-Free provides comprehensive protection against bugs.",
        "date_published": "2023-09-25"
    }
]

# Utility function to find a technical bulletin by ID
def find_bulletin_by_id(bulletin_id):
    return next((bulletin for bulletin in technical_bulletins if bulletin["id"] == bulletin_id), None)

# Endpoint to retrieve all technical bulletins
@app.route('/api/bulletins', methods=['GET'])
def get_all_bulletins():
    """
    Get a list of all technical bulletins.
    
    Returns:
        JSON response containing a list of all technical bulletins.
    """
    return jsonify({"bulletins": technical_bulletins}), 200

# Endpoint to retrieve a technical bulletin by ID
@app.route('/api/bulletins/<int:bulletin_id>', methods=['GET'])
def get_bulletin_by_id(bulletin_id):
    """
    Get a specific technical bulletin by its ID.
    
    Args:
        bulletin_id (int): ID of the technical bulletin.
    
    Returns:
        JSON response containing the technical bulletin if found, otherwise 404 error.
    """
    bulletin = find_bulletin_by_id(bulletin_id)
    if bulletin:
        return jsonify({"bulletin": bulletin}), 200
    else:
        return jsonify({"error": f"Bulletin with ID {bulletin_id} not found"}), 404

# Global error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle unexpected errors globally.
    
    Args:
        e (Exception): The exception object.
    
    Returns:
        JSON response with error details and status code.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point to run the Flask application
if __name__ == '__main__':
    # Set debug to False for production
    app.run(debug=False, host='0.0.0.0', port=5000)
```
