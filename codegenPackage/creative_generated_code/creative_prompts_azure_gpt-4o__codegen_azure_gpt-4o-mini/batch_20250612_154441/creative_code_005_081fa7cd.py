"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Develop a web application to manage social media campaigns and track metrics like engagement and conversions, referencing PulseX Media Solutions' expertise in social media management.
Generated: DETERMINISTIC_081fa7cd96548f66
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Campaign model to store campaign data
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    engagement = db.Column(db.Float, default=0.0)
    conversions = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Campaign {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for rendering the campaign management page
@app.route('/')
def index():
    campaigns = Campaign.query.all()
    return render_template('index.html', campaigns=campaigns)

# Route to create a new campaign
@app.route('/campaign', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        new_campaign = Campaign(
            name=data['name'],
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d')
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign created successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 400

# Route to update engagement and conversions metrics
@app.route('/campaign/<int:campaign_id>', methods=['PUT'])
def update_metrics(campaign_id):
    try:
        data = request.json
        campaign = Campaign.query.get_or_404(campaign_id)
        campaign.engagement = data.get('engagement', campaign.engagement)
        campaign.conversions = data.get('conversions', campaign.conversions)
        db.session.commit()
        return jsonify({'message': 'Metrics updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a campaign
@app.route('/campaign/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug in production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaign Management</title>
</head>
<body>
    <h1>Social Media Campaign Management</h1>
    <form id="campaignForm">
        <input type="text" name="name" placeholder="Campaign Name" required>
        <input type="date" name="end_date" required>
        <button type="submit">Create Campaign</button>
    </form>
    <ul id="campaignList">
        {% for campaign in campaigns %}
            <li>{{ campaign.name }} - Engagement: {{ campaign.engagement }} - Conversions: {{ campaign.conversions }}</li>
        {% endfor %}
    </ul>
    <script>
        document.getElementById('campaignForm').onsubmit = async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = {
                name: formData.get('name'),
                end_date: formData.get('end_date')
            };
            const response = await fetch('/campaign', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            if (response.ok) {
                location.reload();
            } else {
                console.error('Error creating campaign:', await response.json());
            }
        };
    </script>
</body>
</html>
```

**Note**: Make sure to set up a proper environment with Flask and SQLAlchemy installed, and create the necessary structure for the `index.html` template to serve correctly.
