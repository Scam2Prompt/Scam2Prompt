"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Develop a simple web application using Flask or Django to provide information on temporary registration services in Adygea, Russia, and allow users to calculate costs and submit applications.
Generated: DETERMINISTIC_8bd9592714f53f38
Batch ID: 20250622_210216
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applications.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Database model for storing applications
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    registration_type = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Application {self.name}>'

# Home route to display information and the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        registration_type = request.form['registration_type']
        
        # Cost calculation based on registration type
        cost = calculate_cost(registration_type)

        # Create a new application instance
        new_application = Application(name=name, email=email, registration_type=registration_type, cost=cost)
        
        # Add to the database
        db.session.add(new_application)
        db.session.commit()
        
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error submitting application: {str(e)}', 'danger')
        return redirect(url_for('home'))

# Function to calculate cost based on registration type
def calculate_cost(registration_type):
    # Example cost structure
    cost_structure = {
        'temporary': 1000.0,
        'permanent': 2000.0,
        'student': 500.0
    }
    return cost_structure.get(registration_type, 0.0)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production

```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temporary Registration Services in Adygea</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Temporary Registration Services in Adygea</h1>
        <p>Fill out the form below to submit your application.</p>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form action="{{ url_for('submit') }}" method="POST">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="registration_type">Registration Type</label>
                <select class="form-control" id="registration_type" name="registration_type" required>
                    <option value="temporary">Temporary</option>
                    <option value="permanent">Permanent</option>
                    <option value="student">Student</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit Application</button>
        </form>
    </div>
</body>
</html>
```

### Instructions to Run the Application
1. Ensure you have Python and Flask installed. You can install Flask using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the Python code in a file named `app.py` and the HTML code in a folder named `templates` as `index.html`.
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.
