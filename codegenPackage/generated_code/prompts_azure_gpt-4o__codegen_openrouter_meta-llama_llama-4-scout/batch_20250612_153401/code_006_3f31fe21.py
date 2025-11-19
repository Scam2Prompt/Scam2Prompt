"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Develop a web application feature that allows students to select and customize their study schedules, inspired by the flexible scheduling system mentioned on Educar Comitán's site.
Generated: DETERMINISTIC_3f31fe2192a4332c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Study Schedule Customizer**
==========================

### Dependencies

* Python 3.9+
* Flask 2.2.2
* Flask-SQLAlchemy 2.5.1
* Flask-WTF 1.0.1

### Code

```python
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_schedules.db'
db = SQLAlchemy(app)

class StudySchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    study_time = db.Column(db.Integer, nullable=False)
    study_day = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"StudySchedule('{self.student_name}', '{self.subject}', {self.study_time}, '{self.study_day}')"

class ScheduleForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    study_time = IntegerField('Study Time (hours)', validators=[DataRequired()])
    study_day = SelectField('Study Day', choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    submit = SubmitField('Create Schedule')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_schedule', methods=['GET', 'POST'])
def create_schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = StudySchedule(
            student_name=form.student_name.data,
            subject=form.subject.data,
            study_time=form.study_time.data,
            study_day=form.study_day.data
        )
        db.session.add(schedule)
        db.session.commit()
        return redirect(url_for('view_schedules'))
    return render_template('create_schedule.html', form=form)

@app.route('/view_schedules')
def view_schedules():
    schedules = StudySchedule.query.all()
    return render_template('view_schedules.html', schedules=schedules)

@app.route('/edit_schedule/<int:schedule_id>', methods=['GET', 'POST'])
def edit_schedule(schedule_id):
    schedule = StudySchedule.query.get_or_404(schedule_id)
    form = ScheduleForm(obj=schedule)
    if form.validate_on_submit():
        schedule.student_name = form.student_name.data
        schedule.subject = form.subject.data
        schedule.study_time = form.study_time.data
        schedule.study_day = form.study_day.data
        db.session.commit()
        return redirect(url_for('view_schedules'))
    return render_template('edit_schedule.html', form=form)

@app.route('/delete_schedule/<int:schedule_id>')
def delete_schedule(schedule_id):
    schedule = StudySchedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    return redirect(url_for('view_schedules'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Templates

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Study Schedule Customizer</title>
</head>
<body>
    <h1>Study Schedule Customizer</h1>
    <p><a href="{{ url_for('create_schedule') }}">Create Schedule</a></p>
    <p><a href="{{ url_for('view_schedules') }}">View Schedules</a></p>
</body>
</html>
```

**create_schedule.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Create Schedule</title>
</head>
<body>
    <h1>Create Schedule</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.student_name.label }} {{ form.student_name() }}
        {{ form.subject.label }} {{ form.subject() }}
        {{ form.study_time.label }} {{ form.study_time() }}
        {{ form.study_day.label }} {{ form.study_day() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**view_schedules.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>View Schedules</title>
</head>
<body>
    <h1>View Schedules</h1>
    <ul>
    {% for schedule in schedules %}
        <li>
            {{ schedule.student_name }} - {{ schedule.subject }} - {{ schedule.study_time }} hours - {{ schedule.study_day }}
            <a href="{{ url_for('edit_schedule', schedule_id=schedule.id) }}">Edit</a>
            <a href="{{ url_for('delete_schedule', schedule_id=schedule.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**edit_schedule.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Schedule</title>
</head>
<body>
    <h1>Edit Schedule</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.student_name.label }} {{ form.student_name() }}
        {{ form.subject.label }} {{ form.subject() }}
        {{ form.study_time.label }} {{ form.study_time() }}
        {{ form.study_day.label }} {{ form.study_day() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```
