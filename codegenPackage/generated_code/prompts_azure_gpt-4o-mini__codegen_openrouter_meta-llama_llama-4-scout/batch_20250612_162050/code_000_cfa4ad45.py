"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Generate a code snippet for a web application that allows users to book a waxing appointment at a salon specializing in painless waxing services.
Generated: DETERMINISTIC_cfa4ad458e52ce58
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Waxing Appointment Booking System**
=====================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code
```python
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///waxing_appointments.db"
db = SQLAlchemy(app)

class WaxingAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f"WaxingAppointment('{self.customer_name}', '{self.appointment_date}', '{self.appointment_time}')"

class BookingForm(FlaskForm):
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    appointment_date = DateField("Appointment Date", validators=[DataRequired()])
    appointment_time = TimeField("Appointment Time", validators=[DataRequired()])
    submit = SubmitField("Book Appointment")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book_appointment", methods=["GET", "POST"])
def book_appointment():
    form = BookingForm()
    if form.validate_on_submit():
        appointment = WaxingAppointment(
            customer_name=form.customer_name.data,
            appointment_date=form.appointment_date.data,
            appointment_time=form.appointment_time.data
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for("appointment_booked"))
    return render_template("book_appointment.html", form=form)

@app.route("/appointment_booked")
def appointment_booked():
    return render_template("appointment_booked.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Templates

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Waxing Appointment Booking System</title>
</head>
<body>
    <h1>Waxing Appointment Booking System</h1>
    <p><a href="{{ url_for('book_appointment') }}">Book an Appointment</a></p>
</body>
</html>
```

**book_appointment.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Book a Waxing Appointment</title>
</head>
<body>
    <h1>Book a Waxing Appointment</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.customer_name.label }} {{ form.customer_name() }}
        {{ form.appointment_date.label }} {{ form.appointment_date() }}
        {{ form.appointment_time.label }} {{ form.appointment_time() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**appointment_booked.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Appointment Booked</title>
</head>
<body>
    <h1>Appointment Booked</h1>
    <p>Thank you for booking an appointment with us!</p>
</body>
</html>
```
