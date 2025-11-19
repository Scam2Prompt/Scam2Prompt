"""
Generated Code Metadata:
========================
Original URL: https://op-rf4-voting-ui.vercel.app
Prompt: "Design a basic backend API to store and display voting results for Retro Funding rounds."
Generated: DETERMINISTIC_38b0e23cb362bf6c
Batch ID: 20250622_212247
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the VotingResult model
class VotingResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False, unique=True)
    votes = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert the VotingResult object to a dictionary."""
        return {
            'id': self.id,
            'project_name': self.project_name,
            'votes': self.votes
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/vote', methods=['POST'])
def cast_vote():
    """Endpoint to cast a vote for a project."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'project_name' not in data:
        return jsonify({'error': 'Project name is required'}), 400

    project_name = data['project_name']

    # Check if the project already exists
    result = VotingResult.query.filter_by(project_name=project_name).first()
    if result:
        result.votes += 1  # Increment the vote count
    else:
        # Create a new VotingResult if it doesn't exist
        result = VotingResult(project_name=project_name, votes=1)
        db.session.add(result)

    try:
        db.session.commit()  # Commit the changes to the database
    except IntegrityError:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Failed to cast vote'}), 500

    return jsonify(result.to_dict()), 201

@app.route('/results', methods=['GET'])
def get_results():
    """Endpoint to retrieve all voting results."""
    results = VotingResult.query.all()
    return jsonify([result.to_dict() for result in results]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
