"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Generate code for a newsletter subscription form that adheres to GDPR compliance, inspired by the ALPS Foundation's email subscription system.
Generated: DETERMINISTIC_36145f8d3561b9cd
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# newsletter_subscription.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import hashlib
import hmac
import secrets

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///newsletter.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    subscribed = db.Column(db.Boolean, default=False)
    confirmation_token = db.Column(db.String(100), nullable=True)
    confirmation_token_expires = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"Subscriber('{self.email}', '{self.name}', {self.subscribed})"

    def generate_confirmation_token(self):
        secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
        token = secrets.token_urlsafe(32)
        self.confirmation_token = token
        self.confirmation_token_expires = datetime.now() + timedelta(days=1)
        db.session.commit()
        return token

    def confirm_subscription(self, token):
        if self.confirmation_token == token and self.confirmation_token_expires > datetime.now():
            self.subscribed = True
            self.confirmation_token = None
            self.confirmation_token_expires = None
            db.session.commit()
            return True
        return False

@app.route("/subscribe", methods=["POST"])
def subscribe():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        email = data.get("email")
        name = data.get("name")

        if not email or not name:
            return jsonify({"error": "Email and name are required"}), 400

        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            if existing_subscriber.subscribed:
                return jsonify({"message": "Already subscribed"}), 200
            else:
                token = existing_subscriber.generate_confirmation_token()
                # Send confirmation email with token
                # For demonstration purposes, just return the token
                return jsonify({"token": token}), 200

        new_subscriber = Subscriber(email=email, name=name)
        db.session.add(new_subscriber)
        db.session.commit()

        token = new_subscriber.generate_confirmation_token()
        # Send confirmation email with token
        # For demonstration purposes, just return the token
        return jsonify({"token": token}), 201

@app.route("/confirm-subscription", methods=["POST"])
def confirm_subscription():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        email = data.get("email")
        token = data.get("token")

        if not email or not token:
            return jsonify({"error": "Email and token are required"}), 400

        subscriber = Subscriber.query.filter_by(email=email).first()
        if not subscriber:
            return jsonify({"error": "Subscriber not found"}), 404

        if subscriber.confirm_subscription(token):
            return jsonify({"message": "Subscription confirmed"}), 200
        else:
            return jsonify({"error": "Invalid or expired token"}), 400

@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        email = data.get("email")

        if not email:
            return jsonify({"error": "Email is required"}), 400

        subscriber = Subscriber.query.filter_by(email=email).first()
        if not subscriber:
            return jsonify({"error": "Subscriber not found"}), 404

        subscriber.subscribed = False
        db.session.commit()
        return jsonify({"message": "Unsubscribed"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```

```sql
-- schema.sql

CREATE TABLE subscribers (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    subscribed BOOLEAN DEFAULT FALSE,
    confirmation_token VARCHAR(100),
    confirmation_token_expires TIMESTAMP
);
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.1
```

```bash
# .env

SECRET_KEY="your_secret_key_here"
DATABASE_URL="your_database_url_here"
```
