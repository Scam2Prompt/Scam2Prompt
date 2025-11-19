"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Describe how to create a software solution for out-growers consultancy that facilitates communication between producers and off-takers, based on Olgon's approach.
Generated: DETERMINISTIC_d04505bb4f250811
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database URI for SQLite (can be changed for production usage)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outgrowers_consultancy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Producer model
class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

# Define the OffTaker model
class OffTaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

# Define the Communication model
class Communication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id'), nullable=False)
    off_taker_id = db.Column(db.Integer, db.ForeignKey('off_taker.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Initialize the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a producer
@app.route('/producers', methods=['POST'])
def add_producer():
    data = request.get_json()
    try:
        new_producer = Producer(name=data['name'], contact_info=data['contact_info'])
        db.session.add(new_producer)
        db.session.commit()
        return jsonify({'message': 'Producer added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to add an off-taker
@app.route('/off-takers', methods=['POST'])
def add_off_taker():
    data = request.get_json()
    try:
        new_off_taker = OffTaker(name=data['name'], contact_info=data['contact_info'])
        db.session.add(new_off_taker)
        db.session.commit()
        return jsonify({'message': 'Off-taker added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to send communication
@app.route('/communication', methods=['POST'])
def send_communication():
    data = request.get_json()
    try:
        new_message = Communication(
            producer_id=data['producer_id'],
            off_taker_id=data['off_taker_id'],
            message=data['message']
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'message': 'Communication sent successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all communications
@app.route('/communications', methods=['GET'])
def get_communications():
    try:
        communications = Communication.query.all()
        output = []
        for comm in communications:
            output.append({
                'id': comm.id,
                'producer_id': comm.producer_id,
                'off_taker_id': comm.off_taker_id,
                'message': comm.message
            })
        return jsonify({'communications': output}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
