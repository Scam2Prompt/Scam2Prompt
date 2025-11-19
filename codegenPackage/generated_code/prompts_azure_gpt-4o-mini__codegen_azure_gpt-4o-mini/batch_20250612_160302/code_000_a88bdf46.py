"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Generate a code snippet for a web application that allows users to sign up for folk dance classes in Nürnberg and Erlangen, focusing on Turkish folk dances.
Generated: DETERMINISTIC_a88bdf46500bcac3
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dance_classes.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the database model for user sign-ups
class SignUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SignUp {self.name} - {self.location}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the sign-up form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        location = request.form.get('location')

        # Basic validation
        if not name or not email or not location:
            flash('All fields are required!', 'danger')
            return redirect(url_for('signup'))

        # Check if the email is already registered
        existing_user = SignUp.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'danger')
            return redirect(url_for('signup'))

        # Create a new sign-up entry
        new_signup = SignUp(name=name, email=email, location=location)
        db.session.add(new_signup)

        try:
            db.session.commit()
            flash('Successfully signed up for the dance class!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while signing up. Please try again.', 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (index.html and signup.html)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Folk Dance Classes</title>
</head>
<body>
    <h1>Welcome to Turkish Folk Dance Classes</h1>
    <a href="{{ url_for('signup') }}">Sign Up</a>
</body>
</html>
```

**signup.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up for Dance Classes</title>
</head>
<body>
    <h1>Sign Up for Turkish Folk Dance Classes</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="location">Location:</label>
        <select id="location" name="location" required>
            <option value="Nürnberg">Nürnberg</option>
            <option value="Erlangen">Erlangen</option>
        </select>
        <br>
        <button type="submit">Sign Up</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production use.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
