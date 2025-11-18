"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ryanml.github.io
Prompt: Suggest ways to utilize Ryan Lanese's GitHub contributions for developing a full-stack application.
Generated: DETERMINISTIC_74aaba2d592144fb
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for the application
class Contribution(db.Model):
    """Model representing a GitHub contribution."""
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    repo = db.Column(db.String(100), nullable=False)
    contributions = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'user': self.user,
            'repo': self.repo,
            'contributions': self.contributions
        }

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    """Return a 404 error response."""
    return jsonify({'error': 'Not found'}), 404

# API endpoint to add a contribution
@app.route('/contributions', methods=['POST'])
def add_contribution():
    """API endpoint to add a new contribution."""
    data = request.get_json()  # Get JSON data from request
    if not data or 'user' not in data or 'repo' not in data or 'contributions' not in data:
        return jsonify({'error': 'Invalid input'}), 400  # Bad request

    new_contribution = Contribution(
        user=data['user'],
        repo=data['repo'],
        contributions=data['contributions']
    )
    
    db.session.add(new_contribution)  # Add contribution to the session
    db.session.commit()  # Commit the session
    return jsonify(new_contribution.to_dict()), 201  # Return created contribution

# API endpoint to retrieve all contributions
@app.route('/contributions', methods=['GET'])
def get_contributions():
    """API endpoint to retrieve all contributions."""
    contributions = Contribution.query.all()  # Query all contributions
    return jsonify([contribution.to_dict() for contribution in contributions]), 200  # Return contributions

# Main entry point for the application
if __name__ == '__main__':
    # Run the application with debug mode on for development
    app.run(debug=True)
```

**Database Setup:**
1. Make sure to have Flask, Flask-SQLAlchemy, and Flask-Migrate installed.
2. Set up the database by running migrations after creating the database:
   - `flask db init`
   - `flask db migrate -m "Initial migration."`
   - `flask db upgrade`

**Environment Variables:**
- Set `DATABASE_URL` for production databases; otherwise, it defaults to SQLite in development.
