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

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///business_plans.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Business Plan Model
class BusinessPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner_name = db.Column(db.String(100), nullable=False)
    plan_description = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    progress = db.Column(db.String(50), default='Pending')

    def __init__(self, partner_name, plan_description):
        self.partner_name = partner_name
        self.plan_description = plan_description

# Business Plan Schema
class BusinessPlanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BusinessPlan

# Initialize the database
with app.app_context():
    db.create_all()

# Route to submit a new business plan
@app.route('/api/business-plans', methods=['POST'])
def add_business_plan():
    try:
        # Get JSON data from request
        data = request.get_json()
        partner_name = data.get('partner_name')
        plan_description = data.get('plan_description')

        # Validate input
        if not partner_name or not plan_description:
            return jsonify({'error': 'Partner name and plan description are required.'}), 400

        # Create a new business plan
        new_plan = BusinessPlan(partner_name, plan_description)
        db.session.add(new_plan)
        db.session.commit()

        # Return the created business plan
        return BusinessPlanSchema().jsonify(new_plan), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all business plans
@app.route('/api/business-plans', methods=['GET'])
def get_business_plans():
    try:
        plans = BusinessPlan.query.all()
        return BusinessPlanSchema(many=True).jsonify(plans), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update the progress of a business plan
@app.route('/api/business-plans/<int:id>', methods=['PUT'])
def update_business_plan(id):
    try:
        # Get the business plan by ID
        plan = BusinessPlan.query.get_or_404(id)

        # Get JSON data from request
        data = request.get_json()
        progress = data.get('progress')

        # Validate input
        if not progress:
            return jsonify({'error': 'Progress status is required.'}), 400

        # Update the progress
        plan.progress = progress
        db.session.commit()

        # Return the updated business plan
        return BusinessPlanSchema().jsonify(plan), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
