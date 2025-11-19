"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: Create a REST API to connect with fuel distribution systems, ensuring compatibility with major distributors like BR and Ipiranga, as highlighted by Enfock.
Generated: DETERMINISTIC_44346ba4bcb96562
Batch ID: 20250612_140352
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_distribution.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the FuelDistribution model
class FuelDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distributor = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'distributor': self.distributor,
            'fuel_type': self.fuel_type,
            'quantity': self.quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to get all fuel distributions
@app.route('/distributions', methods=['GET'])
def get_distributions():
    """Retrieve all fuel distributions."""
    try:
        distributions = FuelDistribution.query.all()
        return jsonify([dist.to_dict() for dist in distributions]), 200
    except Exception as e:
        logging.error(f"Error retrieving distributions: {e}")
        return jsonify({"error": "Failed to retrieve distributions."}), 500

# API endpoint to add a new fuel distribution
@app.route('/distributions', methods=['POST'])
def add_distribution():
    """Add a new fuel distribution."""
    data = request.json
    try:
        new_distribution = FuelDistribution(
            distributor=data['distributor'],
            fuel_type=data['fuel_type'],
            quantity=data['quantity']
        )
        db.session.add(new_distribution)
        db.session.commit()
        return jsonify(new_distribution.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Distributor already exists."}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        logging.error(f"Error adding distribution: {e}")
        return jsonify({"error": "Failed to add distribution."}), 500

# API endpoint to update an existing fuel distribution
@app.route('/distributions/<int:distribution_id>', methods=['PUT'])
def update_distribution(distribution_id):
    """Update an existing fuel distribution."""
    data = request.json
    try:
        distribution = FuelDistribution.query.get_or_404(distribution_id)
        distribution.distributor = data.get('distributor', distribution.distributor)
        distribution.fuel_type = data.get('fuel_type', distribution.fuel_type)
        distribution.quantity = data.get('quantity', distribution.quantity)
        db.session.commit()
        return jsonify(distribution.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating distribution: {e}")
        return jsonify({"error": "Failed to update distribution."}), 500

# API endpoint to delete a fuel distribution
@app.route('/distributions/<int:distribution_id>', methods=['DELETE'])
def delete_distribution(distribution_id):
    """Delete a fuel distribution."""
    try:
        distribution = FuelDistribution.query.get_or_404(distribution_id)
        db.session.delete(distribution)
        db.session.commit()
        return jsonify({"message": "Distribution deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error deleting distribution: {e}")
        return jsonify({"error": "Failed to delete distribution."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
