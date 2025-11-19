"""
Generated Code Metadata:
========================
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Generate code for an online appointment system for a pet grooming service, including features for scheduling and contact forms as described on the Petland Brasil website.
Generated: DETERMINISTIC_f465ada02e9b7816
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Online Appointment System for Pet Grooming Service**
=====================================================

**Database Schema**
------------------

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL
);

CREATE TABLE services (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE appointments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_id INT NOT NULL,
  date DATE NOT NULL,
  time TIME NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

CREATE TABLE contacts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  message TEXT NOT NULL
);
```

**Backend API (Python with Flask)**
---------------------------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@localhost/pet_grooming"
db = SQLAlchemy(app)

class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  address = db.Column(db.String(255), nullable=False)

class Service(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text)
  price = db.Column(db.DECIMAL(10, 2), nullable=False)

class Appointment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
  service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
  date = db.Column(db.Date, nullable=False)
  time = db.Column(db.Time, nullable=False)

class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  message = db.Column(db.Text, nullable=False)

@app.route("/schedule", methods=["POST"])
def schedule_appointment():
  try:
    data = request.get_json()
    customer = Customer(name=data["name"], email=data["email"], phone=data["phone"], address=data["address"])
    db.session.add(customer)
    db.session.commit()

    service = Service.query.get(data["service_id"])
    if not service:
      return jsonify({"error": "Service not found"}), 404

    appointment = Appointment(customer_id=customer.id, service_id=data["service_id"], date=datetime.strptime(data["date"], "%Y-%m-%d").date(), time=datetime.strptime(data["time"], "%H:%M").time())
    db.session.add(appointment)
    db.session.commit()

    return jsonify({"message": "Appointment scheduled successfully"}), 201
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500

@app.route("/contact", methods=["POST"])
def send_contact_message():
  try:
    data = request.get_json()
    contact = Contact(name=data["name"], email=data["email"], message=data["message"])
    db.session.add(contact)
    db.session.commit()

    return jsonify({"message": "Message sent successfully"}), 201
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500

@app.route("/services", methods=["GET"])
def get_services():
  try:
    services = Service.query.all()
    return jsonify([{"id": s.id, "name": s.name, "description": s.description, "price": s.price} for s in services])
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(debug=True)
```

**Frontend (JavaScript with HTML/CSS)**
--------------------------------------

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pet Grooming Appointment System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Schedule an Appointment</h1>
  <form id="schedule-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <label for="address">Address:</label>
    <input type="text" id="address" name="address"><br><br>
    <label for="service_id">Service:</label>
    <select id="service_id" name="service_id"></select><br><br>
    <label for="date">Date:</label>
    <input type="date" id="date" name="date"><br><br>
    <label for="time">Time:</label>
    <input type="time" id="time" name="time"><br><br>
    <button type="submit">Schedule</button>
  </form>

  <h1>Contact Us</h1>
  <form id="contact-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="message">Message:</label>
    <textarea id="message" name="message"></textarea><br><br>
    <button type="submit">Send</button>
  </form>

  <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

const scheduleForm = document.getElementById("schedule-form");
const contactForm = document.getElementById("contact-form");

scheduleForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(scheduleForm);
  const data = {
    name: formData.get("name"),
    email: formData.get("email"),
    phone: formData.get("phone"),
    address: formData.get("address"),
    service_id: formData.get("service_id"),
    date: formData.get("date"),
    time: formData.get("time"),
  };

  try {
    const response = await fetch("/schedule", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
});

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(contactForm);
  const data = {
    name: formData.get("name"),
    email: formData.get("email"),
    message: formData.get("message"),
  };

  try {
    const response = await fetch("/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
});

// Get services and populate select dropdown
fetch("/services")
  .then((response) => response.json())
  .then((services) => {
    const serviceSelect = document.getElementById("service_id");
    services.forEach((service) => {
      const option = document.createElement("option");
      option.value = service.id;
      option.text = service.name;
      serviceSelect.appendChild(option);
    });
  })
  .catch((error) => console.error(error));
```
