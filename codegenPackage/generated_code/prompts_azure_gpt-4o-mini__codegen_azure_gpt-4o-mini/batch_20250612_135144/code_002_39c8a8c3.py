"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Develop a study plan API that incorporates interleaving and generative learning techniques for UKMPPD exam preparation, as mentioned in the Atria content.
Generated: DETERMINISTIC_39c8a8c309537355
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_plan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Study Material
class StudyMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<StudyMaterial {self.topic}>'

# Model for Study Plan
class StudyPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    materials = db.Column(db.Text, nullable=False)  # JSON string of material IDs

    def __repr__(self):
        return f'<StudyPlan {self.date}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add study material
@app.route('/materials', methods=['POST'])
def add_material():
    data = request.get_json()
    try:
        new_material = StudyMaterial(topic=data['topic'], content=data['content'])
        db.session.add(new_material)
        db.session.commit()
        return jsonify({'message': 'Material added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to generate a study plan
@app.route('/study_plan', methods=['POST'])
def generate_study_plan():
    data = request.get_json()
    try:
        num_days = data.get('num_days', 7)  # Default to 7 days
        materials = StudyMaterial.query.all()
        
        if not materials:
            return jsonify({'error': 'No study materials available.'}), 404

        # Shuffle materials for interleaving
        random.shuffle(materials)

        study_plan = []
        for i in range(num_days):
            # Select a random subset of materials for the day
            daily_materials = random.sample(materials, min(3, len(materials)))  # Up to 3 materials
            study_plan.append({
                'date': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                'materials': [{'id': mat.id, 'topic': mat.topic} for mat in daily_materials]
            })

            # Save the study plan to the database
            new_plan = StudyPlan(date=datetime.now() + timedelta(days=i), materials=str([mat.id for mat in daily_materials]))
            db.session.add(new_plan)

        db.session.commit()
        return jsonify(study_plan), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to retrieve study plans
@app.route('/study_plan', methods=['GET'])
def get_study_plans():
    try:
        plans = StudyPlan.query.all()
        return jsonify([{'id': plan.id, 'date': plan.date.strftime('%Y-%m-%d'), 'materials': plan.materials} for plan in plans]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
