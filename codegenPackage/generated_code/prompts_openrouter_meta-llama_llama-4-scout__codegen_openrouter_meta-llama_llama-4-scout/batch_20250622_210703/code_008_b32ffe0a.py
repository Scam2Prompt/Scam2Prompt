"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Recommend APIs or libraries for building a web application to manage and track the impact of community development programs, like those offered by جمعية التنمية الأهلية بتبوك.
Generated: DETERMINISTIC_b32ffe0a1c185b77
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///community_development.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Define a model for community development programs
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    impact = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Program('{self.name}', '{self.description}', {self.impact})"

# Define a model for program metrics
class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    metric_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Metric('{self.metric_name}', {self.value})"

# API endpoint to create a new program
@app.route('/programs', methods=['POST'])
def create_program():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        program = Program(name=data['name'], description=data['description'])
        db.session.add(program)
        db.session.commit()
        return jsonify({"message": "Program created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    try:
        programs = Program.query.all()
        output = []
        for program in programs:
            program_data = {
                'id': program.id,
                'name': program.name,
                'description': program.description,
                'impact': program.impact
            }
            output.append(program_data)
        return jsonify({"programs": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a program's impact
@app.route('/programs/<int:program_id>/impact', methods=['PATCH'])
def update_impact(program_id):
    try:
        program = Program.query.get(program_id)
        if not program:
            return jsonify({"error": "Program not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        program.impact = data['impact']
        db.session.commit()
        return jsonify({"message": "Program impact updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to create a new metric for a program
@app.route('/programs/<int:program_id>/metrics', methods=['POST'])
def create_metric(program_id):
    try:
        program = Program.query.get(program_id)
        if not program:
            return jsonify({"error": "Program not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        metric = Metric(program_id=program_id, metric_name=data['metric_name'], value=data['value'])
        db.session.add(metric)
        db.session.commit()
        return jsonify({"message": "Metric created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
