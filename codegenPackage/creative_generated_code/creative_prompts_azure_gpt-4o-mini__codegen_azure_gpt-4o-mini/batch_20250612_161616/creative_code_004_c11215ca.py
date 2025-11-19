"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sopa.vg
Prompt: Suggest a library for building a restaurant menu application that emphasizes local, organic ingredients, akin to the philosophy of Sopa Restaurante.
Generated: DETERMINISTIC_c11215ca90a11bf2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# restaurant_menu.py

"""
A simple restaurant menu application that emphasizes local, organic ingredients.
This application utilizes Flask for the web framework and SQLAlchemy for the database ORM.
"""

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant_menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Menu Item
class MenuItem(db.Model):
    """Represents a menu item in the restaurant."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_organic = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the MenuItem to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_organic': self.is_organic
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/menu', methods=['GET'])
def get_menu():
    """Get the list of menu items."""
    try:
        menu_items = MenuItem.query.all()
        return jsonify([item.to_dict() for item in menu_items]), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/menu', methods=['POST'])
def add_menu_item():
    """Add a new menu item to the menu."""
    data = request.get_json()
    
    if not data or not all(key in data for key in ('name', 'description', 'price', 'is_organic')):
        abort(400, description="Missing information in request data.")
    
    new_item = MenuItem(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        is_organic=data['is_organic']
    )
    
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    """Delete a menu item by its ID."""
    item = MenuItem.query.get(item_id)
    
    if item is None:
        abort(404, description="Menu item not found.")
    
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Menu item deleted."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Running the application
    app.run(debug=True)
```

Make sure to install the required libraries using the following command:
```bash
pip install Flask Flask-SQLAlchemy
```
