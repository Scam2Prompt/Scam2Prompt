"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Generate a code snippet for a web application that allows users to input their energy consumption data and receive recommendations for improving energy efficiency, inspired by Digar Green's consulting services.
Generated: DETERMINISTIC_a736e1ddd17f3ab2
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_consumption.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the EnergyConsumption model
class EnergyConsumption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Float, nullable=False)

# Create a schema for input validation
class EnergyConsumptionSchema(Schema):
    user_id = fields.Int(required=True)
    consumption = fields.Float(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/submit_consumption', methods=['POST'])
def submit_consumption():
    """
    Endpoint to submit energy consumption data.
    Expects a JSON payload with user_id and consumption.
    Returns recommendations based on the input data.
    """
    # Validate and deserialize input
    schema = EnergyConsumptionSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Save the data to the database
    new_entry = EnergyConsumption(user_id=data['user_id'], consumption=data['consumption'])
    db.session.add(new_entry)
    db.session.commit()

    # Generate recommendations based on consumption
    recommendations = generate_recommendations(data['consumption'])

    return jsonify({
        "message": "Data submitted successfully.",
        "recommendations": recommendations
    }), 201

def generate_recommendations(consumption):
    """
    Generate energy efficiency recommendations based on consumption.
    This is a placeholder function and can be expanded with real logic.
    """
    if consumption < 100:
        return ["Great job! Keep maintaining your low energy usage."]
    elif 100 <= consumption < 300:
        return ["Consider using energy-efficient appliances.", "Check for drafts in your home."]
    else:
        return ["Evaluate your energy usage habits.", "Consider a home energy audit."]

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
