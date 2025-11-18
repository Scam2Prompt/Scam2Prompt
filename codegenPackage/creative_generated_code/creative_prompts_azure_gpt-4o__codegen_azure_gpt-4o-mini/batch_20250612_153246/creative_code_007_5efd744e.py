"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Suggest an API for integrating a műanyag nyílászáró (plastic window and door) catalog into a website, with filtering options for légkamrák száma (number of air chambers) and hőszigetelés (thermal insulation).
Generated: DETERMINISTIC_5efd744ebe39fc05
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for the plastic window and door catalog
class WindowDoor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    air_chambers = db.Column(db.Integer, nullable=False)
    thermal_insulation = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'air_chambers': self.air_chambers,
            'thermal_insulation': self.thermal_insulation
        }

# Route to get the catalog with filtering options
@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    try:
        # Get filtering parameters from the request
        air_chambers = request.args.get('air_chambers', type=int)
        thermal_insulation = request.args.get('thermal_insulation', type=float)

        # Query the database based on provided filters
        query = WindowDoor.query

        if air_chambers is not None:
            query = query.filter(WindowDoor.air_chambers == air_chambers)

        if thermal_insulation is not None:
            query = query.filter(WindowDoor.thermal_insulation <= thermal_insulation)

        # Fetch the results
        results = query.all()
        return jsonify([window_door.to_dict() for window_door in results]), 200

    except Exception as e:
        # Handle exceptions and return an error message
        return jsonify({"error": str(e)}), 500

# Function to create the database (if it doesn't already exist)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
