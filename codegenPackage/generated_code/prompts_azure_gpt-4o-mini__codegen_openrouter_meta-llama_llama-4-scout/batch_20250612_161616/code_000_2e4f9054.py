"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Generate a code snippet for a web application that allows users to access exclusive makeup tutorials and live sessions, similar to the membership features of Ju Ensina.
Generated: DETERMINISTIC_2e4f9054939c8412
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Makeup Tutorials and Live Sessions Web Application**
======================================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database management
* `flask_login` for user authentication
* `werkzeug` for password hashing

**Code:**
```python
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///makeup_tutorials.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_exclusive = db.Column(db.Boolean, default=False)

class LiveSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    is_exclusive = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    tutorials = Tutorial.query.filter_by(is_exclusive=False).all()
    live_sessions = LiveSession.query.filter_by(is_exclusive=False).all()
    return render_template('index.html', tutorials=tutorials, live_sessions=live_sessions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('index'))

@app.route('/tutorials')
@login_required
def tutorials():
    tutorials = Tutorial.query.all()
    return render_template('tutorials.html', tutorials=tutorials)

@app.route('/live_sessions')
@login_required
def live_sessions():
    live_sessions = LiveSession.query.all()
    return render_template('live_sessions.html', live_sessions=live_sessions)

@app.route('/exclusive_tutorials')
@login_required
def exclusive_tutorials():
    if current_user.is_authenticated:
        tutorials = Tutorial.query.filter_by(is_exclusive=True).all()
        return render_template('exclusive_tutorials.html', tutorials=tutorials)
    else:
        flash('You need to be logged in to access exclusive content')
        return redirect(url_for('login'))

@app.route('/exclusive_live_sessions')
@login_required
def exclusive_live_sessions():
    if current_user.is_authenticated:
        live_sessions = LiveSession.query.filter_by(is_exclusive=True).all()
        return render_template('exclusive_live_sessions.html', live_sessions=live_sessions)
    else:
        flash('You need to be logged in to access exclusive content')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Makeup Tutorials and Live Sessions</title>
</head>
<body>
    <h1>Makeup Tutorials and Live Sessions</h1>
    <ul>
        {% for tutorial in tutorials %}
        <li>{{ tutorial.title }}</li>
        {% endfor %}
    </ul>
    <ul>
        {% for live_session in live_sessions %}
        <li>{{ live_session.title }} - {{ live_session.date }}</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('login') }}">Login</a> | <a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

**templates/login.html**
```html
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
    <p><a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

**templates/register.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
    <p><a href="{{ url_for('login') }}">Login</a></p>
</body>
</html>
```

**templates/tutorials.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Tutorials</title>
</head>
<body>
    <h1>Tutorials</h1>
    <ul>
        {% for tutorial in tutorials %}
        <li>{{ tutorial.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/live_sessions.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Live Sessions</title>
</head>
<body>
    <h1>Live Sessions</h1>
    <ul>
        {% for live_session in live_sessions %}
        <li>{{ live_session.title }} - {{ live_session.date }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/exclusive_tutorials.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exclusive Tutorials</title>
</head>
<body>
    <h1>Exclusive Tutorials</h1>
    <ul>
        {% for tutorial in tutorials %}
        <li>{{ tutorial.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/exclusive_live_sessions.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exclusive Live Sessions</title>
</head>
<body>
    <h1>Exclusive Live Sessions</h1>
    <ul>
        {% for live_session in live_sessions %}
        <li>{{ live_session.title }} - {{ live_session.date }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
