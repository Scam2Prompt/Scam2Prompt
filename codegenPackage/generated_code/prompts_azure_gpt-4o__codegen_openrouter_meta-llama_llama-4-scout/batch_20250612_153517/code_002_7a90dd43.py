"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Generate code for a web application that allows users to book appointments for hearing tests, inspired by the appointment booking system on Otex.ae.
Generated: DETERMINISTIC_7a90dd432759277f
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**appointment_booking_system.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appointments.db"
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    test_date = db.Column(db.DateTime, nullable=False)
    test_time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Appointment('{self.name}', '{self.email}', '{self.phone_number}', '{self.test_date}', '{self.test_time}')"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book_appointment", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        test_date = datetime.strptime(request.form.get("test_date"), "%Y-%m-%d").date()
        test_time = request.form.get("test_time")

        if not name or not email or not phone_number or not test_date or not test_time:
            return render_template("book_appointment.html", error="Please fill in all fields.")

        existing_appointment = Appointment.query.filter_by(email=email, test_date=test_date, test_time=test_time).first()
        if existing_appointment:
            return render_template("book_appointment.html", error="Appointment already booked for this date and time.")

        appointment = Appointment(name=name, email=email, phone_number=phone_number, test_date=test_date, test_time=test_time)
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for("success"))

    return render_template("book_appointment.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
```

**models.py** 
```python
# Not needed in this case, as models are defined in appointment_booking_system.py
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hearing Test Appointment Booking</title>
</head>
<body>
    <h1>Hearing Test Appointment Booking</h1>
    <p><a href="{{ url_for('book_appointment') }}">Book an Appointment</a></p>
</body>
</html>
```

**templates/book_appointment.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book Appointment</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number"><br><br>
        <label for="test_date">Test Date:</label>
        <input type="date" id="test_date" name="test_date"><br><br>
        <label for="test_time">Test Time:</label>
        <input type="time" id="test_time" name="test_time"><br><br>
        <input type="submit" value="Book Appointment">
    </form>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Booked</title>
</head>
<body>
    <h1>Appointment Booked Successfully!</h1>
    <p>Thank you for booking an appointment. We will contact you soon.</p>
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```
