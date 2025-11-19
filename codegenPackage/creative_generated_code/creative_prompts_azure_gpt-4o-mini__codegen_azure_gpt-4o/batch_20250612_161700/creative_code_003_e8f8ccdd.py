"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: What are some best practices for creating a fundraising campaign API for an NGO, taking cues from the initiatives of Amma Parivaar Orphanage?
Generated: DETERMINISTIC_e8f8ccddb0574b94
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid
import datetime

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for campaigns
campaigns = {}

# Utility function to generate unique IDs
def generate_unique_id():
    return str(uuid.uuid4())

# Error handler for internal server errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({'error': e.description}), e.code
    return jsonify({'error': 'An internal server error occurred'}), 500

# Route: Create a new fundraising campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    """
    POST /campaigns
    Creates a new fundraising campaign.
    Request body:
    - name: str (required)
    - description: str (optional)
    - goal_amount: float (required)
    """
    data = request.json

    # Validate required fields
    if not data or 'name' not in data or 'goal_amount' not in data:
        return jsonify({'error': 'Missing required fields: name and goal_amount'}), 400

    try:
        # Create campaign object
        campaign_id = generate_unique_id()
        campaign = {
            'id': campaign_id,
            'name': data['name'],
            'description': data.get('description', ''),
            'goal_amount': float(data['goal_amount']),
            'current_amount': 0.0,
            'start_date': datetime.datetime.utcnow().isoformat(),
            'end_date': data.get('end_date', None),  # Optional: end date for campaign
            'status': 'active'  # Default status
        }

        # Store in memory
        campaigns[campaign_id] = campaign

        return jsonify({'message': 'Campaign created successfully', 'campaign': campaign}), 201
    except ValueError:
        return jsonify({'error': 'Invalid data format'}), 400

# Route: Get details of a specific campaign
@app.route('/campaigns/<campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """
    GET /campaigns/<campaign_id>
    Retrieves details of a specific campaign by ID.
    """
    campaign = campaigns.get(campaign_id)
    if not campaign:
        return jsonify({'error': 'Campaign not found'}), 404

    return jsonify({'campaign': campaign}), 200

# Route: Donate to a campaign
@app.route('/campaigns/<campaign_id>/donate', methods=['POST'])
def donate_to_campaign(campaign_id):
    """
    POST /campaigns/<campaign_id>/donate
    Adds a donation to a specified campaign.
    Request body:
    - amount: float (required)
    """
    campaign = campaigns.get(campaign_id)
    if not campaign:
        return jsonify({'error': 'Campaign not found'}), 404

    data = request.json

    # Validate donation amount
    if not data or 'amount' not in data:
        return jsonify({'error': 'Missing required field: amount'}), 400

    try:
        donation_amount = float(data['amount'])
        if donation_amount <= 0:
            return jsonify({'error': 'Donation amount must be greater than zero'}), 400

        # Update campaign's current amount
        campaign['current_amount'] += donation_amount

        # Check for campaign completion
        if campaign['current_amount'] >= campaign['goal_amount']:
            campaign['status'] = 'completed'

        return jsonify({'message': 'Donation added successfully', 'campaign': campaign}), 200
    except ValueError:
        return jsonify({'error': 'Invalid donation amount'}), 400

# Route: List all campaigns
@app.route('/campaigns', methods=['GET'])
def list_campaigns():
    """
    GET /campaigns
    Lists all fundraising campaigns.
    Optional query parameters:
    - status: str (filter by campaign status)
    """
    status = request.args.get('status')
    if status:
        filtered_campaigns = [campaign for campaign in campaigns.values() if campaign['status'] == status]
        return jsonify({'campaigns': filtered_campaigns}), 200

    return jsonify({'campaigns': list(campaigns.values())}), 200

# Start Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
