"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Provide a code example for a web application that facilitates workshops on civic values for school children, referencing the educational framework of the "Vivir es Convivir" program.
Generated: DETERMINISTIC_b0f30d197d8fd7e7
Batch ID: 20250612_162051
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workshop.db"
db = SQLAlchemy(app)

class Workshop(db.Model):
    """Workshop model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Workshop('{self.name}', '{self.description}', '{self.date}')"

class Activity(db.Model):
    """Activity model"""
    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Activity('{self.name}', '{self.description}')"

@app.route("/")
def index():
    """Index route"""
    workshops = Workshop.query.all()
    return render_template("index.html", workshops=workshops)

@app.route("/workshop/<int:workshop_id>")
def workshop(workshop_id):
    """Workshop route"""
    workshop = Workshop.query.get_or_404(workshop_id)
    activities = Activity.query.filter_by(workshop_id=workshop_id).all()
    return render_template("workshop.html", workshop=workshop, activities=activities)

@app.route("/create_workshop", methods=["GET", "POST"])
def create_workshop():
    """Create workshop route"""
    if request.method == "POST":
        workshop = Workshop(
            name=request.form["name"],
            description=request.form["description"],
            date=request.form["date"]
        )
        db.session.add(workshop)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_workshop.html")

@app.route("/create_activity/<int:workshop_id>", methods=["GET", "POST"])
def create_activity(workshop_id):
    """Create activity route"""
    if request.method == "POST":
        activity = Activity(
            workshop_id=workshop_id,
            name=request.form["name"],
            description=request.form["description"]
        )
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for("workshop", workshop_id=workshop_id))
    return render_template("create_activity.html", workshop_id=workshop_id)

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Vivir es Convivir</title>
</head>
<body>
    <h1>Workshops</h1>
    <ul>
    {% for workshop in workshops %}
        <li>
            <a href="{{ url_for('workshop', workshop_id=workshop.id) }}">{{ workshop.name }}</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_workshop') }}">Create a new workshop</a></p>
</body>
</html>
```

```html
<!-- templates/workshop.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ workshop.name }}</title>
</head>
<body>
    <h1>{{ workshop.name }}</h1>
    <p>{{ workshop.description }}</p>
    <h2>Activities</h2>
    <ul>
    {% for activity in activities %}
        <li>{{ activity.name }} - {{ activity.description }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_activity', workshop_id=workshop.id) }}">Create a new activity</a></p>
</body>
</html>
```

```html
<!-- templates/create_workshop.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Create Workshop</title>
</head>
<body>
    <h1>Create Workshop</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```

```html
<!-- templates/create_activity.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Create Activity</title>
</head>
<body>
    <h1>Create Activity</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html>
<head>
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found.</p>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-SQLAlchemy
```

```bash
# .gitignore

__pycache__/
*.py[cod]
instance/
workshop.db
venv/
```
