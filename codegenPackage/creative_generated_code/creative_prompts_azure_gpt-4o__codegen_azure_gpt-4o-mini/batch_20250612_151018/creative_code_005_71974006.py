"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a RESTful API that allows querying FOSS@RIT profiles by username, major/year, and areas of expertise (e.g., Python, Rust, Linux).
Generated: DETERMINISTIC_71974006c2fb2248
Batch ID: 20250612_151018
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foss_profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FOSS profile model
class FOSSProfile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    major_year = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the FOSSProfile object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'major_year': self.major_year,
            'expertise': self.expertise.split(',')  # Convert comma-separated string to list
        }

# Route for querying profiles
@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    """Query FOSS profiles based on username, major/year, and areas of expertise."""
    username = request.args.get('username')
    major_year = request.args.get('major_year')
    expertise = request.args.get('expertise')

    # Build the query
    query = FOSSProfile.query

    if username:
        query = query.filter(FOSSProfile.username.ilike(f'%{username}%'))
    if major_year:
        query = query.filter(FOSSProfile.major_year.ilike(f'%{major_year}%'))
    if expertise:
        query = query.filter(FOSSProfile.expertise.ilike(f'%{expertise}%'))

    try:
        results = query.all()
        return jsonify([profile.to_dict() for profile in results]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for method not allowed
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405

# Main entry point
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
