"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Generate code for a web-based STEAM program that integrates science, technology, engineering, art, and mathematics, similar to the interdisciplinary approach mentioned on the Del Sol Montessori website.
Generated: DETERMINISTIC_9c49e1de18daaded
Batch ID: 20250612_152000
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///steam.db"
db = SQLAlchemy(app)


# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.category}')"


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    project = db.relationship("Project", backref=db.backref("resources", lazy=True))

    def __repr__(self):
        return f"Resource('{self.title}', '{self.url}')"


# Routes
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)


@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template("project.html", project=project)


@app.route("/resource/<int:resource_id>")
def resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return render_template("resource.html", resource=resource)


@app.route("/create_project", methods=["GET", "POST"])
def create_project():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        category = request.form["category"]
        project = Project(title=title, description=description, category=category)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_project.html")


@app.route("/create_resource/<int:project_id>", methods=["GET", "POST"])
def create_resource(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        title = request.form["title"]
        url = request.form["url"]
        resource = Resource(title=title, url=url, project=project)
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for("project", project_id=project_id))
    return render_template("create_resource.html", project=project)


# Error Handling
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STEAM Program</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/index.html -->

{% extends "base.html" %}

{% block content %}
    <h1>STEAM Projects</h1>
    <ul>
        {% for project in projects %}
            <li><a href="{{ url_for('project', project_id=project.id) }}">{{ project.title }}</a></li>
        {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/project.html -->

{% extends "base.html" %}

{% block content %}
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <h2>Resources:</h2>
    <ul>
        {% for resource in project.resources %}
            <li><a href="{{ resource.url }}">{{ resource.title }}</a></li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_resource', project_id=project.id) }}">Add Resource</a></p>
{% endblock %}
```

```html
<!-- templates/create_project.html -->

{% extends "base.html" %}

{% block content %}
    <h1>Create Project</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="category">Category:</label>
        <input type="text" id="category" name="category"><br><br>
        <input type="submit" value="Create">
    </form>
{% endblock %}
```

```html
<!-- templates/create_resource.html -->

{% extends "base.html" %}

{% block content %}
    <h1>Create Resource for {{ project.title }}</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="url">URL:</label>
        <input type="text" id="url" name="url"><br><br>
        <input type="submit" value="Create">
    </form>
{% endblock %}
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #337ab7;
}

main {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```
