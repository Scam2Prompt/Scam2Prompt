"""
Generated Code Metadata:
========================
Original URL: https://ezway.com.br
Prompt: Generate a code snippet for a basic testimonial page like the one on EZ Way, showcasing student reviews and ratings.
Generated: DETERMINISTIC_1cd73d94e36e6a59
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# testimonial.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testimonials.db"
db = SQLAlchemy(app)


class Testimonial(db.Model):
    """Represents a student testimonial."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Testimonial('{self.name}', '{self.review}', {self.rating})"


@app.route("/testimonials")
def testimonials():
    """Renders the testimonial page."""
    testimonials = Testimonial.query.all()
    return render_template("testimonials.html", testimonials=testimonials)


@app.errorhandler(404)
def not_found(e):
    """Handles 404 errors."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/testimonials.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testimonials</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>What Our Students Say</h1>
    <div class="testimonials">
        {% for testimonial in testimonials %}
        <div class="testimonial">
            <h2>{{ testimonial.name }}</h2>
            <p>{{ testimonial.review }}</p>
            <p>Rating: {{ testimonial.rating }}/5</p>
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

.testimonials {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.testimonial {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

.testimonial h2 {
    margin-top: 0;
}

.testimonial p {
    margin-bottom: 20px;
}
```

```python
# create_testimonials.py

from testimonial import db, Testimonial

def create_testimonials():
    testimonials = [
        Testimonial(name="John Doe", review="Excellent course!", rating=5),
        Testimonial(name="Jane Smith", review="Very informative.", rating=4),
        Testimonial(name="Bob Johnson", review="Great experience!", rating=5),
    ]

    with db.session.begin():
        for testimonial in testimonials:
            db.session.add(testimonial)

if __name__ == "__main__":
    with db.session.begin():
        create_testimonials()
```
