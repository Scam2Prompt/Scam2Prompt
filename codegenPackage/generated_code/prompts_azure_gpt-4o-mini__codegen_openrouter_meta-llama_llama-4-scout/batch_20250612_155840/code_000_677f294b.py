"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: Generate a code snippet for a web application that showcases construction projects, emphasizing the commitment to excellence and innovation as described by Albatros SPA.
Generated: DETERMINISTIC_677f294b9a165d6a
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///construction.db"
db = SQLAlchemy(app)


# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Project('{self.name}', '{self.description}', '{self.image_url}')"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Route for the homepage
@app.route("/")
def index():
    try:
        projects = Project.query.all()
        return render_template("index.html", projects=projects)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500


# Route for project details
@app.route("/project/<int:project_id>")
def project_details(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        return render_template("project.html", project=project)
    except Exception as e:
        return render_template("404.html", error=str(e)), 404


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Albatros SPA Construction Projects</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Albatros SPA Construction Projects</h1>
        <p>Commitment to Excellence and Innovation</p>
    </header>
    <main>
        <section class="projects">
            {% for project in projects %}
                <article>
                    <h2>{{ project.name }}</h2>
                    <p>{{ project.description }}</p>
                    <img src="{{ project.image_url }}" alt="{{ project.name }}">
                    <a href="{{ url_for('project_details', project_id=project.id) }}">View Details</a>
                </article>
            {% endfor %}
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/project.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.name }} - Albatros SPA Construction</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>{{ project.name }}</h1>
    </header>
    <main>
        <section class="project-details">
            <p>{{ project.description }}</p>
            <img src="{{ project.image_url }}" alt="{{ project.name }}">
        </section>
    </main>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header h1 {
    margin: 0;
}

.projects {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

article {
    margin: 1em;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

article h2 {
    margin-top: 0;
}

.project-details {
    padding: 1em;
}
```

```python
# requirements.txt

Flask
Flask-SQLAlchemy
```

```bash
# Run the application
# Create a new terminal and navigate to the project directory
# Run the following commands:
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python app.py
```
