"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Develop a REST API for SKI Foundation's "Kerjasama Pendampingan Bisnis kepada Pelaku UMKM" program, allowing partners to submit business plans and track their implementation progress.
Generated: DETERMINISTIC_1f7dbdb0f82f46e9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**SKI Foundation REST API**
==========================

**dependencies**
---------------

* `flask`: `2.0.2`
* `flask_sqlalchemy`: `2.5.1`
* `marshmallow`: `3.10.0`
* `werkzeug`: `2.0.1`

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class BusinessPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner_name = db.Column(db.String(100), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    plan_description = db.Column(db.Text, nullable=False)
    implementation_progress = db.Column(db.String(100), nullable=False, default='Not Started')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, partner_name, business_name, plan_description):
        self.partner_name = partner_name
        self.business_name = business_name
        self.plan_description = plan_description

class BusinessPlanSchema(Schema):
    id = fields.Int()
    partner_name = fields.Str(required=True)
    business_name = fields.Str(required=True)
    plan_description = fields.Str(required=True)
    implementation_progress = fields.Str()
    created_at = fields.DateTime()
```

**routes.py**
```python
from flask import Flask, request, jsonify
from models import db, BusinessPlan, BusinessPlanSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ski_foundation.db'
db.init_app(app)

business_plan_schema = BusinessPlanSchema()
business_plans_schema = BusinessPlanSchema(many=True)

@app.route('/business-plans', methods=['POST'])
def create_business_plan():
    try:
        data = request.get_json()
        errors = business_plan_schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
        business_plan = BusinessPlan(**data)
        db.session.add(business_plan)
        db.session.commit()
        return jsonify(business_plan_schema.dump(business_plan)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/business-plans', methods=['GET'])
def get_business_plans():
    try:
        business_plans = BusinessPlan.query.all()
        return jsonify(business_plans_schema.dump(business_plans)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/business-plans/<int:business_plan_id>', methods=['GET'])
def get_business_plan(business_plan_id):
    try:
        business_plan = BusinessPlan.query.get(business_plan_id)
        if business_plan is None:
            return jsonify({'error': 'Business plan not found'}), 404
        return jsonify(business_plan_schema.dump(business_plan)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/business-plans/<int:business_plan_id>/progress', methods=['PATCH'])
def update_implementation_progress(business_plan_id):
    try:
        business_plan = BusinessPlan.query.get(business_plan_id)
        if business_plan is None:
            return jsonify({'error': 'Business plan not found'}), 404
        data = request.get_json()
        business_plan.implementation_progress = data['implementation_progress']
        db.session.commit()
        return jsonify(business_plan_schema.dump(business_plan)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

**main.py**
```python
from routes import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**requirements.txt**
```
flask==2.0.2
flask_sqlalchemy==2.5.1
marshmallow==3.10.0
werkzeug==2.0.1
```
