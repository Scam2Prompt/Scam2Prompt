"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Develop a web application that showcases the curricular and extracurricular activities of a school, similar to the offerings at Param Gyan Niketan, including sections for sports, music, and art.
Generated: DETERMINISTIC_08c2822a2b563446
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**School Activities Web Application**
=====================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database operations

**requirements.txt:**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

**app.py:**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_activities.db'
db = SQLAlchemy(app)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Activity('{self.name}', '{self.category}')"

@app.route('/')
def index():
    activities = Activity.query.all()
    sports = [a for a in activities if a.category == 'sports']
    music = [a for a in activities if a.category == 'music']
    art = [a for a in activities if a.category == 'art']
    return render_template('index.html', sports=sports, music=music, art=art)

@app.route('/add_activity', methods=['GET', 'POST'])
def add_activity():
    if request.method == 'POST':
        activity = Activity(
            name=request.form['name'],
            description=request.form['description'],
            category=request.form['category']
        )
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_activity.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**models.py:**
```python
# Not needed, moved to app.py
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Activities</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>School Activities</h1>
    <section id="sports">
        <h2>Sports</h2>
        <ul>
        {% for sport in sports %}
            <li>{{ sport.name }} - {{ sport.description }}</li>
        {% endfor %}
        </ul>
    </section>
    <section id="music">
        <h2>Music</h2>
        <ul>
        {% for m in music %}
            <li>{{ m.name }} - {{ m.description }}</li>
        {% endfor %}
        </ul>
    </section>
    <section id="art">
        <h2>Art</h2>
        <ul>
        {% for a in art %}
            <li>{{ a.name }} - {{ a.description }}</li>
        {% endfor %}
        </ul>
    </section>
    <p><a href="{{ url_for('add_activity') }}">Add a new activity</a></p>
</body>
</html>
```

**templates/add_activity.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Activity</title>
</head>
<body>
    <h1>Add a new activity</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="category">Category:</label>
        <select id="category" name="category">
            <option value="sports">Sports</option>
            <option value="music">Music</option>
            <option value="art">Art</option>
        </select><br><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>
```

**templates/404.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**static/style.css:**
```css
body {
    font-family: Arial, sans-serif;
}

section {
    margin-bottom: 20px;
}

h2 {
    margin-top: 0;
}
```

**run:**
```bash
python
>>> from app import db
>>> db.create_all()
``` 
or 
```bash
flask db init 
flask db migrate 
flask db upgrade 
python app.py
```
