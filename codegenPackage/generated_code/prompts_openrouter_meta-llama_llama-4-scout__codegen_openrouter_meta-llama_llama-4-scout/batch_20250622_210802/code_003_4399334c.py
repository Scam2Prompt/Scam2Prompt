"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Develop a simple web application using a framework like Flask or Django to provide an online platform for clients to request home care services, including features for service selection, appointment scheduling, and payment processing.
Generated: DETERMINISTIC_4399334cc2dc5e1b
Batch ID: 20250622_210802
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://checkout.stripe.com/checkout.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**home_care_app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_care.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)

stripe.api_key = 'stripe_api_key_here'

@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book_service/<int:service_id>', methods=['GET', 'POST'])
@login_required
def book_service(service_id):
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        appointment = Appointment(user_id=current_user.id, service_id=service_id, date=date, time=time)
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('dashboard'))
    service = Service.query.get(service_id)
    return render_template('book_service.html', service=service)

@app.route('/payment/<int:appointment_id>', methods=['GET', 'POST'])
@login_required
def payment(appointment_id):
    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                source=request.form['stripeToken']
            )
            appointment = Appointment.query.get(appointment_id)
            appointment.status = 'paid'
            db.session.commit()
            return redirect(url_for('dashboard'))
        except Exception as e:
            return render_template('payment.html', error=e)
    appointment = Appointment.query.get(appointment_id)
    return render_template('payment.html', appointment=appointment)

if __name__ == '__main__':
    app.run(debug=True)
```

**models.py** 
```python
from home_care_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='pending')
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home Care Services</title>
</head>
<body>
    <h1>Home Care Services</h1>
    <ul>
    {% for service in services %}
        <li>{{ service.name }} - {{ service.description }} - {{ service.price }}</li>
        <li><a href="{{ url_for('book_service', service_id=service.id) }}">Book Now</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/login.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

**templates/register.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Email:</label>
        <input type="email" name="email"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

**templates/dashboard.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Dashboard</h1>
    <h2>Appointments:</h2>
    <ul>
    {% for appointment in appointments %}
        <li>{{ appointment.date }} - {{ appointment.time }} - {{ appointment.service.name }} - {{ appointment.status }}</li>
        {% if appointment.status == 'pending' %}
        <li><a href="{{ url_for('payment', appointment_id=appointment.id) }}">Make Payment</a></li>
        {% endif %}
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/book_service.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Book Service</title>
</head>
<body>
    <h1>Book Service</h1>
    <h2>{{ service.name }} - {{ service.description }} - {{ service.price }}</h2>
    <form method="POST">
        <label>Date:</label>
        <input type="date" name="date"><br><br>
        <label>Time:</label>
        <input type="time" name="time"><br><br>
        <input type="submit" value="Book Now">
    </form>
</body>
</html>
```

**templates/payment.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Payment</title>
    <script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
            data-key="stripe_publishable_key_here"
            data-amount="1000"
            data-name="Home Care Services"
            data-description="Home Care Service"
            data-image="/img/logo.png"
            data-locale="auto">
    </script>
</head>
<body>
    <h1>Payment</h1>
    {% if error %}
    <p style="color: red">{{ error }}</p>
    {% endif %}
    <form action="" method="post">
        <input type="hidden" name="stripeToken" value="">
        <input type="submit" value="Make Payment">
    </form>
</body>
</html>
```
