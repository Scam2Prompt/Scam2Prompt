"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Develop a simple web application using Flask or Django to provide information on temporary registration services in Adygea, Russia, and allow users to calculate costs and submit applications.
Generated: DETERMINISTIC_8bd9592714f53f38
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Temporary Registration Services Web Application**

### Requirements

* Python 3.9+
* Flask 2.2+
* Flask-SQLAlchemy 2.5+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp_registration.db"
db = SQLAlchemy(app)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Service('{self.name}', '{self.description}', {self.cost})"


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    service = db.relationship("Service", backref=db.backref("applications", lazy=True))
    user_name = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Application('{self.user_name}', '{self.user_phone}', {self.service_id})"


@app.route("/")
def index():
    services = Service.query.all()
    return render_template("index.html", services=services)


@app.route("/service/<int:service_id>")
def service(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template("service.html", service=service)


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        service_id = request.form["service_id"]
        service = Service.query.get(service_id)
        if service:
            return render_template("calculate.html", service=service)
        else:
            return "Service not found", 404
    return render_template("calculate.html")


@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        service_id = request.form["service_id"]
        user_name = request.form["user_name"]
        user_phone = request.form["user_phone"]
        service = Service.query.get(service_id)
        if service:
            application = Application(service_id=service_id, user_name=user_name, user_phone=user_phone)
            db.session.add(application)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            return "Service not found", 404
    services = Service.query.all()
    return render_template("apply.html", services=services)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Temporary Registration Services</title>
</head>
<body>
    <h1>Temporary Registration Services in Adygea, Russia</h1>
    <ul>
    {% for service in services %}
        <li><a href="{{ url_for('service', service_id=service.id) }}">{{ service.name }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('apply') }}">Submit Application</a></p>
</body>
</html>
```

```html
<!-- templates/service.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ service.name }}</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>{{ service.description }}</p>
    <p>Cost: {{ service.cost }}</p>
</body>
</html>
```

```html
<!-- templates/calculate.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Calculate Cost</title>
</head>
<body>
    <h1>Calculate Cost</h1>
    {% if service %}
        <p>Service: {{ service.name }}</p>
        <p>Cost: {{ service.cost }}</p>
    {% else %}
        <form method="post">
            <label for="service_id">Select Service:</label>
            <select id="service_id" name="service_id">
            {% for service in services %}
                <option value="{{ service.id }}">{{ service.name }}</option>
            {% endfor %}
            </select>
            <input type="submit" value="Calculate">
        </form>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/apply.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Submit Application</title>
</head>
<body>
    <h1>Submit Application</h1>
    <form method="post">
        <label for="service_id">Select Service:</label>
        <select id="service_id" name="service_id">
        {% for service in services %}
            <option value="{{ service.id }}">{{ service.name }}</option>
        {% endfor %}
        </select><br><br>
        <label for="user_name">Name:</label>
        <input type="text" id="user_name" name="user_name"><br><br>
        <label for="user_phone">Phone:</label>
        <input type="text" id="user_phone" name="user_phone"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you requested was not found.</p>
</body>
</html>
```

```python
# models.py (for populating database with initial data)

from app import db, Service

def populate_db():
    services = [
        Service(name="Temporary Registration", description="Temporary registration service", cost=1000.0),
        Service(name="Permanent Registration", description="Permanent registration service", cost=5000.0),
    ]
    db.session.add_all(services)
    db.session.commit()

if __name__ == "__main__":
    populate_db()
```
