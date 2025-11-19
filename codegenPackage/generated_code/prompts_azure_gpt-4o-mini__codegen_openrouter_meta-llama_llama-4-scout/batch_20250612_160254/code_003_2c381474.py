"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: How can I create a web application that provides online training modules for material handling equipment, based on the features of CoLa Training Services?
Generated: DETERMINISTIC_2c38147461a0d219
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Material Handling Equipment Training Modules Web Application**

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Login 0.6+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_modules.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class TrainingModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    training_modules = TrainingModule.query.all()
    return render_template('index.html', training_modules=training_modules)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/training-module/<int:module_id>')
@login_required
def training_module(module_id):
    module = TrainingModule.query.get(module_id)
    if module:
        return render_template('training_module.html', module=module)
    return 'Module not found', 404

@app.route('/create-training-module', methods=['GET', 'POST'])
@login_required
def create_training_module():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        content = request.form['content']
        module = TrainingModule(title=title, description=description, content=content)
        db.session.add(module)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_training_module.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Material Handling Equipment Training Modules</title>
</head>
<body>
    <h1>Training Modules</h1>
    <ul>
    {% for module in training_modules %}
        <li><a href="{{ url_for('training_module', module_id=module.id) }}">{{ module.title }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_training_module') }}">Create a new training module</a></p>
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
    <form method="post">
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
<!-- templates/training_module.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ module.title }}</title>
</head>
<body>
    <h1>{{ module.title }}</h1>
    <p>{{ module.description }}</p>
    <p>{{ module.content }}</p>
</body>
</html>
```

```html
<!-- templates/create_training_module.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Create a new training module</title>
</head>
<body>
    <h1>Create a new training module</h1>
    <form method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```
