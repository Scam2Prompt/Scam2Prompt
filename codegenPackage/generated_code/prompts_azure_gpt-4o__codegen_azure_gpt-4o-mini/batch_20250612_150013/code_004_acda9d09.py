"""
Generated Code Metadata:
========================
Original URL: https://nyatoken.net
Prompt: Suggest an API for booking luxury travel packages and managing incentive programs for companies, inspired by the offerings on nyatoken.net.
Generated: DETERMINISTIC_acda9d0917096d98
Batch ID: 20250612_150013
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_packages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the TravelPackage model
class TravelPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<TravelPackage {self.name}>'

# Define the IncentiveProgram model
class IncentiveProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    incentive_details = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<IncentiveProgram {self.company_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new travel package
@app.route('/api/travel-packages', methods=['POST'])
def create_travel_package():
    data = request.json
    try:
        new_package = TravelPackage(
            name=data['name'],
            price=data['price'],
            description=data.get('description')
        )
        db.session.add(new_package)
        db.session.commit()
        return jsonify({'message': 'Travel package created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Package with this name already exists.'}), 400
    except Exception as e:
        logging.error(f'Error creating travel package: {e}')
        return jsonify({'error': 'An error occurred while creating the package.'}), 500

# API endpoint to get all travel packages
@app.route('/api/travel-packages', methods=['GET'])
def get_travel_packages():
    packages = TravelPackage.query.all()
    return jsonify([{'id': pkg.id, 'name': pkg.name, 'price': pkg.price, 'description': pkg.description} for pkg in packages]), 200

# API endpoint to create a new incentive program
@app.route('/api/incentive-programs', methods=['POST'])
def create_incentive_program():
    data = request.json
    try:
        new_program = IncentiveProgram(
            company_name=data['company_name'],
            incentive_details=data.get('incentive_details')
        )
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'message': 'Incentive program created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Incentive program for this company already exists.'}), 400
    except Exception as e:
        logging.error(f'Error creating incentive program: {e}')
        return jsonify({'error': 'An error occurred while creating the incentive program.'}), 500

# API endpoint to get all incentive programs
@app.route('/api/incentive-programs', methods=['GET'])
def get_incentive_programs():
    programs = IncentiveProgram.query.all()
    return jsonify([{'id': prog.id, 'company_name': prog.company_name, 'incentive_details': prog.incentive_details} for prog in programs]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
