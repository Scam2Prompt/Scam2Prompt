"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Write a Python script using Flask to create an API for retrieving information about eco-lodges, such as "سان لند," including features like "traditional cooking" and "nature tours."
Generated: DETERMINISTIC_f6f99f75d11bd752
Batch ID: 20250612_150130
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

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_lodges.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the EcoLodge model
class EcoLodge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    features = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the EcoLodge object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'features': self.features.split(',')  # Split features into a list
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/eco-lodges', methods=['GET'])
def get_eco_lodges():
    """Retrieve a list of eco-lodges."""
    try:
        eco_lodges = EcoLodge.query.all()
        return jsonify([lodge.to_dict() for lodge in eco_lodges]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/eco-lodges/<int:lodge_id>', methods=['GET'])
def get_eco_lodge(lodge_id):
    """Retrieve a specific eco-lodge by ID."""
    try:
        lodge = EcoLodge.query.get_or_404(lodge_id)
        return jsonify(lodge.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/eco-lodges', methods=['POST'])
def create_eco_lodge():
    """Create a new eco-lodge."""
    data = request.get_json()
    if not data or 'name' not in data or 'features' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_lodge = EcoLodge(name=data['name'], features=','.join(data['features']))
    try:
        db.session.add(new_lodge)
        db.session.commit()
        return jsonify(new_lodge.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
