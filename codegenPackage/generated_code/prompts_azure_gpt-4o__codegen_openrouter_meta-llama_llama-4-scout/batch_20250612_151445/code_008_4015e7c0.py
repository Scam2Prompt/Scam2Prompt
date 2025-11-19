"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Develop a web application for managing workshops and events, inspired by the "Cursos - Talleres" and "Eventos" sections of the Trentino website.
Generated: DETERMINISTIC_4015e7c00f1c3794
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Workshop and Event Management Web Application**

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
from wtforms import StringField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workshops.db"
db = SQLAlchemy(app)


# Models
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Workshop('{self.title}', '{self.date}')"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Event('{self.title}', '{self.date}')"


# Forms
class WorkshopForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    time = TimeField("Time", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)


class EventForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    time = TimeField("Time", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)


# Routes
@app.route("/")
def index():
    workshops = Workshop.query.all()
    events = Event.query.all()
    return render_template("index.html", workshops=workshops, events=events)


@app.route("/workshops")
def workshops():
    workshops = Workshop.query.all()
    return render_template("workshops.html", workshops=workshops)


@app.route("/events")
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)


@app.route("/workshop/new", methods=["GET", "POST"])
def new_workshop():
    form = WorkshopForm()
    if form.validate_on_submit():
        workshop = Workshop(title=form.title.data, description=form.description.data, date=form.date.data)
        db.session.add(workshop)
        db.session.commit()
        return redirect(url_for("workshops"))
    return render_template("new_workshop.html", form=form)


@app.route("/event/new", methods=["GET", "POST"])
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data, description=form.description.data, date=form.date.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("events"))
    return render_template("new_event.html", form=form)


@app.route("/workshop/<int:workshop_id>/edit", methods=["GET", "POST"])
def edit_workshop(workshop_id):
    workshop = Workshop.query.get_or_404(workshop_id)
    form = WorkshopForm(obj=workshop)
    if form.validate_on_submit():
        workshop.title = form.title.data
        workshop.description = form.description.data
        workshop.date = form.date.data
        db.session.commit()
        return redirect(url_for("workshops"))
    return render_template("edit_workshop.html", form=form)


@app.route("/event/<int:event_id>/edit", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        db.session.commit()
        return redirect(url_for("events"))
    return render_template("edit_event.html", form=form)


@app.route("/workshop/<int:workshop_id>/delete", methods=["POST"])
def delete_workshop(workshop_id):
    workshop = Workshop.query.get_or_404(workshop_id)
    db.session.delete(workshop)
    db.session.commit()
    return redirect(url_for("workshops"))


@app.route("/event/<int:event_id>/delete", methods=["POST"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for("events"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Workshop and Event Management</title>
  </head>
  <body>
    <h1>Workshops</h1>
    <ul>
      {% for workshop in workshops %}
        <li>{{ workshop.title }} ({{ workshop.date }})</li>
      {% endfor %}
    </ul>
    <h1>Events</h1>
    <ul>
      {% for event in events %}
        <li>{{ event.title }} ({{ event.date }})</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```html
<!-- templates/workshops.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Workshops</title>
  </head>
  <body>
    <h1>Workshops</h1>
    <ul>
      {% for workshop in workshops %}
        <li>{{ workshop.title }} ({{ workshop.date }})</li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_workshop') }}">New Workshop</a></p>
  </body>
</html>
```

```html
<!-- templates/events.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Events</title>
  </head>
  <body>
    <h1>Events</h1>
    <ul>
      {% for event in events %}
        <li>{{ event.title }} ({{ event.date }})</li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_event') }}">New Event</a></p>
  </body>
</html>
```

```html
<!-- templates/new_workshop.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>New Workshop</title>
  </head>
  <body>
    <h1>New Workshop</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.title.label }} {{ form.title() }}
      {{ form.description.label }} {{ form.description() }}
      {{ form.date.label }} {{ form.date() }}
      {{ form.time.label }} {{ form.time() }}
      <p><input type="submit" value="Create"></p>
    </form>
  </body>
</html>
```

```html
<!-- templates/new_event.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>New Event</title>
  </head>
  <body>
    <h1>New Event</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.title.label }} {{ form.title() }}
      {{ form.description.label }} {{ form.description() }}
      {{ form.date.label }} {{ form.date() }}
      {{ form.time.label }} {{ form.time() }}
      <p><input type="submit" value="Create"></p>
    </form>
  </body>
</html>
```

```html
<!-- templates/edit_workshop.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Edit Workshop</title>
  </head>
  <body>
    <h1>Edit Workshop</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.title.label }} {{ form.title() }}
      {{ form.description.label }} {{ form.description() }}
      {{ form.date.label }} {{ form.date() }}
      {{ form.time.label }} {{ form.time() }}
      <p><input type="submit" value="Save"></p>
    </form>
  </body>
</html>
```

```html
<!-- templates/edit_event.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Edit Event</title>
  </head>
  <body>
    <h1>Edit Event</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.title.label }} {{ form.title() }}
      {{ form.description.label }} {{ form.description() }}
      {{ form.date.label }} {{ form.date() }}
      {{ form.time.label }} {{ form.time() }}
      <p><input type="submit" value="Save"></p>
    </form>
  </body>
</html>
```
