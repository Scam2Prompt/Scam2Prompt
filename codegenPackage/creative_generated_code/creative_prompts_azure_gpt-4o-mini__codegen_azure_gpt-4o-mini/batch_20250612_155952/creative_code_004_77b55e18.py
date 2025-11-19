"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Design a simple web application that displays the schedule and details of the basketball training camps offered by L-Zero, allowing users to register directly through the app.
Generated: DETERMINISTIC_77b55e187a673888
Batch ID: 20250612_155952
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///camps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Define the Camp model
class Camp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to display the list of camps
@app.route('/')
def index():
    camps = Camp.query.all()
    return render_template('index.html', camps=camps)

# Route to register for a camp
@app.route('/register/<int:camp_id>', methods=['GET', 'POST'])
def register(camp_id):
    camp = Camp.query.get_or_404(camp_id)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        if not name or not email:
            flash('Name and email are required!', 'danger')
            return redirect(url_for('register', camp_id=camp_id))
        
        # Create a new registration
        new_registration = Registration(camp_id=camp.id, name=name, email=email)
        db.session.add(new_registration)
        db.session.commit()
        
        flash('You have successfully registered for the camp!', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html', camp=camp)

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

### Template Files

**`templates/index.html`**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basketball Training Camps</title>
</head>
<body>
    <h1>Basketball Training Camps</h1>
    <ul>
        {% for camp in camps %}
            <li>
                <h2>{{ camp.name }}</h2>
                <p>Date: {{ camp.date.strftime('%Y-%m-%d') }}</p>
                <p>{{ camp.description }}</p>
                <a href="{{ url_for('register', camp_id=camp.id) }}">Register</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**`templates/register.html`**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for {{ camp.name }}</title>
</head>
<body>
    <h1>Register for {{ camp.name }}</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**`templates/404.html`**
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
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- To run the application, save the code in a file (e.g., `app.py`) and execute it with `python app.py`. 
- This code should be placed in a directory structure that allows proper loading of the templates.
