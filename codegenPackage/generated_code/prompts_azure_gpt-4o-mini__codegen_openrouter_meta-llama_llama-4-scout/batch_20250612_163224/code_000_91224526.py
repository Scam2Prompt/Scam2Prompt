"""
Generated Code Metadata:
========================
Original URL: https://jgtcom.com
Prompt: Generate a code snippet for a fashion e-commerce website that showcases premium fabrics and sophisticated clothing, similar to JGT's offerings.
Generated: DETERMINISTIC_91224526f7971fc6
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fashion_ecommerce.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fashion.db"
db = SQLAlchemy(app)


# Define Fabric model
class Fabric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Fabric('{self.name}')"


# Define Clothing model
class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    fabric_id = db.Column(db.Integer, db.ForeignKey("fabric.id"), nullable=False)
    fabric = db.relationship("Fabric", backref=db.backref("clothings", lazy=True))

    def __repr__(self):
        return f"Clothing('{self.name}')"


# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Route for homepage
@app.route("/")
def index():
    fabrics = Fabric.query.all()
    clothings = Clothing.query.all()
    return render_template("index.html", fabrics=fabrics, clothings=clothings)


# Route for fabric details
@app.route("/fabric/<int:fabric_id>")
def fabric_details(fabric_id):
    fabric = Fabric.query.get_or_404(fabric_id)
    return render_template("fabric.html", fabric=fabric)


# Route for clothing details
@app.route("/clothing/<int:clothing_id>")
def clothing_details(clothing_id):
    clothing = Clothing.query.get_or_404(clothing_id)
    return render_template("clothing.html", clothing=clothing)


# Route for adding new fabric
@app.route("/add_fabric", methods=["GET", "POST"])
def add_fabric():
    if request.method == "POST":
        fabric = Fabric(name=request.form["name"], description=request.form["description"])
        db.session.add(fabric)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_fabric.html")


# Route for adding new clothing
@app.route("/add_clothing", methods=["GET", "POST"])
def add_clothing():
    if request.method == "POST":
        clothing = Clothing(
            name=request.form["name"],
            description=request.form["description"],
            fabric_id=request.form["fabric_id"],
        )
        db.session.add(clothing)
        db.session.commit()
        return redirect(url_for("index"))
    fabrics = Fabric.query.all()
    return render_template("add_clothing.html", fabrics=fabrics)


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
    <title>Fashion E-commerce</title>
</head>
<body>
    <h1>Fashion E-commerce</h1>
    <h2>Fabrics</h2>
    <ul>
    {% for fabric in fabrics %}
        <li>{{ fabric.name }} ({{ fabric.description }})</li>
    {% endfor %}
    </ul>
    <h2>Clothing</h2>
    <ul>
    {% for clothing in clothings %}
        <li>{{ clothing.name }} ({{ clothing.description }}) - {{ clothing.fabric.name }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_fabric') }}">Add new fabric</a></p>
    <p><a href="{{ url_for('add_clothing') }}">Add new clothing</a></p>
</body>
</html>
```

```html
<!-- templates/fabric.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fabric Details</title>
</head>
<body>
    <h1>Fabric Details</h1>
    <h2>{{ fabric.name }}</h2>
    <p>{{ fabric.description }}</p>
</body>
</html>
```

```html
<!-- templates/clothing.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clothing Details</title>
</head>
<body>
    <h1>Clothing Details</h1>
    <h2>{{ clothing.name }}</h2>
    <p>{{ clothing.description }}</p>
    <p>Fabric: {{ clothing.fabric.name }}</p>
</body>
</html>
```

```html
<!-- templates/add_fabric.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Fabric</title>
</head>
<body>
    <h1>Add Fabric</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Add Fabric">
    </form>
</body>
</html>
```

```html
<!-- templates/add_clothing.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Clothing</title>
</head>
<body>
    <h1>Add Clothing</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="fabric_id">Fabric:</label>
        <select id="fabric_id" name="fabric_id">
        {% for fabric in fabrics %}
            <option value="{{ fabric.id }}">{{ fabric.name }}</option>
        {% endfor %}
        </select><br><br>
        <input type="submit" value="Add Clothing">
    </form>
</body>
</html>
```
