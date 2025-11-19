"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Develop a RESTful API for managing outdoor advertising campaigns, including endpoints for creating, reading, updating, and deleting campaigns, inspired by the services provided by WOW MEDIA."
Generated: DETERMINISTIC_37882fe724c8aa4f
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for campaigns (for demonstration purposes)
campaigns = {}
campaign_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    global campaign_id_counter
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'location' not in data or 'budget' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Create a new campaign
    campaign = {
        "id": campaign_id_counter,
        "name": data['name'],
        "location": data['location'],
        "budget": data['budget']
    }
    campaigns[campaign_id_counter] = campaign
    campaign_id_counter += 1

    return jsonify(campaign), 201

# Endpoint to retrieve all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    return jsonify(list(campaigns.values())), 200

# Endpoint to retrieve a single campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    campaign = campaigns.get(campaign_id)
    if not campaign:
        return jsonify({"error": "Not Found", "message": "Campaign not found"}), 404
    return jsonify(campaign), 200

# Endpoint to update a campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    data = request.get_json()
    campaign = campaigns.get(campaign_id)

    if not campaign:
        return jsonify({"error": "Not Found", "message": "Campaign not found"}), 404

    # Validate input
    if not data or 'name' not in data or 'location' not in data or 'budget' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Update the campaign
    campaign.update({
        "name": data['name'],
        "location": data['location'],
        "budget": data['budget']
    })

    return jsonify(campaign), 200

# Endpoint to delete a campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = campaigns.pop(campaign_id, None)
    if not campaign:
        return jsonify({"error": "Not Found", "message": "Campaign not found"}), 404
    return jsonify({"message": "Campaign deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
