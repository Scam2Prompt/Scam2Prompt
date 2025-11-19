"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Generate code to track and display tennis training schedules for multiple trainers, ensuring each trainer's availability is updated dynamically on the club's website.
Generated: DETERMINISTIC_6772265f4e8da263
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tennis_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Trainer
class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    availability = db.relationship('Availability', backref='trainer', lazy=True)

# Database model for Availability
class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

# Schema for Trainer
class TrainerSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    availability = fields.List(fields.Nested('AvailabilitySchema'))

# Schema for Availability
class AvailabilitySchema(Schema):
    id = fields.Int()
    trainer_id = fields.Int(required=True)
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new trainer
@app.route('/trainers', methods=['POST'])
def add_trainer():
    try:
        data = request.get_json()
        trainer_schema = TrainerSchema()
        trainer = trainer_schema.load(data)
        new_trainer = Trainer(name=trainer['name'])
        db.session.add(new_trainer)
        db.session.commit()
        return trainer_schema.dump(new_trainer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update trainer availability
@app.route('/trainers/<int:trainer_id>/availability', methods=['POST'])
def add_availability(trainer_id):
    try:
        data = request.get_json()
        availability_schema = AvailabilitySchema()
        availability = availability_schema.load(data)
        new_availability = Availability(
            trainer_id=trainer_id,
            start_time=datetime.fromisoformat(availability['start_time']),
            end_time=datetime.fromisoformat(availability['end_time'])
        )
        db.session.add(new_availability)
        db.session.commit()
        return availability_schema.dump(new_availability), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all trainers with their availability
@app.route('/trainers', methods=['GET'])
def get_trainers():
    try:
        trainers = Trainer.query.all()
        trainer_schema = TrainerSchema(many=True)
        return trainer_schema.dump(trainers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
