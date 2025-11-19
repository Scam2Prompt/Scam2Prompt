"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Develop a RESTful API that provides information on the advantages of solar energy autoconsumption for businesses, inspired by the Nexe Energetic content.
Generated: DETERMINISTIC_60337e6e3eed4ca7
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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data representing advantages of solar energy autoconsumption for businesses
solar_advantages = [
    {
        "id": 1,
        "advantage": "Cost Savings",
        "description": "Reduced electricity bills due to self-generated energy."
    },
    {
        "id": 2,
        "advantage": "Energy Independence",
        "description": "Less reliance on utility providers and price fluctuations."
    },
    {
        "id": 3,
        "advantage": "Sustainability",
        "description": "Lower carbon footprint and contribution to renewable energy."
    },
    {
        "id": 4,
        "advantage": "Increased Property Value",
        "description": "Enhanced property value due to installation of solar panels."
    },
    {
        "id": 5,
        "advantage": "Government Incentives",
        "description": "Access to tax credits and rebates for renewable energy."
    }
]

@app.route('/api/solar-advantages', methods=['GET'])
def get_solar_advantages():
    """
    Retrieve the list of advantages of solar energy autoconsumption for businesses.
    
    Returns:
        JSON response containing a list of advantages.
    """
    try:
        return jsonify(solar_advantages), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching data."}), 500

@app.route('/api/solar-advantages/<int:id>', methods=['GET'])
def get_solar_advantage(id):
    """
    Retrieve a specific advantage by its ID.
    
    Args:
        id (int): The ID of the advantage to retrieve.

    Returns:
        JSON response containing the advantage details or an error message if not found.
    """
    try:
        advantage = next((adv for adv in solar_advantages if adv["id"] == id), None)
        
        if advantage is None:
            return jsonify({"error": "Advantage not found."}), 404
        
        return jsonify(advantage), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching data."}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode for development (set to False in production)
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install the required packages if they are not installed yet:
```bash
pip install Flask Flask-Cors
```
