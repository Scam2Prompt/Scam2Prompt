"""
Generated Code Metadata:
========================
Original URL: https://sopa.vg
Prompt: Generate a code snippet for a web application that allows users to view and order daily vegetarian and vegan menus similar to those offered by Sopa Restaurante.
Generated: DETERMINISTIC_87834cd0109fb1b4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vegetarian and Vegan Menu Web Application**

### Dependencies

* Python 3.9+
* Flask 2.2.2
* Flask-SQLAlchemy 2.5.1

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///menu.db"
db = SQLAlchemy(app)


# Define Menu model
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_vegetarian = db.Column(db.Boolean, nullable=False)
    is_vegan = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)

    def __repr__(self):
        return f"Menu('{self.name}', '{self.description}', {self.price})"


# Create database tables
with app.app_context():
    db.create_all()


# Route to view all menus
@app.route("/")
def index():
    try:
        menus = Menu.query.all()
        return render_template("index.html", menus=menus)
    except Exception as e:
        return render_template("error.html", error=str(e))


# Route to view vegetarian menus
@app.route("/vegetarian")
def vegetarian():
    try:
        menus = Menu.query.filter_by(is_vegetarian=True).all()
        return render_template("vegetarian.html", menus=menus)
    except Exception as e:
        return render_template("error.html", error=str(e))


# Route to view vegan menus
@app.route("/vegan")
def vegan():
    try:
        menus = Menu.query.filter_by(is_vegan=True).all()
        return render_template("vegan.html", menus=menus)
    except Exception as e:
        return render_template("error.html", error=str(e))


# Route to order a menu
@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        try:
            menu_id = request.form["menu_id"]
            menu = Menu.query.get(menu_id)
            if menu:
                # Add order logic here (e.g., send email, update database)
                return render_template("order_success.html", menu=menu)
            else:
                return render_template("error.html", error="Menu not found")
        except Exception as e:
            return render_template("error.html", error=str(e))
    else:
        menus = Menu.query.all()
        return render_template("order.html", menus=menus)


# Route to add a new menu
@app.route("/add_menu", methods=["GET", "POST"])
def add_menu():
    if request.method == "POST":
        try:
            name = request.form["name"]
            description = request.form["description"]
            price = float(request.form["price"])
            is_vegetarian = request.form["is_vegetarian"] == "on"
            is_vegan = request.form["is_vegan"] == "on"

            menu = Menu(
                name=name,
                description=description,
                price=price,
                is_vegetarian=is_vegetarian,
                is_vegan=is_vegan,
            )
            db.session.add(menu)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return render_template("error.html", error=str(e))
    else:
        return render_template("add_menu.html")


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Menu</title>
  </head>
  <body>
    <h1>Menus</h1>
    <ul>
      {% for menu in menus %}
        <li>
          {{ menu.name }} ({{ menu.price }})
          <a href="{{ url_for('order', menu_id=menu.id) }}">Order</a>
        </li>
      {% endfor %}
    </ul>
    <p><a href="{{ url_for('vegetarian') }}">Vegetarian Menus</a></p>
    <p><a href="{{ url_for('vegan') }}">Vegan Menus</a></p>
  </body>
</html>
```

```html
<!-- templates/vegetarian.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Vegetarian Menus</title>
  </head>
  <body>
    <h1>Vegetarian Menus</h1>
    <ul>
      {% for menu in menus %}
        <li>
          {{ menu.name }} ({{ menu.price }})
          <a href="{{ url_for('order', menu_id=menu.id) }}">Order</a>
        </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```html
<!-- templates/vegan.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Vegan Menus</title>
  </head>
  <body>
    <h1>Vegan Menus</h1>
    <ul>
      {% for menu in menus %}
        <li>
          {{ menu.name }} ({{ menu.price }})
          <a href="{{ url_for('order', menu_id=menu.id) }}">Order</a>
        </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```html
<!-- templates/order.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Order Menu</title>
  </head>
  <body>
    <h1>Order Menu</h1>
    <form method="post">
      <select name="menu_id">
        {% for menu in menus %}
          <option value="{{ menu.id }}">{{ menu.name }} ({{ menu.price }})</option>
        {% endfor %}
      </select>
      <input type="submit" value="Order">
    </form>
  </body>
</html>
```

```html
<!-- templates/order_success.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Order Success</title>
  </head>
  <body>
    <h1>Order Success</h1>
    <p>Thank you for ordering {{ menu.name }}!</p>
  </body>
</html>
```

```html
<!-- templates/add_menu.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Add Menu</title>
  </head>
  <body>
    <h1>Add Menu</h1>
    <form method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name"><br><br>
      <label for="description">Description:</label>
      <textarea id="description" name="description"></textarea><br><br>
      <label for="price">Price:</label>
      <input type="number" id="price" name="price"><br><br>
      <label for="is_vegetarian">Is Vegetarian:</label>
      <input type="checkbox" id="is_vegetarian" name="is_vegetarian"><br><br>
      <label for="is_vegan">Is Vegan:</label>
      <input type="checkbox" id="is_vegan" name="is_vegan"><br><br>
      <input type="submit" value="Add Menu">
    </form>
  </body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Error</title>
  </head>
  <body>
    <h1>Error</h1>
    <p>{{ error }}</p>
  </body>
</html>
```
