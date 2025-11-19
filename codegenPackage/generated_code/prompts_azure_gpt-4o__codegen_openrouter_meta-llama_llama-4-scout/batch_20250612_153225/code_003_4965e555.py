"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Provide code examples for creating a lead generation system with targeted campaigns, as described in Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_4965e55534dfa717
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/campaigns`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/campaigns/1/leads`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/leads`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Lead Generation System with Targeted Campaigns**
=====================================================

### **Database Schema**
```sql
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    target_audience VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE campaign_leads (
    campaign_id INTEGER NOT NULL,
    lead_id INTEGER NOT NULL,
    PRIMARY KEY (campaign_id, lead_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id),
    FOREIGN KEY (lead_id) REFERENCES leads(id)
);
```

### **Python Implementation**
```python
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost/lead_gen")
db = SQLAlchemy(app)

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler("lead_gen.log", maxBytes=1024*1024*10, backupCount=10)
logger.addHandler(file_handler)

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Lead('{self.name}', '{self.email}')"

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    target_audience = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Campaign('{self.name}', '{self.target_audience}')"

class CampaignLead(db.Model):
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"), primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey("lead.id"), primary_key=True)

    def __repr__(self):
        return f"CampaignLead('{self.campaign_id}', '{self.lead_id}')"

@app.route("/leads", methods=["POST"])
def create_lead():
    try:
        data = request.get_json()
        lead = Lead(name=data["name"], email=data["email"], phone=data.get("phone"))
        db.session.add(lead)
        db.session.commit()
        logger.info(f"Lead created: {lead}")
        return jsonify({"message": "Lead created successfully"}), 201
    except SQLAlchemyError as e:
        logger.error(f"Error creating lead: {e}")
        return jsonify({"message": "Error creating lead"}), 500

@app.route("/campaigns", methods=["POST"])
def create_campaign():
    try:
        data = request.get_json()
        campaign = Campaign(name=data["name"], description=data.get("description"), target_audience=data["target_audience"])
        db.session.add(campaign)
        db.session.commit()
        logger.info(f"Campaign created: {campaign}")
        return jsonify({"message": "Campaign created successfully"}), 201
    except SQLAlchemyError as e:
        logger.error(f"Error creating campaign: {e}")
        return jsonify({"message": "Error creating campaign"}), 500

@app.route("/campaigns/<int:campaign_id>/leads", methods=["POST"])
def add_lead_to_campaign(campaign_id):
    try:
        campaign = Campaign.query.get(campaign_id)
        if not campaign:
            return jsonify({"message": "Campaign not found"}), 404
        data = request.get_json()
        lead = Lead.query.filter_by(email=data["email"]).first()
        if not lead:
            lead = Lead(name=data["name"], email=data["email"], phone=data.get("phone"))
            db.session.add(lead)
            db.session.commit()
        campaign_lead = CampaignLead(campaign_id=campaign_id, lead_id=lead.id)
        db.session.add(campaign_lead)
        db.session.commit()
        logger.info(f"Lead added to campaign: {campaign} - {lead}")
        return jsonify({"message": "Lead added to campaign successfully"}), 201
    except SQLAlchemyError as e:
        logger.error(f"Error adding lead to campaign: {e}")
        return jsonify({"message": "Error adding lead to campaign"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### **API Endpoints**

*   **POST /leads**: Create a new lead
*   **POST /campaigns**: Create a new campaign
*   **POST /campaigns/&lt;int:campaign_id&gt;/leads**: Add a lead to a campaign

### **Example Use Cases**

*   Create a new lead: `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"}' http://localhost:5000/leads`
*   Create a new campaign: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Summer Sale", "description": "Discounts on all products", "target_audience": "existing_customers"}' http://localhost:5000/campaigns`
*   Add a lead to a campaign: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com", "phone": "0987654321"}' http://localhost:5000/campaigns/1/leads`
