"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Recommend a framework for building a hospital website optimized for lead generation and patient engagement, as per Vivada Infotech's services.
Generated: DETERMINISTIC_0b25251d4bf73de9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create a Lead model to store lead information
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Lead {self.name}>'

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for lead generation form submission
@app.route('/submit', methods=['POST'])
def submit_lead():
    try:
        # Retrieve data from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create a new Lead instance
        new_lead = Lead(name=name, email=email, phone=phone, message=message)

        # Add to the session and commit to the database
        db.session.add(new_lead)
        db.session.commit()

        # Flash a success message
        flash('Your message has been sent successfully!', 'success')

    except Exception as e:
        # Roll back the session in case of an error
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('home'))

# Error handling route for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling route for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main execution: run the app
if __name__ == '__main__':
    # Run the application on localhost:5000
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Website</title>
</head>
<body>
    <h1>Welcome to Our Hospital</h1>
    <form action="{{ url_for('submit_lead') }}" method="post">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="text" name="phone" placeholder="Your Phone" required>
        <textarea name="message" placeholder="Your Message"></textarea>
        <button type="submit">Send Message</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
          {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Go back to home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again later.</p>
    <a href="{{ url_for('home') }}">Go back to home</a>
</body>
</html>
```
