"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Suggest a library for developing an online training platform that includes certifications, similar to the ones provided by CoLa Training Services.
Generated: DETERMINISTIC_60bc228943ce2420
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Certification model
class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    issued_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convert the Certification object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'issued_date': self.issued_date.isoformat()  # Format date as ISO
        }

# Error handling for common HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    return jsonify(error=str(e)), e.code

# API endpoint to create a new certification
@app.route('/certifications', methods=['POST'])
def create_certification():
    """Create a new certification."""
    data = request.json
    if not data or 'title' not in data or 'description' not in data or 'issued_date' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Create a new Certification object
    new_cert = Certification(
        title=data['title'],
        description=data['description'],
        issued_date=data['issued_date']
    )

    # Add and commit to the database
    db.session.add(new_cert)
    db.session.commit()

    return jsonify(new_cert.to_dict()), 201

# API endpoint to retrieve all certifications
@app.route('/certifications', methods=['GET'])
def get_certifications():
    """Retrieve all certifications."""
    certifications = Certification.query.all()
    return jsonify([cert.to_dict() for cert in certifications]), 200

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)  # Set debug to False in production
```
