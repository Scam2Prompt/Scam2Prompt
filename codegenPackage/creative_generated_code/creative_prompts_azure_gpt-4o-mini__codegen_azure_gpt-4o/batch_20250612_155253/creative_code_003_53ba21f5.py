"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Develop an API that tracks the evolution of political campaigns in McHenry County, Illinois, incorporating data from Fair Maps Illinois.
Generated: DETERMINISTIC_53ba21f5ac3fe0e6
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database (replace with actual database integration, e.g., PostgreSQL, MongoDB)
campaigns = {}

@app.route('/')
def home():
    """
    Home route to provide basic information about the API.
    """
    return jsonify({"message": "Welcome to the McHenry County Political Campaign Tracker API"})

@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    """
    Endpoint to retrieve all campaigns.
    """
    try:
        return jsonify({"campaigns": campaigns}), 200
    except Exception as e:
        logging.error(f"Error retrieving campaigns: {e}")
        return jsonify({"error": "An error occurred while retrieving campaigns"}), 500

@app.route('/campaigns/<string:campaign_id>', methods=['GET'])
def get_campaign_by_id(campaign_id):
    """
    Endpoint to retrieve a campaign by its ID.
    """
    try:
        campaign = campaigns.get(campaign_id)
        if not campaign:
            return jsonify({"error": f"Campaign with ID {campaign_id} not found"}), 404
        return jsonify({"campaign": campaign}), 200
    except Exception as e:
        logging.error(f"Error retrieving campaign {campaign_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the campaign"}), 500

@app.route('/campaigns', methods=['POST'])
def add_campaign():
    """
    Endpoint to add a new campaign.
    """
    try:
        data = request.get_json()
        campaign_id = data.get("id")
        if not campaign_id:
            return jsonify({"error": "Campaign ID is required"}), 400
        if campaign_id in campaigns:
            return jsonify({"error": f"Campaign with ID {campaign_id} already exists"}), 400
        
        campaigns[campaign_id] = {
            "name": data.get("name"),
            "description": data.get("description"),
            "candidate": data.get("candidate"),
            "status": data.get("status"),
            "source": "Fair Maps Illinois",
            "timestamp": data.get("timestamp")
        }
        return jsonify({"message": f"Campaign {campaign_id} added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding campaign: {e}")
        return jsonify({"error": "An error occurred while adding the campaign"}), 500

@app.route('/campaigns/<string:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    """
    Endpoint to update an existing campaign.
    """
    try:
        if campaign_id not in campaigns:
            return jsonify({"error": f"Campaign with ID {campaign_id} not found"}), 404
        
        data = request.get_json()
        campaigns[campaign_id].update({
            "name": data.get("name", campaigns[campaign_id]["name"]),
            "description": data.get("description", campaigns[campaign_id]["description"]),
            "candidate": data.get("candidate", campaigns[campaign_id]["candidate"]),
            "status": data.get("status", campaigns[campaign_id]["status"]),
            "timestamp": data.get("timestamp", campaigns[campaign_id]["timestamp"])
        })
        return jsonify({"message": f"Campaign {campaign_id} updated successfully"}), 200
    except Exception as e:
        logging.error(f"Error updating campaign {campaign_id}: {e}")
        return jsonify({"error": "An error occurred while updating the campaign"}), 500

@app.route('/campaigns/<string:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    """
    Endpoint to delete a campaign.
    """
    try:
        if campaign_id not in campaigns:
            return jsonify({"error": f"Campaign with ID {campaign_id} not found"}), 404
        
        del campaigns[campaign_id]
        return jsonify({"message": f"Campaign {campaign_id} deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting campaign {campaign_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the campaign"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```
