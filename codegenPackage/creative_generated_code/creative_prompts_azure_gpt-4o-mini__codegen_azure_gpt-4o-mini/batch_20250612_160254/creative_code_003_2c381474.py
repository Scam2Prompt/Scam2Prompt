"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: How can I create a web application that provides online training modules for material handling equipment, based on the features of CoLa Training Services?
Generated: DETERMINISTIC_2c38147461a0d219
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///training_modules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the TrainingModule model
class TrainingModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<TrainingModule {self.title}>'

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of training modules."""
    modules = TrainingModule.query.all()
    return render_template('index.html', modules=modules)

# Route for adding a new training module
@app.route('/add', methods=['GET', 'POST'])
def add_module():
    """Handle the addition of a new training module."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        content_url = request.form['content_url']
        
        # Error handling for module creation
        try:
            new_module = TrainingModule(title=title, description=description, content_url=content_url)
            db.session.add(new_module)
            db.session.commit()
            flash('Training module added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding module: {str(e)}', 'danger')
    
    return render_template('add_module.html')

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions by returning the appropriate error message."""
    return render_template('error.html', error=e), e.code

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Training Modules</title>
</head>
<body>
    <h1>Training Modules</h1>
    <a href="{{ url_for('add_module') }}">Add New Module</a>
    <ul>
        {% for module in modules %}
            <li>{{ module.title }} - {{ module.description }} <a href="{{ module.content_url }}">View Content</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_module.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Training Module</title>
</head>
<body>
    <h1>Add New Training Module</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <label for="content_url">Content URL:</label>
        <input type="url" name="content_url" required>
        <button type="submit">Add Module</button>
    </form>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Go back</a>
</body>
</html>
```

### Instructions for Running the Application
1. Install necessary dependencies:
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Migrate
    ```
2. Set your environment variables for `SECRET_KEY` and `DATABASE_URL`.
3. Initialize the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```
4. Run the application:
    ```bash
    python app.py
    ```
