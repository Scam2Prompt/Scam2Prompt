"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Design a REST API for managing promotional campaigns on an online gambling site like Hi88, including endpoints for creating, updating, and tracking user participation.
Generated: DETERMINISTIC_051e00bbcd843d4e
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for campaigns and user participation
campaigns = {}
user_participation = {}

# Helper function for error responses
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# Endpoint to create a promotional campaign
@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Basic validation
        if not name or not start_date or not end_date:
            return error_response('Name, start_date, and end_date are required.')

        campaign_id = str(uuid4())
        campaigns[campaign_id] = {
            'id': campaign_id,
            'name': name,
            'description': description,
            'start_date': start_date,
            'end_date': end_date,
            'participants': []
        }

        return jsonify({'message': 'Campaign created successfully', 'campaign': campaigns[campaign_id]}), 201
    except Exception as e:
        return error_response(f'An error occurred: {str(e)}', status_code=500)

# Endpoint to update a promotional campaign
@app.route('/api/campaigns/<campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    try:
        if campaign_id not in campaigns:
            return error_response('Campaign not found.', status_code=404)

        data = request.json
        name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Update fields only if provided
        if name:
            campaigns[campaign_id]['name'] = name
        if description:
            campaigns[campaign_id]['description'] = description
        if start_date:
            campaigns[campaign_id]['start_date'] = start_date
        if end_date:
            campaigns[campaign_id]['end_date'] = end_date

        return jsonify({'message': 'Campaign updated successfully', 'campaign': campaigns[campaign_id]}), 200
    except Exception as e:
        return error_response(f'An error occurred: {str(e)}', status_code=500)

# Endpoint to track user participation in a campaign
@app.route('/api/campaigns/<campaign_id>/participate', methods=['POST'])
def participate_in_campaign(campaign_id):
    try:
        if campaign_id not in campaigns:
            return error_response('Campaign not found.', status_code=404)

        data = request.json
        user_id = data.get('user_id')

        if not user_id:
            return error_response('user_id is required.')

        # Ensure user has not already participated
        if user_id in campaigns[campaign_id]['participants']:
            return error_response('User has already participated in this campaign.')

        campaigns[campaign_id]['participants'].append(user_id)

        # Track participation globally
        if user_id not in user_participation:
            user_participation[user_id] = []
        user_participation[user_id].append(campaign_id)

        return jsonify({'message': 'User participation recorded successfully'}), 200
    except Exception as e:
        return error_response(f'An error occurred: {str(e)}', status_code=500)

# Endpoint to retrieve campaign details
@app.route('/api/campaigns/<campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    try:
        if campaign_id not in campaigns:
            return error_response('Campaign not found.', status_code=404)

        return jsonify({'campaign': campaigns[campaign_id]}), 200
    except Exception as e:
        return error_response(f'An error occurred: {str(e)}', status_code=500)

# Endpoint to retrieve user participation
@app.route('/api/users/<user_id>/participation', methods=['GET'])
def get_user_participation(user_id):
    try:
        participation = user_participation.get(user_id, [])
        return jsonify({'user_id': user_id, 'campaigns': participation}), 200
    except Exception as e:
        return error_response(f'An error occurred: {str(e)}', status_code=500)

# Entry point to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
