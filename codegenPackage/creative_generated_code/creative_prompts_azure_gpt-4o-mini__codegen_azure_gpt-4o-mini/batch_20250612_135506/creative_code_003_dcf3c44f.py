"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Develop a REST API endpoint that returns information about different types of towels, such as Ihram towels and bath robes, similar to what is offered by Regency Towel.
Generated: DETERMINISTIC_dcf3c44f88bb1df2
Batch ID: 20250612_135506
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///towels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for towels
class Towel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Towel object to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'material': self.material,
            'color': self.color,
            'price': self.price,
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/towels', methods=['GET'])
def get_towels():
    """API Endpoint to retrieve information about towels."""
    try:
        towels = Towel.query.all()
        return jsonify([towel.to_dict() for towel in towels]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/towels', methods=['POST'])
def add_towel():
    """API Endpoint to add a new towel."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('type', 'material', 'color', 'price')):
        return jsonify({"error": "Missing fields."}), 400

    new_towel = Towel(
        type=data['type'],
        material=data['material'],
        color=data['color'],
        price=data['price']
    )
    
    try:
        db.session.add(new_towel)
        db.session.commit()
        return jsonify(new_towel.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
