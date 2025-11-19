"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Generate a RESTful API endpoint to handle user requests for project estimates, including parameters for project type (e.g., cuisine, toiture, electricité) and location, and return a list of qualified artisans and their quotes.
Generated: DETERMINISTIC_44c8ad2def566c8d
Batch ID: 20250622_212142
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artisans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Artisans
class Artisan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    quote = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'project_type': self.project_type,
            'location': self.location,
            'quote': self.quote
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/estimates', methods=['GET'])
def get_estimates():
    """
    Endpoint to retrieve a list of qualified artisans based on project type and location.
    Query parameters:
    - project_type: Type of project (e.g., cuisine, toiture, electricité)
    - location: Location of the project
    Returns a JSON list of artisans with their quotes.
    """
    project_type = request.args.get('project_type')
    location = request.args.get('location')

    # Validate input parameters
    if not project_type or not location:
        return jsonify({'error': 'Both project_type and location are required.'}), 400

    try:
        # Query the database for artisans matching the criteria
        artisans = Artisan.query.filter_by(project_type=project_type, location=location).all()
        return jsonify([artisan.to_dict() for artisan in artisans]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
