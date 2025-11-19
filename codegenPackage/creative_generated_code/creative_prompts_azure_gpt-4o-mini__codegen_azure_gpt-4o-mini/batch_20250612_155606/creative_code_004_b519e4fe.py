"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzo.protocol-rez.org
Prompt: Suggest a framework for building a course platform that includes video training and user testimonials, similar to the structure described on the Renzo Protocol site.
Generated: DETERMINISTIC_b519e4fe14bf8938
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///courses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Course model
class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(200), nullable=False)
    testimonials = db.relationship('Testimonial', backref='course', lazy=True)

# Define the Testimonial model
class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

# Route to render the homepage with courses
@app.route('/')
def home():
    try:
        courses = Course.query.all()
        return render_template('home.html', courses=courses)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all testimonials for a specific course
@app.route('/course/<int:course_id>/testimonials', methods=['GET'])
def get_testimonials(course_id):
    try:
        testimonials = Testimonial.query.filter_by(course_id=course_id).all()
        return jsonify([{"user_name": t.user_name, "feedback": t.feedback} for t in testimonials])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

### HTML Template (home.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Platform</title>
</head>
<body>
    <h1>Available Courses</h1>
    <ul>
        {% for course in courses %}
            <li>
                <h2>{{ course.title }}</h2>
                <p>{{ course.description }}</p>
                <video width="320" height="240" controls>
                    <source src="{{ course.video_url }}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <a href="/course/{{ course.id }}/testimonials">View Testimonials</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes
- Ensure that you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your Python environment.
- Set up your environment variables for the database and Flask debug mode as needed.
- Create the necessary database tables and migrate the schema using Flask-Migrate.
