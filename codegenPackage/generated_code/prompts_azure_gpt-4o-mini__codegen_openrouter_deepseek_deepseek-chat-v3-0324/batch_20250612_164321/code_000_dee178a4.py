"""
Generated Code Metadata:
========================
Original URL: https://cuotaschevrolet.com.ar
Prompt: What features should I consider when developing a payment plan API for car purchases, specifically for Chevrolet vehicles?
Generated: DETERMINISTIC_dee178a4184b53a0
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python Flask-based API skeleton for a payment plan system for Chevrolet vehicles. This includes key features like vehicle selection, payment calculation, and plan management:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from decimal import Decimal
import logging
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chevrolet_payment_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database Models
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)  # e.g., 'Silverado', 'Tahoe'
    trim = db.Column(db.String(50))
    year = db.Column(db.Integer, nullable=False)
    base_price = db.Column(db.Numeric(10, 2), nullable=False)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'trim': self.trim,
            'year': self.year,
            'base_price': str(self.base_price),
            'available': self.available
        }

class PaymentPlan(db.Model):
    __tablename__ = 'payment_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    down_payment = db.Column(db.Numeric(10, 2), nullable=False)
    term_months = db.Column(db.Integer, nullable=False)  # 12, 24, 36, etc.
    interest_rate = db.Column(db.Numeric(5, 2), nullable=False)
    monthly_payment = db.Column(db.Numeric(10, 2), nullable=False)
    total_cost = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    vehicle = db.relationship('Vehicle', backref='payment_plans')
    
    def to_dict(self):
        return {
            'id': self.id,
            'vehicle_id': self.vehicle_id,
            'down_payment': str(self.down_payment),
            'term_months': self.term_months,
            'interest_rate': str(self.interest_rate),
            'monthly_payment': str(self.monthly_payment),
            'total_cost': str(self.total_cost)
        }

# Error Handlers
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    logger.error(f'HTTP error: {e.code} - {e.description}')
    return jsonify({
        'error': e.description,
        'status_code': e.code
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f'Unexpected error: {str(e)}')
    return jsonify({
        'error': 'An unexpected error occurred',
        'status_code': 500
    }), 500

# Helper Functions
def calculate_payment_plan(base_price, down_payment, term_months, interest_rate):
    """Calculate monthly payment and total cost using simple interest formula"""
    principal = Decimal(base_price) - Decimal(down_payment)
    monthly_rate = Decimal(interest_rate) / Decimal(100) / Decimal(12)
    
    if term_months == 0:
        raise ValueError("Term in months cannot be zero")
    
    # Monthly payment calculation
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -term_months)
    
    # Round to 2 decimal places
    monthly_payment = monthly_payment.quantize(Decimal('0.01'))
    total_cost = (monthly_payment * term_months) + Decimal(down_payment)
    
    return monthly_payment, total_cost

# API Endpoints
@app.route('/api/vehicles', methods=['GET'])
def get_available_vehicles():
    """Get all available Chevrolet vehicles"""
    try:
        vehicles = Vehicle.query.filter_by(available=True).all()
        return jsonify([vehicle.to_dict() for vehicle in vehicles])
    except Exception as e:
        logger.error(f"Error fetching vehicles: {str(e)}")
        raise

@app.route('/api/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle_details(vehicle_id):
    """Get details for a specific vehicle"""
    try:
        vehicle = Vehicle.query.get_or_404(vehicle_id)
        return jsonify(vehicle.to_dict())
    except Exception as e:
        logger.error(f"Error fetching vehicle {vehicle_id}: {str(e)}")
        raise

@app.route('/api/payment-plans', methods=['POST'])
def create_payment_plan():
    """Create a new payment plan for a vehicle"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['vehicle_id', 'down_payment', 'term_months', 'interest_rate']
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")
        
        # Get vehicle
        vehicle = Vehicle.query.get_or_404(data['vehicle_id'])
        
        # Calculate payment plan
        monthly_payment, total_cost = calculate_payment_plan(
            vehicle.base_price,
            data['down_payment'],
            data['term_months'],
            data['interest_rate']
        )
        
        # Create and save payment plan
        plan = PaymentPlan(
            vehicle_id=vehicle.id,
            down_payment=data['down_payment'],
            term_months=data['term_months'],
            interest_rate=data['interest_rate'],
            monthly_payment=monthly_payment,
            total_cost=total_cost
        )
        
        db.session.add(plan)
        db.session.commit()
        
        return jsonify(plan.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating payment plan: {str(e)}")
        raise

@app.route('/api/payment-plans/<int:plan_id>', methods=['GET'])
def get_payment_plan(plan_id):
    """Get details for a specific payment plan"""
    try:
        plan = PaymentPlan.query.get_or_404(plan_id)
        return jsonify(plan.to_dict())
    except Exception as e:
        logger.error(f"Error fetching payment plan {plan_id}: {str(e)}")
        raise

# Initialize Database
@app.before_first_request
def initialize_database():
    db.create_all()
    
    # Add sample Chevrolet vehicles if none exist
    if Vehicle.query.count() == 0:
        vehicles = [
            Vehicle(model='Silverado', trim='LT', year=2023, base_price=42900.00),
            Vehicle(model='Tahoe', trim='Premier', year=2023, base_price=67900.00),
            Vehicle(model='Equinox', trim='LT', year=2023, base_price=29995.00),
            Vehicle(model='Traverse', trim='RS', year=2023, base_price=38995.00),
            Vehicle(model='Camaro', trim='LT1', year=2023, base_price=34995.00)
        ]
        db.session.bulk_save_objects(vehicles)
        db.session.commit()
        logger.info("Added sample Chevrolet vehicles to database")

if __name__ == '__main__':
    app.run(debug=True)
```
