"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: Generate code to create a multilingual job posting system for recruiting Latin American talent in European markets, as discussed in Management en Red's blog.
Generated: DETERMINISTIC_da3f5be57263ee2b
Batch ID: 20250612_152924
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
from flask_babel import Babel, gettext
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///jobs.db')
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
        return f'<Job {self.title} ({self.language})>'

# Create the database tables
with app.app_context():
    db.create_all()

# Set up the language selection
@babel.localeselector
def get_locale():
    # Use the best match for the user's preferred language
    return request.accept_languages.best_match(['en', 'es', 'pt'])

# Route to create a new job posting
@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        language = data.get('language')

        if not title or not description or not language:
            return jsonify({'error': gettext('Missing required fields')}), 400

        new_job = Job(title=title, description=description, language=language)
        db.session.add(new_job)
        db.session.commit()

        return jsonify({'message': gettext('Job posted successfully!')}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all job postings
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = Job.query.all()
        return jsonify([{'id': job.id, 'title': job.title, 'description': job.description, 'language': job.language} for job in jobs]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Babel

### Instructions
1. Set up a virtual environment and install the required packages.
2. Set the `DATABASE_URL` environment variable for your database connection.
3. Run the application and use the `/jobs` endpoint to create and retrieve job postings.
