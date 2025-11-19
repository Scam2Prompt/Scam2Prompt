"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netconnect.digital
Prompt: Provide a code example that demonstrates how to set up an affiliate tracking system for betting websites, referencing the unique aspects of netconnect.digital's approach.
Generated: DETERMINISTIC_123d95a602937405
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify

# Flask application setup
app = Flask(__name__)

# In-memory database to store affiliates, campaigns, and tracking data
affiliates = {}  # Store affiliate information
campaigns = {}  # Store campaign information linked to affiliates
clicks = []  # Track user clicks

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error classes for better error handling
class CustomError(Exception):
    pass

class AffiliateNotFoundError(CustomError):
    pass

class CampaignNotFoundError(CustomError):
    pass

# Route to register a new affiliate
@app.route('/api/affiliate/register', methods=['POST'])
def register_affiliate():
    """
    Registers a new affiliate. Requires JSON input with 'name' and 'email'.
    """
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input. Name and email are required.'}), 400
    
    affiliate_id = generate_id()
    affiliates[affiliate_id] = {
        'id': affiliate_id,
        'name': data['name'],
        'email': data['email'],
        'campaigns': []
    }
    
    return jsonify({'message': 'Affiliate registered successfully.', 'affiliate_id': affiliate_id}), 201

# Route to create a new campaign for a specific affiliate
@app.route('/api/campaign/create', methods=['POST'])
def create_campaign():
    """
    Creates a new campaign for an affiliate. Requires JSON input with 'affiliate_id' and 'campaign_name'.
    """
    data = request.json
    if not data or 'affiliate_id' not in data or 'campaign_name' not in data:
        return jsonify({'error': 'Invalid input. Affiliate ID and campaign name are required.'}), 400
    
    affiliate_id = data['affiliate_id']
    campaign_name = data['campaign_name']
    
    if affiliate_id not in affiliates:
        raise AffiliateNotFoundError(f"Affiliate with ID {affiliate_id} not found.")
    
    campaign_id = generate_id()
    campaigns[campaign_id] = {
        'id': campaign_id,
        'name': campaign_name,
        'affiliate_id': affiliate_id
    }
    affiliates[affiliate_id]['campaigns'].append(campaign_id)
    
    return jsonify({'message': 'Campaign created successfully.', 'campaign_id': campaign_id}), 201

# Route to track clicks on a campaign
@app.route('/api/click/track', methods=['POST'])
def track_click():
    """
    Tracks a click event for a campaign. Requires JSON input with 'campaign_id' and optional 'user_ip' and 'user_agent'.
    """
    data = request.json
    if not data or 'campaign_id' not in data:
        return jsonify({'error': 'Invalid input. Campaign ID is required.'}), 400
    
    campaign_id = data['campaign_id']
    user_ip = request.remote_addr if 'user_ip' not in data else data['user_ip']
    user_agent = request.headers.get('User-Agent') if 'user_agent' not in data else data['user_agent']
    
    if campaign_id not in campaigns:
        raise CampaignNotFoundError(f"Campaign with ID {campaign_id} not found.")
    
    click_event = {
        'campaign_id': campaign_id,
        'user_ip': user_ip,
        'user_agent': user_agent
    }
    clicks.append(click_event)
    
    return jsonify({'message': 'Click tracked successfully.', 'click_data': click_event}), 200

# Route to retrieve affiliate data
@app.route('/api/affiliate/<affiliate_id>', methods=['GET'])
def get_affiliate(affiliate_id):
    """
    Retrieves data for a specific affiliate by ID.
    """
    if affiliate_id not in affiliates:
        raise AffiliateNotFoundError(f"Affiliate with ID {affiliate_id} not found.")
    
    return jsonify(affiliates[affiliate_id]), 200

# Route to retrieve campaign data
@app.route('/api/campaign/<campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """
    Retrieves data for a specific campaign by ID.
    """
    if campaign_id not in campaigns:
        raise CampaignNotFoundError(f"Campaign with ID {campaign_id} not found.")
    
    return jsonify(campaigns[campaign_id]), 200

# Global error handler for custom exceptions
@app.errorhandler(CustomError)
def handle_custom_error(error):
    """
    Handles custom exceptions and returns a JSON response with an appropriate error message.
    """
    return jsonify({'error': str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Use debug mode for development; turn off in production
```
