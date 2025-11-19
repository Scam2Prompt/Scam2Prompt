"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Create an API that provides information about the different occupational medical exams available at Medicid IPS, including details on exams for high-altitude work and confined spaces.
Generated: DETERMINISTIC_5ef254cdc9b6acad
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application and API
app = Flask(__name__)
api = Api(app)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicid_ips.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the OccupationalExam model
class OccupationalExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    requirements = db.Column(db.String(300), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Resource for handling Occupational Medical Exams
class OccupationalExamsResource(Resource):
    def get(self):
        """Retrieve all occupational medical exams."""
        try:
            exams = OccupationalExam.query.all()
            return jsonify([{
                'id': exam.id,
                'name': exam.name,
                'description': exam.description,
                'requirements': exam.requirements
            } for exam in exams])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    def post(self):
        """Add a new occupational medical exam."""
        data = request.json
        if not data or 'name' not in data or 'description' not in data or 'requirements' not in data:
            return jsonify({'error': 'Invalid data provided.'}), 400

        new_exam = OccupationalExam(
            name=data['name'],
            description=data['description'],
            requirements=data['requirements']
        )
        try:
            db.session.add(new_exam)
            db.session.commit()
            return jsonify({'message': 'Exam added successfully.'}), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

# Resource for handling specific exams
class OccupationalExamResource(Resource):
    def get(self, exam_id):
        """Retrieve a specific occupational medical exam by ID."""
        exam = OccupationalExam.query.get(exam_id)
        if exam is None:
            return jsonify({'error': 'Exam not found.'}), 404
        return jsonify({
            'id': exam.id,
            'name': exam.name,
            'description': exam.description,
            'requirements': exam.requirements
        })

# Add resources to the API
api.add_resource(OccupationalExamsResource, '/api/exams')
api.add_resource(OccupationalExamResource, '/api/exams/<int:exam_id>')

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
