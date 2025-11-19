"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Create an API endpoint that allows users to retrieve information about the different DragonZ families and their special powers for the Clash of DragonZ game.
Generated: DETERMINISTIC_556bf9224950b8b6
Batch ID: 20250612_135829
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

app = Flask(__name__)

# Configure your database URI (this is just an example; adjust as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dragonz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class DragonFamily(db.Model):
    """Model representing a Dragon Family."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    special_power = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the DragonFamily instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'special_power': self.special_power
        }

@app.route('/api/dragonfamilies', methods=['GET'])
def get_dragon_families():
    """API endpoint to retrieve all dragon families and their special powers."""
    try:
        families = DragonFamily.query.all()
        return jsonify([family.to_dict() for family in families]), 200
    except SQLAlchemyError as e:
        # Log the error (not shown here for simplicity)
        return jsonify({'error': 'An error occurred while retrieving dragon families.'}), 500

@app.route('/api/dragonfamilies/<int:id>', methods=['GET'])
def get_dragon_family(id):
    """API endpoint to retrieve a specific dragon family by ID."""
    try:
        family = DragonFamily.query.get_or_404(id)
        return jsonify(family.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (not shown here for simplicity)
        return jsonify({'error': 'An error occurred while retrieving the dragon family.'}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

Make sure to set up your database and populate it with the required data for the `DragonFamily` model before running the Flask application.
