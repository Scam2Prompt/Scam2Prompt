"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Design a Flask web application that allows users to browse and order Grupo ProBolsa's sustainable promotional products, including reusable bags.
Generated: DETERMINISTIC_bd2ffb531a977a45
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///probolsa.db"
db = SQLAlchemy(app)


# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price})"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"Order('{self.user_name}', '{self.user_email}', {self.product_id})"


# Routes
@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)


@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        user_name = request.form["user_name"]
        user_email = request.form["user_email"]
        product_id = request.form["product_id"]
        product = Product.query.get(product_id)
        if product:
            order = Order(user_name=user_name, user_email=user_email, product=product)
            db.session.add(order)
            db.session.commit()
            return redirect(url_for("success"))
        else:
            return "Product not found", 404
    products = Product.query.all()
    return render_template("order.html", products=products)


@app.route("/success")
def success():
    return render_template("success.html")


# Error Handling
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

**models.py** was removed as it is not required. All models are now in **app.py**.

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grupo ProBolsa</title>
</head>
<body>
    <h1>Grupo ProBolsa Sustainable Promotional Products</h1>
    <ul>
    {% for product in products %}
        <li>
            <a href="{{ url_for('product', product_id=product.id) }}">{{ product.name }}</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/product.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: {{ product.price }}</p>
    <img src="{{ product.image_url }}" alt="{{ product.name }}">
</body>
</html>
```

**templates/order.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order</title>
</head>
<body>
    <h1>Order</h1>
    <form method="POST">
        <label for="user_name">Name:</label>
        <input type="text" id="user_name" name="user_name"><br><br>
        <label for="user_email">Email:</label>
        <input type="email" id="user_email" name="user_email"><br><br>
        <label for="product_id">Product:</label>
        <select id="product_id" name="product_id">
        {% for product in products %}
            <option value="{{ product.id }}">{{ product.name }}</option>
        {% endfor %}
        </select><br><br>
        <input type="submit" value="Order">
    </form>
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
    <title>Success</title>
</head>
<body>
    <h1>Order Successful!</h1>
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
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
</body>
</html>
```

**templates/500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error: Internal Server Error</h1>
</body>
</html>
```
