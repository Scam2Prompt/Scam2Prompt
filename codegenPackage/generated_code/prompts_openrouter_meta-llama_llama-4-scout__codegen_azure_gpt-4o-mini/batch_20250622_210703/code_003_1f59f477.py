"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Develop a simple API to retrieve information about dōTERRA essential oils, including their ingredients, benefits, and uses.
Generated: DETERMINISTIC_1f59f47720f924bf
Batch ID: 20250622_210703
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essential_oils.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the EssentialOil model
class EssentialOil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    uses = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the EssentialOil object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'benefits': self.benefits,
            'uses': self.uses
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/oils', methods=['GET'])
def get_oils():
    """Retrieve a list of all essential oils."""
    try:
        oils = EssentialOil.query.all()
        return jsonify([oil.to_dict() for oil in oils]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/oils/<int:oil_id>', methods=['GET'])
def get_oil(oil_id):
    """Retrieve information about a specific essential oil by ID."""
    try:
        oil = EssentialOil.query.get_or_404(oil_id)
        return jsonify(oil.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/oils', methods=['POST'])
def add_oil():
    """Add a new essential oil to the database."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'ingredients', 'benefits', 'uses')):
        return jsonify({'error': 'Missing data'}), 400

    new_oil = EssentialOil(
        name=data['name'],
        ingredients=data['ingredients'],
        benefits=data['benefits'],
        uses=data['uses']
    )

    try:
        db.session.add(new_oil)
        db.session.commit()
        return jsonify(new_oil.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
