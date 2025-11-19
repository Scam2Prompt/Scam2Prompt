"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a code snippet for a web application that allows users to book live music services for weddings and corporate events, similar to the offerings of Orquesta Dorada in Trujillo.
Generated: DETERMINISTIC_75839fb565d54d18
Batch ID: 20250612_162051
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
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///music_services.db"
db = SQLAlchemy(app)


# Models
class User(db.Model):
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


class MusicService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    music_service_id = db.Column(db.Integer, db.ForeignKey("music_service.id"), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    user = db.relationship("User", backref=db.backref("bookings", lazy=True))
    music_service = db.relationship("MusicService", backref=db.backref("bookings", lazy=True))

    def __init__(self, user_id, music_service_id, event_date):
        self.user_id = user_id
        self.music_service_id = music_service_id
        self.event_date = event_date


# Routes
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        new_user = User(data["name"], data["email"], data["password"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            return jsonify({"message": "Logged in successfully"}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/music-services", methods=["GET"])
def get_music_services():
    try:
        music_services = MusicService.query.all()
        output = []
        for service in music_services:
            service_data = {
                "id": service.id,
                "name": service.name,
                "description": service.description,
                "price": service.price,
            }
            output.append(service_data)
        return jsonify({"music_services": output}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/book-music-service", methods=["POST"])
def book_music_service():
    try:
        data = request.json
        new_booking = Booking(
            data["user_id"],
            data["music_service_id"],
            datetime.datetime.strptime(data["event_date"], "%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Music service booked successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.3
```

```sql
-- schema.sql

-- No schema needed, using SQLAlchemy to create tables
```
