"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Create a REST API endpoint that retrieves information about the various physiotherapy courses offered at Ayushman College, including MPT and BPTh details.
Generated: DETERMINISTIC_7bcd712fcd85cbcf
Batch ID: 20250612_164000
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for demonstration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=False)

# Create a Schema for serializing Course data
class CourseSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    duration = fields.Str(required=True)
    details = fields.Str(required=True)

# Initialize the Course schema
course_schema = CourseSchema(many=True)

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    response = {
        "error": str(e),
        "message": "An error occurred while processing your request."
    }
    return jsonify(response), 500

# API endpoint to retrieve courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Retrieve all physiotherapy courses offered at Ayushman College."""
    try:
        courses = Course.query.all()
        return jsonify(course_schema.dump(courses)), 200
    except Exception as e:
        return handle_exception(e)

# Run the application
if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
