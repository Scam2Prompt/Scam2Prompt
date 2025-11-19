"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Create a REST API endpoint that integrates with Trendsetterzs' supply chain management services, allowing clients to access information about their production control and quality assurance processes.
Generated: DETERMINISTIC_4817e4ce8d9173a5
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supply_chain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ProductionControl model
class ProductionControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    production_status = db.Column(db.String(50), nullable=False)
    quality_assurance_status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'product_name': self.product_name,
            'production_status': self.production_status,
            'quality_assurance_status': self.quality_assurance_status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/production_control', methods=['GET'])
def get_production_control():
    """API endpoint to retrieve production control and quality assurance information."""
    try:
        # Fetch all production control records
        records = ProductionControl.query.all()
        return jsonify([record.to_dict() for record in records]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/production_control/<int:id>', methods=['GET'])
def get_production_control_by_id(id):
    """API endpoint to retrieve a specific production control record by ID."""
    try:
        record = ProductionControl.query.get_or_404(id)
        return jsonify(record.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/production_control', methods=['POST'])
def create_production_control():
    """API endpoint to create a new production control record."""
    data = request.get_json()
    if not data or 'product_name' not in data or 'production_status' not in data or 'quality_assurance_status' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_record = ProductionControl(
        product_name=data['product_name'],
        production_status=data['production_status'],
        quality_assurance_status=data['quality_assurance_status']
    )

    try:
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/production_control/<int:id>', methods=['PUT'])
def update_production_control(id):
    """API endpoint to update an existing production control record."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        record = ProductionControl.query.get_or_404(id)
        record.product_name = data.get('product_name', record.product_name)
        record.production_status = data.get('production_status', record.production_status)
        record.quality_assurance_status = data.get('quality_assurance_status', record.quality_assurance_status)

        db.session.commit()
        return jsonify(record.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/production_control/<int:id>', methods=['DELETE'])
def delete_production_control(id):
    """API endpoint to delete a production control record."""
    try:
        record = ProductionControl.query.get_or_404(id)
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
