"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ng-mc.de
Prompt: Design a simple web application that tracks management consulting projects and evaluates their effectiveness, using insights from Norbert Gabriel's experience in various industries.
Generated: DETERMINISTIC_6d70281003acaee2
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    effectiveness_score = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Project {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a new project
@app.route('/add_project', methods=['POST'])
def add_project():
    try:
        data = request.json
        new_project = Project(
            name=data['name'],
            industry=data['industry'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d') if 'end_date' in data else None,
            effectiveness_score=data.get('effectiveness_score', None)
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([{
            'id': project.id,
            'name': project.name,
            'industry': project.industry,
            'start_date': project.start_date.strftime('%Y-%m-%d'),
            'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
            'effectiveness_score': project.effectiveness_score
        } for project in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to evaluate project effectiveness
@app.route('/evaluate/<int:project_id>', methods=['POST'])
def evaluate_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        data = request.json
        project.effectiveness_score = data['effectiveness_score']
        db.session.commit()
        return jsonify({'message': 'Project evaluated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Start the application
if __name__ == '__main__':
    app.run(debug=True)

# Sample HTML for index.html (should be placed in a 'templates' directory)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulting Projects Tracker</title>
</head>
<body>
    <h1>Management Consulting Projects Tracker</h1>
    <form id="projectForm">
        <input type="text" name="name" placeholder="Project Name" required>
        <input type="text" name="industry" placeholder="Industry" required>
        <input type="date" name="start_date" required>
        <input type="date" name="end_date">
        <input type="number" name="effectiveness_score" placeholder="Effectiveness Score">
        <button type="submit">Add Project</button>
    </form>
    <div id="projectsList"></div>
    <script>
        document.getElementById('projectForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const response = await fetch('/add_project', {
                method: 'POST',
                body: JSON.stringify({
                    name: formData.get('name'),
                    industry: formData.get('industry'),
                    start_date: formData.get('start_date'),
                    end_date: formData.get('end_date'),
                    effectiveness_score: formData.get('effectiveness_score')
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const result = await response.json();
            alert(result.message || result.error);
        };
    </script>
</body>
</html>
'''
```
