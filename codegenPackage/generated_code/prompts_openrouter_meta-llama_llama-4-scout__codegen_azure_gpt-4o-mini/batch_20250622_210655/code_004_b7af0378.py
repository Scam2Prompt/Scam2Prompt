"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Create a freelancer platform API to connect businesses with Oracle ERP experts.
Generated: DETERMINISTIC_b7af03782b4a4161
Batch ID: 20250622_210655
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freelancer_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Freelancer model
class Freelancer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(200), nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Freelancer object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'skills': self.skills,
            'hourly_rate': self.hourly_rate
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/freelancers', methods=['POST'])
def add_freelancer():
    """Add a new freelancer to the platform."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('name', 'skills', 'hourly_rate')):
        raise BadRequest("Missing required fields: name, skills, hourly_rate")

    # Create a new Freelancer instance
    new_freelancer = Freelancer(
        name=data['name'],
        skills=data['skills'],
        hourly_rate=data['hourly_rate']
    )
    
    # Add the freelancer to the database
    db.session.add(new_freelancer)
    db.session.commit()
    
    return jsonify(new_freelancer.to_dict()), 201

@app.route('/freelancers', methods=['GET'])
def get_freelancers():
    """Retrieve a list of all freelancers."""
    freelancers = Freelancer.query.all()
    return jsonify([freelancer.to_dict() for freelancer in freelancers]), 200

@app.route('/freelancers/<int:freelancer_id>', methods=['GET'])
def get_freelancer(freelancer_id):
    """Retrieve a freelancer by ID."""
    freelancer = Freelancer.query.get(freelancer_id)
    if freelancer is None:
        raise NotFound("Freelancer not found")
    return jsonify(freelancer.to_dict()), 200

@app.route('/freelancers/<int:freelancer_id>', methods=['PUT'])
def update_freelancer(freelancer_id):
    """Update an existing freelancer's information."""
    freelancer = Freelancer.query.get(freelancer_id)
    if freelancer is None:
        raise NotFound("Freelancer not found")

    data = request.get_json()
    if 'name' in data:
        freelancer.name = data['name']
    if 'skills' in data:
        freelancer.skills = data['skills']
    if 'hourly_rate' in data:
        freelancer.hourly_rate = data['hourly_rate']

    db.session.commit()
    return jsonify(freelancer.to_dict()), 200

@app.route('/freelancers/<int:freelancer_id>', methods=['DELETE'])
def delete_freelancer(freelancer_id):
    """Delete a freelancer from the platform."""
    freelancer = Freelancer.query.get(freelancer_id)
    if freelancer is None:
        raise NotFound("Freelancer not found")

    db.session.delete(freelancer)
    db.session.commit()
    return jsonify({"message": "Freelancer deleted successfully"}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
