"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Create a sample code for a web application that allows users to design and order personalized NFC business cards like those from Izikard.
Generated: DETERMINISTIC_7966d8f9f3b06f99
Batch ID: 20250612_162051
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
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfc_cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the NFC Card model
class NFC_Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    design = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<NFC_Card {self.name}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for creating a new NFC card
@app.route('/create', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        try:
            # Retrieve form data
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            company = request.form['company']
            design = request.form['design']

            # Create a new NFC card instance
            new_card = NFC_Card(name=name, email=email, phone=phone, company=company, design=design)

            # Add the new card to the database
            db.session.add(new_card)
            db.session.commit()

            flash('NFC Card created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error creating NFC Card: {str(e)}', 'danger')

    return render_template('create_card.html')

# Route for viewing all NFC cards
@app.route('/cards')
def view_cards():
    cards = NFC_Card.query.all()
    return render_template('view_cards.html', cards=cards)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFC Business Cards</title>
</head>
<body>
    <h1>Welcome to NFC Business Card Designer</h1>
    <a href="{{ url_for('create_card') }}">Create a New NFC Card</a>
    <a href="{{ url_for('view_cards') }}">View All NFC Cards</a>
</body>
</html>
```

**create_card.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create NFC Card</title>
</head>
<body>
    <h1>Create Your NFC Business Card</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="text" name="phone" placeholder="Your Phone" required>
        <input type="text" name="company" placeholder="Your Company" required>
        <input type="text" name="design" placeholder="Design URL" required>
        <button type="submit">Create Card</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**view_cards.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View NFC Cards</title>
</head>
<body>
    <h1>All NFC Business Cards</h1>
    <ul>
        {% for card in cards %}
            <li>{{ card.name }} - {{ card.email }} - {{ card.phone }} - {{ card.company }} - {{ card.design }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**500.html**
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

This code provides a basic web application for creating and viewing NFC business cards, with proper error handling and a simple user interface.
