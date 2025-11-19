"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Generate code to create a REST API endpoint for querying pediatric dentist details by location and specialty, inspired by the functionality on https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_754f3a1a3ee4d6e8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dentists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Dentist model
class Dentist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Dentist object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'specialty': self.specialty
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/dentists', methods=['GET'])
def get_dentists():
    """
    Query pediatric dentists by location and specialty.
    Query parameters:
    - location: The location to filter dentists.
    - specialty: The specialty to filter dentists.
    Returns a JSON response with the list of matching dentists.
    """
    location = request.args.get('location')
    specialty = request.args.get('specialty')

    # Validate query parameters
    if not location and not specialty:
        return jsonify({'error': 'At least one query parameter (location or specialty) is required.'}), 400

    try:
        # Build the query based on provided parameters
        query = Dentist.query
        if location:
            query = query.filter(Dentist.location.ilike(f'%{location}%'))
        if specialty:
            query = query.filter(Dentist.specialty.ilike(f'%{specialty}%'))

        # Execute the query and convert results to a list of dictionaries
        dentists = query.all()
        return jsonify([dentist.to_dict() for dentist in dentists]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string.
- This code includes basic error handling and input validation.
