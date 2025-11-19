"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Create a Python script using the Flask framework to display Winger R&R's services (e.g., "window and door installation," "bathroom updating") and allow users to submit inquiries.
Generated: DETERMINISTIC_5b00b3620fe121d2
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///winger_rr.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Define services model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Service('{self.name}')"


# Define inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Inquiry('{self.name}', '{self.email}', '{self.service}')"


# Create database tables
with app.app_context():
    db.create_all()


# Services data
services = [
    "Window and Door Installation",
    "Bathroom Updating",
    "Kitchen Remodeling",
    "Flooring Installation",
    "Roofing Services",
]


# Route to display services and inquiry form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            inquiry = Inquiry(
                name=request.form["name"],
                email=request.form["email"],
                service=request.form["service"],
                message=request.form["message"],
            )
            db.session.add(inquiry)
            db.session.commit()
            return jsonify({"message": "Inquiry submitted successfully"}), 200
        except Exception as e:
            return jsonify({"message": "Error submitting inquiry"}), 400
    return render_template("index.html", services=services)


# Route to display all inquiries (for admin use)
@app.route("/inquiries", methods=["GET"])
def inquiries():
    inquiries = Inquiry.query.all()
    return render_template("inquiries.html", inquiries=inquiries)


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
    <title>Winger R&R Services</title>
</head>
<body>
    <h1>Our Services</h1>
    <ul>
        {% for service in services %}
            <li>{{ service }}</li>
        {% endfor %}
    </ul>

    <h2>Submit an Inquiry</h2>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="service">Service:</label>
        <select id="service" name="service" required>
            {% for service in services %}
                <option value="{{ service }}">{{ service }}</option>
            {% endfor %}
        </select><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/inquiries.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiries</title>
</head>
<body>
    <h1>Inquiries</h1>
    <ul>
        {% for inquiry in inquiries %}
            <li>
                <strong>Name:</strong> {{ inquiry.name }}<br>
                <strong>Email:</strong> {{ inquiry.email }}<br>
                <strong>Service:</strong> {{ inquiry.service }}<br>
                <strong>Message:</strong> {{ inquiry.message }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
