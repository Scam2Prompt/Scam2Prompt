"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Generate code to create a search functionality for verifying certificates issued for vocational training programs, as described on the RSP Bharat website.
Generated: DETERMINISTIC_3acba6b2a5bc44b0
Batch ID: 20250612_152306
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

# Initialize Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certificates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Certificate model to represent the certificates table
class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certificate_number = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    issued_date = db.Column(db.String(100), nullable=False)
    training_program = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'certificate_number': self.certificate_number,
            'name': self.name,
            'issued_date': self.issued_date,
            'training_program': self.training_program
        }

# Initialize the database (for demonstration purposes only)
# This should be done in a separate migration script in production
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/search_certificate', methods=['GET'])
def search_certificate():
    """
    Search for a certificate by certificate number.
    
    Returns:
        JSON response containing the certificate details or an error message.
    """
    cert_number = request.args.get('certificate_number')

    if not cert_number:
        return jsonify({"error": "Certificate number is required"}), 400

    try:
        # Query the database for the certificate
        certificate = Certificate.query.filter_by(certificate_number=cert_number).first()

        if certificate:
            return jsonify(certificate.to_dict()), 200
        else:
            return jsonify({"error": "Certificate not found"}), 404
    except SQLAlchemyError as e:
        # Log the error (in production, you would log to a file or monitoring service)
        print(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while querying the database"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a basic search functionality for certificates using Flask and SQLAlchemy. It includes error handling, comments for clarity, and follows good practices for web applications.
