"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Recommend libraries or APIs to create a web-based volunteer registration system for a maker community similar to Perú Makers.
Generated: DETERMINISTIC_5a282e346380fd02
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# volunteer_registration.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Volunteer model
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    skills = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Volunteer {self.name}>'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to register a new volunteer
@app.route('/register', methods=['POST'])
def register_volunteer():
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('name', 'email', 'skills')):
        raise BadRequest("Missing required fields: 'name', 'email', 'skills'")

    # Create a new volunteer instance
    new_volunteer = Volunteer(
        name=data['name'],
        email=data['email'],
        skills=data['skills']
    )

    # Add the new volunteer to the session and commit to the database
    db.session.add(new_volunteer)
    db.session.commit()

    return jsonify({"message": "Volunteer registered successfully!", "id": new_volunteer.id}), 201

# Route to get all volunteers
@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([{'id': v.id, 'name': v.name, 'email': v.email, 'skills': v.skills} for v in volunteers]), 200

# Error handler for NotFound errors
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for BadRequest errors
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', True), host='0.0.0.0', port=5000)
```

### Required Libraries
To run this code, ensure you have the following libraries installed:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code in a file named `volunteer_registration.py`.
2. Run the application using the command:
   ```bash
   python volunteer_registration.py
   ```
3. Use a tool like Postman or curl to interact with the API endpoints:
   - POST `/register` to register a volunteer.
   - GET `/volunteers` to retrieve the list of volunteers.
