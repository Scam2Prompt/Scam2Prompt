"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Suggest a library or framework for building a job placement portal similar to the "Servizi per il Lavoro" section of Araform, with features for candidate submissions and employer listings.
Generated: DETERMINISTIC_3d7940535cdc79a1
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# job_placement_portal.py

# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_placement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Candidate {self.name}>'

# Define the Employer model
class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    job_listings = db.relationship('JobListing', backref='employer', lazy=True)

    def __repr__(self):
        return f'<Employer {self.company_name}>'

# Define the Job Listing model
class JobListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)

    def __repr__(self):
        return f'<JobListing {self.title}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e), code=e.code), e.code

# Route to submit a candidate
@app.route('/candidates', methods=['POST'])
def add_candidate():
    """Add a new candidate"""
    try:
        data = request.get_json()
        new_candidate = Candidate(name=data['name'], resume=data['resume'])
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to list candidates
@app.route('/candidates', methods=['GET'])
def list_candidates():
    """List all candidates"""
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in candidates]), 200

# Route to submit an employer
@app.route('/employers', methods=['POST'])
def add_employer():
    """Add a new employer"""
    try:
        data = request.get_json()
        new_employer = Employer(company_name=data['company_name'])
        db.session.add(new_employer)
        db.session.commit()
        return jsonify({'message': 'Employer added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to list employers
@app.route('/employers', methods=['GET'])
def list_employers():
    """List all employers"""
    employers = Employer.query.all()
    return jsonify([{'id': e.id, 'company_name': e.company_name} for e in employers]), 200

# Route to create a job listing
@app.route('/job_listings', methods=['POST'])
def create_job_listing():
    """Create a new job listing"""
    try:
        data = request.get_json()
        new_job_listing = JobListing(title=data['title'], description=data['description'], employer_id=data['employer_id'])
        db.session.add(new_job_listing)
        db.session.commit()
        return jsonify({'message': 'Job listing created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to list job listings
@app.route('/job_listings', methods=['GET'])
def list_job_listings():
    """List all job listings"""
    job_listings = JobListing.query.all()
    return jsonify([{'id': jl.id, 'title': jl.title, 'description': jl.description} for jl in job_listings]), 200

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
