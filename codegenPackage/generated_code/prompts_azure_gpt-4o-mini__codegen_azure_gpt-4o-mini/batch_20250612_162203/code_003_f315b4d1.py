"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Create an API that provides personalized course recommendations for students based on their admission exam preparation needs, inspired by the offerings at Educar Comitán.
Generated: DETERMINISTIC_f315b4d18a6c27dc
Batch ID: 20250612_162203
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Course {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get personalized course recommendations
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    try:
        # Get JSON data from the request
        data = request.get_json()
        admission_exam = data.get('admission_exam')
        preferred_subjects = data.get('preferred_subjects', [])
        level = data.get('level', 'beginner')

        # Validate input data
        if not admission_exam or not preferred_subjects:
            return jsonify({'error': 'Admission exam and preferred subjects are required.'}), 400

        # Query the database for courses based on the input criteria
        recommendations = Course.query.filter(
            Course.subject.in_(preferred_subjects),
            Course.level == level
        ).all()

        # Prepare the response data
        response_data = [{'id': course.id, 'name': course.name, 'subject': course.subject, 'level': course.level} for course in recommendations]

        return jsonify({'recommendations': response_data}), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle any other errors
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Sample data for testing purposes
@app.route('/add_sample_courses', methods=['POST'])
def add_sample_courses():
    try:
        sample_courses = [
            Course(name='Math Basics', subject='Mathematics', level='beginner'),
            Course(name='Advanced Physics', subject='Physics', level='advanced'),
            Course(name='Chemistry 101', subject='Chemistry', level='beginner'),
            Course(name='Statistics for Beginners', subject='Mathematics', level='beginner'),
            Course(name='Biology Advanced', subject='Biology', level='advanced')
        ]
        db.session.bulk_save_objects(sample_courses)
        db.session.commit()
        return jsonify({'message': 'Sample courses added successfully.'}), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
