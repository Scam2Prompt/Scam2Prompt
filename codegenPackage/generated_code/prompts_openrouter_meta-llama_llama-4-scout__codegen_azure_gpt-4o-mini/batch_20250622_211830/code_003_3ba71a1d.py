"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Design a simple user interface for an e-book platform that allows users to browse and download e-books, with features like instant access and a secure platform for transactions."
Generated: DETERMINISTIC_3ba71a1d5bb3a905
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebooks.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Define the EBook model
class EBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    file_path = db.Column(db.String(150), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    ebooks = EBook.query.all()  # Fetch all e-books from the database
    return render_template('home.html', ebooks=ebooks)

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        # Check if the username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html')

# Route for downloading an e-book
@app.route('/download/<int:ebook_id>')
def download(ebook_id):
    ebook = EBook.query.get_or_404(ebook_id)  # Fetch the e-book or return 404
    return redirect(url_for('static', filename=ebook.file_path))  # Redirect to the file path

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Book Platform</title>
</head>
<body>
    <h1>Welcome to the E-Book Platform</h1>
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('login') }}">Login</a>
    <h2>Available E-Books</h2>
    <ul>
        {% for ebook in ebooks %}
            <li>
                {{ ebook.title }} by {{ ebook.author }} 
                <a href="{{ url_for('download', ebook_id=ebook.id) }}">Download</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**register.html**
```html
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
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**login.html**
```html
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
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Go back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
- The `static` folder should contain the e-book files for download.
