"""
Generated Code Metadata:
========================
Original URL: https://celestia.top
Prompt: Recommend tools or libraries for creating a case study repository system, inspired by the thought-provoking articles and case studies mentioned in Celestia's Études Newsletter.
Generated: DETERMINISTIC_b6f0a68f3ca43a6b
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study Repository System

This script provides a basic implementation of a case study repository system.
It allows users to add, retrieve, and list case studies. The system is designed
to be extensible and can be integrated with various storage backends.

Dependencies:
- Flask: A lightweight WSGI web application framework.
- SQLAlchemy: An ORM for database interactions.

To run this application, ensure you have Flask and SQLAlchemy installed:
pip install Flask SQLAlchemy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///case_studies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CaseStudy model
class CaseStudy(db.Model):
    """Model representing a case study."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the CaseStudy instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/case_studies', methods=['POST'])
def add_case_study():
    """Endpoint to add a new case study."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Title and content are required.'}), 400

    new_case_study = CaseStudy(title=title, content=content)

    try:
        db.session.add(new_case_study)
        db.session.commit()
        return jsonify(new_case_study.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Case study with this title already exists.'}), 409

@app.route('/case_studies', methods=['GET'])
def list_case_studies():
    """Endpoint to retrieve all case studies."""
    case_studies = CaseStudy.query.all()
    return jsonify([case_study.to_dict() for case_study in case_studies]), 200

@app.route('/case_studies/<int:case_study_id>', methods=['GET'])
def get_case_study(case_study_id):
    """Endpoint to retrieve a specific case study by ID."""
    case_study = CaseStudy.query.get_or_404(case_study_id)
    return jsonify(case_study.to_dict()), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
