"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Create an API that provides personalized course recommendations for students based on their admission exam preparation needs, inspired by the offerings at Educar Comitán.
Generated: DETERMINISTIC_f315b4d18a6c27dc
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Course model to represent the courses in the database
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tags = db.Column(db.String(200), nullable=False)  # Comma-separated tags

    def __repr__(self):
        return f'<Course {self.name}>'

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Function to recommend courses based on student needs
def recommend_courses(student_needs):
    # Fetch all courses from the database
    courses = Course.query.all()
    course_tags = [course.tags.split(",") for course in courses]  # Convert tags into a list
    course_matrix = np.zeros((len(courses), len(set(tag for tags in course_tags for tag in tags))))

    # Create a mapping of tags to indices
    tag_index = {tag: idx for idx, tag in enumerate(set(tag for tags in course_tags for tag in tags))}
    
    # Populate the course matrix
    for i, tags in enumerate(course_tags):
        for tag in tags:
            course_matrix[i][tag_index[tag.strip()]] = 1  # Binary representation

    # Create a vector for student needs
    student_vector = np.zeros(len(tag_index))
    for tag in student_needs:
        if tag in tag_index:
            student_vector[tag_index[tag]] = 1  # Binary representation

    # Calculate cosine similarity
    similarities = cosine_similarity([student_vector], course_matrix).flatten()
    
    # Get recommended course indices based on similarity
    recommended_indices = similarities.argsort()[-5:][::-1]  # Top 5 recommendations
    recommended_courses = [courses[idx].name for idx in recommended_indices]

    return recommended_courses

# API endpoint to get course recommendations
@app.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        data = request.get_json()
        student_needs = data.get('needs', [])
        
        if not student_needs:
            return jsonify({"error": "Needs list cannot be empty."}), 400
        
        recommendations = recommend_courses(student_needs)
        return jsonify({"recommendations": recommendations}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This API uses Flask and SQLAlchemy for creating a simple web server and database interaction.
- Course recommendations are based on cosine similarity of tags.
- Proper error handling is included for both empty input and unexpected exceptions.
- The database is initialized with a SQLite backend, but can be changed to another SQL database as needed.
- Run this code in an environment where Flask and SQLAlchemy are installed. Use `pip install Flask Flask-SQLAlchemy scikit-learn` to install the required packages.
