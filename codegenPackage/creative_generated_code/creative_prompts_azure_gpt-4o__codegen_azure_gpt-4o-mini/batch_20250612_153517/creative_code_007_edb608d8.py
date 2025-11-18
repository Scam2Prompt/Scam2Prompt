"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Create a REST API endpoint for retrieving MG car models and their promotional offers, including details like discounts and warranty policies.
Generated: DETERMINISTIC_edb608d8623ca9f3
Batch ID: 20250612_153517
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
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mg_cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the MG Car Model and Promotional Offer models
class CarModel(db.Model):
    __tablename__ = 'car_models'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

class PromotionalOffer(db.Model):
    __tablename__ = 'promotional_offers'
    
    id = db.Column(db.Integer, primary_key=True)
    car_model_id = db.Column(db.Integer, db.ForeignKey('car_models.id'), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)
    warranty_months = db.Column(db.Integer, nullable=False)

    car_model = db.relationship('CarModel', backref=db.backref('promotional_offers', lazy=True))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to retrieve car models and their promotional offers
@app.route('/api/mg_car_models', methods=['GET'])
def get_car_models():
    try:
        car_models = CarModel.query.all()
        result = []

        for model in car_models:
            offers = []
            for offer in model.promotional_offers:
                offers.append({
                    'discount_percentage': offer.discount_percentage,
                    'warranty_months': offer.warranty_months
                })
            result.append({
                'id': model.id,
                'name': model.name,
                'year': model.year,
                'promotional_offers': offers
            })

        return jsonify(result), 200

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('DEBUG', 'True') == 'True')
```
