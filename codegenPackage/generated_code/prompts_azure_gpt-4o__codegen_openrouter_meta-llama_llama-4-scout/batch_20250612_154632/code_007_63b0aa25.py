"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Develop a web form for mentor applications, ensuring applicants can submit their information to join a team like the one described on uEmbark.
Generated: DETERMINISTIC_63b0aa25b52da691
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mentor Application Form**
==========================

### Backend (Python, Flask)

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mentor_applications.db"
db = SQLAlchemy(app)

class MentorApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    experience = db.Column(db.Text, nullable=False)
    motivation = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, phone_number, experience, motivation):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.experience = experience
        self.motivation = motivation

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "experience": self.experience,
            "motivation": self.motivation,
        }

@app.route("/apply", methods=["POST"])
def apply():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        required_fields = ["name", "email", "phone_number", "experience", "motivation"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        application = MentorApplication(
            data["name"],
            data["email"],
            data["phone_number"],
            data["experience"],
            data["motivation"],
        )
        db.session.add(application)
        db.session.commit()
        return jsonify({"message": "Application submitted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Frontend (HTML, CSS, JavaScript)

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mentor Application Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Mentor Application Form</h1>
    <form id="application-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone_number">Phone Number:</label>
        <input type="tel" id="phone_number" name="phone_number" required>

        <label for="experience">Experience:</label>
        <textarea id="experience" name="experience" required></textarea>

        <label for="motivation">Motivation:</label>
        <textarea id="motivation" name="motivation" required></textarea>

        <button type="submit">Submit Application</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
}

form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

```javascript
// script.js
const form = document.getElementById("application-form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/apply", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.ok) {
            console.log(result);
            alert("Application submitted successfully!");
            form.reset();
        } else {
            console.error(result);
            alert(result.error);
        }
    } catch (error) {
        console.error(error);
        alert("Error submitting application");
    }
});
```
