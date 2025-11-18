"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Develop an API that allows users to input their energy consumption and receive tailored solar panel installation plans, as described in Soltec Solutions' individual planning services.
Generated: DETERMINISTIC_afb798eda5a50287
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solar_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the SolarPlan model
class SolarPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_consumption = db.Column(db.Float, nullable=False)
    panel_count = db.Column(db.Integer, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)

# Define the schema for input validation
class SolarPlanSchema(Schema):
    energy_consumption = fields.Float(required=True)
    panel_count = fields.Integer(required=True)
    total_cost = fields.Float(required=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/solar-plan', methods=['POST'])
def create_solar_plan():
    """
    Create a tailored solar panel installation plan based on energy consumption.
    Request body should include energy consumption value.
    """
    # Validate and deserialize input data
    try:
        data = request.json
        schema = SolarPlanSchema()
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Logic for calculating solar panel installation plan
    energy_consumption = validated_data['energy_consumption']
    
    # Example calculations (these should be replaced with valid logic)
    panel_count = max(1, int(energy_consumption // 300))  # 300 kWh per panel
    total_cost = panel_count * 2500  # Assuming $2500 per panel

    # Create a new SolarPlan entry in the database
    new_plan = SolarPlan(energy_consumption=energy_consumption, panel_count=panel_count, total_cost=total_cost)
    
    try:
        db.session.add(new_plan)
        db.session.commit()
        return jsonify({"message": "Solar plan created successfully", "plan": schema.dump(new_plan)}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500

@app.route('/api/solar-plans', methods=['GET'])
def get_solar_plans():
    """
    Retrieve all solar panel installation plans from the database.
    """
    try:
        plans = SolarPlan.query.all()
        schema = SolarPlanSchema(many=True)
        return jsonify(schema.dump(plans)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
