"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Develop a REST API that allows users to retrieve information about wine tasting seminars, including details like location, time, and sommelier information, as seen in the FestiVin Caraquet program.
Generated: DETERMINISTIC_d3fbe6886cd77419
Batch ID: 20250612_153225
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wineseminar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Wine Seminar model
class WineSeminar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    sommelier = db.Column(db.String(100), nullable=False)

# Create a schema for serializing Wine Seminar data
class WineSeminarSchema(Schema):
    id = fields.Int()
    location = fields.Str(required=True)
    time = fields.Str(required=True)
    sommelier = fields.Str(required=True)

# Initialize the schema
seminar_schema = WineSeminarSchema()
seminars_schema = WineSeminarSchema(many=True)

# Error handling for database operations
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    return jsonify({"error": str(error)}), 500

# Route to retrieve all wine seminars
@app.route('/seminars', methods=['GET'])
def get_seminars():
    seminars = WineSeminar.query.all()
    return seminars_schema.dump(seminars), 200

# Route to retrieve a specific wine seminar by ID
@app.route('/seminars/<int:seminar_id>', methods=['GET'])
def get_seminar(seminar_id):
    seminar = WineSeminar.query.get_or_404(seminar_id)
    return seminar_schema.dump(seminar), 200

# Route to create a new wine seminar
@app.route('/seminars', methods=['POST'])
def create_seminar():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        seminar = seminar_schema.load(data)
        
        # Create a new seminar instance
        new_seminar = WineSeminar(**seminar)
        db.session.add(new_seminar)
        db.session.commit()
        
        return seminar_schema.dump(new_seminar), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Route to update an existing wine seminar
@app.route('/seminars/<int:seminar_id>', methods=['PUT'])
def update_seminar(seminar_id):
    seminar = WineSeminar.query.get_or_404(seminar_id)
    try:
        data = request.get_json()
        updated_seminar = seminar_schema.load(data)
        
        # Update seminar details
        seminar.location = updated_seminar['location']
        seminar.time = updated_seminar['time']
        seminar.sommelier = updated_seminar['sommelier']
        
        db.session.commit()
        return seminar_schema.dump(seminar), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

# Route to delete a wine seminar
@app.route('/seminars/<int:seminar_id>', methods=['DELETE'])
def delete_seminar(seminar_id):
    seminar = WineSeminar.query.get_or_404(seminar_id)
    db.session.delete(seminar)
    db.session.commit()
    return jsonify({"message": "Seminar deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
