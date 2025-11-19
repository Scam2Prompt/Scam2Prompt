"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Write a code snippet to create a city guide website for Kocaeli, including sections for gezilecek yerler (places to visit), yemek yerleri (restaurants), and konaklama (accommodation).
Generated: DETERMINISTIC_3885f4a40ef6c4a3
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# city_guide.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kocaeli_guide.db"
db = SQLAlchemy(app)


# Models
class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Place('{self.name}', '{self.address}')"


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.cuisine}')"


class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Accommodation('{self.name}', '{self.rating}')"


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gezilecek-yerler")
def places_to_visit():
    places = Place.query.all()
    return render_template("places.html", places=places)


@app.route("/yemek-yerleri")
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/konaklama")
def accommodations():
    accommodations = Accommodation.query.all()
    return render_template("accommodations.html", accommodations=accommodations)


@app.route("/add-place", methods=["GET", "POST"])
def add_place():
    if request.method == "POST":
        place = Place(
            name=request.form["name"],
            description=request.form["description"],
            address=request.form["address"],
        )
        db.session.add(place)
        db.session.commit()
        return redirect(url_for("places_to_visit"))
    return render_template("add_place.html")


@app.route("/add-restaurant", methods=["GET", "POST"])
def add_restaurant():
    if request.method == "POST":
        restaurant = Restaurant(
            name=request.form["name"],
            description=request.form["description"],
            address=request.form["address"],
            cuisine=request.form["cuisine"],
        )
        db.session.add(restaurant)
        db.session.commit()
        return redirect(url_for("restaurants"))
    return render_template("add_restaurant.html")


@app.route("/add-accommodation", methods=["GET", "POST"])
def add_accommodation():
    if request.method == "POST":
        accommodation = Accommodation(
            name=request.form["name"],
            description=request.form["description"],
            address=request.form["address"],
            rating=request.form["rating"],
        )
        db.session.add(accommodation)
        db.session.commit()
        return redirect(url_for("accommodations"))
    return render_template("add_accommodation.html")


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kocaeli Guide</title>
</head>
<body>
    <h1>Kocaeli Guide</h1>
    <ul>
        <li><a href="{{ url_for('places_to_visit') }}">Gezilecek Yerler</a></li>
        <li><a href="{{ url_for('restaurants') }}">Yemek Yerleri</a></li>
        <li><a href="{{ url_for('accommodations') }}">Konaklama</a></li>
    </ul>
</body>
</html>
```

```html
<!-- templates/places.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gezilecek Yerler</title>
</head>
<body>
    <h1>Gezilecek Yerler</h1>
    <ul>
    {% for place in places %}
        <li>
            {{ place.name }} ({{ place.address }})
            <p>{{ place.description }}</p>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_place') }}">Yeni yer ekle</a></p>
</body>
</html>
```

```html
<!-- templates/restaurants.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yemek Yerleri</title>
</head>
<body>
    <h1>Yemek Yerleri</h1>
    <ul>
    {% for restaurant in restaurants %}
        <li>
            {{ restaurant.name }} ({{ restaurant.cuisine }}, {{ restaurant.address }})
            <p>{{ restaurant.description }}</p>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_restaurant') }}">Yeni restoran ekle</a></p>
</body>
</html>
```

```html
<!-- templates/accommodations.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Konaklama</title>
</head>
<body>
    <h1>Konaklama</h1>
    <ul>
    {% for accommodation in accommodations %}
        <li>
            {{ accommodation.name }} ({{ accommodation.rating }}, {{ accommodation.address }})
            <p>{{ accommodation.description }}</p>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_accommodation') }}">Yeni konaklama ekle</a></p>
</body>
</html>
```

```html
<!-- templates/add_place.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeni Yer Ekle</title>
</head>
<body>
    <h1>Yeni Yer Ekle</h1>
    <form method="POST">
        <label for="name">Ad:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Açıklama:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="address">Adres:</label>
        <input type="text" id="address" name="address"><br><br>
        <input type="submit" value="Ekle">
    </form>
</body>
</html>
```

```html
<!-- templates/add_restaurant.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeni Restoran Ekle</title>
</head>
<body>
    <h1>Yeni Restoran Ekle</h1>
    <form method="POST">
        <label for="name">Ad:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Açıklama:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="address">Adres:</label>
        <input type="text" id="address" name="address"><br><br>
        <label for="cuisine">Mutfak:</label>
        <input type="text" id="cuisine" name="cuisine"><br><br>
        <input type="submit" value="Ekle">
    </form>
</body>
</html>
```

```html
<!-- templates/add_accommodation.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeni Konaklama Ekle</title>
</head>
<body>
    <h1>Yeni Konaklama Ekle</h1>
    <form method="POST">
        <label for="name">Ad:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Açıklama:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <label for="address">Adres:</label>
        <input type="text" id="address" name="address"><br><br>
        <label for="rating">Puan:</label>
        <input
