"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Create an API endpoint for a cleaning service platform that retrieves available cleaning packages, similar to the customized solutions offered by Star Cleaning Services.
Generated: DETERMINISTIC_442990a1c0ad3d50
Batch ID: 20250612_160703
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

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CleaningPackage model
class CleaningPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the CleaningPackage object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/cleaning-packages', methods=['GET'])
def get_cleaning_packages():
    """
    Retrieve all available cleaning packages.

    Returns:
        JSON response containing a list of cleaning packages.
    """
    try:
        packages = CleaningPackage.query.all()
        return jsonify([package.to_dict() for package in packages]), 200
    except SQLAlchemyError as e:
        # Log the error (logging not implemented in this example)
        return jsonify({'error': 'An error occurred while retrieving packages.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
