"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Provide an example of a campaign design API that could be used to track engagement metrics, reflecting the campaign design services of Meta Force 360.
Generated: DETERMINISTIC_d989fb5f9fe1833a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory storage for campaigns and engagement metrics
campaigns = {}
engagement_metrics = {}

# Helper function to generate a unique ID
def generate_id():
    return str(uuid.uuid4())

# API Endpoint: Create a new campaign
@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        # Validate request payload
        if 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid payload. 'name' and 'description' are required."}), 400
        
        # Generate a new campaign ID
        campaign_id = generate_id()
        campaign = {
            "id": campaign_id,
            "name": data['name'],
            "description": data['description'],
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        campaigns[campaign_id] = campaign
        
        return jsonify({"message": "Campaign created successfully.", "campaign": campaign}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint: Track engagement metrics for a campaign
@app.route('/api/campaigns/<campaign_id>/engagement', methods=['POST'])
def track_engagement(campaign_id):
    try:
        data = request.json
        # Validate if campaign exists
        if campaign_id not in campaigns:
            return jsonify({"error": "Campaign not found."}), 404
        
        # Validate request payload
        if 'engagement_type' not in data or 'count' not in data:
            return jsonify({"error": "Invalid payload. 'engagement_type' and 'count' are required."}), 400

        engagement_type = data['engagement_type']
        count = data['count']
        
        # Initialize engagement metrics for the campaign if not already present
        if campaign_id not in engagement_metrics:
            engagement_metrics[campaign_id] = {}
        
        # Update engagement metrics for the specified engagement type
        if engagement_type not in engagement_metrics[campaign_id]:
            engagement_metrics[campaign_id][engagement_type] = 0
        
        engagement_metrics[campaign_id][engagement_type] += count
        
        return jsonify({"message": "Engagement tracked successfully.", "metrics": engagement_metrics[campaign_id]}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint: Retrieve engagement metrics for a campaign
@app.route('/api/campaigns/<campaign_id>/engagement', methods=['GET'])
def get_engagement_metrics(campaign_id):
    try:
        # Validate if campaign exists
        if campaign_id not in campaigns:
            return jsonify({"error": "Campaign not found."}), 404

        # Retrieve engagement metrics
        metrics = engagement_metrics.get(campaign_id, {})
        
        return jsonify({"campaign_id": campaign_id, "metrics": metrics}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint: List all campaigns
@app.route('/api/campaigns', methods=['GET'])
def list_campaigns():
    try:
        return jsonify({"campaigns": list(campaigns.values())}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
