"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate a code snippet for a web application that allows users to book dumpster rentals online, similar to the system used by Junk in The Box ATL.
Generated: DETERMINISTIC_5be85b97a57238b3
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dumpster_rentals.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize the database

# Define the database model for a dumpster rental
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rental_date = db.Column(db.DateTime, nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Rental {self.customer_name}, {self.rental_date}, {self.size}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the home page template

# Route for booking a dumpster rental
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        try:
            # Collect form data
            customer_name = request.form['customer_name']
            rental_date = datetime.strptime(request.form['rental_date'], '%Y-%m-%d')
            duration_days = int(request.form['duration_days'])
            size = request.form['size']
            
            # Create a new Rental instance
            new_rental = Rental(customer_name=customer_name, rental_date=rental_date,
                                duration_days=duration_days, size=size)
            db.session.add(new_rental)  # Add the rental to the session
            db.session.commit()  # Commit the session to save to the database
            
            flash('Rental booked successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))  # Redirect to home page
        except ValueError as e:
            flash('Error: ' + str(e), 'danger')  # Handle value errors
        except Exception as e:
            flash('An error occurred: ' + str(e), 'danger')  # Handle generic errors
    
    return render_template('book.html')  # Render the booking form template

# Route for viewing all rentals
@app.route('/rentals')
def rentals():
    all_rentals = Rental.query.all()  # Query all rentals from the database
    return render_template('rentals.html', rentals=all_rentals)  # Render rentals page with data

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render custom 404 page

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Notes for HTML Templates
You will need to create the following HTML templates in a `templates` folder:
1. `index.html` - A homepage for the application.
2. `book.html` - A form for booking a dumpster rental.
3. `rentals.html` - A page that lists all rentals.
4. `404.html` - A custom 404 error page.

Make sure to include Bootstrap or any CSS framework for styling as per your requirements.
