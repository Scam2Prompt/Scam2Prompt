"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Develop a web application that showcases the curricular and extracurricular activities of a school, similar to the offerings at Param Gyan Niketan, including sections for sports, music, and art.
Generated: DETERMINISTIC_08c2822a2b563446
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_activities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Activity model
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Activity {self.name} - {self.category}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    """Render the homepage with a list of activities."""
    activities = Activity.query.all()
    return render_template('index.html', activities=activities)

# Route to add a new activity
@app.route('/add', methods=['GET', 'POST'])
def add_activity():
    """Handle the addition of new activities."""
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        new_activity = Activity(name=name, category=category)
        try:
            db.session.add(new_activity)
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            return "An error occurred while adding the activity. Please try again."
    
    return render_template('add_activity.html')

# Route to view details of a specific activity
@app.route('/activity/<int:activity_id>')
def activity_detail(activity_id):
    """Render the detail page for a specific activity."""
    activity = Activity.query.get_or_404(activity_id)
    return render_template('activity_detail.html', activity=activity)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Activities</title>
</head>
<body>
    <h1>Curricular and Extracurricular Activities</h1>
    <a href="{{ url_for('add_activity') }}">Add New Activity</a>
    <ul>
        {% for activity in activities %}
            <li>
                <a href="{{ url_for('activity_detail', activity_id=activity.id) }}">{{ activity.name }}</a> - {{ activity.category }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- add_activity.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Activity</title>
</head>
<body>
    <h1>Add New Activity</h1>
    <form action="{{ url_for('add_activity') }}" method="POST">
        <label for="name">Activity Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" required>
        <br>
        <button type="submit">Add Activity</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- activity_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activity Detail</title>
</head>
<body>
    <h1>{{ activity.name }}</h1>
    <p>Category: {{ activity.category }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```
