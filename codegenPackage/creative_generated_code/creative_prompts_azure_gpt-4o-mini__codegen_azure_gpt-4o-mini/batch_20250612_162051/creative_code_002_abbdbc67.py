"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arbella.co.il
Prompt: Create a REST API endpoint that allows users to retrieve information about different yogurt flavors, including peach and strawberry, from Arbella's product line.
Generated: DETERMINISTIC_abbdbc679ed9b320
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yogurt_flavors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define YogurtFlavor model
class YogurtFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the YogurtFlavor object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database and add initial flavors if not exists
@app.before_first_request
def create_tables():
    db.create_all()
    if not YogurtFlavor.query.first():  # Check if the table is empty
        # Add initial yogurt flavors
        peach = YogurtFlavor(name='Peach', description='A delicious peach-flavored yogurt.')
        strawberry = YogurtFlavor(name='Strawberry', description='A delightful strawberry-flavored yogurt.')
        db.session.add(peach)
        db.session.add(strawberry)
        db.session.commit()

# Define a route to retrieve yogurt flavors
@app.route('/api/yogurt_flavors', methods=['GET'])
def get_yogurt_flavors():
    """Retrieve a list of yogurt flavors."""
    try:
        flavors = YogurtFlavor.query.all()
        return jsonify([flavor.to_dict() for flavor in flavors]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'An error occurred while retrieving flavors.'}), 500

# Define a route to retrieve a specific yogurt flavor by name
@app.route('/api/yogurt_flavors/<string:name>', methods=['GET'])
def get_yogurt_flavor(name):
    """Retrieve a specific yogurt flavor by name."""
    try:
        flavor = YogurtFlavor.query.filter_by(name=name).first()
        if flavor is None:
            return jsonify({'error': 'Yogurt flavor not found.'}), 404
        return jsonify(flavor.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'An error occurred while retrieving the flavor.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
