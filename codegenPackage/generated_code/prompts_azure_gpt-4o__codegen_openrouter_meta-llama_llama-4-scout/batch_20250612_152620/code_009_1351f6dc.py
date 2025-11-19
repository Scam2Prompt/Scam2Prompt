"""
Generated Code Metadata:
========================
Original URL: https://scimar.ca
Prompt: Generate code to integrate Scimar's hepatalin research into a web-based platform for outreach initiatives, ensuring collaboration features for non-profits and Indigenous communities.
Generated: DETERMINISTIC_1351f6dc60b91d5d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hepatalin.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the Research model
class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define the Collaboration model
class Collaboration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    research_id = db.Column(db.Integer, db.ForeignKey('research.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('collaborations', lazy=True))

# Load the user for login purposes
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the research page
@app.route('/research')
@login_required
def research():
    research_list = Research.query.all()
    return render_template('research.html', research_list=research_list)

# Route for creating new research
@app.route('/research/new', methods=['GET', 'POST'])
@login_required
def new_research():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        research = Research(title=title, description=description, created_by=current_user.id)
        db.session.add(research)
        db.session.commit()
        return redirect(url_for('research'))
    return render_template('new_research.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, role='user')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# API endpoint for adding collaborations
@app.route('/collaborate', methods=['POST'])
@login_required
def collaborate():
    try:
        research_id = request.json['research_id']
        user_id = request.json['user_id']
        collaboration = Collaboration(research_id=research_id, user_id=user_id)
        db.session.add(collaboration)
        db.session.commit()
        return jsonify({'message': 'Collaboration added successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint for removing collaborations
@app.route('/collaborate/remove', methods=['POST'])
@login_required
def remove_collaboration():
    try:
        research_id = request.json['research_id']
        user_id = request.json['user_id']
        collaboration = Collaboration.query.filter_by(research_id=research_id, user_id=user_id).first()
        if collaboration:
            db.session.delete(collaboration)
            db.session.commit()
            return jsonify({'message': 'Collaboration removed successfully'}), 200
        return jsonify({'message': 'Collaboration not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Hepatalin Research Platform</h1>
    <p><a href="{{ url_for('research') }}">View Research</a></p>
    <p><a href="{{ url_for('login') }}">Login</a></p>
    <p><a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

```html
<!-- templates/research.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Research</title>
</head>
<body>
    <h1>Research</h1>
    <ul>
    {% for research in research_list %}
        <li>{{ research.title }} ({{ research.description }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_research') }}">Create New Research</a></p>
</body>
</html>
```

```html
<!-- templates/new_research.html -->
<!DOCTYPE html>
<html>
<head>
    <title>New Research</title>
</head>
<body>
    <h1>Create New Research</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Create">
    </form>
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
<!-- templates/register.html -->
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
</body>
</html>
```
