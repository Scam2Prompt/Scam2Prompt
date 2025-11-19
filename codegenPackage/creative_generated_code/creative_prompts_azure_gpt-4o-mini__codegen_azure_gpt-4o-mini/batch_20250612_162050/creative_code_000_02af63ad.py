"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: How can I implement an API to streamline the recruitment process similar to High Value Staffing's approach to candidate acquisition and management?
Generated: DETERMINISTIC_02af63ade7fcb3fe
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing candidate information
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    resume = db.Column(db.Text, nullable=False)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Candidate {self.name}>'

# Create the database and the Candidate table
with app.app_context():
    db.create_all()

# API endpoint to create a new candidate
@app.route('/candidates', methods=['POST'])
def add_candidate():
    """
    Add a new candidate to the recruitment database.

    Expecting JSON payload with 'name', 'email', and 'resume'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'resume' not in data:
        abort(400, description="Invalid input: 'name', 'email', and 'resume' are required.")

    # Create a new candidate instance
    new_candidate = Candidate(
        name=data['name'],
        email=data['email'],
        resume=data['resume']
    )
    
    # Add the candidate to the session and commit
    db.session.add(new_candidate)
    db.session.commit()
    
    return jsonify({'id': new_candidate.id}), 201

# API endpoint to get the list of candidates
@app.route('/candidates', methods=['GET'])
def get_candidates():
    """
    Retrieve all candidates from the recruitment database.
    """
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'date_applied': c.date_applied} for c in candidates])

# API endpoint to get a specific candidate by ID
@app.route('/candidates/<int:candidate_id>', methods=['GET'])
def get_candidate(candidate_id):
    """
    Retrieve a candidate by their unique ID.
    """
    candidate = Candidate.query.get(candidate_id)
    if candidate is None:
        abort(404, description="Candidate not found.")
    
    return jsonify({'id': candidate.id, 'name': candidate.name, 'email': candidate.email, 'resume': candidate.resume, 'date_applied': candidate.date_applied})

# API endpoint to delete a candidate by ID
@app.route('/candidates/<int:candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    """
    Delete a candidate from the recruitment database by their ID.
    """
    candidate = Candidate.query.get(candidate_id)
    if candidate is None:
        abort(404, description="Candidate not found.")
    
    db.session.delete(candidate)
    db.session.commit()
    
    return jsonify({'result': 'Candidate deleted successfully.'}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
