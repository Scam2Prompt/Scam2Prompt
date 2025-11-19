"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Create a REST API that provides information about the different diplomas and courses in aesthetic medicine offered by Academia Medicina Estética.
Generated: DETERMINISTIC_a8dbef3e8bd2b9c2
Batch ID: 20250612_161616
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure Database (SQLite for simplicity, can be replaced with any other)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///academia_medicina_estetica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Diploma Model
class Diploma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Diploma Schema
class DiplomaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Diploma

# Initialize the database tables
with app.app_context():
    db.create_all()

# Route to get all diplomas
@app.route('/api/diplomas', methods=['GET'])
def get_diplomas():
    try:
        diplomas = Diploma.query.all()
        diploma_schema = DiplomaSchema(many=True)
        return jsonify(diploma_schema.dump(diplomas)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new diploma
@app.route('/api/diplomas', methods=['POST'])
def add_diploma():
    try:
        data = request.json
        new_diploma = Diploma(name=data['name'], description=data['description'])
        db.session.add(new_diploma)
        db.session.commit()
        diploma_schema = DiplomaSchema()
        return jsonify(diploma_schema.dump(new_diploma)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get a diploma by ID
@app.route('/api/diplomas/<int:id>', methods=['GET'])
def get_diploma(id):
    try:
        diploma = Diploma.query.get_or_404(id)
        diploma_schema = DiplomaSchema()
        return jsonify(diploma_schema.dump(diploma)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Dependencies
To run this code, make sure you have the following Python packages installed:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```

### Note
- This code provides basic CRUD operations for diplomas in aesthetic medicine.
- Ensure to configure the database as needed for your production environment.
