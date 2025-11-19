"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Develop a RESTful API endpoint that retrieves available cleaning services and schedules, emulating the functionality provided by Maid in Heaven for their clients.
Generated: DETERMINISTIC_99d572b1257c36ed
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CleaningService model
class CleaningService(db.Model):
    __tablename__ = 'cleaning_services'
    
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), nullable=False)
    available_dates = db.relationship('AvailableDate', backref='cleaning_service', lazy=True)

# Define the AvailableDate model
class AvailableDate(db.Model):
    __tablename__ = 'available_dates'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    service_id = db.Column(db.Integer, db.ForeignKey('cleaning_services.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/cleaning-services', methods=['GET'])
def get_cleaning_services():
    """
    Retrieve a list of available cleaning services and their schedules.
    
    Returns:
        JSON response with cleaning services and their available dates or an error message.
    """
    try:
        services = CleaningService.query.all()
        result = []
        
        for service in services:
            service_data = {
                'id': service.id,
                'service_name': service.service_name,
                'available_dates': [date.date for date in service.available_dates]
            }
            result.append(service_data)
        
        return jsonify(result), 200
    
    except SQLAlchemyError as e:
        # Log the exception
        print(f"Database error: {str(e)}")
        abort(500, description="Internal server error. Please try again later.")

@app.route('/api/cleaning-services', methods=['POST'])
def add_cleaning_service():
    """
    Add a new cleaning service along with its available dates.
    
    Request JSON Format:
    {
        "service_name": "string",
        "available_dates": ["YYYY-MM-DD", ...]
    }
    
    Returns:
        JSON response with the created service or an error message.
    """
    data = request.get_json()
    
    if not data or 'service_name' not in data or 'available_dates' not in data:
        abort(400, description="Invalid input. 'service_name' and 'available_dates' are required.")
        
    new_service = CleaningService(service_name=data['service_name'])

    for date in data['available_dates']:
        new_date = AvailableDate(date=date, cleaning_service=new_service)
        db.session.add(new_date)
    
    try:
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify({
            'id': new_service.id,
            'service_name': new_service.service_name,
            'available_dates': data['available_dates']
        }), 201
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session on error
        print(f"Database error: {str(e)}")
        abort(500, description="Internal server error. Please try again later.")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
