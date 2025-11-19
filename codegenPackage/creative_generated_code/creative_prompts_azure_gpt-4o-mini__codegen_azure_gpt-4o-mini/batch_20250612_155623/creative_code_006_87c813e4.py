"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: What libraries can I use to build a web application that helps victims of online fraud report their cases, taking cues from The Legato's approach?
Generated: DETERMINISTIC_87c813e41ccf3832
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application development
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity; can be replaced with other databases)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fraud_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the FraudReport model
class FraudReport(db.Model):
    """Database model for storing fraud reports."""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<FraudReport {self.id}>'

# Define schema for validation
class FraudReportSchema(Schema):
    """Schema for fraud report validation."""
    user_name = fields.String(required=True)
    email = fields.Email(required=True)
    details = fields.String(required=True)

# Initialize schema
fraud_report_schema = FraudReportSchema()

@app.route('/')
def index():
    """Render the homepage for reporting fraud cases."""
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report_fraud():
    """Endpoint to submit a fraud report."""
    try:
        # Validate input data
        data = request.get_json()
        fraud_report = fraud_report_schema.load(data)

        # Create new fraud report instance
        new_report = FraudReport(**fraud_report)

        # Add report to the database
        db.session.add(new_report)
        db.session.commit()

        return jsonify({'message': 'Fraud report submitted successfully!'}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle other errors
        return jsonify({'error': str(e)}), 500

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    """Return a custom 404 error message."""
    return jsonify({'error': 'Not found'}), 404

# Main block to run the application
if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

### Instructions:
1. Make sure to have Flask, SQLAlchemy, Flask-Migrate, and Marshmallow installed.
2. Create a basic HTML template named `index.html` within a `templates` directory for the homepage.
3. Run the application and navigate to the homepage to submit fraud reports.
