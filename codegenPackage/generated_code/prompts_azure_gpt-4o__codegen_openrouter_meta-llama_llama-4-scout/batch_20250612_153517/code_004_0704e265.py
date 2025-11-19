"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a web application prototype for clients to design and customize their own cosmetic brand, incorporating the full-service workflow described by Fabricare Cosméticos.
Generated: DETERMINISTIC_0704e2650c7b429e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for the web application prototype. However, I need to clarify that I'll be providing a high-level implementation in Python using the Flask web framework, and a SQLite database for simplicity. 

Here is the code:

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cosmetic_brand.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('brands', lazy=True))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('products', lazy=True))

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    user = User.query.get(1)  # Assuming user is logged in
    brands = user.brands
    return render_template('dashboard.html', brands=brands)

@app.route('/brand/create', methods=['GET', 'POST'])
def create_brand():
    if request.method == 'POST':
        name = request.form['name']
        user_id = 1  # Assuming user is logged in
        brand = Brand(name=name, user_id=user_id)
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_brand.html')

@app.route('/product/create/<int:brand_id>', methods=['GET', 'POST'])
def create_product(brand_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        product = Product(name=name, description=description, brand_id=brand_id)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('dashboard'))
    brand = Brand.query.get(brand_id)
    return render_template('create_product.html', brand=brand)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Cosmetic Brand</title>
</head>
<body>
    <h1>Cosmetic Brand</h1>
    <p><a href="{{ url_for('register') }}">Register</a></p>
    <p><a href="{{ url_for('login') }}">Login</a></p>
</body>
</html>
```

```html
<!-- templates/register.html -->

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

```html
<!-- templates/login.html -->

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

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Dashboard</h1>
    <h2>Brands:</h2>
    <ul>
    {% for brand in brands %}
        <li>{{ brand.name }} (<a href="{{ url_for('create_product', brand_id=brand.id) }}">Create Product</a>)</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_brand') }}">Create Brand</a></p>
</body>
</html>
```

```html
<!-- templates/create_brand.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Create Brand</title>
</head>
<body>
    <h1>Create Brand</h1>
    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name"><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```

```html
<!-- templates/create_product.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Create Product</title>
</head>
<body>
    <h1>Create Product for {{ brand.name }}</h1>
    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name"><br><br>
        <label>Description:</label>
        <textarea name="description"></textarea><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```
