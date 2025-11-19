"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Develop a REST API using Flask that allows users to search for PG accommodations by location, room type (single, double, triple), and price range, similar to the features offered by Moms PG.
Generated: DETERMINISTIC_27d5be4fddeacccf
Batch ID: 20250612_154428
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
from werkzeug.exceptions import BadRequest, NotFound
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pg_accommodations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Accommodation model
class Accommodation(db.Model):
    __tablename__ = 'accommodations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    room_type = db.Column(db.String(20), nullable=False)  # 'single', 'double', 'triple'
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    contact = db.Column(db.String(50))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'room_type': self.room_type,
            'price': self.price,
            'description': self.description,
            'contact': self.contact
        }

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handlers
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({'error': str(e)}), 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({'error': str(e)}), 404

@app.errorhandler(500)
def handle_server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# Search endpoint
@app.route('/api/accommodations', methods=['GET'])
def search_accommodations():
    try:
        # Get query parameters
        location = request.args.get('location')
        room_type = request.args.get('room_type')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        
        # Start with base query
        query = Accommodation.query
        
        # Apply filters
        if location:
            query = query.filter(Accommodation.location.ilike(f'%{location}%'))
        if room_type:
            if room_type.lower() not in ['single', 'double', 'triple']:
                raise BadRequest('Invalid room type. Must be single, double, or triple')
            query = query.filter(Accommodation.room_type == room_type.lower())
        if min_price is not None:
            query = query.filter(Accommodation.price >= min_price)
        if max_price is not None:
            query = query.filter(Accommodation.price <= max_price)
        
        # Execute query and return results
        accommodations = query.all()
        return jsonify([acc.to_dict() for acc in accommodations])
    
    except Exception as e:
        raise BadRequest(str(e))

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)
```
