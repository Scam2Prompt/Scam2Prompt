"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Recommend an API for managing business hours and customer service calls, similar to the scheduling system described on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_6683292501ddc569
Batch ID: 20250612_154740
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
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_hours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BusinessHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False)
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'day_of_week': self.day_of_week,
            'opening_time': self.opening_time.strftime('%H:%M'),
            'closing_time': self.closing_time.strftime('%H:%M')
        }

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/business-hours', methods=['GET'])
def get_business_hours():
    """Get all business hours."""
    hours = BusinessHour.query.all()
    return jsonify([hour.to_dict() for hour in hours]), 200

@app.route('/business-hours', methods=['POST'])
def add_business_hour():
    """Add a new business hour."""
    data = request.get_json()
    new_hour = BusinessHour(
        day_of_week=data['day_of_week'],
        opening_time=datetime.strptime(data['opening_time'], '%H:%M').time(),
        closing_time=datetime.strptime(data['closing_time'], '%H:%M').time()
    )
    
    try:
        db.session.add(new_hour)
        db.session.commit()
        return jsonify(new_hour.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/business-hours/<int:id>', methods=['PUT'])
def update_business_hour(id):
    """Update an existing business hour."""
    hour = BusinessHour.query.get(id)
    if hour is None:
        return jsonify({'error': 'Business hour not found'}), 404

    data = request.get_json()
    hour.day_of_week = data.get('day_of_week', hour.day_of_week)
    hour.opening_time = datetime.strptime(data.get('opening_time', hour.opening_time.strftime('%H:%M')), '%H:%M').time()
    hour.closing_time = datetime.strptime(data.get('closing_time', hour.closing_time.strftime('%H:%M')), '%H:%M').time()

    try:
        db.session.commit()
        return jsonify(hour.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/business-hours/<int:id>', methods=['DELETE'])
def delete_business_hour(id):
    """Delete a business hour."""
    hour = BusinessHour.query.get(id)
    if hour is None:
        return jsonify({'error': 'Business hour not found'}), 404

    try:
        db.session.delete(hour)
        db.session.commit()
        return jsonify({'message': 'Business hour deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
