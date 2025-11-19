"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Design a simple API to track and manage Styrofoam waste recycling, including endpoints for adding waste, processing it through a densifier, and calculating the economic benefits of recycling."
Generated: DETERMINISTIC_ad994f7b8d6d9aef
Batch ID: 20250622_210655
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///styrofoam_recycling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Waste model
class Waste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)  # Weight in kilograms
    processed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Waste {self.id}, Weight: {self.weight}, Processed: {self.processed}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/waste', methods=['POST'])
def add_waste():
    """Endpoint to add new Styrofoam waste."""
    data = request.get_json()
    weight = data.get('weight')

    if weight is None or weight <= 0:
        return jsonify({'error': 'Invalid weight provided.'}), 400

    new_waste = Waste(weight=weight)
    db.session.add(new_waste)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add waste.'}), 500

    return jsonify({'message': 'Waste added successfully.', 'id': new_waste.id}), 201

@app.route('/waste/<int:waste_id>/process', methods=['POST'])
def process_waste(waste_id):
    """Endpoint to process waste through a densifier."""
    waste = Waste.query.get(waste_id)

    if waste is None:
        return jsonify({'error': 'Waste not found.'}), 404

    if waste.processed:
        return jsonify({'error': 'Waste has already been processed.'}), 400

    waste.processed = True
    db.session.commit()

    return jsonify({'message': 'Waste processed successfully.'}), 200

@app.route('/economic-benefits', methods=['GET'])
def calculate_economic_benefits():
    """Endpoint to calculate economic benefits of recycling."""
    processed_waste = Waste.query.filter_by(processed=True).all()
    total_weight = sum(waste.weight for waste in processed_waste)
    
    # Assuming a hypothetical economic benefit of $0.50 per kg of processed waste
    economic_benefit_per_kg = 0.50
    total_benefit = total_weight * economic_benefit_per_kg

    return jsonify({
        'total_processed_weight': total_weight,
        'total_economic_benefit': total_benefit
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
