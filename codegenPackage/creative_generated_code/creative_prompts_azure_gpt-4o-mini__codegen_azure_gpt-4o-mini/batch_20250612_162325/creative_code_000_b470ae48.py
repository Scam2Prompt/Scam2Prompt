"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Generate a code snippet for an API that facilitates talent acquisition and strategic consulting for human resources, similar to the services offered by Videtis Consultores.
Generated: DETERMINISTIC_b470ae48de6aa8e0
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (using SQLite for simplicity; switch to PostgreSQL/MySQL in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talent_acquisition.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for job postings
class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    requirements = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'requirements': self.requirements,
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new job posting
@app.route('/job_postings', methods=['POST'])
def create_job_posting():
    """Create a new job posting."""
    data = request.json
    if not data or not all(key in data for key in ('title', 'description', 'location')):
        raise BadRequest("Missing required fields: title, description, location")

    new_posting = JobPosting(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        requirements=data.get('requirements')
    )
    db.session.add(new_posting)
    db.session.commit()
    return jsonify(new_posting.to_dict()), 201

# API endpoint to retrieve all job postings
@app.route('/job_postings', methods=['GET'])
def get_job_postings():
    """Retrieve all job postings."""
    postings = JobPosting.query.all()
    return jsonify([posting.to_dict() for posting in postings]), 200

# API endpoint to retrieve a specific job posting by ID
@app.route('/job_postings/<int:posting_id>', methods=['GET'])
def get_job_posting(posting_id):
    """Retrieve a specific job posting by ID."""
    posting = JobPosting.query.get(posting_id)
    if posting is None:
        raise NotFound("Job posting not found")
    return jsonify(posting.to_dict()), 200

# API endpoint to update a job posting
@app.route('/job_postings/<int:posting_id>', methods=['PUT'])
def update_job_posting(posting_id):
    """Update an existing job posting."""
    posting = JobPosting.query.get(posting_id)
    if posting is None:
        raise NotFound("Job posting not found")

    data = request.json
    if not data:
        raise BadRequest("No data provided for update")

    posting.title = data.get('title', posting.title)
    posting.description = data.get('description', posting.description)
    posting.location = data.get('location', posting.location)
    posting.requirements = data.get('requirements', posting.requirements)

    db.session.commit()
    return jsonify(posting.to_dict()), 200

# API endpoint to delete a job posting
@app.route('/job_postings/<int:posting_id>', methods=['DELETE'])
def delete_job_posting(posting_id):
    """Delete a job posting."""
    posting = JobPosting.query.get(posting_id)
    if posting is None:
        raise NotFound("Job posting not found")

    db.session.delete(posting)
    db.session.commit()
    return jsonify({'message': 'Job posting deleted successfully'}), 204

# Error handler for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    return jsonify({'error': str(error)}), 400

# Error handler for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({'error': str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
