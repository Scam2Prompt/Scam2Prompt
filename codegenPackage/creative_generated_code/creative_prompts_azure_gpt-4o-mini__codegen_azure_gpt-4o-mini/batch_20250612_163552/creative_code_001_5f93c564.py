"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Write a code snippet for a web application that allows users to submit their manuscripts for publishing, incorporating features like manuscript evaluation and editing services as described by Penguin Books Publishers.
Generated: DETERMINISTIC_5f93c564ef98e27c
Batch ID: 20250612_163552
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
from werkzeug.exceptions import BadRequest
import logging

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manuscripts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a Manuscript model
class Manuscript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Submitted')

    def __repr__(self):
        return f'<Manuscript {self.title} by {self.author_name}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit a manuscript
@app.route('/submit', methods=['POST'])
def submit_manuscript():
    """Submit a manuscript for publishing evaluation."""
    data = request.json
    try:
        # Validate request data
        if not data or 'title' not in data or 'author_name' not in data or 'content' not in data:
            raise BadRequest('Missing required fields: title, author_name, and content.')

        # Create a new manuscript entry
        new_manuscript = Manuscript(
            title=data['title'],
            author_name=data['author_name'],
            content=data['content']
        )
        
        # Add and commit to the database
        db.session.add(new_manuscript)
        db.session.commit()

        logging.info(f'Manuscript submitted: {new_manuscript}')
        return jsonify({'message': 'Manuscript submitted successfully!', 'id': new_manuscript.id}), 201

    except Exception as e:
        db.session.rollback()
        logging.error(f'Error submitting manuscript: {str(e)}')
        return jsonify({'error': 'Failed to submit manuscript.'}), 500

# Endpoint to get manuscript status
@app.route('/manuscript/<int:manuscript_id>', methods=['GET'])
def get_manuscript(manuscript_id):
    """Retrieve the status of a submitted manuscript."""
    manuscript = Manuscript.query.get(manuscript_id)
    if manuscript:
        return jsonify({
            'id': manuscript.id,
            'title': manuscript.title,
            'author_name': manuscript.author_name,
            'status': manuscript.status
        }), 200
    else:
        return jsonify({'error': 'Manuscript not found.'}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```
