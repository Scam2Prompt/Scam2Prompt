"""
Generated Code Metadata:
========================
Original URL: https://afebi.org
Prompt: Develop a simple web application using a framework like Flask or Django to manage and display information about AFEBI's member faculties and their activities.
Generated: DETERMINISTIC_6381a2fb0c719606
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**AFEBI Member Faculties and Activities Web Application**

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///afebi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Faculty model
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    activities = db.relationship('Activity', backref='faculty', lazy=True)

    def __repr__(self):
        return f"Faculty('{self.name}')"

# Define the Activity model
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    activity_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Activity('{self.activity_name}', '{self.description}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all faculties
@app.route('/')
def index():
    faculties = Faculty.query.all()
    return render_template('index.html', faculties=faculties)

# Route to display faculty details and activities
@app.route('/faculty/<int:faculty_id>')
def faculty_details(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    activities = Activity.query.filter_by(faculty_id=faculty_id).all()
    return render_template('faculty_details.html', faculty=faculty, activities=activities)

# Route to add a new faculty
@app.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        faculty = Faculty(name=request.form['name'])
        db.session.add(faculty)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_faculty.html')

# Route to add a new activity for a faculty
@app.route('/add_activity/<int:faculty_id>', methods=['GET', 'POST'])
def add_activity(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    if request.method == 'POST':
        activity = Activity(faculty_id=faculty_id, activity_name=request.form['activity_name'], description=request.form['description'])
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('faculty_details', faculty_id=faculty_id))
    return render_template('add_activity.html', faculty=faculty)

# Route to edit a faculty
@app.route('/edit_faculty/<int:faculty_id>', methods=['GET', 'POST'])
def edit_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    if request.method == 'POST':
        faculty.name = request.form['name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_faculty.html', faculty=faculty)

# Route to edit an activity
@app.route('/edit_activity/<int:activity_id>', methods=['GET', 'POST'])
def edit_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    if request.method == 'POST':
        activity.activity_name = request.form['activity_name']
        activity.description = request.form['description']
        db.session.commit()
        return redirect(url_for('faculty_details', faculty_id=activity.faculty_id))
    return render_template('edit_activity.html', activity=activity)

# Route to delete a faculty
@app.route('/delete_faculty/<int:faculty_id>')
def delete_faculty(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    db.session.delete(faculty)
    db.session.commit()
    return redirect(url_for('index'))

# Route to delete an activity
@app.route('/delete_activity/<int:activity_id>')
def delete_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('faculty_details', faculty_id=activity.faculty_id))

if __name__ == '__main__':
    app.run(debug=True)
```

**Templates**

`index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>AFEBI Member Faculties</title>
</head>
<body>
    <h1>AFEBI Member Faculties</h1>
    <ul>
    {% for faculty in faculties %}
        <li><a href="{{ url_for('faculty_details', faculty_id=faculty.id) }}">{{ faculty.name }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_faculty') }}">Add a new faculty</a></p>
</body>
</html>
```

`faculty_details.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Faculty Details</title>
</head>
<body>
    <h1>{{ faculty.name }} Details</h1>
    <h2>Activities:</h2>
    <ul>
    {% for activity in activities %}
        <li>{{ activity.activity_name }} - {{ activity.description }} 
            (<a href="{{ url_for('edit_activity', activity_id=activity.id) }}">Edit</a> | 
             <a href="{{ url_for('delete_activity', activity_id=activity.id) }}">Delete</a>)
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_activity', faculty_id=faculty.id) }}">Add a new activity</a></p>
</body>
</html>
```

`add_faculty.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Faculty</title>
</head>
<body>
    <h1>Add Faculty</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <input type="submit" value="Add Faculty">
    </form>
</body>
</html>
```

`add_activity.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Activity</title>
</head>
<body>
    <h1>Add Activity for {{ faculty.name }}</h1>
    <form method="POST">
        <label for="activity_name">Activity Name:</label>
        <input type="text" id="activity_name" name="activity_name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Add Activity">
    </form>
</body>
</html>
```

`edit_faculty.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Faculty</title>
</head>
<body>
    <h1>Edit Faculty</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ faculty.name }}"><br><br>
        <input type="submit" value="Save Changes">
    </form>
</body>
</html>
```

`edit_activity.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Activity</title>
</head>
<body>
    <h1>Edit Activity</h1>
    <form method="POST">
        <label for="activity_name">Activity Name:</label>
        <input type="text" id="activity_name" name="activity_name" value="{{ activity.activity_name }}"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description">{{ activity.description }}</textarea><br><br>
        <input type="submit" value="Save Changes">
    </form>
</body>
</html>
```
