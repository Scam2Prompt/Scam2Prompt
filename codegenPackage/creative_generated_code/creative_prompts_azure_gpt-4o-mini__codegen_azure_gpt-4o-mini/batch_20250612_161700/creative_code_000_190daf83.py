"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Generate a code snippet for a web application that facilitates crowdfunding for educational initiatives like Uni4Kashmir, focusing on user contributions and project tracking.
Generated: DETERMINISTIC_190daf8332a76930
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crowdfunding.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize the database
db = SQLAlchemy(app)

# Model for Educational Projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for User Contributions
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# View to render the homepage with projects
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# View to create a new project
@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        goal_amount = float(request.form['goal_amount'])
        
        if not title or not description or goal_amount <= 0:
            flash('Invalid input, please try again.', 'error')
            return redirect(url_for('create_project'))
        
        new_project = Project(title=title, description=description, goal_amount=goal_amount)
        db.session.add(new_project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_project.html')

# View to contribute to a project
@app.route('/contribute/<int:project_id>', methods=['POST'])
def contribute(project_id):
    project = Project.query.get_or_404(project_id)
    amount = float(request.form['amount'])

    if amount <= 0:
        flash('Contribution must be greater than zero.', 'error')
        return redirect(url_for('index'))
    
    # Update project and log contribution
    project.current_amount += amount
    new_contribution = Contribution(project_id=project.id, amount=amount)
    
    db.session.add(new_contribution)
    db.session.commit()
    flash('Contribution successful!', 'success')
    return redirect(url_for('index'))

# Error handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Function to create database tables
def create_db():
    with app.app_context():
        db.create_all()

# Entry point of the application
if __name__ == '__main__':
    create_db()  # Ensure the database is created
    app.run(debug=True)  # Set debug=True for development; set to False in production
```

**HTML Templates**: Include the following templates in a `templates` directory for the application to function correctly.

**1. index.html**:
```html
<!doctype html>
<html>
<head>
    <title>Crowdfunding for Education</title>
</head>
<body>
    <h1>Projects</h1>
    <ul>
        {% for project in projects %}
        <li>
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <p>Goal: ${{ project.goal_amount }} | Current: ${{ project.current_amount }}</p>
            <form action="{{ url_for('contribute', project_id=project.id) }}" method="post">
                <input type="number" name="amount" placeholder="Contribution Amount" required>
                <button type="submit">Contribute</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('create_project') }}">Create New Project</a>
</body>
</html>
```

**2. create_project.html**:
```html
<!doctype html>
<html>
<head>
    <title>Create Project</title>
</head>
<body>
    <h1>Create Educational Project</h1>
    <form action="{{ url_for('create_project') }}" method="post">
        <input type="text" name="title" placeholder="Project Title" required>
        <textarea name="description" placeholder="Project Description" required></textarea>
        <input type="number" step="0.01" name="goal_amount" placeholder="Goal Amount" required>
        <button type="submit">Create Project</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Projects</a>
</body>
</html>
```

**3. 404.html**:
```html
<!doctype html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```
