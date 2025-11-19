"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Develop a web-based dashboard for tracking the impact metrics of Kibera Hamlets programs, such as the number of children fed through "Feed me a simple lunch" or the number of girls mentored in the Girls Empowerment Programme.
Generated: DETERMINISTIC_cd764f9597b78904
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Kibera Hamlets Program Dashboard**
=====================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database operations
* `flask_login` for user authentication

**Code:**
```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kibera_hamlets.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Program('{self.name}')"

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    program = db.relationship('Program', backref=db.backref('metrics', lazy=True))
    name = db.Column(db.String(128), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Metric('{self.name}', '{self.value}')"

# Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    programs = Program.query.all()
    return render_template('index.html', programs=programs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/programs/<int:program_id>')
@login_required
def program_details(program_id):
    program = Program.query.get(program_id)
    metrics = program.metrics.all()
    return render_template('program_details.html', program=program, metrics=metrics)

@app.route('/metrics/<int:metric_id>')
@login_required
def metric_details(metric_id):
    metric = Metric.query.get(metric_id)
    return render_template('metric_details.html', metric=metric)

@app.route('/add_metric', methods=['POST'])
@login_required
def add_metric():
    program_id = request.form['program_id']
    name = request.form['name']
    value = request.form['value']
    metric = Metric(program_id=program_id, name=name, value=value)
    db.session.add(metric)
    db.session.commit()
    return redirect(url_for('program_details', program_id=program_id))

@app.route('/update_metric', methods=['POST'])
@login_required
def update_metric():
    metric_id = request.form['metric_id']
    value = request.form['value']
    metric = Metric.query.get(metric_id)
    metric.value = value
    db.session.commit()
    return redirect(url_for('metric_details', metric_id=metric_id))

@app.route('/delete_metric', methods=['POST'])
@login_required
def delete_metric():
    metric_id = request.form['metric_id']
    program_id = request.form['program_id']
    metric = Metric.query.get(metric_id)
    db.session.delete(metric)
    db.session.commit()
    return redirect(url_for('program_details', program_id=program_id))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Kibera Hamlets Program Dashboard</title>
</head>
<body>
    <h1>Programs</h1>
    <ul>
    {% for program in programs %}
        <li><a href="{{ url_for('program_details', program_id=program.id) }}">{{ program.name }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('login') }}">Login</a></p>
</body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

```html
<!-- templates/program_details.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Program Details</title>
</head>
<body>
    <h1>{{ program.name }}</h1>
    <h2>Metrics</h2>
    <ul>
    {% for metric in metrics %}
        <li>{{ metric.name }}: {{ metric.value }} (<a href="{{ url_for('metric_details', metric_id=metric.id) }}">View</a> | <a href="{{ url_for('update_metric', metric_id=metric.id) }}">Update</a> | <a href="{{ url_for('delete_metric', metric_id=metric.id, program_id=program.id) }}">Delete</a>)</li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('add_metric') }}" method="POST">
        <input type="hidden" name="program_id" value="{{ program.id }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="value">Value:</label>
        <input type="text" id="value" name="value"><br><br>
        <input type="submit" value="Add Metric">
    </form>
</body>
</html>
```

```html
<!-- templates/metric_details.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Metric Details</title>
</head>
<body>
    <h1>{{ metric.name }}: {{ metric.value }}</h1>
</body>
</html>
```

```python
# create database tables
with app.app_context():
    db.create_all()
```
