"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: Generate a code snippet for a web application that showcases a selection of high-end furniture and innovative decor accessories, similar to the offerings on origines-decoration.com.
Generated: DETERMINISTIC_b603bb500d5cc598
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Furniture and Decor Web Application**
=====================================

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"
```

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
db.init_app(app)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/category/<int:category_id>')
def category(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category.html', category=category)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            image_url=request.form['image_url']
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Furniture and Decor</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('add_product') }}">Add Product</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Featured Products</h1>
        <ul>
            {% for product in products %}
            <li>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: {{ product.price }}</p>
                <img src="{{ product.image_url }}" alt="{{ product.name }}">
                <a href="{{ url_for('product', product_id=product.id) }}">View Details</a>
            </li>
            {% endfor %}
        </ul>
    </main>
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
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>{{ product.name }}</h1>
        <p>{{ product.description }}</p>
        <p>Price: {{ product.price }}</p>
        <img src="{{ product.image_url }}" alt="{{ product.name }}">
    </main>
</body>
</html>
```

**templates/category.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category.name }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>{{ category.name }}</h1>
        <ul>
            {% for product in category.products %}
            <li>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: {{ product.price }}</p>
                <img src="{{ product.image_url }}" alt="{{ product.name }}">
            </li>
            {% endfor %}
        </ul>
    </main>
</body>
</html>
```

**templates/add_product.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Add Product</h1>
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="description">Description:</label>
            <textarea id="description" name="description"></textarea><br><br>
            <label for="price">Price:</label>
            <input type="number" id="price" name="price"><br><br>
            <label for="image_url">Image URL:</label>
            <input type="text" id="image_url" name="image_url"><br><br>
            <input type="submit" value="Add Product">
        </form>
    </main>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.product {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.product h2 {
    margin-top: 0;
}

.product p {
    margin-bottom: 10px;
}

.product a {
    text-decoration: none;
    color: #337ab7;
}
```
