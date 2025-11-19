"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Write a code snippet for a web application that facilitates conflict resolution workshops in Igbo communities, inspired by the initiatives of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_3348f5c0f81dbb71
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a strong secret key
db = SQLAlchemy(app)

# Define Workshop model
class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Workshop {self.title}>'

# Route for home page
@app.route('/')
def home():
    # Query all workshops from the database
    workshops = Workshop.query.all()
    return render_template('home.html', workshops=workshops)

# Route for adding a new workshop
@app.route('/add_workshop', methods=['GET', 'POST'])
def add_workshop():
    if request.method == 'POST':
        # Get data from the form
        title = request.form['title']
        date_str = request.form['date']
        location = request.form['location']
        description = request.form['description']

        # Validate date format
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('add_workshop'))

        # Create a new workshop instance
        new_workshop = Workshop(title=title, date=date, location=location, description=description)

        # Add and commit to the database
        try:
            db.session.add(new_workshop)
            db.session.commit()
            flash('Workshop added successfully!', 'success')
        except Exception as e:
            db.session.rollback()  # Rollback in case of an error
            flash('Error adding workshop: ' + str(e), 'error')
        
        return redirect(url_for('home'))
    
    return render_template('add_workshop.html')

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```

Please ensure to create the corresponding HTML templates (`home.html`, `add_workshop.html`, and `404.html`) for this application to function correctly.
