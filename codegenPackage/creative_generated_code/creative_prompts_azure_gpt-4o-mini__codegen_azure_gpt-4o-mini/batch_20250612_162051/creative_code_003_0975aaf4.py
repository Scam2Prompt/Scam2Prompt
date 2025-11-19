"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Develop a RESTful API endpoint that retrieves best-selling jewelry items, akin to the Polki Chandbalis and diamond rings from Atmanam Jewels.
Generated: DETERMINISTIC_0975aaf4c6edf678
Batch ID: 20250612_162051
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry.db'  # Change to your database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Jewelry model definition
class Jewelry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    best_selling = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the Jewelry object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'price': self.price,
            'best_selling': self.best_selling
        }

@app.route('/api/jewelry/best-selling', methods=['GET'])
def get_best_selling_jewelry():
    """Retrieve best-selling jewelry items."""
    try:
        # Query for best-selling jewelry
        best_selling_items = Jewelry.query.filter_by(best_selling=True).all()
        return jsonify([item.to_dict() for item in best_selling_items]), 200
    
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/jewelry', methods=['POST'])
def add_jewelry():
    """Add a new jewelry item to the database."""
    data = request.json
    try:
        new_item = Jewelry(
            name=data['name'],
            type=data['type'],
            price=data['price'],
            best_selling=data.get('best_selling', False)
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    
    except (KeyError, TypeError) as e:
        return jsonify({'error': f'Missing or invalid data: {str(e)}'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
