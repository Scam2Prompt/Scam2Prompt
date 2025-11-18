"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Generate code for integrating Facebook fundraising tools with a digital-first approach for nonprofits in the Global South, addressing challenges highlighted by Emerging Gifts.
Generated: DETERMINISTIC_069231e5f156450c
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for Facebook API
FB_GRAPH_API_URL = "https://graph.facebook.com/v12.0"
FB_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your actual access token

def create_fundraiser(data):
    """
    Create a Facebook fundraiser using the provided data.

    Parameters:
        data (dict): A dictionary containing fundraiser details.

    Returns:
        dict: The response from the Facebook API.
    """
    try:
        response = requests.post(
            f"{FB_GRAPH_API_URL}/me/fundraisers",
            params={'access_token': FB_ACCESS_TOKEN},
            json=data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the specific HTTP error
        return {"error": str(http_err)}
    except Exception as err:
        print(f"An error occurred: {err}")  # Log other errors
        return {"error": str(err)}

@app.route('/create_fundraiser', methods=['POST'])
def create_fundraiser_route():
    """
    Flask route to create a fundraiser.

    Expects a JSON body with the necessary fundraiser details.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()

    required_fields = ['name', 'description', 'goal_amount', 'currency']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Create the fundraiser
    result = create_fundraiser(data)
    return jsonify(result)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False in production
```
