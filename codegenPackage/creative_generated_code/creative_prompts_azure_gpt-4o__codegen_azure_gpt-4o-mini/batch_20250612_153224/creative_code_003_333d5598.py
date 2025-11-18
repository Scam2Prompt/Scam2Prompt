"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Generate code for a web application that tracks humanitarian interventions and medical aid distribution, aligning with Jusoor International's programs.
Generated: DETERMINISTIC_333d55984762f9a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hum_interventions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for tracking interventions
class HumanitarianIntervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    intervention_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(200), nullable=False)
    aid_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Intervention {self.id} - {self.program_name}>"

# Create the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new humanitarian intervention
@app.route('/interventions', methods=['POST'])
def add_intervention():
    try:
        data = request.get_json()
        new_intervention = HumanitarianIntervention(
            program_name=data['program_name'],
            intervention_type=data['intervention_type'],
            description=data.get('description'),
            location=data['location'],
            aid_amount=data['aid_amount']
        )
        db.session.add(new_intervention)
        db.session.commit()
        return jsonify({'message': 'Intervention added successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all interventions
@app.route('/interventions', methods=['GET'])
def get_interventions():
    try:
        interventions = HumanitarianIntervention.query.all()
        return jsonify([{
            'id': intervention.id,
            'program_name': intervention.program_name,
            'intervention_type': intervention.intervention_type,
            'description': intervention.description,
            'date': intervention.date.isoformat(),
            'location': intervention.location,
            'aid_amount': intervention.aid_amount
        } for intervention in interventions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an intervention
@app.route('/interventions/<int:id>', methods=['PUT'])
def update_intervention(id):
    try:
        data = request.get_json()
        intervention = HumanitarianIntervention.query.get_or_404(id)
        
        intervention.program_name = data.get('program_name', intervention.program_name)
        intervention.intervention_type = data.get('intervention_type', intervention.intervention_type)
        intervention.description = data.get('description', intervention.description)
        intervention.location = data.get('location', intervention.location)
        intervention.aid_amount = data.get('aid_amount', intervention.aid_amount)

        db.session.commit()
        return jsonify({'message': 'Intervention updated successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete an intervention
@app.route('/interventions/<int:id>', methods=['DELETE'])
def delete_intervention(id):
    try:
        intervention = HumanitarianIntervention.query.get_or_404(id)
        db.session.delete(intervention)
        db.session.commit()
        return jsonify({'message': 'Intervention deleted successfully.'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
