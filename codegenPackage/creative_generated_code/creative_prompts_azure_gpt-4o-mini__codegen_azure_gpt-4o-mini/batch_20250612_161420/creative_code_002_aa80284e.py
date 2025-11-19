"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marqador.com
Prompt: Create an API endpoint that retrieves details about personalized stamps for children and businesses, similar to the offerings on marQadoR.
Generated: DETERMINISTIC_aa80284e09e9553c
Batch ID: 20250612_161420
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

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stamps.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Stamp model for the database
class Stamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Stamp object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/stamps', methods=['GET'])
def get_stamps():
    """
    Retrieve a list of all personalized stamps.
    Returns:
        JSON response with a list of stamps or an error message.
    """
    try:
        # Fetch all stamps from the database
        stamps = Stamp.query.all()
        return jsonify([stamp.to_dict() for stamp in stamps]), 200
    except SQLAlchemyError as e:
        # Log the error and return a 500 error response
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

@app.route('/api/stamps/<int:stamp_id>', methods=['GET'])
def get_stamp(stamp_id):
    """
    Retrieve details of a specific stamp by ID.
    Args:
        stamp_id (int): The ID of the stamp to retrieve.
    Returns:
        JSON response with stamp details or an error message.
    """
    try:
        stamp = Stamp.query.get_or_404(stamp_id)  # Automatically returns 404 if not found
        return jsonify(stamp.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
