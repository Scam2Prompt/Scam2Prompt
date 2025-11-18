"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Write a Python script using Flask to create an API for retrieving information about eco-lodges, such as "سان لند," including features like "traditional cooking" and "nature tours."
Generated: DETERMINISTIC_f6f99f75d11bd752
Batch ID: 20250612_150130
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (this is an example; configure it as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_lodges.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# EcoLodge model representing the eco-lodges table
class EcoLodge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    features = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'features': self.features.split(', ')  # Split features into a list
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve information about eco-lodges
@app.route('/api/ecolodges', methods=['GET'])
def get_ecolodges():
    try:
        # Retrieve all eco-lodges from the database
        eco_lodges = EcoLodge.query.all()
        return jsonify([lodge.to_dict() for lodge in eco_lodges]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new eco-lodge (for demonstration purposes)
@app.route('/api/ecolodges', methods=['POST'])
def add_ecolodge():
    data = request.get_json()
    
    if not data or 'name' not in data or 'features' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_lodge = EcoLodge(name=data['name'], features=', '.join(data['features']))
    
    try:
        db.session.add(new_lodge)
        db.session.commit()
        return jsonify(new_lodge.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
