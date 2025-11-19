"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genteparaservir.org
Prompt: Create a REST API endpoint for a church community platform that includes functionalities for "Seminarios" and "Peregrinación a Tierra Santa" as described on Gente Para Servir.
Generated: DETERMINISTIC_250769937e3d2332
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///church_community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database, migration, and marshmallow
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# Define the Seminario model
class Seminario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date

# Define the Seminario schema
class SeminarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seminario

# Define the Peregrinación model
class Peregrinacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    details = db.Column(db.Text, nullable=True)

    def __init__(self, destination, date, details):
        self.destination = destination
        self.date = date
        self.details = details

# Define the Peregrinación schema
class PeregrinacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Peregrinacion

# Initialize schemas
sem_schema = SeminarioSchema()
seminarios_schema = SeminarioSchema(many=True)

pere_schema = PeregrinacionSchema()
peregrinaciones_schema = PeregrinacionSchema(many=True)

# Create a new Seminario
@app.route('/seminarios', methods=['POST'])
def add_seminario():
    try:
        title = request.json['title']
        description = request.json.get('description', '')
        date = request.json['date']
        new_seminario = Seminario(title, description, date)
        db.session.add(new_seminario)
        db.session.commit()
        return sem_schema.jsonify(new_seminario), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all Seminarios
@app.route('/seminarios', methods=['GET'])
def get_seminarios():
    seminarios = Seminario.query.all()
    return seminarios_schema.jsonify(seminarios)

# Create a new Peregrinación
@app.route('/peregrinaciones', methods=['POST'])
def add_peregrinacion():
    try:
        destination = request.json['destination']
        date = request.json['date']
        details = request.json.get('details', '')
        new_peregrinacion = Peregrinacion(destination, date, details)
        db.session.add(new_peregrinacion)
        db.session.commit()
        return pere_schema.jsonify(new_peregrinacion), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all Peregrinaciones
@app.route('/peregrinaciones', methods=['GET'])
def get_peregrinaciones():
    peregrinaciones = Peregrinacion.query.all()
    return peregrinaciones_schema.jsonify(peregrinaciones)

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
