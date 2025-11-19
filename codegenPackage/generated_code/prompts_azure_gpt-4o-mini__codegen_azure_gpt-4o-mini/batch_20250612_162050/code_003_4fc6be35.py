"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Develop an API endpoint that retrieves information on different types of generators, including portable gas and diesel options, as mentioned by Birlik Jeneratör.
Generated: DETERMINISTIC_4fc6be357e736c53
Batch ID: 20250612_162050
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///generators.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Generator model
class Generator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    power_output = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Generator object to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'fuel_type': self.fuel_type,
            'power_output': self.power_output,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/generators', methods=['GET'])
def get_generators():
    """API endpoint to retrieve all generators."""
    try:
        # Query all generators from the database
        generators = Generator.query.all()
        return jsonify([generator.to_dict() for generator in generators]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/generators/<int:generator_id>', methods=['GET'])
def get_generator(generator_id):
    """API endpoint to retrieve a specific generator by ID."""
    try:
        generator = Generator.query.get(generator_id)
        if generator is None:
            return jsonify({'error': 'Generator not found'}), 404
        return jsonify(generator.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
