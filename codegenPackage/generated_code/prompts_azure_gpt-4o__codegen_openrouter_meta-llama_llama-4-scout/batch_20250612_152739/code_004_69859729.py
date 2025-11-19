"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Create an API endpoint in Flask to retrieve customer reviews for Suzuki Capital Motors' sales and after-sales services, based on the testimonials provided on the website.
Generated: DETERMINISTIC_698597294a4d2fbd
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///suzuki_capital_motors.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Testimonial(db.Model):
    """Represents a customer testimonial."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    service_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Testimonial('{self.name}', '{self.review}', {self.rating}, '{self.service_type}')"


@app.route("/api/testimonials", methods=["GET"])
def get_testimonials():
    """
    Retrieves customer testimonials.

    Query Parameters:
    - service_type (str): Type of service (sales or after-sales)
    - rating (int): Rating filter (1-5)

    Returns:
    - A JSON response containing a list of testimonials.
    """

    try:
        service_type = request.args.get("service_type")
        rating = request.args.get("rating", type=int)

        query = Testimonial.query

        if service_type:
            query = query.filter_by(service_type=service_type)

        if rating:
            query = query.filter_by(rating=rating)

        testimonials = query.all()

        result = [
            {
                "id": testimonial.id,
                "name": testimonial.name,
                "review": testimonial.review,
                "rating": testimonial.rating,
                "service_type": testimonial.service_type,
            }
            for testimonial in testimonials
        ]

        return jsonify(result)

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt

Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

```python
# test_app.py

import unittest
from app import app, db, Testimonial

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_testimonials(self):
        with app.app_context():
            testimonial1 = Testimonial(name="John Doe", review="Great service!", rating=5, service_type="sales")
            testimonial2 = Testimonial(name="Jane Doe", review="Good after-sales service.", rating=4, service_type="after-sales")
            db.session.add_all([testimonial1, testimonial2])
            db.session.commit()

        response = app.test_client().get("/api/testimonials")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_testimonials_by_service_type(self):
        with app.app_context():
            testimonial1 = Testimonial(name="John Doe", review="Great service!", rating=5, service_type="sales")
            testimonial2 = Testimonial(name="Jane Doe", review="Good after-sales service.", rating=4, service_type="after-sales")
            db.session.add_all([testimonial1, testimonial2])
            db.session.commit()

        response = app.test_client().get("/api/testimonials?service_type=sales")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_testimonials_by_rating(self):
        with app.app_context():
            testimonial1 = Testimonial(name="John Doe", review="Great service!", rating=5, service_type="sales")
            testimonial2 = Testimonial(name="Jane Doe", review="Good after-sales service.", rating=4, service_type="after-sales")
            db.session.add_all([testimonial1, testimonial2])
            db.session.commit()

        response = app.test_client().get("/api/testimonials?rating=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

if __name__ == "__main__":
    unittest.main()
```
