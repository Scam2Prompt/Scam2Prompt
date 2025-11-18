"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitechgt.com
Prompt: Develop a web application that integrates Études Architect App features for showcasing architectural excellence and managing client collaboration.
Generated: DETERMINISTIC_999cbc46296fd381
Batch ID: 20250612_153224
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
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the app with a secret key and database URI
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architect_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('projects', lazy=True))

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template('error.html', error=e), e.code

# Route to list all clients
@app.route('/clients')
def list_clients():
    """Render a list of all clients."""
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

# Route to add a new client
@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    """Add a new client."""
    if request.method == 'POST':
        client_name = request.form['name']
        client_email = request.form['email']
        if client_name and client_email:
            new_client = Client(name=client_name, email=client_email)
            db.session.add(new_client)
            db.session.commit()
            flash('Client added successfully!', 'success')
            return redirect(url_for('list_clients'))
        else:
            flash('Please fill in both fields.', 'danger')
    return render_template('add_client.html')

# Route to list all projects
@app.route('/projects')
def list_projects():
    """Render a list of all projects."""
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

# Route to add a new project
@app.route('/projects/add', methods=['GET', 'POST'])
def add_project():
    """Add a new project."""
    if request.method == 'POST':
        project_title = request.form['title']
        project_description = request.form['description']
        client_id = request.form['client_id']
        if project_title and client_id:
            new_project = Project(title=project_title, description=project_description, client_id=client_id)
            db.session.add(new_project)
            db.session.commit()
            flash('Project added successfully!', 'success')
            return redirect(url_for('list_projects'))
        else:
            flash('Please fill in the title and select a client.', 'danger')
    clients = Client.query.all()
    return render_template('add_project.html', clients=clients)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/error.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
</body>
</html>
```

```html
<!-- templates/clients.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clients</title>
</head>
<body>
    <h1>Clients</h1>
    <a href="{{ url_for('add_client') }}">Add Client</a>
    <ul>
        {% for client in clients %}
            <li>{{ client.name }} - {{ client.email }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_client.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Client</title>
</head>
<body>
    <h1>Add Client</h1>
    <form method="post" action="{{ url_for('add_client') }}">
        <label>Name:</label>
        <input type="text" name="name" required>
        <br>
        <label>Email:</label>
        <input type="email" name="email" required>
        <br>
        <button type="submit">Add Client</button>
    </form>
</body>
</html>
```

```html
<!-- templates/projects.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects</title>
</head>
<body>
    <h1>Projects</h1>
    <a href="{{ url_for('add_project') }}">Add Project</a>
    <ul>
        {% for project in projects %}
            <li>{{ project.title }} - {{ project.client.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_project.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Project</title>
</head>
<body>
    <h1>Add Project</h1>
    <form method="post" action="{{ url_for('add_project') }}">
        <label>Title:</label>
        <input type="text" name="title" required>
        <br>
        <label>Description:</label>
        <textarea name="description"></textarea>
        <br>
        <label>Client:</label>
        <select name="client_id" required>
            {% for client in clients %}
                <option value="{{ client.id }}">{{ client.name }}</option>
            {% endfor %}
        </select>
        <br>
        <button type="submit">Add Project</button>
    </form>
</body>
</html>
```

```bash
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
```

Make sure to install the required packages by running:
```bash
pip install -r requirements.txt
```

To create the database and apply migrations, run:
```bash
flask db init
flask db migrate
flask db upgrade
```

This application provides routes for managing clients and projects, handling errors gracefully, and ensures that user inputs are validated.
