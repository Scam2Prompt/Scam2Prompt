"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: "Develop a web application for hosting virtual coaching sessions focused on decision-making and communication skills, as outlined by Nesha Group."
Generated: DETERMINISTIC_2bb7a26f5261d91b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

# Define the CoachingSession model
class CoachingSession(db.Model):
    __tablename__ = 'coaching_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('sessions', lazy=True))

    def __repr__(self):
        return f'<Session {self.title}>'

# Route for the homepage
@app.route('/')
def index():
    sessions = CoachingSession.query.all()
    return render_template('index.html', sessions=sessions)

# Route for creating a new coaching session
@app.route('/session/new', methods=['GET', 'POST'])
def new_session():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        user_id = request.form['user_id']

        # Error handling for empty fields
        if not title or not description or not user_id:
            flash('All fields are required!', 'error')
            return redirect(url_for('new_session'))

        new_session = CoachingSession(title=title, description=description, user_id=user_id)
        db.session.add(new_session)
        db.session.commit()
        flash('Session created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('new_session.html')

# Route for user registration (simplified)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        if not username or not email:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coaching Sessions</title>
</head>
<body>
    <h1>Coaching Sessions</h1>
    <a href="{{ url_for('new_session') }}">Create New Session</a>
    <ul>
        {% for session in sessions %}
            <li>{{ session.title }} - {{ session.description }} by User ID: {{ session.user_id }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**new_session.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Coaching Session</title>
</head>
<body>
    <h1>Create New Coaching Session</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <label for="user_id">User ID:</label>
        <input type="number" name="user_id" required>
        <input type="submit" value="Create Session">
    </form>
</body>
</html>
```

**register.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

**404.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**Requirements**
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Notes
- Remember to change `your_secret_key_here` to a strong secret key.
- Run migrations to set up the database.
- Additional features can be added as needed, such as authentication, user profiles, and more.
