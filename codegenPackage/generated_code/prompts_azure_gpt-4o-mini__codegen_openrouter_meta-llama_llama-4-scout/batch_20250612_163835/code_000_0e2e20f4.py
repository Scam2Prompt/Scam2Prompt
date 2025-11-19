"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Generate a code snippet for a web application that displays a list of used cars, including details like model, year, mileage, and price, similar to the Helfen Motors inventory.
Generated: DETERMINISTIC_0e2e20f49e9ff435
Batch ID: 20250612_163835
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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///used_cars.db"
db = SQLAlchemy(app)


class UsedCar(db.Model):
    """Model for used car inventory."""

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"UsedCar('{self.model}', {self.year}, {self.mileage}, {self.price})"

    def to_dict(self):
        """Convert used car object to dictionary."""
        return {
            "id": self.id,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "price": self.price,
        }


# Create the database tables
with app.app_context():
    db.create_all()


# API endpoint to get all used cars
@app.route("/used-cars", methods=["GET"])
def get_used_cars():
    try:
        used_cars = UsedCar.query.all()
        return jsonify([car.to_dict() for car in used_cars])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to get a used car by ID
@app.route("/used-cars/<int:car_id>", methods=["GET"])
def get_used_car(car_id):
    try:
        used_car = UsedCar.query.get(car_id)
        if used_car is None:
            return jsonify({"error": "Car not found"}), 404
        return jsonify(used_car.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to add a new used car
@app.route("/used-cars", methods=["POST"])
def add_used_car():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        new_car = UsedCar(
            model=data["model"],
            year=data["year"],
            mileage=data["mileage"],
            price=data["price"],
        )
        db.session.add(new_car)
        db.session.commit()
        return jsonify(new_car.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# API endpoint to update an existing used car
@app.route("/used-cars/<int:car_id>", methods=["PUT"])
def update_used_car(car_id):
    try:
        used_car = UsedCar.query.get(car_id)
        if used_car is None:
            return jsonify({"error": "Car not found"}), 404
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        used_car.model = data.get("model", used_car.model)
        used_car.year = data.get("year", used_car.year)
        used_car.mileage = data.get("mileage", used_car.mileage)
        used_car.price = data.get("price", used_car.price)
        db.session.commit()
        return jsonify(used_car.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# API endpoint to delete a used car
@app.route("/used-cars/<int:car_id>", methods=["DELETE"])
def delete_used_car(car_id):
    try:
        used_car = UsedCar.query.get(car_id)
        if used_car is None:
            return jsonify({"error": "Car not found"}), 404
        db.session.delete(used_car)
        db.session.commit()
        return jsonify({"message": "Car deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

```javascript
// used-cars.js (frontend example)

fetch("/used-cars")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// Add a new used car
const newCar = {
  model: "Toyota Camry",
  year: 2015,
  mileage: 80000,
  price: 15000,
};

fetch("/used-cars", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(newCar),
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

```html
<!-- index.html (frontend example) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Used Cars</title>
</head>
<body>
    <h1>Used Cars</h1>
    <ul id="used-cars-list"></ul>

    <script>
        fetch("/used-cars")
            .then(response => response.json())
            .then(data => {
                const usedCarsList = document.getElementById("used-cars-list");
                data.forEach(car => {
                    const listItem = document.createElement("li");
                    listItem.textContent = `${car.model} (${car.year}) - ${car.mileage} miles, $${car.price}`;
                    usedCarsList.appendChild(listItem);
                });
            })
            .catch(error => console.error(error));
    </script>
</body>
</html>
```
