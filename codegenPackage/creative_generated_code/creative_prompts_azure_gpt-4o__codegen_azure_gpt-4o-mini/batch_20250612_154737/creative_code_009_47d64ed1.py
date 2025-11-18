"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grants-archive-cf.webflow.io
Prompt: Develop a REST API endpoint to fetch Gitcoin Grants round data, including funding and grantee details, from a database populated using the Gitcoin Grants Archive.
Generated: DETERMINISTIC_47d64ed15e5cbcd7
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gitcoin_grants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for the Gitcoin Grants data
class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String(50), nullable=False)
    grantee_name = db.Column(db.String(100), nullable=False)
    funding_amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'round': self.round,
            'grantee_name': self.grantee_name,
            'funding_amount': self.funding_amount
        }

# Endpoint to fetch Gitcoin Grants round data
@app.route('/api/grants', methods=['GET'])
def get_grants():
    """
    Fetches Gitcoin Grants round data from the database.
    
    Returns:
        JSON response containing a list of grants and their details.
    """
    try:
        # Fetch all grants from the database
        grants = Grant.query.all()
        # Convert the grants to a list of dictionaries
        return jsonify([grant.to_dict() for grant in grants]), 200
    except SQLAlchemyError as e:
        # Log the error (consider using a logging library)
        print(f"Database error: {str(e)}")
        return jsonify({'error': 'Failed to fetch grants'}), 500

# Error handling for not found routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    
    Returns:
        JSON response indicating that the resource was not found.
    """
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for server errors
@app.errorhandler(500)
def server_error(error):
    """
    Handle 500 internal server errors.
    
    Returns:
        JSON response indicating an internal server error occurred.
    """
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=False)  # Set debug=True during development only
```
