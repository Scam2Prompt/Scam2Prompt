"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Develop a REST API in Flask to manage sports club memberships, including features for retrieving class schedules, trainer details, and pricing plans as described on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_a4b542da536ed10e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(80), nullable=False)
    membership_type = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)

class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(80), nullable=False)
    schedule_time = db.Column(db.String(80), nullable=False)

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String(80), nullable=False)
    specialty = db.Column(db.String(80), nullable=False)

class PricingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Routes for managing memberships
@app.route('/memberships', methods=['GET', 'POST'])
def manage_memberships():
    if request.method == 'GET':
        memberships = Membership.query.all()
        return jsonify([{'id': m.id, 'member_name': m.member_name, 'membership_type': m.membership_type, 'start_date': m.start_date, 'end_date': m.end_date} for m in memberships]), 200
    
    if request.method == 'POST':
        data = request.json
        new_membership = Membership(member_name=data['member_name'], membership_type=data['membership_type'], end_date=data.get('end_date'))
        db.session.add(new_membership)
        db.session.commit()
        return jsonify({'id': new_membership.id}), 201

# Routes for class schedules
@app.route('/classes', methods=['GET'])
def get_classes():
    classes = ClassSchedule.query.all()
    return jsonify([{'id': c.id, 'class_name': c.class_name, 'schedule_time': c.schedule_time} for c in classes]), 200

# Routes for trainer details
@app.route('/trainers', methods=['GET'])
def get_trainers():
    trainers = Trainer.query.all()
    return jsonify([{'id': t.id, 'trainer_name': t.trainer_name, 'specialty': t.specialty} for t in trainers]), 200

# Routes for pricing plans
@app.route('/pricing', methods=['GET'])
def get_pricing():
    pricing_plans = PricingPlan.query.all()
    return jsonify([{'id': p.id, 'plan_name': p.plan_name, 'price': p.price} for p in pricing_plans]), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
