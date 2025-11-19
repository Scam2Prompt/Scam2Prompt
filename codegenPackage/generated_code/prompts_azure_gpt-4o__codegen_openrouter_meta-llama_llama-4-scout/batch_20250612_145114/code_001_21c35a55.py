"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop a web application using Flask that allows users to request roofing estimates, incorporating King Roofing's specific services like skylight installation and SWR underlayments.
Generated: DETERMINISTIC_21c35a55e56de578
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roofing_estimates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RoofingEstimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"RoofingEstimate('{self.customer_name}', '{self.address}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        try:
            estimate = RoofingEstimate(
                customer_name=request.form['customer_name'],
                address=request.form['address'],
                phone_number=request.form['phone_number'],
                email=request.form['email'],
                service_type=request.form['service_type'],
                description=request.form.get('description', '')
            )
            db.session.add(estimate)
            db.session.commit()
            return jsonify({'message': 'Estimate submitted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error submitting estimate'}), 400
    return render_template('estimate.html')

@app.route('/services')
def services():
    services = [
        {'name': 'Skylight Installation', 'description': 'Get a professional skylight installation from King Roofing'},
        {'name': 'SWR Underlayments', 'description': 'Protect your roof with SWR underlayments from King Roofing'}
    ]
    return render_template('services.html', services=services)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                return jsonify({'message': 'Logged in successfully'}), 200
            else:
                return jsonify({'message': 'Invalid credentials'}), 401
        except Exception as e:
            return jsonify({'message': 'Error logging in'}), 400
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = User(username=request.form['username'])
            user.set_password(request.form['password'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'Registered successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error registering'}), 400
    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>King Roofing</title>
</head>
<body>
    <h1>King Roofing</h1>
    <p>Welcome to King Roofing. Get a roofing estimate today!</p>
    <a href="{{ url_for('estimate') }}">Request an Estimate</a>
</body>
</html>
```

```html
<!-- templates/estimate.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request an Estimate</title>
</head>
<body>
    <h1>Request an Estimate</h1>
    <form method="POST">
        <label for="customer_name">Customer Name:</label>
        <input type="text" id="customer_name" name="customer_name" required><br><br>
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required><br><br>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="">Select a service</option>
            <option value="Skylight Installation">Skylight Installation</option>
            <option value="SWR Underlayments">SWR Underlayments</option>
        </select><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/services.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services</title>
</head>
<body>
    <h1>Our Services</h1>
    <ul>
    {% for service in services %}
        <li>
            <h2>{{ service.name }}</h2>
            <p>{{ service.description }}</p>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

```html
<!-- templates/register.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```
