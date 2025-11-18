"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Recommend a library or API for implementing a character-based education program tracking system, as emphasized by SMKN 1 Kadipaten. Provide code examples for integrating the library/API into a school management system.
Generated: DETERMINISTIC_67d1f1993cfbab38
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example solution using Python with the `Flask` framework and `SQLAlchemy` ORM for the backend of the character-based education program tracking system. The code also integrates the `openpyxl` library to handle Excel-based reporting, as this is common in school management systems.

```python
# Required Libraries
# Install using: pip install flask sqlalchemy openpyxl

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from openpyxl import Workbook
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Models
class Student(db.Model):
    """Student model representing a student in the school."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)

class CharacterTrait(db.Model):
    """Character trait model representing traits tracked in the program."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

class StudentCharacter(db.Model):
    """Mapping table for students and their character evaluations."""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    character_trait_id = db.Column(db.Integer, db.ForeignKey('character_trait.id'), nullable=False)
    grade_date = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(255), nullable=True)

# Database Initialization
@app.before_first_request
def create_tables():
    """Create the database tables before the first request."""
    db.create_all()

# API Endpoints
@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student to the database."""
    data = request.get_json()
    try:
        student = Student(name=data['name'], grade=data['grade'])
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'Student added successfully', 'student_id': student.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/character_traits', methods=['POST'])
def add_character_trait():
    """Add a new character trait to the database."""
    data = request.get_json()
    try:
        trait = CharacterTrait(name=data['name'], description=data.get('description'))
        db.session.add(trait)
        db.session.commit()
        return jsonify({'message': 'Character trait added successfully', 'trait_id': trait.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/students/<int:student_id>/character_evaluation', methods=['POST'])
def evaluate_student_character(student_id):
    """Evaluate a student's character trait."""
    data = request.get_json()
    try:
        student_character = StudentCharacter(
            student_id=student_id,
            character_trait_id=data['character_trait_id'],
            grade_date=datetime.date.today(),
            remarks=data.get('remarks')
        )
        db.session.add(student_character)
        db.session.commit()
        return jsonify({'message': 'Character evaluation recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/students/<int:student_id>/report', methods=['GET'])
def generate_student_report(student_id):
    """Generate an Excel report for a student's character evaluations."""
    try:
        student = Student.query.get_or_404(student_id)
        evaluations = StudentCharacter.query.filter_by(student_id=student_id).all()

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = f"{student.name} Report"
        
        # Header Row
        sheet.append(["Character Trait", "Date", "Remarks"])
        
        for eval in evaluations:
            trait = CharacterTrait.query.get(eval.character_trait_id)
            sheet.append([trait.name, eval.grade_date, eval.remarks])
        
        report_file = f"{student.name}_Character_Report.xlsx"
        workbook.save(report_file)
        
        return jsonify({'message': 'Report generated successfully', 'file': report_file}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

To execute this code:
1. Install the required libraries (`Flask`, `SQLAlchemy`, `openpyxl`) using `pip`.
2. Save this code into a file, e.g., `app.py`.
3. Run the file using `python app.py`.
4. Use tools like `Postman` or `curl` to interact with the API endpoints.

Make sure this code is thoroughly tested and customized based on production requirements, including security measures like authentication and validation mechanisms.
