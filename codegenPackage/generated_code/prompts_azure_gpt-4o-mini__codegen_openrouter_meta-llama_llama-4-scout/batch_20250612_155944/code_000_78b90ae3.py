"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Generate a code snippet for a web application that showcases a portfolio of architectural projects similar to those featured on Linea 7's website, emphasizing user-centric design and functionality.
Generated: DETERMINISTIC_78b90ae3951f3584
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Portfolio Web Application Code Snippet**
```python
# app.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.image_url}')"

@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template("project.html", project=project)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Add contact form submission handling logic here
        return render_template("contact.html", success=True)
    return render_template("contact.html")

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
    <title>Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="projects">
            {% for project in projects %}
                <article>
                    <h2>{{ project.title }}</h2>
                    <p>{{ project.description }}</p>
                    <img src="{{ project.image_url }}" alt="{{ project.title }}">
                    <a href="{{ url_for('project', project_id=project.id) }}">View Project</a>
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
    <title>{{ project.title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="project">
            <h1>{{ project.title }}</h1>
            <p>{{ project.description }}</p>
            <img src="{{ project.image_url }}" alt="{{ project.title }}">
        </section>
    </main>
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
    <title>Contact</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="contact">
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
            {% if success %}
                <p>Message sent successfully!</p>
            {% endif %}
        </section>
    </main>
</body>
</html>
```

```css
/* static/styles.css */

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

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.projects {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.contact {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #444;
}
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
```

```bash
# Run the application
python app.py
```
