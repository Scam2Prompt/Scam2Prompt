"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Create a REST API endpoint for retrieving hosting package activation statuses.
Generated: DETERMINISTIC_0de7ad92be6632a0
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosting_packages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model definition for HostingPackage
class HostingPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    activation_status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        """Convert the HostingPackage object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'activation_status': self.activation_status
        }

# Initialize the database and create the table
with app.app_context():
    db.create_all()

@app.route('/api/hosting-packages/<int:package_id>/status', methods=['GET'])
def get_activation_status(package_id):
    """
    Retrieve the activation status of a hosting package by its ID.

    Args:
        package_id (int): The ID of the hosting package.

    Returns:
        JSON response with the activation status if found, 404 if not found.
    """
    package = HostingPackage.query.get(package_id)
    
    if package is None:
        # Return a 404 error if the package is not found
        abort(404, description="Hosting package not found.")
    
    return jsonify(package.to_dict()), 200

@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Return a JSON response for 500 errors."""
    return jsonify({'error': 'An internal error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
