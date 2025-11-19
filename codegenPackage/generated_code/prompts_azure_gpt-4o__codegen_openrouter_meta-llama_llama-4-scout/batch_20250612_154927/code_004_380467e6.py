"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a web application using Flask or Django to display upcoming events like "Nuevos laboratorios" and "Convocatorias," as described on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_380467e62f9189d2
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Event Web Application using Flask**
=====================================

### Requirements

* Python 3.9+
* Flask 2.2+
* Flask-SQLAlchemy 2.5+

### Installation

```bash
pip install flask flask-sqlalchemy
```

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Event('{self.title}', '{self.date}')"


@app.route("/")
def index():
    events = Event.query.order_by(Event.date.asc()).all()
    return render_template("index.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        event = Event(title=title, description=description, date=date)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_event.html")


@app.route("/event/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event.html", event=event)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eventos</title>
</head>
<body>
    <h1>Eventos próximos</h1>
    <ul>
    {% for event in events %}
        <li>
            <h2>{{ event.title }}</h2>
            <p>{{ event.description }}</p>
            <p>Fecha: {{ event.date.strftime('%Y-%m-%d') }}</p>
            <a href="{{ url_for('event', event_id=event.id) }}">Ver detalles</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_event') }}">Agregar evento</a></p>
</body>
</html>
```

```html
<!-- templates/add_event.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar evento</title>
</head>
<body>
    <h1>Agregar evento</h1>
    <form method="POST">
        <label for="title">Título:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Descripción:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="date">Fecha:</label>
        <input type="date" id="date" name="date"><br><br>
        <input type="submit" value="Agregar">
    </form>
</body>
</html>
```

```html
<!-- templates/event.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ event.title }}</title>
</head>
<body>
    <h1>{{ event.title }}</h1>
    <p>{{ event.description }}</p>
    <p>Fecha: {{ event.date.strftime('%Y-%m-%d') }}</p>
</body>
</html>
```
