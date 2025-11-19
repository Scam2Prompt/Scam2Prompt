"""
Generated Code Metadata:
========================
Original URL: https://ezway.com.br
Prompt: Write a Python script to create a simple English language learning website similar to EZ Way, including sections for courses and contact information.
Generated: DETERMINISTIC_df4d6561319669ef
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Course(db.Model):
    """Represents a course in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"

class ContactMessage(db.Model):
    """Represents a contact message in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"ContactMessage('{self.name}', '{self.email}')"

@app.route('/')
def index():
    """Renders the index page."""
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course(course_id):
    """Renders a course page."""
    course = Course.query.get_or_404(course_id)
    return render_template('course.html', course=course)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles contact form submission."""
    if request.method == 'POST':
        contact_message = ContactMessage(
            name=request.form['name'],
            email=request.form['email'],
            message=request.form['message']
        )
        db.session.add(contact_message)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Learning Website</title>
</head>
<body>
    <h1>Courses</h1>
    <ul>
    {% for course in courses %}
        <li>
            <a href="{{ url_for('course', course_id=course.id) }}">{{ course.name }}</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('contact') }}">Contact Us</a></p>
</body>
</html>
```

```html
<!-- templates/course.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ course.name }}</title>
</head>
<body>
    <h1>{{ course.name }}</h1>
    <p>{{ course.description }}</p>
</body>
</html>
```

```html
<!-- templates/contact.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-SQLAlchemy
```

```bash
# Run the following commands in the terminal:

# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create the database
flask db init
flask db migrate
flask db upgrade

# Run the application
python app.py
```
