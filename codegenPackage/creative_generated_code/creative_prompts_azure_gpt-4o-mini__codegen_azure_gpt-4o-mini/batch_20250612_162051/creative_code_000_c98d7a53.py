"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsa.academy
Prompt: How can I write a code snippet to create a volunteer registration form for a sports academy similar to Jambalaya Soccer Academy?
Generated: DETERMINISTIC_c98d7a530e535622
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Define the Volunteer model
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    experience = db.Column(db.String(250))

    def __repr__(self):
        return f'<Volunteer {self.name}>'

# Route for displaying the registration form
@app.route('/', methods=['GET', 'POST'])
def register_volunteer():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        experience = request.form.get('experience')

        # Basic validation for required fields
        if not name or not email:
            flash('Name and email are required!', 'danger')
            return redirect(url_for('register_volunteer'))

        # Create a new Volunteer instance
        new_volunteer = Volunteer(name=name, email=email, phone=phone, experience=experience)

        # Add to the session and commit to the database
        try:
            db.session.add(new_volunteer)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register_volunteer'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('register.html')

# Error handling for unexpected HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    return f"An error occurred: {e}", e.code

# Create the database before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (`templates/register.html`)**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Registration Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Volunteer Registration Form</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        
        <form method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="text" class="form-control" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="experience">Experience</label>
                <textarea class="form-control" id="experience" name="experience"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. Use `pip install flask flask-sqlalchemy` to install them if necessary.
