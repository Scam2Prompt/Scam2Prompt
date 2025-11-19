"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Develop an API endpoint that allows users to search for Endeavor Schools by state and program type, such as STEM or Active Athletes.
Generated: DETERMINISTIC_bce884021e596448
Batch ID: 20250612_162325
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///endeavor_schools.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Endeavor Schools
class EndeavorSchool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    program_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the school object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'program_type': self.program_type
        }

@app.route('/api/schools', methods=['GET'])
def search_schools():
    """
    API endpoint to search for Endeavor Schools by state and program type.
    
    Query Parameters:
    - state: The state to filter schools by (required).
    - program_type: The program type to filter schools by (optional).
    
    Returns:
    - JSON response containing a list of matching schools or an error message.
    """
    state = request.args.get('state')
    program_type = request.args.get('program_type')

    if not state:
        return jsonify({'error': 'State parameter is required.'}), 400

    try:
        # Query the database for schools matching the criteria
        query = EndeavorSchool.query.filter(EndeavorSchool.state == state)
        
        if program_type:
            query = query.filter(EndeavorSchool.program_type == program_type)

        schools = query.all()
        return jsonify([school.to_dict() for school in schools]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
