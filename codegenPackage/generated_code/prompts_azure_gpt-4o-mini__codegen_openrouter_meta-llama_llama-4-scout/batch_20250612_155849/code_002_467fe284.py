"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Generate a code snippet for a web application that allows users to report technical issues 24/7, inspired by the support services provided by BlocPrest.
Generated: DETERMINISTIC_467fe28417a8b25b
Batch ID: 20250612_155849
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
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///support.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class SupportTicket(db.Model):
    """Model for support tickets"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    issue = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"SupportTicket('{self.name}', '{self.email}')"

    def to_dict(self):
        """Convert to dictionary for JSON response"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "issue": self.issue,
            "created_at": self.created_at.isoformat(),
        }


@app.route("/submit", methods=["POST"])
def submit_ticket():
    """Submit a new support ticket"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        required_fields = ["name", "email", "issue"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        ticket = SupportTicket(
            name=data["name"],
            email=data["email"],
            issue=data["issue"],
        )
        db.session.add(ticket)
        db.session.commit()

        return jsonify({"message": "Ticket submitted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/tickets", methods=["GET"])
def get_tickets():
    """Retrieve all support tickets"""
    try:
        tickets = SupportTicket.query.all()
        return jsonify([ticket.to_dict() for ticket in tickets])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```javascript
// script.js

const form = document.getElementById("support-form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch("/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.ok) {
            console.log(result);
            form.reset();
        } else {
            console.error(result.error);
        }
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Support Form</title>
</head>
<body>
    <h1>Report Technical Issue</h1>
    <form id="support-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="issue">Issue:</label>
        <textarea id="issue" name="issue" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <script src="script.js"></script>
</body>
</html>
```
