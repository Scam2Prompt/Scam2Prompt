"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Develop a simple web application that showcases Homefoods' range of ethnic soups, including Neri-Neri and Fava Soup, with user reviews.
Generated: DETERMINISTIC_cbd9a1a9142081fc
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**homefoods.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///homefoods.db"
db = SQLAlchemy(app)


# Define the Soup model
class Soup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Soup('{self.name}', '{self.description}')"


# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soup_id = db.Column(db.Integer, db.ForeignKey("soup.id"), nullable=False)
    soup = db.relationship("Soup", backref=db.backref("reviews", lazy=True))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Review('{self.soup.name}', '{self.rating}', '{self.comment}')"


# Create the database tables
with app.app_context():
    db.create_all()


# Home route
@app.route("/")
def home():
    soups = Soup.query.all()
    return render_template("home.html", soups=soups)


# Soup details route
@app.route("/soup/<int:soup_id>")
def soup_details(soup_id):
    soup = Soup.query.get_or_404(soup_id)
    reviews = soup.reviews.all()
    return render_template("soup_details.html", soup=soup, reviews=reviews)


# Add review route
@app.route("/soup/<int:soup_id>/add_review", methods=["POST"])
def add_review(soup_id):
    soup = Soup.query.get_or_404(soup_id)
    review = Review(
        soup=soup,
        rating=request.form["rating"],
        comment=request.form["comment"],
    )
    db.session.add(review)
    db.session.commit()
    return redirect(url_for("soup_details", soup_id=soup_id))


# Add soup route
@app.route("/add_soup", methods=["GET", "POST"])
def add_soup():
    if request.method == "POST":
        soup = Soup(
            name=request.form["name"],
            description=request.form["description"],
        )
        db.session.add(soup)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_soup.html")


if __name__ == "__main__":
    app.run(debug=True)
```

**templates/home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homefoods</title>
</head>
<body>
    <h1>Homefoods</h1>
    <h2>Our Soups</h2>
    <ul>
    {% for soup in soups %}
        <li>
            <a href="{{ url_for('soup_details', soup_id=soup.id) }}">{{ soup.name }}</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/soup_details.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ soup.name }}</title>
</head>
<body>
    <h1>{{ soup.name }}</h1>
    <p>{{ soup.description }}</p>
    <h2>Reviews</h2>
    <ul>
    {% for review in reviews %}
        <li>
            Rating: {{ review.rating }} - {{ review.comment }}
        </li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('add_review', soup_id=soup.id) }}" method="post">
        <label for="rating">Rating:</label>
        <input type="number" id="rating" name="rating" required>
        <br>
        <label for="comment">Comment:</label>
        <textarea id="comment" name="comment" required></textarea>
        <br>
        <input type="submit" value="Add Review">
    </form>
</body>
</html>
```

**templates/add_soup.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Soup</title>
</head>
<body>
    <h1>Add Soup</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <input type="submit" value="Add Soup">
    </form>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```
