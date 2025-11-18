"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Suggest an API for designing and simulating the functionality of pipeline rollers with adjustable rigging stands, similar to the products offered by SPM Equipment.
Generated: DETERMINISTIC_05740ab5b9e0185e
Batch ID: 20250612_153246
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
from sqlalchemy.exc import IntegrityError, OperationalError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rollers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Roller model
class Roller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight_capacity = db.Column(db.Float, nullable=False)
    height_adjustment_range = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Roller {self.name}>'

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Route to create a new roller
@app.route('/rollers', methods=['POST'])
def create_roller():
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('name', 'weight_capacity', 'height_adjustment_range')):
        return jsonify({'error': 'Missing data'}), 400

    new_roller = Roller(
        name=data['name'],
        weight_capacity=data['weight_capacity'],
        height_adjustment_range=data['height_adjustment_range']
    )
    
    try:
        db.session.add(new_roller)
        db.session.commit()
        return jsonify({'message': 'Roller created successfully!', 'id': new_roller.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Roller already exists'}), 409
    except OperationalError:
        return jsonify({'error': 'Database operational error'}), 500

# Route to get all rollers
@app.route('/rollers', methods=['GET'])
def get_rollers():
    rollers = Roller.query.all()
    return jsonify([{'id': roller.id, 'name': roller.name, 
                     'weight_capacity': roller.weight_capacity, 
                     'height_adjustment_range': roller.height_adjustment_range} for roller in rollers]), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
