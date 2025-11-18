"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kakaxa.pages.dev
Prompt: Develop a marketing dashboard for tracking airdrop campaigns and pre-sale progress for a meme cryptocurrency like $KAKAXA.
Generated: DETERMINISTIC_0766b37a24220c4d
Batch ID: 20250612_152235
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
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for Airdrop Campaigns
class AirdropCampaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_tokens = db.Column(db.Float, nullable=False)
    claimed_tokens = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<AirdropCampaign {self.name}>'

# Define a model for Pre-sale Progress
class PresaleProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_tokens = db.Column(db.Float, nullable=False)
    sold_tokens = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<PresaleProgress Sold: {self.sold_tokens}/{self.total_tokens}>'

# Create database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Home route for the dashboard
@app.route('/')
def home():
    campaigns = AirdropCampaign.query.all()
    presale = PresaleProgress.query.first()  # Assume only one presale progress entry
    return render_template('dashboard.html', campaigns=campaigns, presale=presale)

# Endpoint to add a new airdrop campaign
@app.route('/add_campaign', methods=['POST'])
def add_campaign():
    try:
        data = request.json
        new_campaign = AirdropCampaign(
            name=data['name'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            total_tokens=data['total_tokens']
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to update presale progress
@app.route('/update_presale', methods=['POST'])
def update_presale():
    try:
        data = request.json
        presale = PresaleProgress.query.first()
        if presale:
            presale.sold_tokens += data['sold_tokens']
            db.session.commit()
            return jsonify({'message': 'Presale updated successfully!'}), 200
        else:
            return jsonify({'error': 'Presale not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```

### HTML Template (dashboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Dashboard</title>
</head>
<body>
    <h1>Airdrop Campaigns</h1>
    <ul>
        {% for campaign in campaigns %}
            <li>{{ campaign.name }}: {{ campaign.claimed_tokens }} / {{ campaign.total_tokens }}</li>
        {% endfor %}
    </ul>

    <h1>Pre-sale Progress</h1>
    <div>
        Total Tokens: {{ presale.total_tokens }} <br>
        Sold Tokens: {{ presale.sold_tokens }}
    </div>
</body>
</html>
```

### Notes
- This is a basic implementation using Flask and SQLite for simplicity. In a production environment, consider using a more robust database and adding user authentication.
- The HTML template should be placed in a folder named `templates` in the same directory as your Flask app file.
- Ensure proper environment variables for secure configurations in production.
- Consider adding more detailed error logging for better diagnostics in production.
