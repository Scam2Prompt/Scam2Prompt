"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Outline a RESTful API design for a service that manages custom wrestling championship belts, referencing the product categories found on wwereplicabelts.com.
Generated: DETERMINISTIC_21a8892f92c10afd
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///belts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Belt
class Belt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# API endpoint to get all belts
@app.route('/belts', methods=['GET'])
def get_belts():
    belts = Belt.query.all()
    return jsonify([belt.to_dict() for belt in belts]), 200

# API endpoint to get a specific belt by ID
@app.route('/belts/<int:belt_id>', methods=['GET'])
def get_belt(belt_id):
    belt = Belt.query.get(belt_id)
    if belt is None:
        abort(404)
    return jsonify(belt.to_dict()), 200

# API endpoint to create a new belt
@app.route('/belts', methods=['POST'])
def create_belt():
    if not request.json or not 'name' in request.json or not 'category' in request.json or not 'price' in request.json:
        abort(400)  # Bad request
    new_belt = Belt(
        name=request.json['name'],
        category=request.json['category'],
        price=request.json['price']
    )
    db.session.add(new_belt)
    db.session.commit()
    return jsonify(new_belt.to_dict()), 201

# API endpoint to update an existing belt
@app.route('/belts/<int:belt_id>', methods=['PUT'])
def update_belt(belt_id):
    belt = Belt.query.get(belt_id)
    if belt is None:
        abort(404)

    if not request.json:
        abort(400)  # Bad request

    # Update belt properties
    belt.name = request.json.get('name', belt.name)
    belt.category = request.json.get('category', belt.category)
    belt.price = request.json.get('price', belt.price)
    
    db.session.commit()
    return jsonify(belt.to_dict()), 200

# API endpoint to delete a belt
@app.route('/belts/<int:belt_id>', methods=['DELETE'])
def delete_belt(belt_id):
    belt = Belt.query.get(belt_id)
    if belt is None:
        abort(404)
    
    db.session.delete(belt)
    db.session.commit()
    return jsonify({'result': True}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
