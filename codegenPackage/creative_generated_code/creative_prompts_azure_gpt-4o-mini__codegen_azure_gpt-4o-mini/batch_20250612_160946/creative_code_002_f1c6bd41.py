"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Create an API endpoint for a coworking space management system that lists monthly and hourly plans, inspired by the offerings at Coworking Comércio.
Generated: DETERMINISTIC_f1c6bd4127fc9564
Batch ID: 20250612_160946
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coworking_space.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Plans
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration_type = db.Column(db.String(10), nullable=False)  # 'monthly' or 'hourly'

# Schema for serialization
class PlanSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    duration_type = fields.Str(required=True)

# Initialize the database and create sample data
@app.before_first_request
def create_tables():
    db.create_all()
    if not Plan.query.first():
        sample_plans = [
            Plan(name='Monthly Basic', price=200, duration_type='monthly'),
            Plan(name='Monthly Premium', price=300, duration_type='monthly'),
            Plan(name='Hourly Drop-in', price=15, duration_type='hourly'),
            Plan(name='Hourly 10-Pack', price=130, duration_type='hourly'),
        ]
        db.session.bulk_save_objects(sample_plans)
        db.session.commit()

# API endpoint to list all plans
@app.route('/api/plans', methods=['GET'])
def get_plans():
    try:
        plans = Plan.query.all()
        plan_schema = PlanSchema(many=True)
        return jsonify(plan_schema.dump(plans)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the necessary dependencies before running the code:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
