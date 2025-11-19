"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavos.rs
Prompt: Suggest a library for building a user-friendly interface for an architectural consulting service, inspired by the features of Études.
Generated: DETERMINISTIC_6a68674ec8faf98a
Batch ID: 20250612_135121
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
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Initialize the database
db = SQLAlchemy(app)

# Define a model for client inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle inquiries submission
@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    try:
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate form data
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('home'))

        # Create a new inquiry
        new_inquiry = Inquiry(name=name, email=email, message=message)
        db.session.add(new_inquiry)
        db.session.commit()
        flash('Inquiry submitted successfully!', 'success')

        return redirect(url_for('home'))
    except Exception as e:
        # Log the error and display a friendly message
        app.logger.error(f"Error submitting inquiry: {e}")
        flash('An error occurred while submitting your inquiry. Please try again later.', 'error')
        return redirect(url_for('home'))

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template('error.html', error=e), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

### HTML Template for `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Consulting Service</title>
</head>
<body>
    <h1>Welcome to Our Architectural Consulting Service</h1>
    <form action="/submit_inquiry" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit">Submit Inquiry</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
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

### HTML Template for `error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="/">Go back to home</a>
</body>
</html>
``` 

### Notes:
- Ensure to install Flask and Flask-SQLAlchemy in your environment using:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Update `your_secret_key_here` with a secure random key before deploying.
