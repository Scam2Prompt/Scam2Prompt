"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Develop an API endpoint that provides details about Shelter's Gas Fireplaces, including their safety features and design versatility.
Generated: DETERMINISTIC_ff60a6e920ed26d3
Batch ID: 20250612_162050
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

# Mock data representing Shelter's Gas Fireplaces details
fireplaces_data = [
    {
        "id": 1,
        "name": "Shelter Premium Gas Fireplace",
        "safety_features": [
            "Automatic shut-off in case of overheating",
            "Child safety lock",
            "Anti-tip design"
        ],
        "design_versatility": [
            "Available in multiple sizes",
            "Modern and classic styles",
            "Customizable finishes"
        ]
    },
    {
        "id": 2,
        "name": "Shelter Comfort Gas Fireplace",
        "safety_features": [
            "CO detection and automatic shut-off",
            "Cool-to-touch exterior",
            "Flame control settings for added safety"
        ],
        "design_versatility": [
            "Compact design for small spaces",
            "Rustic and contemporary options",
            "Easy-to-install modular design"
        ]
    }
]

@app.route('/api/fireplaces', methods=['GET'])
def get_fireplaces():
    """
    API endpoint to retrieve details about Shelter's Gas Fireplaces.
    
    Returns:
        JSON response containing a list of fireplaces with their safety features 
        and design versatility.
    """
    try:
        # Return fireplace details as JSON response
        return jsonify({
            "status": "success",
            "data": fireplaces_data
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
