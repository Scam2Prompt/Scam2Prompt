"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innetdigital.com
Prompt: Develop a dashboard using Python and Flask to monitor data-driven strategies and campaign performance metrics, as emphasized by Innet Plus Digital's services.
Generated: DETERMINISTIC_857baf2654f1966a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Mock data for campaigns
campaign_data = [
    {
        "id": 1,
        "name": "SEO Strategy",
        "performance": {
            "clicks": 1200,
            "impressions": 15000,
            "conversions": 45
        },
        "created_at": "2023-01-10"
    },
    {
        "id": 2,
        "name": "Social Media Ads",
        "performance": {
            "clicks": 800,
            "impressions": 12000,
            "conversions": 30
        },
        "created_at": "2023-02-15"
    },
    {
        "id": 3,
        "name": "Email Marketing",
        "performance": {
            "clicks": 450,
            "impressions": 5000,
            "conversions": 50
        },
        "created_at": "2023-03-20"
    }
]

# Route: Home/Dashboard
@app.route("/")
def dashboard():
    """
    Render the dashboard page with campaign data.
    """
    try:
        return render_template("dashboard.html", campaigns=campaign_data)
    except Exception as e:
        logging.error(f"Error rendering dashboard: {e}")
        return jsonify({"error": "Unable to load dashboard"}), 500

# Route: Get campaign data (JSON format)
@app.route("/api/campaigns", methods=["GET"])
def get_campaigns():
    """
    API endpoint to fetch campaign performance data in JSON format.
    """
    try:
        return jsonify({"campaigns": campaign_data}), 200
    except Exception as e:
        logging.error(f"Error fetching campaigns: {e}")
        return jsonify({"error": "Unable to fetch campaign data"}), 500

# Route: Add new campaign
@app.route("/api/campaigns", methods=["POST"])
def add_campaign():
    """
    API endpoint to add a new campaign.
    Expects JSON payload with 'name' and 'performance' fields.
    """
    try:
        data = request.json
        if not data or "name" not in data or "performance" not in data:
            return jsonify({"error": "Invalid input"}), 400

        new_campaign = {
            "id": len(campaign_data) + 1,
            "name": data["name"],
            "performance": data["performance"],
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        campaign_data.append(new_campaign)
        return jsonify(new_campaign), 201
    except Exception as e:
        logging.error(f"Error adding campaign: {e}")
        return jsonify({"error": "Unable to add campaign"}), 500

# Route: Get specific campaign by ID
@app.route("/api/campaigns/<int:campaign_id>", methods=["GET"])
def get_campaign(campaign_id):
    """
    API endpoint to fetch a specific campaign by ID.
    """
    try:
        campaign = next((c for c in campaign_data if c["id"] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404
        return jsonify(campaign), 200
    except Exception as e:
        logging.error(f"Error fetching campaign {campaign_id}: {e}")
        return jsonify({"error": "Unable to fetch campaign"}), 500

# Route: Update campaign by ID
@app.route("/api/campaigns/<int:campaign_id>", methods=["PUT"])
def update_campaign(campaign_id):
    """
    API endpoint to update a campaign's data by ID.
    Expects JSON payload with updated fields.
    """
    try:
        data = request.json
        campaign = next((c for c in campaign_data if c["id"] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404

        campaign.update(data)
        return jsonify(campaign), 200
    except Exception as e:
        logging.error(f"Error updating campaign {campaign_id}: {e}")
        return jsonify({"error": "Unable to update campaign"}), 500

# Route: Delete campaign by ID
@app.route("/api/campaigns/<int:campaign_id>", methods=["DELETE"])
def delete_campaign(campaign_id):
    """
    API endpoint to delete a campaign by ID.
    """
    try:
        global campaign_data
        campaign = next((c for c in campaign_data if c["id"] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404

        campaign_data = [c for c in campaign_data if c["id"] != campaign_id]
        return jsonify({"message": "Campaign deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting campaign {campaign_id}: {e}")
        return jsonify({"error": "Unable to delete campaign"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

**Notes:**
1. Ensure you have the `Flask` library installed. Use `pip install flask` to do so.
2. Create a `templates/dashboard.html` file to display the campaigns using HTML.
3. Use environment settings for production (e.g., setting `debug=False` and using a production server like Gunicorn).
