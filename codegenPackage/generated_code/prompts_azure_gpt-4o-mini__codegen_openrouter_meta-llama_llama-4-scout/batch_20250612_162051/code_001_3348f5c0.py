"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Write a code snippet for a web application that facilitates conflict resolution workshops in Igbo communities, inspired by the initiatives of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_3348f5c0f81dbb71
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# conflict_resolution_workshop.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conflict_resolution.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False, default='participant')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

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
            return redirect(url_for('workshops'))
    return render_template('login.html')

@app.route('/workshops')
@login_required
def workshops():
    workshops = [
        {'id': 1, 'name': 'Conflict Resolution Workshop 1', 'description': 'This is a workshop'},
        {'id': 2, 'name': 'Conflict Resolution Workshop 2', 'description': 'This is another workshop'}
    ]
    return render_template('workshops.html', workshops=workshops)

@app.route('/workshop/<int:workshop_id>')
@login_required
def workshop_details(workshop_id):
    workshop = {'id': workshop_id, 'name': f'Conflict Resolution Workshop {workshop_id}', 'description': 'This is a workshop'}
    return render_template('workshop_details.html', workshop=workshop)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conflict Resolution Workshop</title>
</head>
<body>
    <h1>Conflict Resolution Workshop</h1>
    <p>Welcome to the conflict resolution workshop platform.</p>
    <p><a href="{{ url_for('login') }}">Login</a> or <a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
<!-- templates/register.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

```html
<!-- templates/workshops.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshops</title>
</head>
<body>
    <h1>Workshops</h1>
    <ul>
    {% for workshop in workshops %}
        <li><a href="{{ url_for('workshop_details', workshop_id=workshop.id) }}">{{ workshop.name }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/workshop_details.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshop Details</title>
</head>
<body>
    <h1>{{ workshop.name }}</h1>
    <p>{{ workshop.description }}</p>
</body>
</html>
```
