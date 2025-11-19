"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Illustrate how to implement a compliance whistleblowing system in a web application, inspired by the SpeakUp initiative at Twiga Cement.
Generated: DETERMINISTIC_2e3eb6ab07c452ec
Batch ID: 20250612_164321
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
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///whistleblower.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing whistleblower reports
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    message = db.Column(db.Text, nullable=False)
    is_anonymous = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "is_anonymous": self.is_anonymous
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit a whistleblower report
@app.route('/report', methods=['POST'])
def submit_report():
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({"error": "Missing data"}), 400
        
        report = Report(
            name=data['name'],
            email=data['email'],
            message=data['message'],
            is_anonymous=data.get('is_anonymous', False)
        )
        
        db.session.add(report)
        db.session.commit()
        
        return jsonify(report.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all reports (admin access only)
@app.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([report.to_dict() for report in reports]), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```

To run this code, ensure you have the required packages installed and set up your environment variables as needed. This code provides a basic whistleblowing system with endpoints to submit reports and view them. Adjustments may be needed to implement user authentication and authorization as per your project requirements.
