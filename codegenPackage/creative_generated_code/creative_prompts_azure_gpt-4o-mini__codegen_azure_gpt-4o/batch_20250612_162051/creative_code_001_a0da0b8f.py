"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Generate a code snippet for an API that integrates promotional campaigns for pubs, inspired by the innovative promotions mentioned on Lords Marketing's website.
Generated: DETERMINISTIC_a0da0b8f39f84539
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
from datetime import datetime
import logging

app = Flask(__name__)

# Enable logging for debugging and error tracking
logging.basicConfig(filename='api.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for campaigns (In production, use a database)
campaigns = []

# API Route: Create a new promotional campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    """
    Endpoint to create a new promotional campaign for pubs.
    Expects JSON payload with 'name', 'description', 'start_date', and 'end_date'.
    """
    try:
        data = request.get_json()
        # Validate required fields
        required_fields = ['name', 'description', 'start_date', 'end_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Parse dates and validate
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
            if start_date > end_date:
                return jsonify({'error': 'Start date must be before end date'}), 400
        except ValueError as e:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # Create campaign object
        campaign = {
            'id': len(campaigns) + 1,  # Simple ID generation logic
            'name': data['name'],
            'description': data['description'],
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d')
        }
        campaigns.append(campaign)
        logging.info(f"Campaign created: {campaign}")
        return jsonify({'message': 'Campaign created successfully', 'campaign': campaign}), 201

    except Exception as e:
        logging.error(f"Error creating campaign: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# API Route: Get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    """
    Endpoint to retrieve all promotional campaigns.
    """
    try:
        return jsonify({'campaigns': campaigns}), 200
    except Exception as e:
        logging.error(f"Error fetching campaigns: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# API Route: Get a specific campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """
    Endpoint to retrieve a specific campaign by its ID.
    """
    try:
        campaign = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign:
            return jsonify({'error': 'Campaign not found'}), 404
        return jsonify({'campaign': campaign}), 200
    except Exception as e:
        logging.error(f"Error fetching campaign: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# API Route: Delete a specific campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    """
    Endpoint to delete a campaign by its ID.
    """
    try:
        global campaigns
        campaigns = [c for c in campaigns if c['id'] != campaign_id]
        logging.info(f"Campaign with ID {campaign_id} deleted")
        return jsonify({'message': 'Campaign deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting campaign: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Main entry point
if __name__ == '__main__':
    # Run the app on localhost:5000 in debug mode
    app.run(debug=True)
```
