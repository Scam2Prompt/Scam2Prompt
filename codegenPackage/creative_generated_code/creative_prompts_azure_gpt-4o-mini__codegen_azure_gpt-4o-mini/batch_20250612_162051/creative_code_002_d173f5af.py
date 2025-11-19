"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Create a REST API that allows users to report human rights abuses, incorporating features discussed in Jusoor International's programs and goals.
Generated: DETERMINISTIC_d173f5aff61605c1
Batch ID: 20250612_162051
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the model for the Human Rights Abuse Report
class AbuseReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, description, location):
        self.description = description
        self.location = location

# Define the schema for serializing the reports
class AbuseReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AbuseReport

# Initialize the schema
abuse_report_schema = AbuseReportSchema()
abuse_reports_schema = AbuseReportSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# POST endpoint to report a human rights abuse
@app.route('/api/reports', methods=['POST'])
def report_abuse():
    try:
        # Get data from request
        data = request.get_json()
        description = data.get('description')
        location = data.get('location')

        # Validate input
        if not description or not location:
            return jsonify({"error": "Description and location are required."}), 400

        # Create a new abuse report
        new_report = AbuseReport(description, location)
        
        # Add to session and commit to database
        db.session.add(new_report)
        db.session.commit()

        return abuse_report_schema.jsonify(new_report), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET endpoint to retrieve all reported abuses
@app.route('/api/reports', methods=['GET'])
def get_reports():
    try:
        all_reports = AbuseReport.query.all()
        return abuse_reports_schema.jsonify(all_reports), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main driver function
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```

### Requirements
To run the above code, you will need:
- `Flask`
- `Flask-SQLAlchemy`
- `Flask-Marshmallow`
- `marshmallow-sqlalchemy`

### Installation
You can install the dependencies via pip:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow-sqlalchemy
```

### Environment Variables
- `DATABASE_URL`: Set this for your database connection string.
- `DEBUG`: Set to 'True' or 'False' to enable/disable debug mode.
