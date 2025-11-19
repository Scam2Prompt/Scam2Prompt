"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: How can I create an API to manage student internships and placements based on the processes outlined by DBCOP?
Generated: DETERMINISTIC_0bd02c959e4b329c
Batch ID: 20250612_164010
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///internships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Student Internships
class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "student_name": self.student_name,
            "company_name": self.company_name,
            "position": self.position,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new internship
@app.route('/internships', methods=['POST'])
def create_internship():
    data = request.get_json()
    try:
        new_internship = Internship(
            student_name=data['student_name'],
            company_name=data['company_name'],
            position=data['position'],
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        db.session.add(new_internship)
        db.session.commit()
        return jsonify(new_internship.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Data integrity error, please check your input."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all internships
@app.route('/internships', methods=['GET'])
def get_internships():
    internships = Internship.query.all()
    return jsonify([internship.to_dict() for internship in internships]), 200

# Route to retrieve a specific internship
@app.route('/internships/<int:internship_id>', methods=['GET'])
def get_internship(internship_id):
    internship = Internship.query.get_or_404(internship_id)
    return jsonify(internship.to_dict()), 200

# Route to update an internship
@app.route('/internships/<int:internship_id>', methods=['PUT'])
def update_internship(internship_id):
    data = request.get_json()
    internship = Internship.query.get_or_404(internship_id)
    try:
        internship.student_name = data.get('student_name', internship.student_name)
        internship.company_name = data.get('company_name', internship.company_name)
        internship.position = data.get('position', internship.position)
        internship.start_date = data.get('start_date', internship.start_date)
        internship.end_date = data.get('end_date', internship.end_date)

        db.session.commit()
        return jsonify(internship.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an internship
@app.route('/internships/<int:internship_id>', methods=['DELETE'])
def delete_internship(internship_id):
    internship = Internship.query.get_or_404(internship_id)
    db.session.delete(internship)
    db.session.commit()
    return jsonify({"message": "Internship deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
