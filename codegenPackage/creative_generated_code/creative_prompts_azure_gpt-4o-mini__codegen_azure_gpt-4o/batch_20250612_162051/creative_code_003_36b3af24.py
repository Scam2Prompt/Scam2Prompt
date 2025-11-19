"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bandadorada.com
Prompt: Develop a RESTful API endpoint that retrieves event entertainment options, including orchestras and digital groups, reflecting the offerings of Orquesta Dorada.
Generated: DETERMINISTIC_36b3af248a5fc4ed
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

# Sample data representing entertainment options
ENTERTAINMENT_OPTIONS = [
    {
        "id": 1,
        "type": "orchestra",
        "name": "Orquesta Dorada",
        "description": "A world-renowned orchestra specializing in classical music and live performances.",
    },
    {
        "id": 2,
        "type": "digital_group",
        "name": "Virtual Beats Collective",
        "description": "A cutting-edge digital group offering immersive virtual performances.",
    },
]

@app.route('/api/entertainment-options', methods=['GET'])
def get_entertainment_options():
    """
    RESTful API endpoint to retrieve event entertainment options.
    Returns a JSON response with available orchestras and digital groups.
    """
    try:
        # Filter options based on query parameters, if provided
        entertainment_type = request.args.get('type')  # Optional query parameter
        if entertainment_type:
            filtered_options = [
                option for option in ENTERTAINMENT_OPTIONS if option['type'] == entertainment_type.lower()
            ]
            return jsonify(filtered_options), 200

        # Return all options if no filter is applied
        return jsonify(ENTERTAINMENT_OPTIONS), 200
    
    except Exception as error:
        # Return error response in case of unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(error)}), 500


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)  # Use debug=True for development, set to False in production
```

### Key Features:
- Endpoint: `/api/entertainment-options`
- HTTP Method: `GET`
- Optional query parameter: `type` (`orchestra` or `digital_group`)
- Error Handling: Captures unexpected errors and delivers a meaningful response.
- Data is hardcoded for demonstration purposes; replace with a database in production.
