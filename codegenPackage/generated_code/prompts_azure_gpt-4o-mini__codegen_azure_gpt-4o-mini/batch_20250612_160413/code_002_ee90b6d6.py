"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Create a web application feature that allows users to sponsor a girl through a donation system, reflecting the "Adopt a Girl" initiative from My Flow Foundation.
Generated: DETERMINISTIC_ee90b6d6453ce434
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    girl_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Donation {self.donor_name} - ${self.amount}>'

# Route to render the sponsorship form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle donation submissions
@app.route('/donate', methods=['POST'])
def donate():
    try:
        # Get data from the form
        donor_name = request.form['donor_name']
        amount = float(request.form['amount'])
        girl_id = int(request.form['girl_id'])

        # Create a new donation instance
        new_donation = Donation(donor_name=donor_name, amount=amount, girl_id=girl_id)

        # Add the donation to the session and commit to the database
        db.session.add(new_donation)
        db.session.commit()

        return jsonify({'message': 'Donation successful!', 'donation': str(new_donation)}), 201

    except ValueError as ve:
        return jsonify({'error': 'Invalid input: ' + str(ve)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error. Please try again.'}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sponsor a Girl</title>
</head>
<body>
    <h1>Sponsor a Girl</h1>
    <form action="/donate" method="POST">
        <label for="donor_name">Your Name:</label>
        <input type="text" id="donor_name" name="donor_name" required>
        
        <label for="amount">Donation Amount:</label>
        <input type="number" id="amount" name="amount" step="0.01" required>
        
        <label for="girl_id">Girl ID:</label>
        <input type="number" id="girl_id" name="girl_id" required>
        
        <button type="submit">Donate</button>
    </form>
</body>
</html>
```

```bash
# requirements.txt

Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
```

```bash
# To set up the database, run the following commands in the terminal:
# 1. Initialize the database
flask db init

# 2. Create the migration script
flask db migrate -m "Initial migration."

# 3. Apply the migration to the database
flask db upgrade
```

This code provides a simple web application feature for the "Adopt a Girl" initiative, allowing users to sponsor a girl through donations. It includes a donation form, error handling, and database integration using Flask and SQLAlchemy.
