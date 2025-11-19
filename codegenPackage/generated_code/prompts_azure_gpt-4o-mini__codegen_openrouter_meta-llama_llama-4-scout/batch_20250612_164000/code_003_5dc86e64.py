"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Develop a REST API endpoint that allows users to query herbal supplement products, specifically those containing Habbatussauda, and return their health benefits and customer reviews.
Generated: DETERMINISTIC_5dc86e64c8a4aa1d
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Habbatussauda Supplements API Endpoint**
==========================================

### Dependencies

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serializing and deserializing data

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habbatussauda_supplements.db"
db = SQLAlchemy(app)


# Define the database models
class Supplement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    habbatussauda = db.Column(db.Boolean, default=False)
    health_benefits = db.Column(db.Text, nullable=False)
    reviews = db.relationship("Review", backref="supplement", lazy=True)

    def __init__(self, name, habbatussauda, health_benefits):
        self.name = name
        self.habbatussauda = habbatussauda
        self.health_benefits = health_benefits


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplement_id = db.Column(db.Integer, db.ForeignKey("supplement.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, supplement_id, rating, comment):
        self.supplement_id = supplement_id
        self.rating = rating
        self.comment = comment


# Define the schema for serialization and deserialization
class SupplementSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    habbatussauda = fields.Bool()
    health_benefits = fields.Str()
    reviews = fields.List(fields.Nested("ReviewSchema"))


class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    rating = fields.Int()
    comment = fields.Str()


# Create the database tables
with app.app_context():
    db.create_all()


# API endpoint to query Habbatussauda supplements
@app.route("/api/habbatussauda-supplements", methods=["GET"])
def get_habbatussauda_supplements():
    try:
        supplements = Supplement.query.filter_by(habbatussauda=True).all()
        schema = SupplementSchema(many=True)
        result = schema.dump(supplements)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to get health benefits and reviews for a supplement
@app.route("/api/supplements/<int:supplement_id>", methods=["GET"])
def get_supplement_details(supplement_id):
    try:
        supplement = Supplement.query.get(supplement_id)
        if supplement is None:
            return jsonify({"error": "Supplement not found"}), 404
        schema = SupplementSchema()
        result = schema.dump(supplement)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

### Example Use Cases

*   **Get Habbatussauda Supplements:**

    *   **Request:** `GET /api/habbatussauda-supplements`
    *   **Response:**

        ```json
[
  {
    "id": 1,
    "name": "Supplement 1",
    "habbatussauda": true,
    "health_benefits": "Health benefits of supplement 1",
    "reviews": [
      {
        "id": 1,
        "rating": 5,
        "comment": "Excellent product!"
      }
    ]
  },
  {
    "id": 2,
    "name": "Supplement 2",
    "habbatussauda": true,
    "health_benefits": "Health benefits of supplement 2",
    "reviews": [
      {
        "id": 2,
        "rating": 4,
        "comment": "Good product!"
      }
    ]
  }
]
```

*   **Get Supplement Details:**

    *   **Request:** `GET /api/supplements/1`
    *   **Response:**

        ```json
{
  "id": 1,
  "name": "Supplement 1",
  "habbatussauda": true,
  "health_benefits": "Health benefits of supplement 1",
  "reviews": [
    {
      "id": 1,
      "rating": 5,
      "comment": "Excellent product!"
    }
  ]
}
```
