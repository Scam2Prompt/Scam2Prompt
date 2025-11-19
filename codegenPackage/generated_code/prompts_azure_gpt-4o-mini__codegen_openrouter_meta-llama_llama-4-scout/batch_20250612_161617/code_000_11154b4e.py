"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a code snippet for a web application that allows users to request a quote for Ataköy Evden Eve Nakliyat services, including options for city and intercity moves.
Generated: DETERMINISTIC_11154b4e2460c8cb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///atakoy_nakliyat.db"
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"City('{self.name}')"


class IntercityMove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_city = db.Column(db.String(100), nullable=False)
    to_city = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"IntercityMove('{self.from_city}', '{self.to_city}', {self.distance})"


class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    intercity_move_id = db.Column(db.Integer, db.ForeignKey('intercity_move.id'))
    intercity_move = db.relationship('IntercityMove', backref=db.backref('quote_requests', lazy=True))
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    move_details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"QuoteRequest('{self.city}', '{self.customer_name}', '{self.customer_email}')"


@app.route('/cities', methods=['GET'])
def get_cities():
    try:
        cities = City.query.all()
        return jsonify([city.name for city in cities])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/intercity-moves', methods=['GET'])
def get_intercity_moves():
    try:
        moves = IntercityMove.query.all()
        return jsonify([{"from_city": move.from_city, "to_city": move.to_city, "distance": move.distance} for move in moves])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/quote-request', methods=['POST'])
def request_quote():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        city = data.get('city')
        intercity_move_id = data.get('intercity_move_id')
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        customer_phone = data.get('customer_phone')
        move_details = data.get('move_details')

        if not city or not customer_name or not customer_email or not customer_phone or not move_details:
            return jsonify({"error": "Please fill in all required fields"}), 400

        intercity_move = IntercityMove.query.get(intercity_move_id)
        if intercity_move_id and not intercity_move:
            return jsonify({"error": "Invalid intercity move ID"}), 400

        quote_request = QuoteRequest(
            city=city,
            intercity_move_id=intercity_move_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            move_details=move_details
        )
        db.session.add(quote_request)
        db.session.commit()

        return jsonify({"message": "Quote request sent successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```javascript
// script.js

const citySelect = document.getElementById('city-select');
const intercityMoveSelect = document.getElementById('intercity-move-select');
const customerNameInput = document.getElementById('customer-name-input');
const customerEmailInput = document.getElementById('customer-email-input');
const customerPhoneInput = document.getElementById('customer-phone-input');
const moveDetailsInput = document.getElementById('move-details-input');
const submitButton = document.getElementById('submit-button');

submitButton.addEventListener('click', async (e) => {
    e.preventDefault();

    const city = citySelect.value;
    const intercityMoveId = intercityMoveSelect.value;
    const customerName = customerNameInput.value;
    const customerEmail = customerEmailInput.value;
    const customerPhone = customerPhoneInput.value;
    const moveDetails = moveDetailsInput.value;

    try {
        const response = await fetch('/quote-request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                city,
                intercity_move_id: intercityMoveId,
                customer_name: customerName,
                customer_email: customerEmail,
                customer_phone: customerPhone,
                move_details: moveDetails
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Quote request sent successfully!');
        } else {
            alert(data.error);
        }
    } catch (error) {
        console.error(error);
    }
});

// populate city and intercity move options
fetch('/cities')
    .then(response => response.json())
    .then(cities => {
        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            citySelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));

fetch('/intercity-moves')
    .then(response => response.json())
    .then(moves => {
        moves.forEach(move => {
            const option = document.createElement('option');
            option.value = move.distance;
            option.textContent = `${move.from_city} to ${move.to_city} (${move.distance} km)`;
            intercityMoveSelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ataköy Evden Eve Nakliyat Quote Request</title>
    <style>
        /* add some basic styling */
        body {
            font-family: Arial, sans-serif;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input, select {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        button {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <h1>Ataköy Evden Eve Nakliyat Quote Request</h1>
    <form>
        <label for="city-select">City:</label>
        <select id="city-select"></select>

        <label for="intercity-move-select">Intercity Move:</label>
        <select id="intercity-move-select"></select>

        <label for="customer-name-input">Customer Name:</label>
        <input type="text" id="customer-name-input">

        <label for="customer-email-input">Customer Email:</label>
        <input type="email" id="customer-email-input">

        <label for="customer-phone-input">Customer Phone:</label>
        <input type="tel" id="customer-phone-input">

        <label for="move-details-input">Move Details:</label>
        <textarea id="move-details-input"></textarea>

        <button id="submit-button">Request Quote</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```
