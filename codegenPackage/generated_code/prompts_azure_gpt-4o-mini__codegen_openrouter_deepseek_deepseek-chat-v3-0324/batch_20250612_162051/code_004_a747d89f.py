"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a RESTful API endpoint that allows healthcare facilities to submit job requests for nurses and support workers, based on the recruitment services provided by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_a747d89f8a658ece
Batch ID: 20250612_162051
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
from werkzeug.exceptions import HTTPException
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/amazing_grace_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class HealthcareFacility(db.Model):
    __tablename__ = 'healthcare_facilities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    job_requests = db.relationship('JobRequest', backref='facility', lazy=True)

class JobRequest(db.Model):
    __tablename__ = 'job_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('healthcare_facilities.id'), nullable=False)
    position_type = db.Column(db.String(50), nullable=False)  # 'nurse' or 'support_worker'
    required_qualifications = db.Column(db.String(200))
    experience_level = db.Column(db.String(50))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    shift_details = db.Column(db.String(200))
    special_requirements = db.Column(db.String(200))
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected', 'filled'
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    """Handle unexpected errors."""
    app.logger.error(f"Unexpected error: {str(e)}")
    return jsonify({
        "error": "An unexpected error occurred",
        "details": str(e)
    }), 500

# API Endpoints
@app.route('/api/job_requests', methods=['POST'])
def create_job_request():
    """
    Create a new job request for nurses or support workers.
    Required fields: facility_id, position_type, start_date
    """
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['facility_id', 'position_type', 'start_date']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Validate position type
    if data['position_type'] not in ['nurse', 'support_worker']:
        return jsonify({"error": "Invalid position type. Must be 'nurse' or 'support_worker'"}), 400
    
    try:
        # Create new job request
        job_request = JobRequest(
            facility_id=data['facility_id'],
            position_type=data['position_type'],
            required_qualifications=data.get('required_qualifications'),
            experience_level=data.get('experience_level'),
            start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
            end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date() if 'end_date' in data else None,
            shift_details=data.get('shift_details'),
            special_requirements=data.get('special_requirements')
        )
        
        db.session.add(job_request)
        db.session.commit()
        
        return jsonify({
            "message": "Job request created successfully",
            "job_request_id": job_request.id
        }), 201
    
    except ValueError as e:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/job_requests/<int:job_request_id>', methods=['GET'])
def get_job_request(job_request_id):
    """Get details of a specific job request."""
    job_request = JobRequest.query.get_or_404(job_request_id)
    
    return jsonify({
        "id": job_request.id,
        "facility_id": job_request.facility_id,
        "position_type": job_request.position_type,
        "required_qualifications": job_request.required_qualifications,
        "experience_level": job_request.experience_level,
        "start_date": job_request.start_date.isoformat() if job_request.start_date else None,
        "end_date": job_request.end_date.isoformat() if job_request.end_date else None,
        "shift_details": job_request.shift_details,
        "special_requirements": job_request.special_requirements,
        "status": job_request.status,
        "created_at": job_request.created_at.isoformat()
    })

@app.route('/api/job_requests/<int:job_request_id>', methods=['PUT'])
def update_job_request(job_request_id):
    """Update an existing job request."""
    job_request = JobRequest.query.get_or_404(job_request_id)
    data = request.get_json()
    
    try:
        if 'position_type' in data:
            if data['position_type'] not in ['nurse', 'support_worker']:
                return jsonify({"error": "Invalid position type. Must be 'nurse' or 'support_worker'"}), 400
            job_request.position_type = data['position_type']
        
        if 'required_qualifications' in data:
            job_request.required_qualifications = data['required_qualifications']
        
        if 'experience_level' in data:
            job_request.experience_level = data['experience_level']
        
        if 'start_date' in data:
            job_request.start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        
        if 'end_date' in data:
            job_request.end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data['end_date'] else None
        
        if 'shift_details' in data:
            job_request.shift_details = data['shift_details']
        
        if 'special_requirements' in data:
            job_request.special_requirements = data['special_requirements']
        
        if 'status' in data:
            if data['status'] not in ['pending', 'approved', 'rejected', 'filled']:
                return jsonify({"error": "Invalid status value"}), 400
            job_request.status = data['status']
        
        db.session.commit()
        
        return jsonify({"message": "Job request updated successfully"})
    
    except ValueError as e:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Helper function to initialize database
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
