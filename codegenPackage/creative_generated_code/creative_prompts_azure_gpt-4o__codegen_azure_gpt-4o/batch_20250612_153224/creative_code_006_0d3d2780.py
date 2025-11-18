"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Provide code to create a dashboard for tracking seasonal campaigns, such as the sacrificial meat distribution project for 1446 AH, as detailed on the Gulf and Aden website.
Generated: DETERMINISTIC_0d3d278087c1dc5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import logging
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(
    filename='dashboard_error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Mock data to simulate campaign tracking
campaigns = [
    {
        "id": 1,
        "name": "Sacrificial Meat Distribution - 1446 AH",
        "description": "Annual charity event to distribute sacrificial meat.",
        "start_date": "2024-06-15",
        "end_date": "2024-06-30",
        "status": "Upcoming",
        "progress": 0,  # Percentage completed
        "total_donations": 0
    }
]

@app.route('/')
def dashboard():
    """
    Render the dashboard page where seasonal campaigns are tracked.
    """
    try:
        return render_template('dashboard.html', campaigns=campaigns)
    except Exception as e:
        logging.error(f"Error rendering dashboard: {e}")
        return "An error occurred while loading the dashboard.", 500


@app.route('/api/campaign/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """
    API endpoint to retrieve details for a specific campaign.
    """
    try:
        campaign = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404
        return jsonify(campaign), 200
    except Exception as e:
        logging.error(f"Error fetching campaign data: {e}")
        return jsonify({"error": "An error occurred"}), 500


@app.route('/api/campaign/<int:campaign_id>', methods=['PUT'])
def update_campaign_progress(campaign_id):
    """
    API endpoint to update campaign progress or donation amount.
    """
    try:
        campaign = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign:
            return jsonify({"error": "Campaign not found"}), 404

        data = request.json
        if 'progress' in data:
            new_progress = data.get('progress')
            if not isinstance(new_progress, int) or not (0 <= new_progress <= 100):
                return jsonify({"error": "Progress must be a valid percentage (0-100)"}), 400
            campaign['progress'] = new_progress
        
        if 'total_donations' in data:
            new_donations = data.get('total_donations')
            if not isinstance(new_donations, (int, float)) or new_donations < 0:
                return jsonify({"error": "Total donations must be a positive number"}), 400
            campaign['total_donations'] = new_donations

        # Update campaign status based on progress
        campaign['status'] = "Completed" if campaign['progress'] == 100 else "Ongoing"

        return jsonify(campaign), 200
    except Exception as e:
        logging.error(f"Error updating campaign progress: {e}")
        return jsonify({"error": "An error occurred"}), 500


@app.template_filter('format_date')
def format_date(value):
    """
    Custom filter to format dates for templates.
    """
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime('%b %d, %Y')
    except ValueError:
        return value


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Template: `dashboard.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seasonal Campaign Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
        .progress-bar { height: 20px; background-color: green; color: white; text-align: center; }
    </style>
</head>
<body>
    <h1>Seasonal Campaign Dashboard</h1>
    <table>
        <thead>
            <tr>
                <th>Campaign</th>
                <th>Description</th>
                <th>Start Date</th>
                <th>End Date</th>
                <th>Status</th>
                <th>Progress</th>
                <th>Total Donations</th>
            </tr>
        </thead>
        <tbody>
            {% for campaign in campaigns %}
            <tr>
                <td>{{ campaign.name }}</td>
                <td>{{ campaign.description }}</td>
                <td>{{ campaign.start_date | format_date }}</td>
                <td>{{ campaign.end_date | format_date }}</td>
                <td>{{ campaign.status }}</td>
                <td>
                    <div class="progress-bar" style="width: {{ campaign.progress }}%;">
                        {{ campaign.progress }}%
                    </div>
                </td>
                <td>${{ campaign.total_donations }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```
