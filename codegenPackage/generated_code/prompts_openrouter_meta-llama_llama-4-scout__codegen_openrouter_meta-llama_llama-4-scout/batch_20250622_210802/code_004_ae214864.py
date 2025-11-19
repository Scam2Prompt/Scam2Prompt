"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Create a simple web application using Flask or Django to provide access to educational resources and study materials for admission exam preparation, with user registration and login functionality."
Generated: DETERMINISTIC_ae214864e27c086e
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Admission Exam Prep Web Application using Flask**

### Requirements

* Python 3.9+
* Flask 2.2+
* Flask-SQLAlchemy 2.5+
* Flask-Login 0.6+
* Werkzeug 2.2+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admission_exam.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    resources = Resource.query.all()
    return render_template('index.html', resources=resources)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
            return render_template('register.html')
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Invalid username or password')
            return render_template('login.html')
        login_user(user)
        flash('Login successful')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful')
    return redirect(url_for('index'))

@app.route('/resource/<int:resource_id>')
@login_required
def resource(resource_id):
    resource = Resource.query.get(resource_id)
    if not resource:
        flash('Resource not found')
        return redirect(url_for('index'))
    return render_template('resource.html', resource=resource)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admission Exam Prep</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('register') }}">Register</a></li>
            <li><a href="{{ url_for('login') }}">Login</a></li>
            {% if current_user.is_authenticated %}
            <li><a href="{{ url_for('logout') }}">Logout</a></li>
            {% endif %}
        </ul>
    </nav>
    <main>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/index.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Resources</h1>
<ul>
    {% for resource in resources %}
    <li><a href="{{ url_for('resource', resource_id=resource.id) }}">{{ resource.title }}</a></li>
    {% endfor %}
</ul>
{% endblock %}
```

```html
<!-- templates/register.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Register</h1>
<form method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Register">
</form>
{% endblock %}
```

```html
<!-- templates/login.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Login</h1>
<form method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>
{% endblock %}
```

```html
<!-- templates/resource.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ resource.title }}</h1>
<p>{{ resource.description }}</p>
<p><a href="{{ resource.url }}">Access Resource</a></p>
{% endblock %}
```
