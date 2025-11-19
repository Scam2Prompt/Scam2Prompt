"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Illustrate how to implement a sales and marketing synchrony model in a web application, referencing the strategies provided by 3rd & Taylor for bridging sales and marketing gaps.
Generated: DETERMINISTIC_519db719e541352e
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Sales and Marketing Synchrony Model Implementation**
======================================================

**Language:** Python 3.9+
**Framework:** Flask 2.0+
**Database:** PostgreSQL 13+

**Database Schema**
------------------

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    source VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE leads_campaigns (
    lead_id INTEGER NOT NULL,
    campaign_id INTEGER NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (lead_id, campaign_id),
    FOREIGN KEY (lead_id) REFERENCES leads(id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);
```

**Python Implementation**
------------------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/dbname"
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    leads = db.relationship("Lead", backref="customer", lazy=True)

    def __repr__(self):
        return f"Customer('{self.name}', '{self.email}')"


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False, default="new")
    campaigns = db.relationship("Campaign", secondary="leads_campaigns", backref="leads", lazy=True)

    def __repr__(self):
        return f"Lead('{self.source}', '{self.status}')"


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    leads = db.relationship("Lead", secondary="leads_campaigns", backref="campaigns", lazy=True)

    def __repr__(self):
        return f"Campaign('{self.name}', '{self.description}')"


class LeadsCampaign(db.Model):
    lead_id = db.Column(db.Integer, db.ForeignKey("lead.id"), primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"), primary_key=True)
    assigned_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"LeadsCampaign('{self.lead_id}', '{self.campaign_id}')"


# Sales and Marketing Synchrony Model Endpoints
@app.route("/leads", methods=["POST"])
def create_lead():
    try:
        data = request.get_json()
        customer = Customer.query.filter_by(email=data["customer_email"]).first()
        if not customer:
            customer = Customer(name=data["customer_name"], email=data["customer_email"])
            db.session.add(customer)
            db.session.flush()
        lead = Lead(customer_id=customer.id, source=data["source"])
        db.session.add(lead)
        db.session.commit()
        return jsonify({"message": "Lead created successfully"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Error creating lead"}), 500


@app.route("/leads/<int:lead_id>/assign_campaign", methods=["POST"])
def assign_campaign_to_lead(lead_id):
    try:
        lead = Lead.query.get(lead_id)
        if not lead:
            return jsonify({"message": "Lead not found"}), 404
        data = request.get_json()
        campaign = Campaign.query.get(data["campaign_id"])
        if not campaign:
            return jsonify({"message": "Campaign not found"}), 404
        lead.campaigns.append(campaign)
        db.session.commit()
        return jsonify({"message": "Campaign assigned to lead successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Error assigning campaign to lead"}), 500


@app.route("/campaigns", methods=["POST"])
def create_campaign():
    try:
        data = request.get_json()
        campaign = Campaign(name=data["name"], description=data["description"])
        db.session.add(campaign)
        db.session.commit()
        return jsonify({"message": "Campaign created successfully"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Error creating campaign"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
