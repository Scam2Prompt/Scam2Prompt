"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Recommend a library or API for managing sports club memberships, similar to "easyVerein," and demonstrate how to integrate it into a web application for tracking tennis court bookings.
Generated: DETERMINISTIC_bc5d1173333d9c53
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tennis_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Membership {self.member_name}>'

# Define CourtBooking model
class CourtBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('membership.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    court_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<CourtBooking {self.id} by Member {self.member_id}>'

# Create database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new membership
@app.route('/memberships', methods=['POST'])
def create_membership():
    data = request.json
    new_membership = Membership(
        member_name=data['member_name'],
        membership_type=data['membership_type'],
        start_date=datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
        end_date=datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    )
    try:
        db.session.add(new_membership)
        db.session.commit()
        return jsonify({'message': 'Membership created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Membership already exists!'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to book a tennis court
@app.route('/bookings', methods=['POST'])
def book_court():
    data = request.json
    new_booking = CourtBooking(
        member_id=data['member_id'],
        booking_date=datetime.strptime(data['booking_date'], '%Y-%m-%d %H:%M').isoformat(),
        court_number=data['court_number']
    )
    try:
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Court booked successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Booking conflict or invalid member ID!'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
