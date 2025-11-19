"""
Generated Code Metadata:
========================
Original URL: https://pomrajufm.edu.bd
Prompt: Generate a sample code for a simple website or portal for Pomra Jameul Ulum Fazil Madrasha to display important notices, exam schedules, and student results.
Generated: DETERMINISTIC_b07e69df74283fd5
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based web application for Pomra Jameul Ulum Fazil Madrasha
# This application displays important notices, exam schedules, and student results.

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Sample data for demonstration purposes
notices = [
    {"id": 1, "title": "Admission Open", "content": "Admissions are open for the new academic year."},
    {"id": 2, "title": "Holiday Notice", "content": "The madrasha will remain closed on Friday."}
]

exam_schedules = [
    {"id": 1, "exam_name": "Midterm Exam", "date": "2023-11-15", "time": "10:00 AM"},
    {"id": 2, "exam_name": "Final Exam", "date": "2023-12-20", "time": "10:00 AM"}
]

student_results = [
    {"id": 1, "name": "John Doe", "roll": 101, "grade": "A"},
    {"id": 2, "name": "Jane Smith", "roll": 102, "grade": "B+"}
]

@app.route('/')
def home():
    """
    Home page displaying links to Notices, Exam Schedules, and Student Results.
    """
    return render_template('home.html')

@app.route('/notices')
def display_notices():
    """
    Page to display all notices.
    """
    return render_template('notices.html', notices=notices)

@app.route('/exam-schedules')
def display_exam_schedules():
    """
    Page to display exam schedules.
    """
    return render_template('exam_schedules.html', exam_schedules=exam_schedules)

@app.route('/student-results')
def display_student_results():
    """
    Page to display student results.
    """
    return render_template('student_results.html', student_results=student_results)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pomra Jameul Ulum Fazil Madrasha</title>
</head>
<body>
    <h1>Welcome to Pomra Jameul Ulum Fazil Madrasha</h1>
    <ul>
        <li><a href="/notices">Important Notices</a></li>
        <li><a href="/exam-schedules">Exam Schedules</a></li>
        <li><a href="/student-results">Student Results</a></li>
    </ul>
</body>
</html>
```

#### `templates/notices.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notices</title>
</head>
<body>
    <h1>Important Notices</h1>
    <ul>
        {% for notice in notices %}
        <li>
            <h2>{{ notice.title }}</h2>
            <p>{{ notice.content }}</p>
        </li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/exam_schedules.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Schedules</title>
</head>
<body>
    <h1>Exam Schedules</h1>
    <ul>
        {% for schedule in exam_schedules %}
        <li>
            <h2>{{ schedule.exam_name }}</h2>
            <p>Date: {{ schedule.date }}</p>
            <p>Time: {{ schedule.time }}</p>
        </li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/student_results.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Results</title>
</head>
<body>
    <h1>Student Results</h1>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Roll</th>
            <th>Grade</th>
        </tr>
        {% for result in student_results %}
        <tr>
            <td>{{ result.name }}</td>
            <td>{{ result.roll }}</td>
            <td>{{ result.grade }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
