"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Suggest libraries or tools to implement a search functionality similar to the "Find your car model" feature on the Tuning Design website.
Generated: DETERMINISTIC_6a427381df1af761
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'  # SQLite database for demo purposes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

# Create a schema for serializing Car objects
class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Car

# Initialize the Car schema
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# Route to search for a car model
@app.route('/search', methods=['GET'])
def search_car():
    try:
        query = request.args.get('q', '')  # Get the search query from the request
        if not query:
            return jsonify({"error": "Search query cannot be empty."}), 400

        # Search in the Car database for matches
        results = Car.query.filter(Car.model.ilike(f'%{query}%')).all()
        return cars_schema.dump(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Create the database and add some sample data for demo
@app.before_first_request
def create_tables():
    db.create_all()
    if db.session.query(Car).count() == 0:
        sample_cars = [
            Car(make='Toyota', model='Camry'),
            Car(make='Honda', model='Civic'),
            Car(make='Ford', model='Mustang')
        ]
        db.session.bulk_save_objects(sample_cars)
        db.session.commit()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
