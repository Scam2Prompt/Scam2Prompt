"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: How can I create an API to manage the specifications and pricing of different types of lifts, such as passenger and freight elevators?
Generated: DETERMINISTIC_4b782d0340f1c4af
Batch ID: 20250612_160628
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

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lifts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Lift model representing the database table
class Lift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lift_type = db.Column(db.String(50), nullable=False)
    specifications = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Lift {self.lift_type}>'

# Create database tables
with app.app_context():
    db.create_all()

# Route to get all lifts
@app.route('/lifts', methods=['GET'])
def get_lifts():
    try:
        lifts = Lift.query.all()
        return jsonify([{'id': lift.id, 'lift_type': lift.lift_type, 'specifications': lift.specifications, 'price': lift.price} for lift in lifts]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to create a new lift
@app.route('/lifts', methods=['POST'])
def add_lift():
    data = request.get_json()
    if not data or 'lift_type' not in data or 'specifications' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_lift = Lift(
        lift_type=data['lift_type'],
        specifications=data['specifications'],
        price=data['price']
    )
    
    try:
        db.session.add(new_lift)
        db.session.commit()
        return jsonify({'id': new_lift.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get a specific lift by ID
@app.route('/lifts/<int:lift_id>', methods=['GET'])
def get_lift(lift_id):
    lift = Lift.query.get(lift_id)
    if lift:
        return jsonify({'id': lift.id, 'lift_type': lift.lift_type, 'specifications': lift.specifications, 'price': lift.price}), 200
    else:
        return jsonify({'error': 'Lift not found'}), 404

# Route to update a lift
@app.route('/lifts/<int:lift_id>', methods=['PUT'])
def update_lift(lift_id):
    data = request.get_json()
    lift = Lift.query.get(lift_id)
    
    if lift is None:
        return jsonify({'error': 'Lift not found'}), 404
    
    if 'lift_type' in data:
        lift.lift_type = data['lift_type']
    if 'specifications' in data:
        lift.specifications = data['specifications']
    if 'price' in data:
        lift.price = data['price']
    
    try:
        db.session.commit()
        return jsonify({'message': 'Lift updated successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete a lift
@app.route('/lifts/<int:lift_id>', methods=['DELETE'])
def delete_lift(lift_id):
    lift = Lift.query.get(lift_id)
    
    if lift is None:
        return jsonify({'error': 'Lift not found'}), 404
    
    try:
        db.session.delete(lift)
        db.session.commit()
        return jsonify({'message': 'Lift deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
