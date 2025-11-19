"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Create a web application to handle customer inquiries and support requests for automotive parts, incorporating features like FAQs and warranty conditions, as described in the "پشتیبانی پرسش‌های پر تکرار" section of the website.
Generated: DETERMINISTIC_dbd54f1564bbf7a5
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

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///support.db"
db = SQLAlchemy(app)


# Models
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Inquiry('{self.name}', '{self.email}')"


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"FAQ('{self.question}')"


class WarrantyCondition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"WarrantyCondition('{self.condition}')"


# Routes
@app.route("/")
def index():
    faqs = FAQ.query.all()
    warranty_conditions = WarrantyCondition.query.all()
    return render_template("index.html", faqs=faqs, warranty_conditions=warranty_conditions)


@app.route("/inquiry", methods=["POST"])
def create_inquiry():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not all([name, email, message]):
            return jsonify({"error": "Please fill in all fields"}), 400

        inquiry = Inquiry(name=name, email=email, message=message)
        db.session.add(inquiry)
        db.session.commit()

        return jsonify({"message": "Inquiry created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/faqs", methods=["GET"])
def get_faqs():
    try:
        faqs = FAQ.query.all()
        return jsonify([{"question": faq.question, "answer": faq.answer} for faq in faqs])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/warranty-conditions", methods=["GET"])
def get_warranty_conditions():
    try:
        warranty_conditions = WarrantyCondition.query.all()
        return jsonify([{"condition": condition.condition} for condition in warranty_conditions])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Support</title>
</head>
<body>
    <h1>Frequently Asked Questions</h1>
    <ul>
    {% for faq in faqs %}
        <li>
            <strong>{{ faq.question }}</strong>
            <p>{{ faq.answer }}</p>
        </li>
    {% endfor %}
    </ul>

    <h1>Warranty Conditions</h1>
    <ul>
    {% for condition in warranty_conditions %}
        <li>
            <p>{{ condition.condition }}</p>
        </li>
    {% endfor %}
    </ul>

    <h1>Support Inquiry</h1>
    <form id="inquiry-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <script>
        const form = document.getElementById('inquiry-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            try {
                const response = await fetch('/inquiry', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                console.log(result);
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
