"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Create a REST API endpoint that integrates with Trendsetterzs' supply chain management services, allowing clients to access information about their production control and quality assurance processes.
Generated: DETERMINISTIC_4817e4ce8d9173a5
Batch ID: 20250612_163740
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

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supply_chain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Production Control and Quality Assurance
class ProductionQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    production_control = db.Column(db.String(255), nullable=False)
    quality_assurance = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'production_control': self.production_control,
            'quality_assurance': self.quality_assurance
        }

# Initialize the database (For demonstration purposes only; remove in production)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/v1/production-quality', methods=['GET'])
def get_production_quality():
    """Get production control and quality assurance data."""
    try:
        # Fetch all records from the database
        records = ProductionQuality.query.all()
        # Convert records to a list of dictionaries
        return jsonify([record.to_dict() for record in records]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/production-quality/<int:id>', methods=['GET'])
def get_production_quality_by_id(id):
    """Get a specific production control and quality assurance record by ID."""
    try:
        record = ProductionQuality.query.get_or_404(id)
        return jsonify(record.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/production-quality', methods=['POST'])
def create_production_quality():
    """Create a new production control and quality assurance record."""
    data = request.get_json()
    if not data or 'production_control' not in data or 'quality_assurance' not in data:
        return jsonify({'error': 'Invalid input data'}), 400
    
    new_record = ProductionQuality(
        production_control=data['production_control'],
        quality_assurance=data['quality_assurance']
    )
    
    try:
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/production-quality/<int:id>', methods=['PUT'])
def update_production_quality(id):
    """Update an existing production control and quality assurance record."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        record = ProductionQuality.query.get_or_404(id)
        record.production_control = data.get('production_control', record.production_control)
        record.quality_assurance = data.get('quality_assurance', record.quality_assurance)
        
        db.session.commit()
        return jsonify(record.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/production-quality/<int:id>', methods=['DELETE'])
def delete_production_quality(id):
    """Delete a production control and quality assurance record by ID."""
    try:
        record = ProductionQuality.query.get_or_404(id)
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
