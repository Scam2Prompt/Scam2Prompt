"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: How can I create an API to manage the repair and servicing of York chillers, including features for scheduling and pricing?
Generated: DETERMINISTIC_83035c52746c123d
Batch ID: 20250612_155349
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///chiller_service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the repairs and servicing of York chillers
class ChillerService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'service_date': self.service_date.isoformat(),
            'description': self.description,
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to schedule a new service
@app.route('/api/services', methods=['POST'])
def schedule_service():
    data = request.get_json()
    if not data or 'service_date' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Bad Request: Missing required fields'}), 400
    
    try:
        service = ChillerService(
            service_date=datetime.fromisoformat(data['service_date']),
            description=data['description'],
            price=float(data['price'])
        )
        db.session.add(service)
        db.session.commit()
        return jsonify(service.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to get all scheduled services
@app.route('/api/services', methods=['GET'])
def get_services():
    services = ChillerService.query.all()
    return jsonify([service.to_dict() for service in services]), 200

# API endpoint to get a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = ChillerService.query.get(service_id)
    if not service:
        return jsonify({'error': 'Not Found'}), 404
    return jsonify(service.to_dict()), 200

# API endpoint to update a service by ID
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = ChillerService.query.get(service_id)
    if not service:
        return jsonify({'error': 'Not Found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Bad Request: No data provided'}), 400
    
    try:
        if 'service_date' in data:
            service.service_date = datetime.fromisoformat(data['service_date'])
        if 'description' in data:
            service.description = data['description']
        if 'price' in data:
            service.price = float(data['price'])
        
        db.session.commit()
        return jsonify(service.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to delete a service by ID
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = ChillerService.query.get(service_id)
    if not service:
        return jsonify({'error': 'Not Found'}), 404
    
    try:
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True', host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

**Note:** Ensure to set the `DATABASE_URL` environment variable for database connection, and install required packages using `pip install Flask Flask-SQLAlchemy`.
