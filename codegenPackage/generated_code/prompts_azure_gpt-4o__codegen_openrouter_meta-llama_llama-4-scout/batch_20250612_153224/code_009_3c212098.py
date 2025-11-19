"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: Develop a web application using Flask that showcases the product range of metallic stickers, including Nickel Metal Stickers and 3D Metal Nickel Stickers, with customization options as described on jttlogos.com.
Generated: DETERMINISTIC_3c21209888e31d5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**metal_stickers_app.py**
```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///metal_stickers.db"
db = SQLAlchemy(app)


# Models
class MetalSticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"MetalSticker('{self.name}', '{self.description}', {self.price})"


class NickelMetalSticker(MetalSticker):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50), nullable=False, default="Nickel")
    size = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"NickelMetalSticker('{self.name}', '{self.description}', {self.price}, '{self.material}', '{self.size}')"


class ThreeDMetalNickelSticker(MetalSticker):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50), nullable=False, default="Nickel")
    size = db.Column(db.String(50), nullable=False)
    thickness = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"ThreeDMetalNickelSticker('{self.name}', '{self.description}', {self.price}, '{self.material}', '{self.size}', {self.thickness})"


# Routes
@app.route("/")
def index():
    metal_stickers = MetalSticker.query.all()
    return render_template("index.html", metal_stickers=metal_stickers)


@app.route("/nickel-metal-stickers")
def nickel_metal_stickers():
    nickel_metal_stickers = NickelMetalSticker.query.all()
    return render_template("nickel_metal_stickers.html", nickel_metal_stickers=nickel_metal_stickers)


@app.route("/3d-metal-nickel-stickers")
def three_d_metal_nickel_stickers():
    three_d_metal_nickel_stickers = ThreeDMetalNickelSticker.query.all()
    return render_template("3d_metal_nickel_stickers.html", three_d_metal_nickel_stickers=three_d_metal_nickel_stickers)


@app.route("/customize", methods=["GET", "POST"])
def customize():
    if request.method == "POST":
        try:
            sticker_type = request.form["sticker_type"]
            name = request.form["name"]
            description = request.form["description"]
            price = float(request.form["price"])

            if sticker_type == "nickel":
                size = request.form["size"]
                nickel_metal_sticker = NickelMetalSticker(name=name, description=description, price=price, size=size)
                db.session.add(nickel_metal_sticker)
            elif sticker_type == "3d":
                size = request.form["size"]
                thickness = float(request.form["thickness"])
                three_d_metal_nickel_sticker = ThreeDMetalNickelSticker(name=name, description=description, price=price, size=size, thickness=thickness)
                db.session.add(three_d_metal_nickel_sticker)

            db.session.commit()
            return jsonify({"message": "Custom sticker created successfully"}), 201
        except Exception as e:
            return jsonify({"message": str(e)}), 400
    return render_template("customize.html")


if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metal Stickers</title>
</head>
<body>
    <h1>Metal Stickers</h1>
    <ul>
        {% for metal_sticker in metal_stickers %}
            <li>{{ metal_sticker.name }} - {{ metal_sticker.description }} - {{ metal_sticker.price }}</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('nickel_metal_stickers') }}">Nickel Metal Stickers</a></p>
    <p><a href="{{ url_for('three_d_metal_nickel_stickers') }}">3D Metal Nickel Stickers</a></p>
    <p><a href="{{ url_for('customize') }}">Customize</a></p>
</body>
</html>
```

**templates/nickel_metal_stickers.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nickel Metal Stickers</title>
</head>
<body>
    <h1>Nickel Metal Stickers</h1>
    <ul>
        {% for nickel_metal_sticker in nickel_metal_stickers %}
            <li>{{ nickel_metal_sticker.name }} - {{ nickel_metal_sticker.description }} - {{ nickel_metal_sticker.price }} - {{ nickel_metal_sticker.size }}</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('index') }}">Back</a></p>
</body>
</html>
```

**templates/3d_metal_nickel_stickers.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Metal Nickel Stickers</title>
</head>
<body>
    <h1>3D Metal Nickel Stickers</h1>
    <ul>
        {% for three_d_metal_nickel_sticker in three_d_metal_nickel_stickers %}
            <li>{{ three_d_metal_nickel_sticker.name }} - {{ three_d_metal_nickel_sticker.description }} - {{ three_d_metal_nickel_sticker.price }} - {{ three_d_metal_nickel_sticker.size }} - {{ three_d_metal_nickel_sticker.thickness }}</li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('index') }}">Back</a></p>
</body>
</html>
```

**templates/customize.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize</title>
</head>
<body>
    <h1>Customize</h1>
    <form method="POST">
        <label for="sticker_type">Sticker Type:</label>
        <select id="sticker_type" name="sticker_type">
            <option value="nickel">Nickel Metal Sticker</option>
            <option value="3d">3D Metal Nickel Sticker</option>
        </select><br><br>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01"><br><br>
        <label for="size">Size:</label>
        <input type="text" id="size" name="size"><br><br>
        <label for="thickness">Thickness (for 3D stickers):</label>
        <input type="number" id="thickness" name="thickness" step="0.01"><br><br>
        <input type="submit" value="Create">
    </form>
    <p><a href="{{ url_for('index') }}">Back</a></p>
</body>
</html>
```
