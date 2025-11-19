"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Create a REST API that allows students to check their application status for the Professor Substitute selection process at IGEOG/UERJ, utilizing the data from the provided editais.
Generated: DETERMINISTIC_63e59549a3528572
Batch ID: 20250612_164005
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Application Model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    application_status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'student_name': self.student_name,
            'application_status': self.application_status
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to check application status by student name
@app.route('/api/status', methods=['GET'])
def get_application_status():
    # Get 'student_name' from query parameters
    student_name = request.args.get('student_name')
    
    if not student_name:
        raise BadRequest("Missing 'student_name' query parameter.")

    # Query the application status
    application = Application.query.filter_by(student_name=student_name).first()
    
    if not application:
        raise NotFound(f"No application found for student: {student_name}")

    return jsonify(application.to_dict()), 200

# Route to add a new application (for demo purposes)
@app.route('/api/apply', methods=['POST'])
def apply():
    data = request.get_json()

    # Validate input data
    if not data or 'student_name' not in data or 'application_status' not in data:
        raise BadRequest("Request must contain 'student_name' and 'application_status'.")

    # Create new application instance
    new_application = Application(
        student_name=data['student_name'],
        application_status=data['application_status']
    )

    # Add the new application to the database
    db.session.add(new_application)
    db.session.commit()

    return jsonify(new_application.to_dict()), 201

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
