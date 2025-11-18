"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Develop a REST API that allows users to retrieve information about wine tasting seminars, including details like location, time, and sommelier information, as seen in the FestiVin Caraquet program.
Generated: DETERMINISTIC_d3fbe6886cd77419
Batch ID: 20250612_153225
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wineseminar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Wine Tasting Seminars
class WineTastingSeminar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    sommelier = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<WineTastingSeminar {self.id}: {self.location} at {self.time}>'

# Schema for serializing seminar data
class SeminarSchema(Schema):
    id = fields.Int()
    location = fields.Str(required=True)
    time = fields.DateTime(required=True)
    sommelier = fields.Str(required=True)

seminar_schema = SeminarSchema()
seminars_schema = SeminarSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to retrieve all wine tasting seminars
@app.route('/seminars', methods=['GET'])
def get_seminars():
    try:
        seminars = WineTastingSeminar.query.all()
        return seminars_schema.dump(seminars), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve a specific seminar by ID
@app.route('/seminars/<int:id>', methods=['GET'])
def get_seminar(id):
    try:
        seminar = WineTastingSeminar.query.get_or_404(id)
        return seminar_schema.dump(seminar), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to create a new seminar
@app.route('/seminars', methods=['POST'])
def add_seminar():
    try:
        data = request.get_json()
        seminar = seminar_schema.load(data)
        new_seminar = WineTastingSeminar(
            location=seminar['location'],
            time=datetime.fromisoformat(seminar['time']),
            sommelier=seminar['sommelier']
        )
        db.session.add(new_seminar)
        db.session.commit()
        return seminar_schema.dump(new_seminar), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an existing seminar
@app.route('/seminars/<int:id>', methods=['PUT'])
def update_seminar(id):
    try:
        seminar = WineTastingSeminar.query.get_or_404(id)
        data = request.get_json()
        
        # Update seminar fields
        seminar.location = data.get('location', seminar.location)
        seminar.time = datetime.fromisoformat(data.get('time', seminar.time.isoformat()))
        seminar.sommelier = data.get('sommelier', seminar.sommelier)
        
        db.session.commit()
        return seminar_schema.dump(seminar), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a seminar
@app.route('/seminars/<int:id>', methods=['DELETE'])
def delete_seminar(id):
    try:
        seminar = WineTastingSeminar.query.get_or_404(id)
        db.session.delete(seminar)
        db.session.commit()
        return jsonify({"message": "Seminar deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
