"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://completecircleconsulting.xyz
Prompt: Create an API endpoint that retrieves and displays a list of professional services offered by a consulting firm focused on nature.
Generated: DETERMINISTIC_3b60b20801763844
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data: List of professional services offered by the consulting firm
services = [
    {"id": 1, "name": "Environmental Impact Assessment", "description": "Assess environmental effects of projects and activities."},
    {"id": 2, "name": "Sustainable Development Consulting", "description": "Advise on practices that promote sustainability."},
    {"id": 3, "name": "Biodiversity Conservation Planning", "description": "Develop plans to protect and conserve biodiversity in natural areas."},
    {"id": 4, "name": "Natural Resource Management", "description": "Strategies for effective management of natural resources."},
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    API endpoint to retrieve the list of professional services.

    Returns:
        JSON response containing the list of services.
    """
    try:
        # Return the services data as JSON
        return jsonify({"success": True, "data": services}), 200

    except Exception as e:
        # Error handling: Return error message with status code 500
        return jsonify({"success": False, "error": str(e)}), 500

# Ensure the application runs only when executed directly
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug=True for development; debug=False for production
```
