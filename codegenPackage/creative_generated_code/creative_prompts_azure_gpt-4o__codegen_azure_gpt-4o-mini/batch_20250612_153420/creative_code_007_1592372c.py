"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Using Flask, create an API endpoint that retrieves and serves data about the Fusion Jiu Jitsu School's class schedules and pricing plans.
Generated: DETERMINISTIC_1592372c221f806d
Batch ID: 20250612_153420
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite in this example for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jiu_jitsu_school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for ClassSchedule
class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(10), nullable=False)
    instructor = db.Column(db.String(50), nullable=True)

# Define a model for PricingPlan
class PricingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(20), nullable=False)

# Initialize the database (for demo purposes, you might not want to do this in production)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve class schedules
@app.route('/api/schedules', methods=['GET'])
def get_schedules():
    try:
        schedules = ClassSchedule.query.all()
        schedule_list = [
            {
                'id': schedule.id,
                'class_name': schedule.class_name,
                'day_of_week': schedule.day_of_week,
                'time': schedule.time,
                'instructor': schedule.instructor
            } for schedule in schedules
        ]
        return jsonify(schedule_list), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve pricing plans
@app.route('/api/pricing', methods=['GET'])
def get_pricing():
    try:
        pricing_plans = PricingPlan.query.all()
        pricing_list = [
            {
                'id': plan.id,
                'plan_name': plan.plan_name,
                'price': plan.price,
                'duration': plan.duration
            } for plan in pricing_plans
        ]
        return jsonify(pricing_list), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Enable debug mode for development (not suitable for production)
    app.run(debug=True)
```

Make sure to create the database and add data before running the application.
