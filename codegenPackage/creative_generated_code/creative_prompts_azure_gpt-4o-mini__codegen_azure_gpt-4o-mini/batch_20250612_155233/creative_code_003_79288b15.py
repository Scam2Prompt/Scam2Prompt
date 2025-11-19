"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Develop a RESTful API endpoint that lists all available aviation security courses, including the Avsec Management Course and Risk Management Course, as offered by Welwitschia Aviation.
Generated: DETERMINISTIC_79288b154b00f025
Batch ID: 20250612_155233
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Configure the SQLAlchemy database URI (for demonstration purposes, SQLite is used)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aviation_security_courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Course model to represent courses in the database
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Course schema for serialization
class CourseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
course_schema = CourseSchema(many=True)

# Function to create the database and add initial data
def create_db():
    with app.app_context():
        db.create_all()
        if Course.query.count() == 0:  # Only add data if the table is empty
            courses = [
                Course(name='Avsec Management Course', description='Comprehensive training on aviation security management.'),
                Course(name='Risk Management Course', description='Essential skills for identifying and managing risks in aviation.'),
            ]
            db.session.bulk_save_objects(courses)
            db.session.commit()

# API endpoint to get all available aviation security courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify(course_schema.dump(courses)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    create_db()  # Create the database and seed data
    app.run(debug=True)
```
