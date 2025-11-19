"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a code snippet for a web application that allows users to submit a prayer request, reflecting the themes of seeking peace and purpose as described on Life's Quest.
Generated: DETERMINISTIC_ac178baebd76b48e
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# prayer_request.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prayer_requests.db"
db = SQLAlchemy(app)


class PrayerRequest(db.Model):
    """Represents a prayer request."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    request_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"PrayerRequest('{self.name}', '{self.email}')"

    def to_dict(self):
        """Converts a PrayerRequest to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "request_text": self.request_text,
        }


@app.route("/prayer-requests", methods=["POST"])
def create_prayer_request():
    """Creates a new prayer request."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        required_fields = ["name", "email", "request_text"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        prayer_request = PrayerRequest(
            name=data["name"],
            email=data["email"],
            request_text=data["request_text"],
        )
        db.session.add(prayer_request)
        db.session.commit()

        return jsonify({"message": "Prayer request created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/prayer-requests", methods=["GET"])
def get_prayer_requests():
    """Retrieves all prayer requests."""
    try:
        prayer_requests = PrayerRequest.query.all()
        return jsonify([request.to_dict() for request in prayer_requests])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```javascript
// prayerRequest.js (for frontend)

// Using fetch API to send a prayer request
const sendPrayerRequest = async (name, email, requestText) => {
    try {
        const response = await fetch('/prayer-requests', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, request_text: requestText }),
        });

        if (!response.ok) {
            throw new Error(response.statusText);
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
};

// Example usage:
sendPrayerRequest('John Doe', 'john@example.com', 'Please grant me peace and purpose.');
```

```html
<!-- index.html (for frontend) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prayer Request</title>
</head>
<body>
    <h1>Submit a Prayer Request</h1>
    <form id="prayer-request-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="request-text">Request:</label>
        <textarea id="request-text" name="request_text"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <script src="prayerRequest.js"></script>
    <script>
        const form = document.getElementById('prayer-request-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const requestText = document.getElementById('request-text').value;
            sendPrayerRequest(name, email, requestText);
        });
    </script>
</body>
</html>
```
