"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a web application prototype for booking plumbing services, including options for emergency calls and specific services like pipe cleaning or asbestos removal, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_f29a6935cfe4e527
Batch ID: 20250612_154909
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plumbing_services.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management

db = SQLAlchemy(app)

# Model for the plumbing service booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    emergency = db.Column(db.Boolean, default=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.id} - {self.service_type}>'

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Booking route
@app.route('/book', methods=['POST'])
def book():
    try:
        name = request.form['name']
        phone = request.form['phone']
        service_type = request.form['service_type']
        emergency = 'emergency' in request.form  # Check if emergency is checked

        # Create a new booking instance
        new_booking = Booking(name=name, phone=phone, service_type=service_type, emergency=emergency)
        db.session.add(new_booking)
        db.session.commit()
        flash('Your booking has been successfully created!', 'success')
    except Exception as e:
        flash(f'An error occurred while booking: {e}', 'danger')
        db.session.rollback()  # Rollback the session in case of error
    return redirect(url_for('home'))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plumbing Service Booking</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Book a Plumbing Service</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="/book">
            <div class="form-group">
                <label for="name">Your Name:</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="text" class="form-control" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="service_type">Service Type:</label>
                <select class="form-control" id="service_type" name="service_type" required>
                    <option value="pipe_cleaning">Pipe Cleaning</option>
                    <option value="asbestos_removal">Asbestos Removal</option>
                    <option value="emergency_service">Emergency Service</option>
                </select>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="emergency" name="emergency">
                <label class="form-check-label" for="emergency">Emergency Call</label>
            </div>
            <button type="submit" class="btn btn-primary">Book Service</button>
        </form>
    </div>
</body>
</html>
```

### Instructions to Run the Application:
1. Ensure you have Python and Flask installed. If not, install Flask using:
   ```
   pip install flask flask_sqlalchemy
   ```
2. Save the Python code as `app.py` and the HTML code as `templates/index.html`.
3. Run the application:
   ```
   python app.py
   ```
4. Navigate to `http://127.0.0.1:5000/` in your web browser to access the booking form.
