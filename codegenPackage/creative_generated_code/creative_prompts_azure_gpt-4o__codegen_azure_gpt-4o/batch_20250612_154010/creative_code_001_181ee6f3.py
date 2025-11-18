"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Recommend libraries or APIs to create a searchable database for psychologists in Oruro, including their certifications, memberships, and participation in courses or seminars as described on the Colegio de Psicólogos de Oruro website.
Generated: DETERMINISTIC_181ee6f313c5c76b
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify  # Flask for API creation
from flask_sqlalchemy import SQLAlchemy    # SQLAlchemy for database handling
from sqlalchemy.exc import SQLAlchemyError # Error handling for database operations

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (use your actual database credentials here)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///psychologists.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Psychologist model to store data
class Psychologist(db.Model):
    __tablename__ = 'psychologists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    certifications = db.Column(db.Text, nullable=True)  # Text for multiple certifications
    memberships = db.Column(db.Text, nullable=True)     # Text for multiple memberships
    courses_seminars = db.Column(db.Text, nullable=True)  # Text for courses/seminars

    def to_dict(self):
        """
        Convert the Psychologist object into a dictionary format for JSON responses.
        """
        return {
            'id': self.id,
            'name': self.name,
            'certifications': self.certifications,
            'memberships': self.memberships,
            'courses_seminars': self.courses_seminars
        }

# Route to add a psychologist to the database
@app.route('/psychologists', methods=['POST'])
def add_psychologist():
    """
    Endpoint to add a new psychologist to the database.
    Expects JSON input with 'name', 'certifications', 'memberships', and 'courses_seminars'.
    """
    try:
        data = request.json
        name = data.get('name')
        certifications = data.get('certifications', '')
        memberships = data.get('memberships', '')
        courses_seminars = data.get('courses_seminars', '')

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        # Create a new Psychologist object
        new_psychologist = Psychologist(
            name=name,
            certifications=certifications,
            memberships=memberships,
            courses_seminars=courses_seminars
        )
        db.session.add(new_psychologist)
        db.session.commit()

        return jsonify({'message': 'Psychologist added successfully', 'psychologist': new_psychologist.to_dict()}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route to search psychologists by name or filter by certifications/memberships/courses_seminars
@app.route('/psychologists/search', methods=['GET'])
def search_psychologists():
    """
    Endpoint to search psychologists based on query parameters.
    Supports filtering by name, certifications, memberships, or courses/seminars.
    """
    try:
        name = request.args.get('name')
        certifications = request.args.get('certifications')
        memberships = request.args.get('memberships')
        courses_seminars = request.args.get('courses_seminars')

        query = Psychologist.query

        # Apply filters based on query parameters
        if name:
            query = query.filter(Psychologist.name.ilike(f'%{name}%'))
        if certifications:
            query = query.filter(Psychologist.certifications.ilike(f'%{certifications}%'))
        if memberships:
            query = query.filter(Psychologist.memberships.ilike(f'%{memberships}%'))
        if courses_seminars:
            query = query.filter(Psychologist.courses_seminars.ilike(f'%{courses_seminars}%'))

        # Execute the query
        results = query.all()
        return jsonify({'psychologists': [psychologist.to_dict() for psychologist in results]}), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route to get all psychologists
@app.route('/psychologists', methods=['GET'])
def get_all_psychologists():
    """
    Endpoint to retrieve all psychologists from the database.
    """
    try:
        psychologists = Psychologist.query.all()
        return jsonify({'psychologists': [psychologist.to_dict() for psychologist in psychologists]}), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Route to get a psychologist by ID
@app.route('/psychologists/<int:id>', methods=['GET'])
def get_psychologist_by_id(id):
    """
    Endpoint to retrieve a psychologist by their ID.
    """
    try:
        psychologist = Psychologist.query.get(id)
        if not psychologist:
            return jsonify({'error': 'Psychologist not found'}), 404
        
        return jsonify({'psychologist': psychologist.to_dict()}), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Error Handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({'error': 'Endpoint not found'}), 404

# Start the Flask application
if __name__ == '__main__':
    # Create the database tables if they do not already exist
    with app.app_context():
        db.create_all()

    # Run the Flask server
    app.run(debug=True)
```
