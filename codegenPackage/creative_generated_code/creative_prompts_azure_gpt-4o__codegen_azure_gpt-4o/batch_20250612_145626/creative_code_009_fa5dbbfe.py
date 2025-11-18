"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Generate code to create a dashboard for monitoring and managing multi-channel advertising campaigns, inspired by 搜了网's advertising services.
Generated: DETERMINISTIC_fa5dbbfe740a549e
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: advertising_dashboard.py

from flask import Flask, render_template, request, jsonify
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database simulation for campaigns
# In production, use a proper database like PostgreSQL or MongoDB
campaigns = [
    {
        "id": 1,
        "name": "Google Ads Campaign",
        "platform": "Google Ads",
        "status": "active",
        "budget": 5000,
        "spend": 1200,
        "clicks": 300,
        "impressions": 15000
    },
    {
        "id": 2,
        "name": "Facebook Ads Campaign",
        "platform": "Facebook Ads",
        "status": "paused",
        "budget": 3000,
        "spend": 800,
        "clicks": 200,
        "impressions": 10000
    }
]

@app.route('/')
def dashboard():
    """
    Route to render the main dashboard page.
    """
    try:
        logging.info("Rendering dashboard with campaign data.")
        return render_template('dashboard.html', campaigns=campaigns)
    except Exception as e:
        logging.error(f"Error rendering dashboard: {e}")
        return "An error occurred while loading the dashboard.", 500

@app.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    """
    API endpoint to retrieve all campaigns.
    """
    try:
        logging.info("Fetching all campaigns.")
        return jsonify(campaigns)
    except Exception as e:
        logging.error(f"Error retrieving campaigns: {e}")
        return jsonify({"error": "Failed to fetch campaigns"}), 500

@app.route('/api/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    """
    API endpoint to update a campaign's status.
    """
    try:
        data = request.json
        new_status = data.get('status')
        if not new_status:
            return jsonify({"error": "Status is required"}), 400

        campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404

        campaign['status'] = new_status
        logging.info(f"Updated campaign(id={campaign_id}) status to '{new_status}'.")
        return jsonify({"success": True, "campaign": campaign})
    except Exception as e:
        logging.error(f"Error updating campaign: {e}")
        return jsonify({"error": "Failed to update campaign"}), 500

@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    """
    API endpoint to create a new campaign.
    """
    try:
        data = request.json
        required_fields = ['name', 'platform', 'budget']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        new_campaign = {
            "id": max([c["id"] for c in campaigns]) + 1 if campaigns else 1,
            "name": data["name"],
            "platform": data["platform"],
            "status": "active",
            "budget": data["budget"],
            "spend": 0,
            "clicks": 0,
            "impressions": 0
        }
        campaigns.append(new_campaign)
        logging.info(f"Created new campaign: {new_campaign}")
        return jsonify({"success": True, "campaign": new_campaign}), 201
    except Exception as e:
        logging.error(f"Error creating campaign: {e}")
        return jsonify({"error": "Failed to create campaign"}), 500

@app.route('/api/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    """
    API endpoint to delete a campaign.
    """
    try:
        campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404

        campaigns.remove(campaign)
        logging.info(f"Deleted campaign(id={campaign_id}).")
        return jsonify({"success": True})
    except Exception as e:
        logging.error(f"Error deleting campaign: {e}")
        return jsonify({"error": "Failed to delete campaign"}), 500

# Run the application
if __name__ == "__main__":
    # Ensure the app is production-ready by using a WSGI server like Gunicorn in deployment.
    app.run(debug=True)  # Set to False in production
```

```html
<!-- File: templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advertising Campaign Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #007BFF;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Advertising Campaign Dashboard</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Platform</th>
                    <th>Status</th>
                    <th>Budget</th>
                    <th>Spend</th>
                    <th>Clicks</th>
                    <th>Impressions</th>
                </tr>
            </thead>
            <tbody>
                {% for campaign in campaigns %}
                <tr>
                    <td>{{ campaign.id }}</td>
                    <td>{{ campaign.name }}</td>
                    <td>{{ campaign.platform }}</td>
                    <td>{{ campaign.status }}</td>
                    <td>${{ campaign.budget }}</td>
                    <td>${{ campaign.spend }}</td>
                    <td>{{ campaign.clicks }}</td>
                    <td>{{ campaign.impressions }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```
