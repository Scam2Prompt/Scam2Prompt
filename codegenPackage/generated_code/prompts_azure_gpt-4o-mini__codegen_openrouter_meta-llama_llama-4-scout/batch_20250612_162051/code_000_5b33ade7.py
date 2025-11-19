"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Generate a code snippet for an e-commerce website that includes features for user login, product display, and a shopping cart, similar to the functionalities described on the Mambo Wood site.
Generated: DETERMINISTIC_5b33ade72507dcdd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**E-Commerce Website Code Snippet**
=====================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Werkzeug 2.0+

### Code
```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get(product_id)
    return render_template('product.html', product=product)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'user_id' in session:
        user_id = session['user_id']
        cart_items = Cart.query.filter_by(user_id=user_id).all()
        return render_template('cart.html', cart_items=cart_items)
    return redirect(url_for('login'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' in session:
        user_id = session['user_id']
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            new_cart_item = Cart(user_id, product_id, quantity)
            db.session.add(new_cart_item)
        db.session.commit()
        return redirect(url_for('cart'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

**login.html**
```html
<form method="post">
    <label>Username:</label>
    <input type="text" name="username"><br><br>
    <label>Password:</label>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>
```

**register.html**
```html
<form method="post">
    <label>Username:</label>
    <input type="text" name="username"><br><br>
    <label>Password:</label>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Register">
</form>
```

**index.html**
```html
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.price }}</li>
    {% endfor %}
</ul>
```

**product.html**
```html
<h1>{{ product.name }}</h1>
<p>Price: {{ product.price }}</p>
```

**cart.html**
```html
<h1>Cart</h1>
<ul>
    {% for item in cart_items %}
        <li>{{ item.product.name }} - {{ item.quantity }}</li>
    {% endfor %}
</ul>
```

### Database Initialization
```python
with app.app_context():
    db.create_all()
    admin = User('admin', 'password')
    db.session.add(admin)
    db.session.commit()
    product1 = Product('Product 1', 10.99)
    product2 = Product('Product 2', 9.99)
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()
```
