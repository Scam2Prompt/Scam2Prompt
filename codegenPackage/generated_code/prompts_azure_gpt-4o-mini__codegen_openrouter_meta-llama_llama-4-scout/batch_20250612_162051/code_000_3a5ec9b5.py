"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Write a code snippet for a web application that allows parents to enroll their children in a daycare program like Kiddoo Playway, focusing on features such as activity-based curriculum and parental webinars.
Generated: DETERMINISTIC_3a5ec9b501a1361a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daycare.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10), nullable=False, default='parent')
    children = db.relationship('Child', backref='parent', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    enrolled = db.Column(db.Boolean, nullable=False, default=False)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Webinar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/enroll_child', methods=['GET', 'POST'])
@login_required
def enroll_child():
    if request.method == 'POST':
        child_name = request.form['child_name']
        child_age = request.form['child_age']
        child = Child(name=child_name, age=child_age, parent_id=current_user.id)
        db.session.add(child)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('enroll_child.html')

@app.route('/view_activities')
@login_required
def view_activities():
    activities = Activity.query.all()
    return render_template('view_activities.html', activities=activities)

@app.route('/view_webinars')
@login_required
def view_webinars():
    webinars = Webinar.query.all()
    return render_template('view_webinars.html', webinars=webinars)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Daycare App</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('login') }}">Login</a></li>
            <li><a href="{{ url_for('logout') }}">Logout</a></li>
        </ul>
    </nav>
    <div class="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to Daycare App</h1>
{% endblock %}
```

```html
<!-- templates/login.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
{% endblock %}
```

```html
<!-- templates/dashboard.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Dashboard</h1>
    <p>Welcome, {{ current_user.username }}!</p>
    <ul>
        <li><a href="{{ url_for('enroll_child') }}">Enroll Child</a></li>
        <li><a href="{{ url_for('view_activities') }}">View Activities</a></li>
        <li><a href="{{ url_for('view_webinars') }}">View Webinars</a></li>
    </ul>
{% endblock %}
```

```html
<!-- templates/enroll_child.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Enroll Child</h1>
    <form method="POST">
        <label for="child_name">Child Name:</label>
        <input type="text" id="child_name" name="child_name"><br><br>
        <label for="child_age">Child Age:</label>
        <input type="number" id="child_age" name="child_age"><br><br>
        <input type="submit" value="Enroll">
    </form>
{% endblock %}
```

```html
<!-- templates/view_activities.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Activities</h1>
    <ul>
    {% for activity in activities %}
        <li>{{ activity.name }} - {{ activity.description }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/view_webinars.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Webinars</h1>
    <ul>
    {% for webinar in webinars %}
        <li>{{ webinar.title }} - {{ webinar.description }} - {{ webinar.date }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```
