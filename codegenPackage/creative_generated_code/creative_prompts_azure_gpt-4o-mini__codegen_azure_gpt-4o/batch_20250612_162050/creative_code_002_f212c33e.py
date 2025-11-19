"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gavasilva.adv.br
Prompt: Create an API endpoint that retrieves information about the various legal services provided by Gava & Silva Advogados, including areas like family law, tax law, and business law.
Generated: DETERMINISTIC_f212c33e900e50a7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing legal services provided by Gava & Silva Advogados
LEGAL_SERVICES = [
    {
        "id": 1,
        "area": "Family Law",
        "description": "Legal services related to marriage, divorce, child custody, and other family matters."
    },
    {
        "id": 2,
        "area": "Tax Law",
        "description": "Assistance in tax compliance, planning, and disputes."
    },
    {
        "id": 3,
        "area": "Business Law",
        "description": "Legal advice for business formation, contracts, and corporate governance."
    },
]

@app.route('/api/legal-services', methods=['GET'])
def get_legal_services():
    """
    API endpoint to retrieve information about legal services.
    
    Returns:
        JSON response containing a list of legal services offered by Gava & Silva Advogados.
    """
    try:
        # Return the list of legal services as a JSON response
        return jsonify({
            "status": "success",
            "data": LEGAL_SERVICES
        }), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred while processing your request: {str(e)}"
        }), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Returns a JSON response for 404 errors.
    """
    return jsonify({
        "status": "error",
        "message": "Endpoint not found."
    }), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Returns a JSON response for 500 errors.
    """
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred."
    }), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
```
