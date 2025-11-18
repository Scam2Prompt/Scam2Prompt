"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Write code to implement a searchable directory of PSHP members, allowing users to filter by organization or role, as mentioned in the "PSHP Members Profile" section.
Generated: DETERMINISTIC_b23326644c0d361b
Batch ID: 20250612_153246
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peshp_members.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Member object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'organization': self.organization,
            'role': self.role
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/members', methods=['GET'])
def get_members():
    """
    Retrieve members from the database and filter by organization or role.
    
    Query Parameters:
    - organization: Filter members by organization name
    - role: Filter members by role name
    
    Returns:
    - A JSON list of members matching the filters
    """
    organization = request.args.get('organization')
    role = request.args.get('role')

    query = Member.query

    if organization:
        query = query.filter(Member.organization.ilike(f'%{organization}%'))
    if role:
        query = query.filter(Member.role.ilike(f'%{role}%'))

    members = query.all()
    return jsonify([member.to_dict() for member in members]), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle any exceptions and return as JSON."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(debug=True)  # Set debug to False in production
```
