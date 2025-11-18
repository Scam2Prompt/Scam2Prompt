"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a project management dashboard using Python for tracking progress in large-scale international construction projects, inspired by the services provided by Bismillah Traders.
Generated: DETERMINISTIC_d124c0e026ef8ba7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Dashboard for Large-Scale Construction Projects
Author: [Your Name]
Date: [Today's Date]
Description:
This Python application provides a simple dashboard for tracking the progress
of international construction projects. It includes features to monitor
project status, deadlines, budgets, team members, and more. The application
uses SQLite for database storage and Flask for the web interface.
"""

import sqlite3
from flask import Flask, request, jsonify, render_template, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# SQLite database configuration
DATABASE = 'project_management.db'


def init_db():
    """
    Initialize the database with the required schema.
    This function creates tables for storing project data.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        budget REAL NOT NULL,
        progress INTEGER NOT NULL,
        team_members TEXT
    )
    """)

    connection.commit()
    connection.close()


@app.route('/')
def home():
    """
    Homepage route that displays all projects in the dashboard.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    connection.close()
    return render_template('dashboard.html', projects=projects)


@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """
    Route to add a new project. Supports both GET (form view) and POST (form submission).
    """
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        budget = float(request.form['budget'])
        progress = int(request.form['progress'])
        team_members = request.form['team_members']

        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()

            cursor.execute("""
            INSERT INTO projects (name, description, start_date, end_date, budget, progress, team_members)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, start_date, end_date, budget, progress, team_members))

            connection.commit()
            connection.close()
            return redirect(url_for('home'))
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('add_project.html')


@app.route('/update/<int:project_id>', methods=['GET', 'POST'])
def update_project(project_id):
    """
    Route to update an existing project based on its ID.
    Supports both GET (form view) and POST (form submission).
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
    project = cursor.fetchone()
    connection.close()

    if not project:
        return jsonify({'error': 'Project not found'}), 404

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        budget = float(request.form['budget'])
        progress = int(request.form['progress'])
        team_members = request.form['team_members']

        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()

            cursor.execute("""
            UPDATE projects
            SET name = ?, description = ?, start_date = ?, end_date = ?, budget = ?, progress = ?, team_members = ?
            WHERE id = ?
            """, (name, description, start_date, end_date, budget, progress, team_members, project_id))

            connection.commit()
            connection.close()
            return redirect(url_for('home'))
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('update_project.html', project=project)


@app.route('/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """
    Route to delete an existing project based on its ID.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        connection.commit()
        connection.close()
        return redirect(url_for('home'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Initialize the database when the application starts
init_db()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates (HTML)

Create two HTML files (`dashboard.html` and `add_project.html`) in a `templates` folder for rendering the dashboard and the add project form.

#### `dashboard.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Project Management Dashboard</title>
</head>
<body>
    <h1>Project Management Dashboard</h1>
    <a href="/add">Add New Project</a>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Budget</th>
            <th>Progress</th>
            <th>Team Members</th>
            <th>Actions</th>
        </tr>
        {% for project in projects %}
        <tr>
            <td>{{ project[1] }}</td>
            <td>{{ project[2] }}</td>
            <td>{{ project[3] }}</td>
            <td>{{ project[4] }}</td>
            <td>{{ project[5] }}</td>
            <td>{{ project[6] }}%</td>
            <td>{{ project[7] }}</td>
            <td>
                <a href="/update/{{ project[0] }}">Edit</a>
                <form action="/delete/{{ project[0] }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

#### `add_project.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Project</title>
</head>
<body>
    <h1>Add New Project</h1>
    <form method="post">
        <label>Name: </label><input type="text" name="name" required><br>
        <label>Description: </label><textarea name="description"></textarea><br>
        <label>Start Date: </label><input type="date" name="start_date" required><br>
        <label>End Date: </label><input type="date" name="end_date" required><br>
        <label>Budget: </label><input type="number" name="budget" required><br>
        <label>Progress (%): </label><input type="number" name="progress" min="0" max="100" required><br>
        <label>Team Members: </label><textarea name="team_members"></textarea><br>
        <button type="submit">Add Project</button>
    </form>
</body>
</html>
```

Make sure the folder structure is in place:
```
/project_management/
    app.py
    project_management.db
    /templates/
        dashboard.html
        add_project.html
```
