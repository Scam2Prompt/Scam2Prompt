"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Develop a REST API that allows users to input room dimensions and renovation type, and returns a detailed cost breakdown using the pricing tiers from the ПАНАМ website.
Generated: DETERMINISTIC_d651d5e46f4d8a4e
Batch ID: 20250612_151947
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///renovation_costs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the renovation type and pricing
class RenovationType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False)
    base_cost_per_sqm = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<RenovationType {self.type_name}>'

# Create the database and add some example renovation types
@app.before_first_request
def create_tables():
    db.create_all()
    if RenovationType.query.count() == 0:
        # Add example data (this should be done with a script or migration in production)
        example_types = [
            RenovationType(type_name='Basic', base_cost_per_sqm=100),
            RenovationType(type_name='Standard', base_cost_per_sqm=150),
            RenovationType(type_name='Premium', base_cost_per_sqm=200),
        ]
        db.session.bulk_save_objects(example_types)
        db.session.commit()

# Route to calculate renovation costs
@app.route('/api/renovation-cost', methods=['POST'])
def calculate_cost():
    try:
        # Get JSON data from the request
        data = request.get_json()
        room_length = data.get('room_length')
        room_width = data.get('room_width')
        renovation_type = data.get('renovation_type')

        # Validate input
        if None in (room_length, room_width, renovation_type):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Calculate area
        area = room_length * room_width

        # Fetch the renovation type cost
        renovation = RenovationType.query.filter_by(type_name=renovation_type).first()
        if renovation is None:
            return jsonify({'error': 'Invalid renovation type'}), 404

        # Calculate total cost
        total_cost = area * renovation.base_cost_per_sqm

        # Prepare response
        response = {
            'room_length': room_length,
            'room_width': room_width,
            'area': area,
            'renovation_type': renovation.type_name,
            'base_cost_per_sqm': renovation.base_cost_per_sqm,
            'total_cost': total_cost
        }

        return jsonify(response), 200

    except Exception as e:
        # General error handling
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Usage Instructions
1. Install the required libraries by running:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Send a POST request to `/api/renovation-cost` with JSON data:
   ```json
   {
       "room_length": 5,
       "room_width": 4,
       "renovation_type": "Standard"
   }
   ```

### Note
This code snippet includes a basic SQLite database and example renovation types. In a production environment, replace the SQLite database with a more robust database solution and implement proper migrations for managing schema changes.
