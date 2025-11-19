"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop an API endpoint that provides details about the types of cookware available at Varejão das Louças, including options for restaurants and hotels.
Generated: DETERMINISTIC_34395a76dd3887cd
Batch ID: 20250612_160657
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

# Mock data for cookware types
cookware_data = [
    {"id": 1, "type": "Frying Pan", "material": "Aluminum", "suitable_for": ["Restaurants", "Hotels"]},
    {"id": 2, "type": "Saucepan", "material": "Stainless Steel", "suitable_for": ["Restaurants"]},
    {"id": 3, "type": "Stockpot", "material": "Cast Iron", "suitable_for": ["Restaurants", "Hotels"]},
    {"id": 4, "type": "Griddle", "material": "Carbon Steel", "suitable_for": ["Hotels"]},
]

@app.route('/api/cookware', methods=['GET'])
def get_cookware():
    """
    API endpoint to retrieve details about cookware available at Varejão das Louças.
    Optional query parameters:
        - suitable_for: Filter results by "Restaurants" or "Hotels".
    Returns:
        JSON response containing cookware details.
    """
    try:
        # Extract query parameter for filtering
        suitable_for = request.args.get('suitable_for', None)

        # Filter cookware data if 'suitable_for' parameter is provided
        if suitable_for:
            filtered_cookware = [
                cookware for cookware in cookware_data
                if suitable_for in cookware["suitable_for"]
            ]
            return jsonify(filtered_cookware), 200

        # Return all cookware data if no filter is applied
        return jsonify(cookware_data), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
