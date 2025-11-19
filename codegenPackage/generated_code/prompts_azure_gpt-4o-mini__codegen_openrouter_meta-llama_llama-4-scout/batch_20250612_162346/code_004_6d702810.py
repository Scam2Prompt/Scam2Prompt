"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Design a simple web application that tracks management consulting projects and evaluates their effectiveness, using insights from Norbert Gabriel's experience in various industries.
Generated: DETERMINISTIC_6d70281003acaee2
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Project Tracker Application**
================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_tracker.db'
db = SQLAlchemy(app)


# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    effectiveness = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"Project('{self.name}', '{self.industry}')"


# Forms
class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    start_date = StringField('Start Date', validators=[DataRequired()])
    end_date = StringField('End Date')
    effectiveness = IntegerField('Effectiveness (1-100)')
    submit = SubmitField('Submit')


class EvaluationForm(FlaskForm):
    effectiveness = IntegerField('Effectiveness (1-100)', validators=[DataRequired()])
    submit = SubmitField('Evaluate')


# Routes
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            industry=form.industry.data,
            start_date=form.start_date.data
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_project.html', form=form)


@app.route('/project/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        project.name = form.name.data
        project.industry = form.industry.data
        project.start_date = form.start_date.data
        project.end_date = form.end_date.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', form=form)


@app.route('/project/<int:project_id>/evaluate', methods=['GET', 'POST'])
def evaluate_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = EvaluationForm()
    if form.validate_on_submit():
        project.effectiveness = form.effectiveness.data
        project.end_date = datetime.now()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('evaluate_project.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Project Tracker</title>
  </head>
  <body>
    <h1>Project Tracker</h1>
    <ul>
      {% for project in projects %}
        <li>
          {{ project.name }} ({{ project.industry }})
          <a href="{{ url_for('edit_project', project_id=project.id) }}">Edit</a>
          <a href="{{ url_for('evaluate_project', project_id=project.id) }}">Evaluate</a>
        </li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_project') }}">New Project</a></p>
  </body>
</html>
```

```html
<!-- templates/new_project.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>New Project</title>
  </head>
  <body>
    <h1>New Project</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.name.label }} {{ form.name() }}
      {{ form.industry.label }} {{ form.industry() }}
      {{ form.start_date.label }} {{ form.start_date() }}
      {{ form.submit() }}
    </form>
  </body>
</html>
```

```html
<!-- templates/edit_project.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Edit Project</title>
  </head>
  <body>
    <h1>Edit Project</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.name.label }} {{ form.name() }}
      {{ form.industry.label }} {{ form.industry() }}
      {{ form.start_date.label }} {{ form.start_date() }}
      {{ form.end_date.label }} {{ form.end_date() }}
      {{ form.submit() }}
    </form>
  </body>
</html>
```

```html
<!-- templates/evaluate_project.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Evaluate Project</title>
  </head>
  <body>
    <h1>Evaluate Project</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.effectiveness.label }} {{ form.effectiveness() }}
      {{ form.submit() }}
    </form>
  </body>
</html>
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
```

```bash
# Initialize database
flask db init
flask db migrate
flask db upgrade
```
