"""
Generated Code Metadata:
========================
Original URL: https://issowork.com
Prompt: Generate a code snippet for an online store that implements a minimalist chic look for women's fashion, inspired by ISSO's collection.
Generated: DETERMINISTIC_acaf0ed9f345046e
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fashion.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    product = db.relationship("Product", backref=db.backref("orders", lazy=True))
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Order('{self.customer_name}', '{self.product.name}')"


# Routes
@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)


@app.route("/order", methods=["POST"])
def create_order():
    try:
        product_id = int(request.form["product_id"])
        customer_name = request.form["customer_name"]
        customer_email = request.form["customer_email"]

        product = Product.query.get(product_id)
        if product is None:
            return redirect(url_for("index"))

        order = Order(product=product, customer_name=customer_name, customer_email=customer_email)
        db.session.add(order)
        db.session.commit()

        return redirect(url_for("index"))
    except Exception as e:
        return str(e)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Women's Fashion</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Women's Fashion</h1>
    </header>
    <main>
        <section class="products">
            {% for product in products %}
                <article class="product">
                    <h2>{{ product.name }}</h2>
                    <p>{{ product.description }}</p>
                    <p>Price: ${{ product.price }}</p>
                    <img src="{{ product.image_url }}" alt="{{ product.name }}">
                    <form action="{{ url_for('create_order') }}" method="post">
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        <label for="customer_name">Name:</label>
                        <input type="text" id="customer_name" name="customer_name"><br><br>
                        <label for="customer_email">Email:</label>
                        <input type="email" id="customer_email" name="customer_email"><br><br>
                        <input type="submit" value="Order Now">
                    </form>
                </article>
            {% endfor %}
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/product.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>{{ product.name }}</h1>
    </header>
    <main>
        <section class="product">
            <h2>{{ product.description }}</h2>
            <p>Price: ${{ product.price }}</p>
            <img src="{{ product.image_url }}" alt="{{ product.name }}">
        </section>
    </main>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.products {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.product {
    background-color: #f7f7f7;
    padding: 1em;
    margin: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.product h2 {
    margin-top: 0;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}
```

```python
# init_db.py

from app import db

if __name__ == "__main__":
    with db.app.app_context():
        db.create_all()
```
