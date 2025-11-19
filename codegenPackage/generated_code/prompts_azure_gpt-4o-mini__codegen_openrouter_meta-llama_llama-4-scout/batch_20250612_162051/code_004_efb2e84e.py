"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Design a simple web application that uses SCOUT's technical documentation to help users select the right attachments for their tractors based on the tasks they plan to perform.
Generated: DETERMINISTIC_efb2e84ec6599c46
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Tractor Attachment Selector Web Application**
=====================================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database operations

**Code:**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tractor_attachments.db"
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Task('{self.name}')"

# Define Attachment model
class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tasks = db.relationship('TaskAttachment', backref='attachment', lazy=True)

    def __repr__(self):
        return f"Attachment('{self.name}')"

# Define Task-Attachment association model
class TaskAttachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    task = db.relationship('Task', backref='attachments', lazy=True)
    attachment_id = db.Column(db.Integer, db.ForeignKey('attachment.id'), nullable=False)

    def __repr__(self):
        return f"TaskAttachment('{self.task_id}', '{self.attachment_id}')"

# Create database tables
with app.app_context():
    db.create_all()

# Route for index page
@app.route("/")
def index():
    tasks = Task.query.all()
    attachments = Attachment.query.all()
    return render_template("index.html", tasks=tasks, attachments=attachments)

# Route for selecting attachments based on tasks
@app.route("/select_attachments", methods=["POST"])
def select_attachments():
    try:
        task_ids = request.form.getlist("tasks")
        attachments = []
        for task_id in task_ids:
            task = Task.query.get(task_id)
            if task:
                attachments.extend(task.attachments)
        return render_template("attachments.html", attachments=[a.attachment for a in attachments])
    except Exception as e:
        return render_template("error.html", error=str(e))

# Route for adding new task
@app.route("/add_task", methods=["POST"])
def add_task():
    try:
        task_name = request.form["task_name"]
        task = Task(name=task_name)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))

# Route for adding new attachment
@app.route("/add_attachment", methods=["POST"])
def add_attachment():
    try:
        attachment_name = request.form["attachment_name"]
        attachment_description = request.form["attachment_description"]
        attachment = Attachment(name=attachment_name, description=attachment_description)
        db.session.add(attachment)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))

# Route for associating task and attachment
@app.route("/associate_task_attachment", methods=["POST"])
def associate_task_attachment():
    try:
        task_id = request.form["task_id"]
        attachment_id = request.form["attachment_id"]
        task_attachment = TaskAttachment(task_id=task_id, attachment_id=attachment_id)
        db.session.add(task_attachment)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Tractor Attachment Selector</title>
</head>
<body>
    <h1>Tractor Attachment Selector</h1>
    <form action="{{ url_for('select_attachments') }}" method="post">
        {% for task in tasks %}
            <input type="checkbox" name="tasks" value="{{ task.id }}">{{ task.name }}<br>
        {% endfor %}
        <input type="submit" value="Select Attachments">
    </form>
    <h2>Add Task</h2>
    <form action="{{ url_for('add_task') }}" method="post">
        <input type="text" name="task_name" placeholder="Task Name">
        <input type="submit" value="Add Task">
    </form>
    <h2>Add Attachment</h2>
    <form action="{{ url_for('add_attachment') }}" method="post">
        <input type="text" name="attachment_name" placeholder="Attachment Name">
        <textarea name="attachment_description" placeholder="Attachment Description"></textarea>
        <input type="submit" value="Add Attachment">
    </form>
    <h2>Associate Task and Attachment</h2>
    <form action="{{ url_for('associate_task_attachment') }}" method="post">
        <select name="task_id">
            {% for task in tasks %}
                <option value="{{ task.id }}">{{ task.name }}</option>
            {% endfor %}
        </select>
        <select name="attachment_id">
            {% for attachment in attachments %}
                <option value="{{ attachment.id }}">{{ attachment.name }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Associate">
    </form>
</body>
</html>
```

**templates/attachments.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Attachments</title>
</head>
<body>
    <h1>Attachments</h1>
    <ul>
        {% for attachment in attachments %}
            <li>{{ attachment.name }} - {{ attachment.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/error.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```
