"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Create a web application outline that includes sections for Spiritual Therapy and Online Courses as described on the Darul Raza site.
Generated: DETERMINISTIC_4a847100032dfdf1
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Model for Spiritual Therapy
class SpiritualTherapy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"SpiritualTherapy('{self.title}')"

# Model for Online Courses
class OnlineCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"OnlineCourse('{self.title}')"

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/spiritual-therapy')
def spiritual_therapy():
    """Render the Spiritual Therapy section."""
    therapies = SpiritualTherapy.query.all()
    return render_template('spiritual_therapy.html', therapies=therapies)

@app.route('/online-courses')
def online_courses():
    """Render the Online Courses section."""
    courses = OnlineCourse.query.all()
    return render_template('online_courses.html', courses=courses)

@app.route('/add-therapy', methods=['POST'])
def add_therapy():
    """Handle the addition of a new Spiritual Therapy entry."""
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        new_therapy = SpiritualTherapy(title=title, description=description)
        db.session.add(new_therapy)
        db.session.commit()
        flash('New therapy added successfully!', 'success')
    else:
        flash('Failed to add therapy. Please provide title and description.', 'danger')
    return redirect(url_for('spiritual_therapy'))

@app.route('/add-course', methods=['POST'])
def add_course():
    """Handle the addition of a new Online Course entry."""
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        new_course = OnlineCourse(title=title, description=description)
        db.session.add(new_course)
        db.session.commit()
        flash('New course added successfully!', 'success')
    else:
        flash('Failed to add course. Please provide title and description.', 'danger')
    return redirect(url_for('online_courses'))

if __name__ == '__main__':
    # Only create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Darul Raza</title>
</head>
<body>
    <h1>Welcome to Darul Raza</h1>
    <nav>
        <ul>
            <li><a href="{{ url_for('spiritual_therapy') }}">Spiritual Therapy</a></li>
            <li><a href="{{ url_for('online_courses') }}">Online Courses</a></li>
        </ul>
    </nav>
</body>
</html>
```

```html
<!-- templates/spiritual_therapy.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spiritual Therapy</title>
</head>
<body>
    <h1>Spiritual Therapy</h1>
    <ul>
        {% for therapy in therapies %}
            <li>{{ therapy.title }}: {{ therapy.description }}</li>
        {% endfor %}
    </ul>
    <h2>Add New Therapy</h2>
    <form method="POST" action="{{ url_for('add_therapy') }}">
        <input type="text" name="title" placeholder="Therapy Title" required>
        <textarea name="description" placeholder="Therapy Description" required></textarea>
        <button type="submit">Add Therapy</button>
    </form>
</body>
</html>
```

```html
<!-- templates/online_courses.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Courses</title>
</head>
<body>
    <h1>Online Courses</h1>
    <ul>
        {% for course in courses %}
            <li>{{ course.title }}: {{ course.description }}</li>
        {% endfor %}
    </ul>
    <h2>Add New Course</h2>
    <form method="POST" action="{{ url_for('add_course') }}">
        <input type="text" name="title" placeholder="Course Title" required>
        <textarea name="description" placeholder="Course Description" required></textarea>
        <button type="submit">Add Course</button>
    </form>
</body>
</html>
```

```bash
# requirements.txt

Flask==2.0.3
Flask-SQLAlchemy==2.5.1
```

Make sure to run `pip install -r requirements.txt` to install dependencies, and set the `SECRET_KEY` to a secure random string for production.
