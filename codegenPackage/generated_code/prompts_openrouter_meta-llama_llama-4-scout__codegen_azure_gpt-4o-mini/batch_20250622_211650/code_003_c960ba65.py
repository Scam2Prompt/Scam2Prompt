"""
Generated Code Metadata:
========================
Original URL: https://cancen.fr
Prompt: What are some libraries or frameworks that can be used to build a website for a non-profit organization like CANCEN, with features such as event calendars, donation management, and news updates?
Generated: DETERMINISTIC_c960ba65cd6b9ddb
Batch ID: 20250622_211650
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nonprofit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Event {self.title}>'

# Define the Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.donor_name}: ${self.amount}>'

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for viewing events
@app.route('/events')
def events():
    all_events = Event.query.all()
    return render_template('events.html', events=all_events)

# Route for adding a new event
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        description = request.form['description']
        new_event = Event(title=title, date=datetime.strptime(date, '%Y-%m-%d'), description=description)
        db.session.add(new_event)
        db.session.commit()
        flash('Event added successfully!', 'success')
        return redirect(url_for('events'))
    return render_template('add_event.html')

# Route for viewing donations
@app.route('/donations')
def donations():
    all_donations = Donation.query.all()
    return render_template('donations.html', donations=all_donations)

# Route for making a donation
@app.route('/make_donation', methods=['GET', 'POST'])
def make_donation():
    if request.method == 'POST':
        donor_name = request.form['donor_name']
        amount = request.form['amount']
        new_donation = Donation(donor_name=donor_name, amount=float(amount))
        db.session.add(new_donation)
        db.session.commit()
        flash('Donation made successfully!', 'success')
        return redirect(url_for('donations'))
    return render_template('make_donation.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure you have the necessary HTML templates (`home.html`, `events.html`, `add_event.html`, `donations.html`, `make_donation.html`, and `404.html`) in a `templates` directory.
- Install the required packages using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Migrate
  ```
- Replace `'your_secret_key'` with a secure random key for production use.
