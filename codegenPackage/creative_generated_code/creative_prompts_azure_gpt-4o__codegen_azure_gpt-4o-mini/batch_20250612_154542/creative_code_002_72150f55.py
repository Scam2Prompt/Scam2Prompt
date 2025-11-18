"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a project management dashboard that allows users to oversee project progress, assign priorities (low, medium, high), and manage tasks using the workflow stages (To do, In progress, Done, Backlog) mentioned on the Zapper webpage.
Generated: DETERMINISTIC_72150f557b108309
Batch ID: 20250612_154542
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# project_management_dashboard.py

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.String(10), nullable=False)  # low, medium, high
    status = db.Column(db.String(20), nullable=False)  # todo, in_progress, done, backlog
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    """
    Retrieve all tasks or create a new one.
    GET: Return a list of all tasks.
    POST: Create a new task with provided details.
    """
    if request.method == 'POST':
        # Create a new task
        data = request.json
        task = Task(
            title=data.get('title'),
            description=data.get('description'),
            priority=data.get('priority'),
            status=data.get('status')
        )
        try:
            db.session.add(task)
            db.session.commit()
            return jsonify(task.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

    # GET tasks
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def update_task(task_id):
    """
    Update or delete a task by ID.
    PUT: Update an existing task with new details.
    DELETE: Remove a task from the database.
    """
    task = Task.query.get_or_404(task_id)

    if request.method == 'PUT':
        # Update existing task
        data = request.json
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.priority = data.get('priority', task.priority)
        task.status = data.get('status', task.status)

        try:
            db.session.commit()
            return jsonify(task.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

    # DELETE task
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Management Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Project Management Dashboard</h1>
        <div id="task-container" class="mt-3"></div>
        <div class="mt-5">
            <h2>Create Task</h2>
            <form id="task-form">
                <input type="text" id="title" placeholder="Task Title" required>
                <textarea id="description" placeholder="Task Description"></textarea>
                <select id="priority">
                    <option value="low">Low</option>
                    <option value="medium">Medium</option>
                    <option value="high">High</option>
                </select>
                <select id="status">
                    <option value="todo">To Do</option>
                    <option value="in_progress">In Progress</option>
                    <option value="done">Done</option>
                    <option value="backlog">Backlog</option>
                </select>
                <button type="submit">Add Task</button>
            </form>
        </div>
    </div>
    <script>
        const taskForm = document.getElementById('task-form');
        const taskContainer = document.getElementById('task-container');

        // Fetch and display tasks
        async function fetchTasks() {
            const response = await fetch('/tasks');
            const tasks = await response.json();
            taskContainer.innerHTML = '';
            tasks.forEach(task => {
                const taskDiv = document.createElement('div');
                taskDiv.innerText = `${task.title} - ${task.status} - Priority: ${task.priority}`;
                taskContainer.appendChild(taskDiv);
            });
        }

        // Add a new task
        taskForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const data = {
                title: document.getElementById('title').value,
                description: document.getElementById('description').value,
                priority: document.getElementById('priority').value,
                status: document.getElementById('status').value,
            };
            const response = await fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            if (response.ok) {
                await fetchTasks();
                taskForm.reset();
            } else {
                alert('Error adding task');
            }
        });

        fetchTasks();  // Initial fetch
    </script>
</body>
</html>
```
