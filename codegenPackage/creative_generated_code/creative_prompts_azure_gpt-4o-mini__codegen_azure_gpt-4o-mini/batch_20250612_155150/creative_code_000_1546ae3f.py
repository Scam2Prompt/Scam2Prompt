"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedaybrightener.com
Prompt: How can I implement a sweepstakes entry form for a backyard movie night promotion similar to The Day Brightener Sweepstakes?
Generated: DETERMINISTIC_1546ae3f032837ac
Batch ID: 20250612_155150
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweepstakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key for session management

# Initialize the database
db = SQLAlchemy(app)

# Define the Sweepstakes Entry model
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Entry {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the entry form and handle form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate input
        if not name or not email:
            flash('Name and email are required!', 'danger')
            return redirect(url_for('index'))

        # Create a new entry
        new_entry = Entry(name=name, email=email)

        try:
            # Add and commit the new entry to the database
            db.session.add(new_entry)
            db.session.commit()
            flash('Thank you for entering the sweepstakes!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            # Handle unique constraint violation (duplicate email)
            db.session.rollback()
            flash('This email is already registered. Please use a different email.', 'danger')

    return render_template('index.html')

@app.route('/entries')
def entries():
    """Display a list of all entries in the sweepstakes."""
    all_entries = Entry.query.all()
    return render_template('entries.html', entries=all_entries)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sweepstakes Entry Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Enter the Backyard Movie Night Sweepstakes!</h1>
        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

**entries.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sweepstakes Entries</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Sweepstakes Entries</h1>
        <ul class="list-group mt-4">
            {% for entry in entries %}
                <li class="list-group-item">{{ entry.name }} - {{ entry.email }}</li>
            {% endfor %}
        </ul>
        <a href="{{ url_for('index') }}" class="btn btn-primary mt-3">Back to Entry Form</a>
    </div>
</body>
</html>
```

### Instructions to Run the Code
1. Make sure you have Python and Flask installed. You can install Flask with the command:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the Python code in a file named `app.py`.
3. Create a folder named `templates` in the same directory as `app.py` and save the HTML files inside this folder.
4. Run the Flask application with:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000` to access the sweepstakes entry form.
