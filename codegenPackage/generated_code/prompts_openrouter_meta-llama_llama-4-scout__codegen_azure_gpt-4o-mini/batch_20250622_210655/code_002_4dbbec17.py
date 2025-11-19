"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Generate a RESTful API endpoint to retrieve information about a specific villa or plot from the Corfu Coastal Collection, including its description, price, and location.
Generated: DETERMINISTIC_4dbbec17c26308dd
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///corfu_coastal_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Villa model
class Villa(db.Model):
    __tablename__ = 'villas'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)

    def to_dict(self):
        """Convert the Villa object to a dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'location': self.location
        }

# Create the database tables (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

# Define the API endpoint to retrieve villa information
@app.route('/api/villas/<int:villa_id>', methods=['GET'])
def get_villa(villa_id):
    """
    Retrieve information about a specific villa by its ID.
    
    Args:
        villa_id (int): The ID of the villa to retrieve.
    
    Returns:
        JSON response with villa details or 404 if not found.
    """
    villa = Villa.query.get(villa_id)
    
    if villa is None:
        # Return a 404 error if the villa is not found
        abort(404, description="Villa not found")
    
    return jsonify(villa.to_dict()), 200

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

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
