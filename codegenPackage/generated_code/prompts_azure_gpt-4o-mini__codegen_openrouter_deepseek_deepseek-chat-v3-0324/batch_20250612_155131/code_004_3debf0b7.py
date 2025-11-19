"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Illustrate how to structure a web application using the file organization seen in the abelltodoit.com.au index.
Generated: DETERMINISTIC_3debf0b79369a676
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: app.py (Main application entry point)
from flask import Flask, render_template
from config import Config
from extensions import db, migrate
from models import Task
from routes import main_bp, api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

```python
# File: config.py (Configuration settings)
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```python
# File: extensions.py (Flask extensions initialization)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
```

```python
# File: models.py (Database models)
from datetime import datetime
from extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.title}>'
```

```python
# File: routes/__init__.py (Blueprint initialization)
from flask import Blueprint

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

from . import main_routes, api_routes
```

```python
# File: routes/main_routes.py (Main routes)
from flask import render_template
from models import Task
from . import main_bp

@main_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
```

```python
# File: routes/api_routes.py (API routes)
from flask import jsonify, request
from models import Task
from extensions import db
from . import api_bp

@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    } for task in tasks])

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'))
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201
```

```python
# File: templates/base.html (Base template)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Todo App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
```

```python
# File: templates/index.html (Main page template)
{% extends "base.html" %}

{% block title %}Home - Todo App{% endblock %}

{% block content %}
    <h1>Todo List</h1>
    <div id="task-list">
        {% for task in tasks %}
            <div class="task">
                <h3>{{ task.title }}</h3>
                <p>{{ task.description }}</p>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

```python
# File: static/css/main.css (Main stylesheet)
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

.task {
    border: 1px solid #ddd;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 4px;
}
```

```python
# File: static/js/main.js (Main JavaScript)
document.addEventListener('DOMContentLoaded', function() {
    console.log('App loaded');
    
    // Example of fetching tasks via API
    fetch('/api/tasks')
        .then(response => response.json())
        .then(tasks => {
            console.log('Tasks loaded:', tasks);
        });
});
```

```python
# File: requirements.txt (Dependencies)
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
python-dotenv==0.19.0
```

```python
# File: .env (Environment variables)
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

```python
# File: .gitignore
__pycache__/
*.py[cod]
*.sqlite
.env
venv/
```
