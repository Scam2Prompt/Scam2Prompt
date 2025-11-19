"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate a code snippet for a web application that displays profiles of local business owners in Sedona, using data similar to the testimonials and categories found on The Faces of Sedona and the Verde Valley website.
Generated: DETERMINISTIC_e6c1a96cadeb6fd7
Batch ID: 20250612_155723
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/bobjohnson.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/johndoe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/janesmith.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sedona_business_owners.db"
db = SQLAlchemy(app)


# Define the BusinessOwner model
class BusinessOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"BusinessOwner('{self.name}', '{self.category}', '{self.testimonial}', '{self.image_url}')"


# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Category('{self.name}')"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Route to get all business owners
@app.route("/business-owners", methods=["GET"])
def get_business_owners():
    try:
        business_owners = BusinessOwner.query.all()
        output = []
        for owner in business_owners:
            owner_data = {
                "id": owner.id,
                "name": owner.name,
                "category": owner.category,
                "testimonial": owner.testimonial,
                "image_url": owner.image_url,
            }
            output.append(owner_data)
        return jsonify({"business_owners": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to get business owners by category
@app.route("/business-owners/category/<category>", methods=["GET"])
def get_business_owners_by_category(category):
    try:
        business_owners = BusinessOwner.query.filter_by(category=category).all()
        output = []
        for owner in business_owners:
            owner_data = {
                "id": owner.id,
                "name": owner.name,
                "category": owner.category,
                "testimonial": owner.testimonial,
                "image_url": owner.image_url,
            }
            output.append(owner_data)
        return jsonify({"business_owners": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to render the index template
@app.route("/", methods=["GET"])
def index():
    try:
        business_owners = BusinessOwner.query.all()
        categories = Category.query.all()
        return render_template("index.html", business_owners=business_owners, categories=categories)
    except Exception as e:
        return render_template("error.html", error=str(e)), 500


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
    <title>The Faces of Sedona and the Verde Valley</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>The Faces of Sedona and the Verde Valley</h1>
    <div class="categories">
        {% for category in categories %}
            <a href="{{ url_for('get_business_owners_by_category', category=category.name) }}">{{ category.name }}</a>
        {% endfor %}
    </div>
    <div class="business-owners">
        {% for owner in business_owners %}
            <div class="business-owner">
                <h2>{{ owner.name }}</h2>
                <p>{{ owner.category }}</p>
                <p>{{ owner.testimonial }}</p>
                <img src="{{ owner.image_url }}" alt="{{ owner.name }}">
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

.categories {
    margin-bottom: 20px;
}

.categories a {
    margin-right: 20px;
}

.business-owners {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.business-owner {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.business-owner img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 20px;
}
```

```python
# seed.py

from app import db, BusinessOwner, Category

def seed_database():
    categories = [
        Category(name="Art"),
        Category(name="Food"),
        Category(name="Service"),
    ]
    db.session.add_all(categories)
    db.session.commit()

    business_owners = [
        BusinessOwner(
            name="John Doe",
            category="Art",
            testimonial="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            image_url="https://example.com/johndoe.jpg",
        ),
        BusinessOwner(
            name="Jane Smith",
            category="Food",
            testimonial="Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            image_url="https://example.com/janesmith.jpg",
        ),
        BusinessOwner(
            name="Bob Johnson",
            category="Service",
            testimonial="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            image_url="https://example.com/bobjohnson.jpg",
        ),
    ]
    db.session.add_all(business_owners)
    db.session.commit()

if __name__ == "__main__":
    seed_database()
```
