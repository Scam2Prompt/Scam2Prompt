"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paybackclaimltd.com
Prompt: Develop a web application that educates users on investment fraud prevention, incorporating the professional guidance and case studies provided by Payback Claim Ltd.
Generated: DETERMINISTIC_4eb3cd56e7b2b5e8
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investor_fraud_prevention.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this in production!

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the model for case studies
class CaseStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<CaseStudy {self.title}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to display case studies
@app.route('/case-studies', methods=['GET'])
def case_studies():
    try:
        cases = CaseStudy.query.all()
        return render_template('case_studies.html', cases=cases)
    except Exception as e:
        logging.error(f"Error fetching case studies: {e}")
        flash('An error occurred while fetching case studies.', 'danger')
        return redirect(url_for('home'))

# Route to add a new case study (for admin use)
@app.route('/add-case-study', methods=['GET', 'POST'])
def add_case_study():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash('Title and content are required!', 'warning')
            return redirect(url_for('add_case_study'))

        new_case = CaseStudy(title=title, content=content)

        try:
            db.session.add(new_case)
            db.session.commit()
            flash('Case study added successfully!', 'success')
            return redirect(url_for('case_studies'))
        except Exception as e:
            logging.error(f"Error adding case study: {e}")
            db.session.rollback()
            flash('An error occurred while adding the case study.', 'danger')

    return render_template('add_case_study.html')

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(e):
    logging.error(f"Server error: {e}")
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)  # Change debug=False in production
```

### HTML Templates

- **home.html**: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Fraud Prevention</title>
</head>
<body>
    <h1>Welcome to Investment Fraud Prevention</h1>
    <p>Learn how to protect yourself from investment fraud.</p>
    <nav>
        <a href="{{ url_for('case_studies') }}">View Case Studies</a>
        <a href="{{ url_for('add_case_study') }}">Add Case Study (Admin)</a>
    </nav>
</body>
</html>
```

- **case_studies.html**: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Case Studies</title>
</head>
<body>
    <h1>Case Studies on Investment Fraud</h1>
    {% for case in cases %}
        <h2>{{ case.title }}</h2>
        <p>{{ case.content }}</p>
    {% endfor %}
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

- **add_case_study.html**: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Case Study</title>
</head>
<body>
    <h1>Add New Case Study</h1>
    <form action="{{ url_for('add_case_study') }}" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <button type="submit">Add Case Study</button>
    </form>
    <a href="{{ url_for('case_studies') }}">Back to Case Studies</a>
</body>
</html>
```

- **404.html**:
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

- **500.html**:
```html
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Requirements
To run the application, ensure you have the following Python packages installed:
```
flask
flask_sqlalchemy
flask_migrate
```

You can install them using:
```bash
pip install flask flask_sqlalchemy flask_migrate
```

Ensure to set up the database with:
```bash
flask db init
flask db migrate
flask db upgrade
```

This code provides a basic web application for educating users on investment fraud prevention with functionalities to view and add case studies.
