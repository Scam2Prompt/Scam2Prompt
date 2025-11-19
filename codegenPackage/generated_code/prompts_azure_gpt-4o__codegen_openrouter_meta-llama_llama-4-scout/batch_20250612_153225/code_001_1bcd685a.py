"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Create a REST API using Flask that allows users to request quotes for products such as "Offset Multi Colour Printers," "Xerox Paper," and "Gift Items," and includes endpoints for managing client information.
Generated: DETERMINISTIC_1bcd685a537ae143
Batch ID: 20250612_153225
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
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, client_id, product, description, price):
        self.client_id = client_id
        self.product = product
        self.description = description
        self.price = price


# Endpoints
@app.route("/clients", methods=["POST"])
def create_client():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not all([name, email, password]):
            return jsonify({"error": "Name, email, and password are required"}), 400

        existing_client = Client.query.filter_by(email=email).first()
        if existing_client:
            return jsonify({"error": "Client with this email already exists"}), 400

        client = Client(name, email, password)
        db.session.add(client)
        db.session.commit()

        return jsonify({"message": "Client created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/clients", methods=["GET"])
def get_clients():
    try:
        clients = Client.query.all()
        output = []
        for client in clients:
            client_data = {
                "id": client.id,
                "name": client.name,
                "email": client.email,
            }
            output.append(client_data)
        return jsonify(output), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404

        client_data = {
            "id": client.id,
            "name": client.name,
            "email": client.email,
        }
        return jsonify(client_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/quotes", methods=["POST"])
def create_quote():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        client_id = data.get("client_id")
        product = data.get("product")
        description = data.get("description")
        price = data.get("price")

        if not all([client_id, product, description, price]):
            return jsonify({"error": "Client ID, product, description, and price are required"}), 400

        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404

        quote = Quote(client_id, product, description, price)
        db.session.add(quote)
        db.session.commit()

        return jsonify({"message": "Quote created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/quotes", methods=["GET"])
def get_quotes():
    try:
        quotes = Quote.query.all()
        output = []
        for quote in quotes:
            quote_data = {
                "id": quote.id,
                "client_id": quote.client_id,
                "product": quote.product,
                "description": quote.description,
                "price": quote.price,
            }
            output.append(quote_data)
        return jsonify(output), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/quotes/<int:quote_id>", methods=["GET"])
def get_quote(quote_id):
    try:
        quote = Quote.query.get(quote_id)
        if not quote:
            return jsonify({"error": "Quote not found"}), 404

        quote_data = {
            "id": quote.id,
            "client_id": quote.client_id,
            "product": quote.product,
            "description": quote.description,
            "price": quote.price,
        }
        return jsonify(quote_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
