"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crypto-io.com
Prompt: How can I build a user-friendly interface for booking haircuts online, taking inspiration from the Gould Barbers website's appointment system?
Generated: DETERMINISTIC_39016ea90ce3ae3b
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

# Model for storing appointment details
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    service = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.name} on {self.date_time}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for booking an appointment
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            date_time = datetime.strptime(request.form['date_time'], '%Y-%m-%d %H:%M')
            service = request.form['service']

            # Validate input fields
            if not name or not email or not date_time or not service:
                raise ValueError("All fields are required.")

            # Create a new appointment
            new_appointment = Appointment(name=name, email=email, date_time=date_time, service=service)
            db.session.add(new_appointment)
            db.session.commit()
            flash('Appointment booked successfully!', 'success')
            return redirect(url_for('index'))
        
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(str(e), 'danger')

    return render_template('book.html')

# Route for viewing appointments
@app.route('/appointments')
def appointments():
    all_appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=all_appointments)

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point of the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Enable debug mode for development
```

### Environment Variables (.env)
```
DATABASE_URI=sqlite:///appointments.db  # Use your preferred database URI
SECRET_KEY=your_secret_key_here  # Replace with your actual secret key
```

### HTML Templates (index.html, book.html, appointments.html, 404.html)
Ensure to create these HTML files in a `templates` directory, styled appropriately to ensure a user-friendly interface.
