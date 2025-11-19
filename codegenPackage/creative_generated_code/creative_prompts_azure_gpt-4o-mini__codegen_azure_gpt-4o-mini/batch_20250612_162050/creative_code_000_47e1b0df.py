"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Generate a code snippet for a web application that facilitates the creation of pocket neighborhoods, incorporating features like shared spaces and multi-generational living.
Generated: DETERMINISTIC_47e1b0df203487ec
Batch ID: 20250612_162050
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pocket_neighborhoods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and serialization
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Neighborhood model
class Neighborhood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    shared_spaces = db.Column(db.String(250), nullable=True)
    multi_generational_living = db.Column(db.Boolean, default=False)

    def __init__(self, name, shared_spaces, multi_generational_living):
        self.name = name
        self.shared_spaces = shared_spaces
        self.multi_generational_living = multi_generational_living

# Neighborhood schema for serialization
class NeighborhoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Neighborhood

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new neighborhood
@app.route('/neighborhoods', methods=['POST'])
def create_neighborhood():
    try:
        # Get data from the request
        name = request.json['name']
        shared_spaces = request.json.get('shared_spaces', '')
        multi_generational_living = request.json.get('multi_generational_living', False)

        # Create a new neighborhood instance
        new_neighborhood = Neighborhood(name, shared_spaces, multi_generational_living)

        # Add the neighborhood to the database
        db.session.add(new_neighborhood)
        db.session.commit()

        # Serialize the neighborhood object for the response
        neighborhood_schema = NeighborhoodSchema()
        return neighborhood_schema.jsonify(new_neighborhood), 201
    except Exception as e:
        # Handle errors and return a 400 response
        return jsonify({'message': 'Error creating neighborhood', 'error': str(e)}), 400

# Route to get all neighborhoods
@app.route('/neighborhoods', methods=['GET'])
def get_neighborhoods():
    try:
        neighborhoods = Neighborhood.query.all()
        neighborhood_schema = NeighborhoodSchema(many=True)
        return neighborhood_schema.jsonify(neighborhoods), 200
    except Exception as e:
        # Handle errors and return a 500 response
        return jsonify({'message': 'Error fetching neighborhoods', 'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
