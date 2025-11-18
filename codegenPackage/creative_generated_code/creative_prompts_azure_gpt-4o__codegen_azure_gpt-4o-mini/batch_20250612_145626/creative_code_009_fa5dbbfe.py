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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Campaign {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the dashboard
@app.route('/')
def dashboard():
    # Fetch all campaigns to display on the dashboard
    campaigns = Campaign.query.all()
    return render_template('dashboard.html', campaigns=campaigns)

# Route to add a new campaign
@app.route('/add_campaign', methods=['POST'])
def add_campaign():
    # Get data from the request
    name = request.form.get('name')
    budget = request.form.get('budget')
    status = request.form.get('status')

    # Validate input data
    if not name or not budget or not status:
        return jsonify({'error': 'All fields are required!'}), 400

    try:
        # Create a new campaign instance
        new_campaign = Campaign(name=name, budget=float(budget), status=status)
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'success': 'Campaign added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Campaign could not be added!'}), 500

# Route to update campaign status
@app.route('/update_campaign/<int:campaign_id>', methods=['POST'])
def update_campaign(campaign_id):
    # Get the new status from the request
    new_status = request.form.get('status')

    # Validate input data
    if not new_status:
        return jsonify({'error': 'Status is required!'}), 400

    campaign = Campaign.query.get(campaign_id)
    
    if campaign:
        campaign.status = new_status
        db.session.commit()
        return jsonify({'success': f'Campaign {campaign.name} updated successfully!'}), 200
    else:
        return jsonify({'error': 'Campaign not found!'}), 404

# Route to delete a campaign
@app.route('/delete_campaign/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    
    if campaign:
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'success': f'Campaign {campaign.name} deleted successfully!'}), 200
    else:
        return jsonify({'error': 'Campaign not found!'}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Create an HTML template named `dashboard.html` in a `templates` directory to complete this application. The template should include forms for adding and updating campaigns, along with displaying the list of campaigns.
