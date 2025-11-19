"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate a code snippet to create an e-commerce API that lists agricultural and construction equipment similar to those found on the Gala Games app website.
Generated: DETERMINISTIC_ee893b1e4dea4c83
Batch ID: 20250612_163324
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Equipment
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def as_dict(self):
        """Return a dictionary representation of the Equipment instance."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

# Create database tables
with app.app_context():
    db.create_all()

# Endpoint to get all equipment
@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    """Fetch all equipment items from the database."""
    try:
        equipment_list = Equipment.query.all()
        return jsonify([item.as_dict() for item in equipment_list]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add new equipment
@app.route('/api/equipment', methods=['POST'])
def add_equipment():
    """Add a new equipment item to the database."""
    data = request.get_json()
    
    try:
        new_equipment = Equipment(
            name=data['name'],
            category=data['category'],
            price=data['price']
        )
        db.session.add(new_equipment)
        db.session.commit()
        return jsonify(new_equipment.as_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error. Check your data.'}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
