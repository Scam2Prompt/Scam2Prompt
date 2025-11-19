"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Develop a RESTful API endpoint that retrieves information about different safari experiences in Tanzania, including mid-range and luxury options, and formats the data for a mobile app.
Generated: DETERMINISTIC_ca102ea597463df8
Batch ID: 20250612_164122
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safari_experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SafariExperience model
class SafariExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'mid-range', 'luxury'
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/safari-experiences', methods=['GET'])
def get_safari_experiences():
    """Retrieve all safari experiences filtered by type if specified."""
    experience_type = request.args.get('type')
    
    try:
        if experience_type:
            experiences = SafariExperience.query.filter_by(type=experience_type).all()
        else:
            experiences = SafariExperience.query.all()
        
        # Convert the experiences to a list of dictionaries
        return jsonify([experience.to_dict() for experience in experiences]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and SQLAlchemy installed in your environment. You can install them using pip:
  ```bash
  pip install Flask SQLAlchemy
  ```
- This code sets up a simple RESTful API using Flask and SQLAlchemy, with a SQLite database for storing safari experiences.
- The API endpoint `/api/safari-experiences` allows for optional filtering by experience type (e.g., 'mid-range' or 'luxury').
- Error handling is included for database-related issues.
