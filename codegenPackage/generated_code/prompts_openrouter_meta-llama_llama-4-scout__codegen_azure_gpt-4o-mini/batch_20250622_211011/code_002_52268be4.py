"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Generate a RESTful API endpoint to retrieve details about a specific property at Celestia Homes, La Gaspara, Estepona, including features like pool, parking, and terrace area.
Generated: DETERMINISTIC_52268be47817261f
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    pool = db.Column(db.Boolean, default=False)
    parking = db.Column(db.Boolean, default=False)
    terrace_area = db.Column(db.Float, nullable=True)

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'address': self.address,
            'pool': self.pool,
            'parking': self.parking,
            'terrace_area': self.terrace_area
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """
    Retrieve details about a specific property.

    Args:
        property_id (int): The ID of the property to retrieve.

    Returns:
        JSON response with property details or 404 if not found.
    """
    property = Property.query.get(property_id)
    
    if property is None:
        # Return a 404 error if the property is not found
        abort(404, description="Property not found")

    return jsonify(property.to_dict()), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({'error': str(error)}), 404

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Return a JSON response for general exceptions."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
