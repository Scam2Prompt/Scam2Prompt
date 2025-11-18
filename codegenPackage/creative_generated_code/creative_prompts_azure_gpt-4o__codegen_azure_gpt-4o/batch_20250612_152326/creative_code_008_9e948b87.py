"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Create a web application using Flask or Django for a company like Sadad Engineering to showcase their completed and ongoing projects, including filtering options by project type and status.
Generated: DETERMINISTIC_9e948b87ea4fe404
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask Web Application for Sadad Engineering Projects

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model: Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    project_type = db.Column(db.String(50), nullable=False)  # Example: 'Residential', 'Commercial'
    status = db.Column(db.String(50), nullable=False)        # Example: 'Completed', 'Ongoing'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'project_type': self.project_type,
            'status': self.status
        }


# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Route: Display Projects with Filtering Options
@app.route('/projects')
def projects():
    try:
        project_type = request.args.get('type')
        status = request.args.get('status')

        # Query filtering based on project type and status
        query = Project.query
        if project_type:
            query = query.filter_by(project_type=project_type)
        if status:
            query = query.filter_by(status=status)

        projects = query.all()
        return render_template('projects.html', projects=projects)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route: Add a Project (For Admin Use)
@app.route('/add_project', methods=['POST'])
def add_project():
    try:
        data = request.json
        new_project = Project(
            name=data['name'],
            description=data['description'],
            project_type=data['project_type'],
            status=data['status']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route: API to get project details (Optional for integrations)
@app.route('/api/projects', methods=['GET'])
def api_projects():
    try:
        project_type = request.args.get('type')
        status = request.args.get('status')

        query = Project.query
        if project_type:
            query = query.filter_by(project_type=project_type)
        if status:
            query = query.filter_by(status=status)

        projects = query.all()
        return jsonify([project.to_dict() for project in projects])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Initialize the database
@app.before_first_request
def setup_db():
    db.create_all()


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (Place in `templates` folder)

#### `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Sadad Engineering Projects</title>
</head>
<body>
    <h1>Welcome to Sadad Engineering</h1>
    <p>Explore our projects!</p>
    <a href="/projects">View Projects</a>
</body>
</html>
```

#### `projects.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Projects - Sadad Engineering</title>
</head>
<body>
    <h1>Projects</h1>

    <form method="GET" action="/projects">
        <label for="type">Filter by Type:</label>
        <select name="type" id="type">
            <option value="">All</option>
            <option value="Residential">Residential</option>
            <option value="Commercial">Commercial</option>
        </select>

        <label for="status">Filter by Status:</label>
        <select name="status" id="status">
            <option value="">All</option>
            <option value="Completed">Completed</option>
            <option value="Ongoing">Ongoing</option>
        </select>

        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for project in projects %}
            <li>
                <strong>{{ project.name }}</strong> - {{ project.project_type }} - {{ project.status }}
                <p>{{ project.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes
1. Install dependencies using `pip install flask flask_sqlalchemy`.
2. Create the database (`projects.db`) by running the app once.
3. You can extend the admin functionality (e.g., creating a separate UI for adding projects).
