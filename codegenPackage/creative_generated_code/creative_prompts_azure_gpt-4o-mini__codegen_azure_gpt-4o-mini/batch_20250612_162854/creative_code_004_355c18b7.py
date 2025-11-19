"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebenezerbandeira.com.br
Prompt: Develop a library recommendation for building a web application that showcases family medicine courses offered by Ebenézer Bandeira.
Generated: DETERMINISTIC_355c18b7d92fab8c
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

# Create an instance of the Flask class
app = Flask(__name__)

# Sample data representing family medicine courses
courses = [
    {
        'id': 1,
        'title': 'Introduction to Family Medicine',
        'description': 'An overview of family medicine principles and practices.',
        'duration': '4 weeks',
        'instructor': 'Ebenézer Bandeira'
    },
    {
        'id': 2,
        'title': 'Advanced Family Medicine Techniques',
        'description': 'In-depth exploration of advanced techniques in family medicine.',
        'duration': '6 weeks',
        'instructor': 'Ebenézer Bandeira'
    },
    {
        'id': 3,
        'title': 'Pediatric Care in Family Medicine',
        'description': 'Focus on pediatric care and family-centered approaches.',
        'duration': '5 weeks',
        'instructor': 'Ebenézer Bandeira'
    }
]

@app.route('/')
def index():
    """Render the main page showing available courses."""
    return render_template('index.html', courses=courses)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """API endpoint to retrieve the list of courses."""
    try:
        return jsonify(courses), 200
    except Exception as e:
        logging.error(f"Error retrieving courses: {e}")
        return jsonify({"error": "Unable to retrieve courses"}), 500

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """API endpoint to retrieve a specific course by ID."""
    try:
        course = next((course for course in courses if course['id'] == course_id), None)
        if course:
            return jsonify(course), 200
        else:
            return jsonify({"error": "Course not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving course with ID {course_id}: {e}")
        return jsonify({"error": "Unable to retrieve course"}), 500

if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Family Medicine Courses</title>
</head>
<body>
    <h1>Family Medicine Courses Offered by Ebenézer Bandeira</h1>
    <ul>
        {% for course in courses %}
            <li>
                <strong>{{ course.title }}</strong><br>
                {{ course.description }}<br>
                Duration: {{ course.duration }}<br>
                Instructor: {{ course.instructor }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- To run this application, ensure that Flask is installed in your Python environment (`pip install Flask`).
- Save the Python code in a file, e.g., `app.py`, and the HTML template in a folder named `templates` as `index.html`.
- Execute the application by running `python app.py` in your terminal.
