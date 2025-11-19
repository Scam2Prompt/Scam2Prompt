"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Develop a REST API in Flask to manage sports club memberships, including features for retrieving class schedules, trainer details, and pricing plans as described on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_a4b542da536ed10e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)

# Define the ClassSchedule model
class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    schedule_time = db.Column(db.String(50), nullable=False)

# Define the Trainer model
class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(100), nullable=False)

# Define the PricingPlan model
class PricingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to retrieve all class schedules
@app.route('/api/class_schedules', methods=['GET'])
def get_class_schedules():
    schedules = ClassSchedule.query.all()
    return jsonify([{'id': schedule.id, 'class_name': schedule.class_name, 'schedule_time': schedule.schedule_time} for schedule in schedules])

# Route to retrieve all trainers
@app.route('/api/trainers', methods=['GET'])
def get_trainers():
    trainers = Trainer.query.all()
    return jsonify([{'id': trainer.id, 'trainer_name': trainer.trainer_name, 'expertise': trainer.expertise} for trainer in trainers])

# Route to retrieve all pricing plans
@app.route('/api/pricing_plans', methods=['GET'])
def get_pricing_plans():
    plans = PricingPlan.query.all()
    return jsonify([{'id': plan.id, 'plan_name': plan.plan_name, 'price': plan.price} for plan in plans])

# Route to create a new membership
@app.route('/api/memberships', methods=['POST'])
def create_membership():
    data = request.get_json()
    if not data or 'member_name' not in data or 'membership_type' not in data:
        abort(400, description="Invalid input data")
    
    new_membership = Membership(
        member_name=data['member_name'],
        membership_type=data['membership_type'],
        end_date=data.get('end_date')
    )
    db.session.add(new_membership)
    db.session.commit()
    return jsonify({'id': new_membership.id}), 201

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
