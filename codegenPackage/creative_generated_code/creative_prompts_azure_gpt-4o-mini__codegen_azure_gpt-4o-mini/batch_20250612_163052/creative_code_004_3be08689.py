"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Construct a web application feature that tracks global investment opportunities and alerts users about significant market events, inspired by the global investment insights from Petrolio Italiano.
Generated: DETERMINISTIC_3be08689c62b10b0
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_opportunities.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Database model for Investment Opportunities
class InvestmentOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<InvestmentOpportunity {self.title}>'

# Function to fetch global market events (mock function)
def fetch_market_events():
    # In a real application, this function would call an external API to get market data
    # Here we mock this by returning a static list
    return [
        {"title": "Market Surge", "description": "Global stocks rise due to economic recovery."},
        {"title": "Oil Prices Drop", "description": "Crude oil prices fall sharply."},
    ]

# Function to notify users about market events (mock notification)
def notify_users(event):
    # In a real application, this might send an email or push notification
    logging.info(f'Notifying users about event: {event["title"]}')

# Scheduled job to check for new market events
def check_market_events():
    try:
        events = fetch_market_events()
        for event in events:
            notify_users(event)
    except Exception as e:
        logging.error(f'Error while checking market events: {e}')

# Create the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_market_events, trigger="interval", seconds=3600)  # Check every hour
scheduler.start()

# API endpoint to add an investment opportunity
@app.route('/api/opportunities', methods=['POST'])
def add_opportunity():
    try:
        data = request.json
        opportunity = InvestmentOpportunity(title=data['title'], description=data['description'])
        db.session.add(opportunity)
        db.session.commit()
        return jsonify({'message': 'Investment opportunity added!', 'id': opportunity.id}), 201
    except Exception as e:
        logging.error(f'Error adding opportunity: {e}')
        return jsonify({'error': 'Failed to add investment opportunity.'}), 500

# API endpoint to get all investment opportunities
@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    try:
        opportunities = InvestmentOpportunity.query.all()
        return jsonify([{'id': opp.id, 'title': opp.title, 'description': opp.description, 'date_added': opp.date_added} for opp in opportunities]), 200
    except Exception as e:
        logging.error(f'Error fetching opportunities: {e}')
        return jsonify({'error': 'Failed to fetch investment opportunities.'}), 500

# Entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production
```

### Note:
Make sure to install required dependencies using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate APScheduler
``` 

Additionally, replace the mock `fetch_market_events` function with actual API integration for real-time data in a production scenario.
