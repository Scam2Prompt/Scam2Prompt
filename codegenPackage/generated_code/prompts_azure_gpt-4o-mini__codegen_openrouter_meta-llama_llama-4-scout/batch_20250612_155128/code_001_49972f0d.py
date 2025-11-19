"""
Generated Code Metadata:
========================
Original URL: https://delta.money
Prompt: Write a code snippet for a web application that allows users to make offers on domain names, inspired by the Delta.Money acquisition model.
Generated: DETERMINISTIC_49972f0d04d9038c
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_offer.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///domain_offers.db"
db = SQLAlchemy(app)


class Domain(db.Model):
    """Represents a domain name"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    offers = db.relationship("Offer", backref="domain", lazy=True)

    def __repr__(self):
        return f"Domain('{self.name}')"


class Offer(db.Model):
    """Represents an offer on a domain name"""
    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey("domain.id"), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Offer('{self.user_name}', '{self.amount}')"


@app.route("/domains", methods=["POST"])
def create_domain():
    """Creates a new domain name"""
    try:
        data = request.get_json()
        if "name" not in data:
            return jsonify({"error": "Domain name is required"}), 400
        domain = Domain(name=data["name"])
        db.session.add(domain)
        db.session.commit()
        return jsonify({"message": f"Domain '{data['name']}' created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/domains/<int:domain_id>/offers", methods=["POST"])
def make_offer(domain_id):
    """Makes an offer on a domain name"""
    try:
        domain = Domain.query.get(domain_id)
        if not domain:
            return jsonify({"error": "Domain not found"}), 404
        data = request.get_json()
        if "user_name" not in data or "amount" not in data:
            return jsonify({"error": "User name and amount are required"}), 400
        offer = Offer(domain_id=domain_id, user_name=data["user_name"], amount=data["amount"])
        db.session.add(offer)
        db.session.commit()
        return jsonify({"message": f"Offer made on domain '{domain.name}' successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/domains/<int:domain_id>/offers", methods=["GET"])
def get_offers(domain_id):
    """Gets all offers on a domain name"""
    try:
        domain = Domain.query.get(domain_id)
        if not domain:
            return jsonify({"error": "Domain not found"}), 404
        offers = Offer.query.filter_by(domain_id=domain_id).all()
        output = [{"id": offer.id, "user_name": offer.user_name, "amount": offer.amount, "created_at": offer.created_at} for offer in offers]
        return jsonify(output), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# test_domain_offer.py

import unittest
from domain_offer import app, db

class TestDomainOfferAPI(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_domain_offers.db"
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_domain(self):
        response = self.app.post("/domains", json={"name": "example.com"})
        self.assertEqual(response.status_code, 201)

    def test_make_offer(self):
        self.app.post("/domains", json={"name": "example.com"})
        response = self.app.post("/domains/1/offers", json={"user_name": "John Doe", "amount": 100.0})
        self.assertEqual(response.status_code, 201)

    def test_get_offers(self):
        self.app.post("/domains", json={"name": "example.com"})
        self.app.post("/domains/1/offers", json={"user_name": "John Doe", "amount": 100.0})
        response = self.app.get("/domains/1/offers")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```
