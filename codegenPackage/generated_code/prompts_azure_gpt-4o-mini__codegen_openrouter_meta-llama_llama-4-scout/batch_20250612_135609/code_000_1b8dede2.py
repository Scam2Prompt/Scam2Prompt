"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Generate a code snippet for an e-commerce website that showcases custom-made fine jewelry, including sections for rings, earrings, and pendants.
Generated: DETERMINISTIC_1b8dede2c1fc7d8e
Batch ID: 20250612_135609
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jewelry.db"
db = SQLAlchemy(app)


# Models
class Jewelry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Jewelry('{self.name}', '{self.description}', '{self.price}', '{self.category}')"


class Ring(Jewelry):
    def __init__(self, name, description, price, metal_type, gemstone):
        super().__init__(name, description, price, "Ring")
        self.metal_type = metal_type
        self.gemstone = gemstone

    def __repr__(self):
        return f"Ring('{self.name}', '{self.description}', '{self.price}', '{self.metal_type}', '{self.gemstone}')"


class Earring(Jewelry):
    def __init__(self, name, description, price, earring_type):
        super().__init__(name, description, price, "Earring")
        self.earring_type = earring_type

    def __repr__(self):
        return f"Earring('{self.name}', '{self.description}', '{self.price}', '{self.earring_type}')"


class Pendant(Jewelry):
    def __init__(self, name, description, price, chain_length):
        super().__init__(name, description, price, "Pendant")
        self.chain_length = chain_length

    def __repr__(self):
        return f"Pendant('{self.name}', '{self.description}', '{self.price}', '{self.chain_length}')"


# Create tables
with app.app_context():
    db.create_all()


# Routes
@app.route("/")
def index():
    rings = Ring.query.all()
    earrings = Earring.query.all()
    pendants = Pendant.query.all()
    return render_template("index.html", rings=rings, earrings=earrings, pendants=pendants)


@app.route("/rings")
def rings():
    rings = Ring.query.all()
    return render_template("rings.html", rings=rings)


@app.route("/earrings")
def earrings():
    earrings = Earring.query.all()
    return render_template("earrings.html", earrings=earrings)


@app.route("/pendants")
def pendants():
    pendants = Pendant.query.all()
    return render_template("pendants.html", pendants=pendants)


@app.route("/add_jewelry", methods=["GET", "POST"])
def add_jewelry():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        category = request.form["category"]

        if category == "ring":
            metal_type = request.form["metal_type"]
            gemstone = request.form["gemstone"]
            ring = Ring(name, description, price, metal_type, gemstone)
            db.session.add(ring)
        elif category == "earring":
            earring_type = request.form["earring_type"]
            earring = Earring(name, description, price, earring_type)
            db.session.add(earring)
        elif category == "pendant":
            chain_length = request.form["chain_length"]
            pendant = Pendant(name, description, price, chain_length)
            db.session.add(pendant)

        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_jewelry.html")


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
    <title>Jewelry Website</title>
</head>
<body>
    <h1>Jewelry Website</h1>
    <h2>Rings</h2>
    <ul>
    {% for ring in rings %}
        <li>{{ ring.name }} - {{ ring.description }} - {{ ring.price }}</li>
    {% endfor %}
    </ul>

    <h2>Earrings</h2>
    <ul>
    {% for earring in earrings %}
        <li>{{ earring.name }} - {{ earring.description }} - {{ earring.price }}</li>
    {% endfor %}
    </ul>

    <h2>Pendants</h2>
    <ul>
    {% for pendant in pendants %}
        <li>{{ pendant.name }} - {{ pendant.description }} - {{ pendant.price }}</li>
    {% endfor %}
    </ul>

    <p><a href="{{ url_for('add_jewelry') }}">Add Jewelry</a></p>
</body>
</html>
```

```html
<!-- templates/rings.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rings</title>
</head>
<body>
    <h1>Rings</h1>
    <ul>
    {% for ring in rings %}
        <li>{{ ring.name }} - {{ ring.description }} - {{ ring.price }} - {{ ring.metal_type }} - {{ ring.gemstone }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/earrings.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Earrings</title>
</head>
<body>
    <h1>Earrings</h1>
    <ul>
    {% for earring in earrings %}
        <li>{{ earring.name }} - {{ earring.description }} - {{ earring.price }} - {{ earring.earring_type }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/pendants.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pendants</title>
</head>
<body>
    <h1>Pendants</h1>
    <ul>
    {% for pendant in pendants %}
        <li>{{ pendant.name }} - {{ pendant.description }} - {{ pendant.price }} - {{ pendant.chain_length }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_jewelry.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Jewelry</title>
</head>
<body>
    <h1>Add Jewelry</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price"><br><br>
        <label for="category">Category:</label>
        <select id="category" name="category">
            <option value="ring">Ring</option>
            <option value="earring">Earring</option>
            <option value="pendant">Pendant</option>
        </select><br><br>
        <div id="ring-fields" style="display: none;">
            <label for="metal_type">Metal Type:</label>
            <input type="text" id="metal_type" name="metal_type"><br><br>
            <label for="gemstone">Gemstone:</label>
            <input type="text" id="gemstone" name="gemstone"><br><br>
        </div>
        <div id="earring-fields" style="display: none;">
            <label for="earring_type">Earring Type:</label>
            <input type="text" id="earring_type" name="earring_type"><br><br>
        </div>
        <div id="pendant-fields" style="display: none;">
            <label for="chain_length">Chain Length:</label>
            <input type="text" id="chain_length" name="chain_length"><br><br>
        </div>
        <input type="submit" value="Submit">
    </form>

    <script>
        const categorySelect = document.getElementById('category');
        const ringFields = document.getElementById('ring-fields');
        const earringFields = document.getElementById('earring-fields');
        const pendantFields = document.getElementById('pendant-fields');

        categorySelect.addEventListener('change', (e) => {
            const selectedCategory = e.target.value;
