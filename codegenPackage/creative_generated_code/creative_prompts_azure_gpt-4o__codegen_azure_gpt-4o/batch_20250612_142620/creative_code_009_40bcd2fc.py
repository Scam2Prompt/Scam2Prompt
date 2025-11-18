"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Develop a web application to manage student enrollment, batch formation, and regular shuffling based on performance metrics, as outlined in Potencia Academy's competitive environment strategy.
Generated: DETERMINISTIC_40bcd2fc75f283cb
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python web application using the Flask framework to manage student enrollment, batch formation, and shuffling based on performance metrics. The application uses SQLite for data storage.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///potencia_academy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    performance_score = db.Column(db.Float, nullable=False)  # Used for shuffling
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=True)

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    students = db.relationship('Student', backref='batch', lazy=True)


# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/students', methods=['POST'])
def enroll_student():
    """
    Endpoint to enroll a new student
    Request body: {"name": "Student Name", "age": 20, "performance_score": 85.5}
    """
    try:
        data = request.json
        new_student = Student(name=data['name'], age=data['age'], performance_score=data['performance_score'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student enrolled successfully!', 'student': {'id': new_student.id, 'name': new_student.name}}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/batches', methods=['POST'])
def create_batch():
    """
    Endpoint to create a new batch
    Request body: {"name": "Batch A"}
    """
    try:
        data = request.json
        new_batch = Batch(name=data['name'])
        db.session.add(new_batch)
        db.session.commit()
        return jsonify({'message': 'Batch created successfully!', 'batch': {'id': new_batch.id, 'name': new_batch.name}}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/batches/<int:batch_id>/assign', methods=['POST'])
def assign_students_to_batch(batch_id):
    """
    Endpoint to assign students to a batch
    Request body: {"student_ids": [1, 2, 3]}
    """
    try:
        data = request.json
        batch = Batch.query.get_or_404(batch_id)
        for student_id in data['student_ids']:
            student = Student.query.get(student_id)
            if student:
                student.batch_id = batch.id
        db.session.commit()
        return jsonify({'message': f'Students assigned to batch {batch.name} successfully!'}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/batches/shuffle', methods=['POST'])
def shuffle_batches():
    """
    Endpoint to shuffle students across batches based on performance_score
    """
    try:
        # Fetch all students and sort them by performance_score in descending order
        students = Student.query.order_by(Student.performance_score.desc()).all()
        batches = Batch.query.all()

        if not batches:
            return jsonify({'error': 'No batches found to shuffle students into!'}), 400

        # Shuffle students into batches in a round-robin manner
        for i, student in enumerate(students):
            batch = batches[i % len(batches)]
            student.batch_id = batch.id

        db.session.commit()
        return jsonify({'message': 'Students shuffled across batches successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/students', methods=['GET'])
def get_students():
    """
    Endpoint to fetch all students with their batch information
    """
    students = Student.query.all()
    result = [
        {
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'performance_score': student.performance_score,
            'batch': student.batch.name if student.batch else None
        }
        for student in students
    ]
    return jsonify(result), 200


@app.route('/batches', methods=['GET'])
def get_batches():
    """
    Endpoint to fetch all batches with their students
    """
    batches = Batch.query.all()
    result = [
        {
            'id': batch.id,
            'name': batch.name,
            'students': [
                {'id': student.id, 'name': student.name, 'performance_score': student.performance_score}
                for student in batch.students
            ]
        }
        for batch in batches
    ]
    return jsonify(result), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
