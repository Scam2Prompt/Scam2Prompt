"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Provide code to integrate a donation or funding system for initiatives like the Idaho Prosperity Fund, ensuring secure transactions and tracking contributions.
Generated: DETERMINISTIC_3b348c8b7df400e1
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

import stripe
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///donations.db"
db = SQLAlchemy(app)

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donor.id"), nullable=False)
    initiative_id = db.Column(db.Integer, db.ForeignKey("initiative.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_id = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, donor_id, initiative_id, amount, transaction_id):
        self.donor_id = donor_id
        self.initiative_id = initiative_id
        self.amount = amount
        self.transaction_id = transaction_id

@app.route("/register", methods=["POST"])
def register_donor():
    try:
        data = request.json
        donor = Donor(data["name"], data["email"], data["password"])
        db.session.add(donor)
        db.session.commit()
        return jsonify({"message": "Donor registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

@app.route("/login", methods=["POST"])
def login_donor():
    try:
        data = request.json
        donor = Donor.query.filter_by(email=data["email"]).first()
        if donor and donor.check_password(data["password"]):
            return jsonify({"message": "Donor logged in successfully"}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/initiatives", methods=["GET"])
def get_initiatives():
    try:
        initiatives = Initiative.query.all()
        output = []
        for initiative in initiatives:
            initiative_data = {
                "id": initiative.id,
                "name": initiative.name,
                "description": initiative.description
            }
            output.append(initiative_data)
        return jsonify({"initiatives": output}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/donate", methods=["POST"])
def make_donation():
    try:
        data = request.json
        donor = Donor.query.filter_by(id=data["donor_id"]).first()
        initiative = Initiative.query.filter_by(id=data["initiative_id"]).first()
        if not donor or not initiative:
            return jsonify({"message": "Donor or initiative not found"}), 404

        charge = stripe.Charge.create(
            amount=int(data["amount"] * 100),
            currency="usd",
            description="Donation to " + initiative.name,
            customer=data["stripe_customer_id"]
        )

        donation = Donation(
            donor_id=data["donor_id"],
            initiative_id=data["initiative_id"],
            amount=data["amount"],
            transaction_id=charge.id
        )
        db.session.add(donation)
        db.session.commit()

        return jsonify({"message": "Donation successful"}), 201
    except stripe.error.CardError as e:
        return jsonify({"message": "Card declined"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# create_tables.py

from donation_system import db

def create_tables():
    db.create_all()

if __name__ == "__main__":
    create_tables()
```

```python
# seed_data.py

from donation_system import db, Initiative

def seed_data():
    initiatives = [
        Initiative("Idaho Prosperity Fund", "A fund to support economic growth in Idaho"),
        Initiative("Education Initiative", "A program to improve education in Idaho")
    ]

    db.session.add_all(initiatives)
    db.session.commit()

if __name__ == "__main__":
    seed_data()
```
