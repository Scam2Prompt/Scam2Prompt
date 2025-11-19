"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Develop an API endpoint that allows users to search for Endeavor Schools by state and program type, such as STEM or Active Athletes.
Generated: DETERMINISTIC_bce884021e596448
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///endeavor_schools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Database model for Endeavor Schools
class EndeavorSchool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    program_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'program_type': self.program_type
        }

# API endpoint to search for schools by state and program type
@app.route('/api/schools/search', methods=['GET'])
def search_schools():
    state = request.args.get('state')
    program_type = request.args.get('program_type')

    # Validate input parameters
    if not state or not program_type:
        return jsonify({'error': 'State and program type are required.'}), 400

    try:
        # Query the database for matching schools
        schools = EndeavorSchool.query.filter_by(state=state, program_type=program_type).all()
        return jsonify([school.to_dict() for school in schools]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
