"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Create an API endpoint for a takeaway food service that includes menu items like homemade pasta and ravioli, with options for pickup and delivery.
Generated: DETERMINISTIC_f79eb003c24f4d8c
Batch ID: 20250612_160507
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MenuItem model
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert the MenuItem object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'is_available': self.is_available
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/menu', methods=['GET'])
def get_menu():
    """API endpoint to retrieve the menu items."""
    try:
        items = MenuItem.query.all()
        return jsonify([item.to_dict() for item in items]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/menu', methods=['POST'])
def add_menu_item():
    """API endpoint to add a new menu item."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_item = MenuItem(name=data['name'], price=data['price'])
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Menu item already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/menu/<int:item_id>', methods=['PUT'])
def update_menu_item(item_id):
    """API endpoint to update an existing menu item."""
    data = request.get_json()
    item = MenuItem.query.get(item_id)

    if not item:
        return jsonify({'error': 'Menu item not found'}), 404

    if 'name' in data:
        item.name = data['name']
    if 'price' in data:
        item.price = data['price']
    if 'is_available' in data:
        item.is_available = data['is_available']

    try:
        db.session.commit()
        return jsonify(item.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    """API endpoint to delete a menu item."""
    item = MenuItem.query.get(item_id)

    if not item:
        return jsonify({'error': 'Menu item not found'}), 404

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Menu item deleted'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
