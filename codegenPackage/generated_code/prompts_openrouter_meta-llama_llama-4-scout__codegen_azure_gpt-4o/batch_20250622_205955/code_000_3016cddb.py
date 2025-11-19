"""
Generated Code Metadata:
========================
Original URL: https://coarco.org
Prompt: "Generate a code for a web portfolio that showcases art projects like 'Multitud Marica. Activación de archivos sexo-disidentes en América Latina' and 'Las Propiedades del Cine de Reempleo', including images and descriptions."
Generated: DETERMINISTIC_3016cddbcb31f6f8
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based web application for showcasing art projects in a portfolio

from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Sample data for art projects
projects = [
    {
        "title": "Multitud Marica. Activación de archivos sexo-disidentes en América Latina",
        "description": "An exploration of queer archives and activism in Latin America.",
        "image": "multitud_marica.jpg"
    },
    {
        "title": "Las Propiedades del Cine de Reempleo",
        "description": "A study of the properties and aesthetics of reused cinema.",
        "image": "cine_reempleo.jpg"
    }
]

# Route for the homepage
@app.route("/")
def home():
    """
    Render the homepage with a list of art projects.
    """
    return render_template("index.html", projects=projects)

# Route for individual project details
@app.route("/project/<int:project_id>")
def project_detail(project_id):
    """
    Render the details of a specific art project.
    :param project_id: The ID of the project to display.
    """
    if project_id < 0 or project_id >= len(projects):
        abort(404)  # Return a 404 error if the project ID is invalid
    return render_template("project.html", project=projects[project_id])

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 error page.
    """
    return render_template("404.html"), 404

# Main entry point for running the application
if __name__ == "__main__":
    # Ensure the app runs in debug mode only in development
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Art Portfolio</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Art Portfolio</h1>
    </header>
    <main>
        <section>
            <h2>Projects</h2>
            <ul>
                {% for project in projects %}
                <li>
                    <a href="/project/{{ loop.index0 }}">
                        <img src="/static/images/{{ project.image }}" alt="{{ project.title }}">
                        <h3>{{ project.title }}</h3>
                        <p>{{ project.description }}</p>
                    </a>
                </li>
                {% endfor %}
            </ul>
        </section>
    </main>
</body>
</html>
```

#### `templates/project.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.title }}</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>{{ project.title }}</h1>
    </header>
    <main>
        <section>
            <img src="/static/images/{{ project.image }}" alt="{{ project.title }}">
            <p>{{ project.description }}</p>
            <a href="/">Back to Portfolio</a>
        </section>
    </main>
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
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>Sorry, the page you are looking for does not exist.</p>
        <a href="/">Back to Portfolio</a>
    </main>
</body>
</html>
```

### Static Files

#### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
}

h1, h2, h3 {
    margin: 0.5rem 0;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin: 1rem 0;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
}

a {
    text-decoration: none;
    color: #007BFF;
}

a:hover {
    text-decoration: underline;
}
```

### Directory Structure
```
project/
├── app.py
├── static/
│   ├── images/
│   │   ├── multitud_marica.jpg
│   │   ├── cine_reempleo.jpg
│   └── styles.css
├── templates/
│   ├── index.html
│   ├── project.html
│   └── 404.html
```
