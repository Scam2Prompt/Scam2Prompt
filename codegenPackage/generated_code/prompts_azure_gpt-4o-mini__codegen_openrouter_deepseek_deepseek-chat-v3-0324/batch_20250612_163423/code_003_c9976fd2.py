"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Develop a RESTful API endpoint for a personal injury law firm that allows clients to submit details about their accidents, including types like truck accidents and slip and fall incidents.
Generated: DETERMINISTIC_c9976fd25e52b6de
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Accident model
class Accident(db.Model):
    __tablename__ = 'accidents'
    
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)
    client_phone = db.Column(db.String(20), nullable=False)
    accident_type = db.Column(db.String(50), nullable=False)
    accident_date = db.Column(db.String(20), nullable=False)
    accident_description = db.Column(db.Text, nullable=False)
    injuries = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Define Accident Schema for validation
class AccidentSchema(Schema):
    client_name = fields.String(required=True)
    client_email = fields.Email(required=True)
    client_phone = fields.String(required=True)
    accident_type = fields.String(required=True)
    accident_date = fields.String(required=True)
    accident_description = fields.String(required=True)
    injuries = fields.String(required=True)

# Initialize schema
accident_schema = AccidentSchema()

# Create database tables
with app.app_context():
    db.create_all()

# API Endpoint for submitting accident details
@app.route('/api/accidents', methods=['POST'])
def submit_accident():
    try:
        # Validate and parse incoming JSON data
        data = request.get_json()
        errors = accident_schema.validate(data)
        if errors:
            raise BadRequest(description=str(errors))
        
        # Create new accident record
        new_accident = Accident(
            client_name=data['client_name'],
            client_email=data['client_email'],
            client_phone=data['client_phone'],
            accident_type=data['accident_type'],
            accident_date=data['accident_date'],
            accident_description=data['accident_description'],
            injuries=data['injuries']
        )
        
        # Save to database
        db.session.add(new_accident)
        db.session.commit()
        
        # Return success response
        return jsonify({
            'message': 'Accident details submitted successfully',
            'accident_id': new_accident.id
        }), 201
        
    except BadRequest as e:
        return jsonify({'error': str(e.description)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An internal server error occurred'}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
```
