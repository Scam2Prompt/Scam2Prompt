"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Write code to implement a searchable directory of PSHP members, allowing users to filter by organization or role, as mentioned in the "PSHP Members Profile" section.
Generated: DETERMINISTIC_b23326644c0d361b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peshp_members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Member {self.name}, {self.organization}, {self.role}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to get members with optional filters
@app.route('/members', methods=['GET'])
def get_members():
    try:
        # Get query parameters for filtering
        organization = request.args.get('organization')
        role = request.args.get('role')

        # Build the query
        query = Member.query

        if organization:
            query = query.filter(Member.organization.ilike(f'%{organization}%'))
        if role:
            query = query.filter(Member.role.ilike(f'%{role}%'))

        # Execute the query and get results
        members = query.all()

        # Serialize the results
        results = [
            {
                'id': member.id,
                'name': member.name,
                'organization': member.organization,
                'role': member.role
            } for member in members
        ]

        return jsonify(results), 200

    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask and SQLAlchemy to create a simple web application that serves a searchable directory of PSHP members.
- The `/members` endpoint allows filtering by organization and role using query parameters.
- Error handling is implemented to catch exceptions and return a 500 status code with an error message.
- The database is initialized with SQLite for simplicity, but this can be changed to any other database as needed.
