"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://depilarmg.com.br
Prompt: Suggest an API that could be used to manage customer loyalty programs for a waxing salon, including tracking sessions and rewards.
Generated: DETERMINISTIC_689927ef77388a1c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loyalty_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sessions = db.relationship('Session', backref='customer', lazy=True)

# Define the Session model
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    rewarded = db.Column(db.Boolean, default=False)

# Define the Reward model
class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)

# Schemas for input validation and serialization
class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class SessionSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    rewarded = fields.Bool()

class RewardSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    points = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    json_data = request.get_json()
    try:
        data = CustomerSchema().load(json_data)
        new_customer = Customer(**data)
        db.session.add(new_customer)
        db.session.commit()
        return CustomerSchema().dump(new_customer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Customer already exists"}), 409

# Route to add a session for a customer
@app.route('/sessions', methods=['POST'])
def add_session():
    json_data = request.get_json()
    try:
        data = SessionSchema().load(json_data)
        new_session = Session(**data)
        db.session.add(new_session)
        db.session.commit()
        return SessionSchema().dump(new_session), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Route to get customer rewards
@app.route('/customers/<int:customer_id>/rewards', methods=['GET'])
def get_rewards(customer_id):
    rewards = Reward.query.filter_by(customer_id=customer_id).all()
    return RewardSchema(many=True).dump(rewards), 200

# Route to add rewards for a customer
@app.route('/rewards', methods=['POST'])
def add_reward():
    json_data = request.get_json()
    try:
        data = RewardSchema().load(json_data)
        new_reward = Reward(**data)
        db.session.add(new_reward)
        db.session.commit()
        return RewardSchema().dump(new_reward), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"message": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
