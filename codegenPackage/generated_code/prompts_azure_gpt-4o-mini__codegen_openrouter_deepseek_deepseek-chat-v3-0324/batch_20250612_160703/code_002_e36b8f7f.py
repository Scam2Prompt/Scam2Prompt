"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Generate a code snippet for a web application that tracks the number of neurological cases registered, inspired by the ICON Foundation's data collection from December 2022 to January 2024.
Generated: DETERMINISTIC_e36b8f7f0d6c92d5
Batch ID: 20250612_160703
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
from datetime import datetime
import logging
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurological_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database model for neurological cases
class NeurologicalCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(100), nullable=False)
    date_registered = db.Column(db.Date, nullable=False)
    patient_age = db.Column(db.Integer)
    patient_gender = db.Column(db.String(10))
    notes = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'case_type': self.case_type,
            'date_registered': self.date_registered.isoformat(),
            'patient_age': self.patient_age,
            'patient_gender': self.patient_gender,
            'notes': self.notes
        }

# Error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Error occurred: {str(e)}")
    if isinstance(e, HTTPException):
        response = jsonify({
            'error': e.name,
            'message': e.description
        })
        response.status_code = e.code
    else:
        response = jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred'
        })
        response.status_code = 500
    return response

# API endpoints
@app.route('/api/cases', methods=['POST'])
def add_case():
    try:
        data = request.get_json()
        
        if not data or 'case_type' not in data or 'date_registered' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        try:
            date_registered = datetime.strptime(data['date_registered'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
            
        new_case = NeurologicalCase(
            case_type=data['case_type'],
            date_registered=date_registered,
            patient_age=data.get('patient_age'),
            patient_gender=data.get('patient_gender'),
            notes=data.get('notes')
        )
        
        db.session.add(new_case)
        db.session.commit()
        
        logger.info(f"New case added: {new_case.id}")
        return jsonify(new_case.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        raise e

@app.route('/api/cases', methods=['GET'])
def get_cases():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        query = NeurologicalCase.query
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                query = query.filter(NeurologicalCase.date_registered >= start_date)
            except ValueError:
                return jsonify({'error': 'Invalid start_date format. Use YYYY-MM-DD'}), 400
                
        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                query = query.filter(NeurologicalCase.date_registered <= end_date)
            except ValueError:
                return jsonify({'error': 'Invalid end_date format. Use YYYY-MM-DD'}), 400
                
        cases = query.all()
        return jsonify([case.to_dict() for case in cases])
        
    except Exception as e:
        raise e

@app.route('/api/cases/stats', methods=['GET'])
def get_stats():
    try:
        start_date = request.args.get('start_date', '2022-12-01')
        end_date = request.args.get('end_date', '2024-01-31')
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
            
        cases = NeurologicalCase.query.filter(
            NeurologicalCase.date_registered.between(start_date, end_date)
        ).all()
        
        total_cases = len(cases)
        case_types = {}
        
        for case in cases:
            case_types[case.case_type] = case_types.get(case.case_type, 0) + 1
            
        return jsonify({
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat(),
            'total_cases': total_cases,
            'case_types': case_types
        })
        
    except Exception as e:
        raise e

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
