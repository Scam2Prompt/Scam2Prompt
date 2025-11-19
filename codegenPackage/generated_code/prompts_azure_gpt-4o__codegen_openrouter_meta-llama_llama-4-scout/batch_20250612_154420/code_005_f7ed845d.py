"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Develop code for a web form that allows customers to submit service requests for HVAC repairs or tune-ups, including fields for contact information, service type (e.g., air conditioning repair, duct cleaning), and preferred appointment time.
Generated: DETERMINISTIC_f7ed845dbfd557dd
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**HVAC Service Request Form**
================================

### Backend (Python, Flask)

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hvac_service_requests.db"
db = SQLAlchemy(app)

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    preferred_appointment_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, phone, service_type, preferred_appointment_time):
        self.name = name
        self.email = email
        self.phone = phone
        self.service_type = service_type
        self.preferred_appointment_time = preferred_appointment_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "service_type": self.service_type,
            "preferred_appointment_time": self.preferred_appointment_time.strftime("%Y-%m-%d %H:%M:%S")
        }

@app.route("/submit_request", methods=["POST"])
def submit_request():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        required_fields = ["name", "email", "phone", "service_type", "preferred_appointment_time"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        service_request = ServiceRequest(
            data["name"],
            data["email"],
            data["phone"],
            data["service_type"],
            datetime.strptime(data["preferred_appointment_time"], "%Y-%m-%d %H:%M:%S")
        )
        db.session.add(service_request)
        db.session.commit()
        return jsonify({"message": "Service request submitted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Frontend (HTML, JavaScript)

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HVAC Service Request Form</title>
    <style>
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
        input, select {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        button[type="submit"] {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <form id="service-request-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="">Select a service type</option>
            <option value="air conditioning repair">Air Conditioning Repair</option>
            <option value="duct cleaning">Duct Cleaning</option>
            <option value="tune-up">Tune-up</option>
        </select>

        <label for="preferred_appointment_time">Preferred Appointment Time:</label>
        <input type="datetime-local" id="preferred_appointment_time" name="preferred_appointment_time" required>

        <button type="submit">Submit Request</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

const form = document.getElementById("service-request-form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = {
        name: formData.get("name"),
        email: formData.get("email"),
        phone: formData.get("phone"),
        service_type: formData.get("service_type"),
        preferred_appointment_time: formData.get("preferred_appointment_time")
    };

    try {
        const response = await fetch("/submit_request", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (response.ok) {
            console.log(result);
            alert("Service request submitted successfully!");
            form.reset();
        } else {
            console.error(result);
            alert("Error submitting service request: " + result.error);
        }
    } catch (error) {
        console.error(error);
        alert("Error submitting service request: " + error.message);
    }
});
```
