"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaguarlandroverjakarta.com
Prompt: Suggest a library or framework to build a simulation tool for credit calculations, as described on jaguarlandroverjakarta.com, with options for different vehicle models.
Generated: DETERMINISTIC_0997a17aa0bb96be
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# credit_calculator.py

"""
Credit Calculator Simulation Tool

This module provides a simulation tool for calculating credit options for different vehicle models.
The code utilizes the Flask web framework to create a RESTful API for credit calculations.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Vehicle model for the database
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    base_price = db.Column(db.Float, nullable=False)  # Base price of the vehicle

    def __repr__(self):
        return f'<Vehicle {self.model}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    """
    Endpoint to add a new vehicle model to the database.
    Request body should contain JSON with 'model' and 'base_price'.
    """
    data = request.get_json()
    try:
        new_vehicle = Vehicle(model=data['model'], base_price=data['base_price'])
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify({'message': 'Vehicle added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/credit_calculation', methods=['POST'])
def calculate_credit():
    """
    Endpoint to calculate credit options for a specific vehicle.
    Request body should contain JSON with 'vehicle_id', 'loan_term', and 'interest_rate'.
    """
    data = request.get_json()
    try:
        vehicle = Vehicle.query.get(data['vehicle_id'])
        if not vehicle:
            return jsonify({'error': 'Vehicle not found.'}), 404
        
        loan_term = data['loan_term']  # in months
        interest_rate = data['interest_rate'] / 100  # Convert percentage to decimal

        # Monthly payment calculation using the formula:
        # M = P[r(1 + r)^n] / [(1 + r)^n – 1]
        P = vehicle.base_price  # Principal amount
        r = interest_rate / 12  # Monthly interest rate
        n = loan_term  # Number of payments

        if r == 0:  # Handling case where interest rate is 0
            monthly_payment = P / n
        else:
            monthly_payment = P * (r * (1 + r)**n) / ((1 + r)**n - 1)

        return jsonify({
            'vehicle_model': vehicle.model,
            'monthly_payment': round(monthly_payment, 2),
            'total_payment': round(monthly_payment * n, 2)
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
    except KeyError:
        return jsonify({'error': 'Invalid data provided.'}), 400

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

To run the above code, ensure that you have Flask and SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
After that, run the script and use a tool like Postman or curl to interact with the API.
