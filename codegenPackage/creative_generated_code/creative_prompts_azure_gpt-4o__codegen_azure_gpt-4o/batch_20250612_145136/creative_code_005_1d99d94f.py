"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Write a script using Flask to display INESO's course details dynamically, including "Especialidad en Ortodoncia" and "Especialidad en Ortodoncia y Ortopedia Maxilofacial," along with their schedules and accreditation.
Generated: DETERMINISTIC_1d99d94f59246f8e
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Data containing course details
course_data = [
    {
        "name": "Especialidad en Ortodoncia",
        "schedule": "Monday to Friday, 9:00 AM - 2:00 PM",
        "accreditation": "Certified by National Orthodontics Board"
    },
    {
        "name": "Especialidad en Ortodoncia y Ortopedia Maxilofacial",
        "schedule": "Monday to Friday, 3:00 PM - 8:00 PM",
        "accreditation": "Certified by International Dental Accreditation Council"
    }
]

@app.route('/')
def home():
    """
    Home route that displays the course details dynamically in HTML.
    """
    return render_template("courses.html", courses=course_data)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    API endpoint to fetch course details in JSON format.
    """
    return jsonify(course_data), 200

if __name__ == '__main__':
    # Run the app on localhost with debugging enabled.
    app.run(debug=True)

# Save this HTML file as 'templates/courses.html' in the same directory as the script
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INESO Courses</title>
</head>
<body>
    <h1>INESO Courses</h1>
    <ul>
        {% for course in courses %}
            <li>
                <h2>{{ course.name }}</h2>
                <p><strong>Schedule:</strong> {{ course.schedule }}</p>
                <p><strong>Accreditation:</strong> {{ course.accreditation }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""
```
