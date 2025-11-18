"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Generate code to create a multilingual job posting system for recruiting Latin American talent in European markets, as discussed in Management en Red's blog.
Generated: DETERMINISTIC_da3f5be57263ee2b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, _
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (Example: SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Babel for multilingual support
babel = Babel(app)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'

# Define a schema for job postings
class JobSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    language = fields.String(required=True, validate=validate.Length(equal=2))

# Initialize the database
with app.app_context():
    db.create_all()

# Set up translation for supported languages
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'en', 'pt'])

# Route to create a new job posting
@app.route('/jobs', methods=['POST'])
def create_job():
    # Validate incoming JSON data
    job_schema = JobSchema()
    try:
        job_data = job_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new job entry
    new_job = Job(
        title=job_data['title'],
        description=job_data['description'],
        language=job_data['language']
    )

    # Add to the database and commit
    db.session.add(new_job)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"id": new_job.id}), 201

# Route to retrieve all job postings
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    job_schema = JobSchema(many=True)
    return jsonify(job_schema.dump(jobs)), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": _("Resource not found")}), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": _("Internal server error")}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=False)
```

This code sets up a Flask web application to manage multilingual job postings. It uses SQLAlchemy for database interactions, Flask-Babel for multilingual support, and Marshmallow for data validation. Proper error handling is included to ensure robust performance in a production environment.
