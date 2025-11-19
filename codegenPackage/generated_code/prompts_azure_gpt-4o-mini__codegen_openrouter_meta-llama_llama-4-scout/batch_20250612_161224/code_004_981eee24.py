"""
Generated Code Metadata:
========================
Original URL: https://walmartcard.top
Prompt: Describe how to create a simple web application that aggregates online shopping tips and tricks similar to those found on Walmart Card.
Generated: DETERMINISTIC_981eee24482383d8
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simple Web Application for Aggregating Online Shopping Tips and Tricks**

### Project Structure
```markdown
- app
  - __init__.py
  - models.py
  - routes.py
  - templates
    - base.html
    - index.html
    - tips.html
  - static
    - style.css
- config.py
- requirements.txt
- run.py
```

### config.py
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///tips.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### requirements.txt
```
Flask
Flask-SQLAlchemy
```

### app/__init__.py
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
```

### app/models.py
```python
from . import db

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Tip({self.title}, {self.content})'
```

### app/routes.py
```python
from flask import render_template, request, redirect, url_for
from . import db
from .models import Tip
from . import create_app

bp = create_app().blueprints

@bp.route('/')
def index():
    tips = Tip.query.all()
    return render_template('index.html', tips=tips)

@bp.route('/tips', methods=['GET', 'POST'])
def tips():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tip = Tip(title=title, content=content)
        db.session.add(tip)
        db.session.commit()
        return redirect(url_for('tips'))
    return render_template('tips.html')

@bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```

### app/templates/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Tips</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('tips') }}">Add Tip</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

### app/templates/index.html
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Shopping Tips</h1>
    <ul>
        {% for tip in tips %}
            <li>
                <h2>{{ tip.title }}</h2>
                <p>{{ tip.content }}</p>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

### app/templates/tips.html
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Add Shopping Tip</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
{% endblock %}
```

### app/static/style.css
```css
body {
    font-family: Arial, sans-serif;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

nav li {
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #337ab7;
}

main {
    max-width: 800px;
    margin: 40px auto;
}
```

### run.py
```python
from app import create_app, db

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
