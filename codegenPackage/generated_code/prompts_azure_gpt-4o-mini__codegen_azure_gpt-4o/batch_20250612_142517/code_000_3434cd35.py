"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: How can I implement a digital-first fundraising program for nonprofits in emerging markets based on the strategies discussed on Emerging Gifts?
Generated: DETERMINISTIC_3434cd35818818cb
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital-First Fundraising Program for Nonprofits in Emerging Markets

This script implements a digital-first fundraising program for nonprofits in emerging markets.
It includes features such as donor management, campaign creation, and online payment integration.
The code is designed to be modular, scalable, and production-ready.
"""

import json
import logging
from datetime import datetime
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database for demonstration purposes
# In production, replace with a proper database (e.g., PostgreSQL, MongoDB)
database = {
    "donors": [],
    "campaigns": []
}

# Error handling classes
class FundraisingError(Exception):
    """Custom exception for fundraising-related errors."""
    pass

# Helper functions
def validate_email(email):
    """Validate email format."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def generate_id():
    """Generate a unique ID based on timestamp."""
    return str(int(datetime.now().timestamp() * 1000))

# Routes
@app.route('/donors', methods=['POST'])
def add_donor():
    """
    Add a new donor to the system.
    Request JSON format:
    {
        "name": "Donor Name",
        "email": "donor@example.com"
    }
    """
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        # Validate input
        if not name or not email:
            raise FundraisingError("Name and email are required.")
        if not validate_email(email):
            raise FundraisingError("Invalid email format.")

        # Add donor to database
        donor = {
            "id": generate_id(),
            "name": name,
            "email": email
        }
        database["donors"].append(donor)
        logging.info(f"Donor added: {donor}")
        return jsonify({"message": "Donor added successfully.", "donor": donor}), 201

    except FundraisingError as e:
        logging.error(f"Error adding donor: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/campaigns', methods=['POST'])
def create_campaign():
    """
    Create a new fundraising campaign.
    Request JSON format:
    {
        "title": "Campaign Title",
        "description": "Campaign Description",
        "goal_amount": 10000
    }
    """
    try:
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        goal_amount = data.get("goal_amount")

        # Validate input
        if not title or not description or not goal_amount:
            raise FundraisingError("Title, description, and goal amount are required.")
        if not isinstance(goal_amount, (int, float)) or goal_amount <= 0:
            raise FundraisingError("Goal amount must be a positive number.")

        # Create campaign
        campaign = {
            "id": generate_id(),
            "title": title,
            "description": description,
            "goal_amount": goal_amount,
            "raised_amount": 0
        }
        database["campaigns"].append(campaign)
        logging.info(f"Campaign created: {campaign}")
        return jsonify({"message": "Campaign created successfully.", "campaign": campaign}), 201

    except FundraisingError as e:
        logging.error(f"Error creating campaign: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/donate', methods=['POST'])
def donate():
    """
    Make a donation to a campaign.
    Request JSON format:
    {
        "campaign_id": "123456789",
        "donor_id": "987654321",
        "amount": 100
    }
    """
    try:
        data = request.get_json()
        campaign_id = data.get("campaign_id")
        donor_id = data.get("donor_id")
        amount = data.get("amount")

        # Validate input
        if not campaign_id or not donor_id or not amount:
            raise FundraisingError("Campaign ID, donor ID, and amount are required.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise FundraisingError("Donation amount must be a positive number.")

        # Find campaign and donor
        campaign = next((c for c in database["campaigns"] if c["id"] == campaign_id), None)
        donor = next((d for d in database["donors"] if d["id"] == donor_id), None)
        if not campaign:
            raise FundraisingError("Campaign not found.")
        if not donor:
            raise FundraisingError("Donor not found.")

        # Update campaign's raised amount
        campaign["raised_amount"] += amount
        logging.info(f"Donation made: {donor['name']} donated {amount} to {campaign['title']}")
        return jsonify({"message": "Donation successful.", "campaign": campaign}), 200

    except FundraisingError as e:
        logging.error(f"Error making donation: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
