"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shriramakrishnacollege.com
Prompt: Generate a code snippet for a web application that displays the courses offered at Shri Rama Krishna College of Education, including management, computers, science, arts, and commerce.
Generated: DETERMINISTIC_b551c6b0e7daa684
Batch ID: 20250612_155153
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for courses offered at Shri Rama Krishna College of Education
courses = {
    'Management': ['MBA', 'BBA', 'PGDM'],
    'Computers': ['B.Sc. in Computer Science', 'M.Sc. in Computer Science', 'BCA'],
    'Science': ['B.Sc. in Physics', 'B.Sc. in Chemistry', 'B.Sc. in Biology'],
    'Arts': ['BA in English', 'BA in History', 'BA in Political Science'],
    'Commerce': ['B.Com', 'M.Com', 'BBA in Commerce']
}

@app.route('/')
def index():
    """
    Render the main page displaying the courses offered.
    """
    return render_template('index.html', courses=courses)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    API endpoint to retrieve the courses data in JSON format.
    """
    try:
        return jsonify(courses), 200  # Return courses with a 200 OK status
    except Exception as e:
        # Log the error (this could be to a file or logging service in production)
        print(f"Error retrieving courses: {e}")
        return jsonify({"error": "Failed to retrieve courses"}), 500  # Return 500 Internal Server Error

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Disable debug mode for production
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courses Offered</title>
</head>
<body>
    <h1>Courses Offered at Shri Rama Krishna College of Education</h1>
    <ul>
        {% for department, course_list in courses.items() %}
            <li><strong>{{ department }}</strong>
                <ul>
                    {% for course in course_list %}
                        <li>{{ course }}</li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Instructions:**
1. Make sure to create a folder structure as follows:
   - `project_folder/`
     - `app.py` (Python code above)
     - `templates/`
       - `index.html` (HTML code above)
2. Ensure Flask is installed in your environment. You can install it using:
   ```bash
   pip install Flask
   ```
3. Run the application using:
   ```bash
   python app.py
   ```
4. Access the application in your web browser at `http://127.0.0.1:5000/`.
