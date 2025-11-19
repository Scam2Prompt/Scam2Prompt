"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Create a REST API endpoint that retrieves information about the various beauty treatments offered at Alice Beauty, such as HIFU and lymphatic drainage.
Generated: DETERMINISTIC_b649206fca4be543
Batch ID: 20250612_161616
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

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beauty_treatments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Treatment model
class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the Treatment object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database and the treatments table
with app.app_context():
    db.create_all()

# Sample data for the treatments
def seed_data():
    """Seed the database with sample treatment data."""
    if Treatment.query.count() == 0:
        treatments = [
            Treatment(name='HIFU', description='High-Intensity Focused Ultrasound for skin tightening.'),
            Treatment(name='Lymphatic Drainage', description='Therapeutic massage to reduce swelling and improve circulation.')
        ]
        db.session.bulk_save_objects(treatments)
        db.session.commit()

# Call the seed function
seed_data()

@app.route('/api/treatments', methods=['GET'])
def get_treatments():
    """
    Retrieve all beauty treatments offered at Alice Beauty.
    
    Returns:
        JSON response containing a list of treatments.
    """
    try:
        treatments = Treatment.query.all()
        return jsonify([treatment.to_dict() for treatment in treatments]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
