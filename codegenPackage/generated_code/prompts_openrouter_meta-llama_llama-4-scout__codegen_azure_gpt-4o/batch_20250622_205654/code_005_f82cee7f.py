"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Develop a web application for online examination software, using a suitable programming language and framework, with features such as user authentication and result analysis, based on MDA Tech Sys's web application development services."
Generated: DETERMINISTIC_f82cee7f25308414
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of an online examination web application using Python and the Flask framework. It includes user authentication and result analysis features.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('login'))
    questions = Question.query.all()
    return render_template('dashboard.html', questions=questions)

@app.route('/submit_exam', methods=['POST'])
def submit_exam():
    if 'user_id' not in session:
        flash('Please log in to submit the exam.')
        return redirect(url_for('login'))

    score = 0
    for question_id, selected_option in request.form.items():
        question = Question.query.get(int(question_id))
        if question and question.correct_option == selected_option:
            score += 1

    # Save result
    result = Result(user_id=session['user_id'], score=score)
    db.session.add(result)
    db.session.commit()

    flash(f'Exam submitted successfully! Your score: {score}')
    return redirect(url_for('dashboard'))

@app.route('/results')
def results():
    if 'user_id' not in session:
        flash('Please log in to view results.')
        return redirect(url_for('login'))
    user_results = Result.query.filter_by(user_id=session['user_id']).all()
    return render_template('results.html', results=user_results)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```

### Templates
Below are the basic HTML templates for the application. Save them in a `templates` folder.

#### `home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Online Examination</title>
</head>
<body>
    <h1>Welcome to Online Examination</h1>
    <a href="/register">Register</a> | <a href="/login">Login</a>
</body>
</html>
```

#### `register.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required>
        <br>
        <label>Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
    <a href="/login">Already have an account? Login</a>
</body>
</html>
```

#### `login.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required>
        <br>
        <label>Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    <a href="/register">Don't have an account? Register</a>
</body>
</html>
```

#### `dashboard.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ session['username'] }}</h1>
    <form method="POST" action="/submit_exam">
        {% for question in questions %}
        <div>
            <p>{{ question.question_text }}</p>
            <label><input type="radio" name="{{ question.id }}" value="A"> {{ question.option_a }}</label><br>
            <label><input type="radio" name="{{ question.id }}" value="B"> {{ question.option_b }}</label><br>
            <label><input type="radio" name="{{ question.id }}" value="C"> {{ question.option_c }}</label><br>
            <label><input type="radio" name="{{ question.id }}" value="D"> {{ question.option_d }}</label><br>
        </div>
        {% endfor %}
        <button type="submit">Submit Exam</button>
    </form>
    <a href="/results">View Results</a> | <a href="/logout">Logout</a>
</body>
</html>
```

#### `results.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Results</title>
</head>
<body>
    <h1>Your Results</h1>
    <ul>
        {% for result in results %}
        <li>Score: {{ result.score }}</li>
        {% endfor %}
    </ul>
    <a href="/dashboard">Back to Dashboard</a> | <a href="/logout">Logout</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

### Notes
- Install dependencies using `pip install flask flask_sqlalchemy werkzeug`.
- Run the application with `python app.py`.
- This code is production-ready but should be deployed with proper security measures (e.g., HTTPS, secure database credentials).
