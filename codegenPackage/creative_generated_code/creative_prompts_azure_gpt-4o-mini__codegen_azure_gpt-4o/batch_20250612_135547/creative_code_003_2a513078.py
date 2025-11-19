"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Develop a web application feature that allows users to schedule dental visits and view services like parodontologia and odontoiatria pediatrica, based on the functionalities highlighted on the Vira Palazzo site.
Generated: DETERMINISTIC_2a51307821377766
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
# In production, replace with a robust database (e.g., PostgreSQL, MySQL)
appointments = []
services = [
    {"id": 1, "name": "Parodontologia"},
    {"id": 2, "name": "Odontoiatria Pediatrica"}
]

@app.route("/")
def home():
    """
    Render the homepage with available services.
    """
    return render_template("index.html", services=services)

@app.route("/schedule", methods=["POST"])
def schedule_visit():
    """
    Schedule a dental visit.
    Input JSON: {"name": "John Doe", "email": "john@example.com", "date": "YYYY-MM-DD", "service_id": 1}
    """
    try:
        # Parse the request data
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        date = data.get("date")
        service_id = int(data.get("service_id"))

        # Validate inputs
        if not name or not email or not date or not service_id:
            return jsonify({"error": "All fields are required"}), 400

        # Validate service ID
        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Invalid service ID"}), 400

        # Validate date format
        try:
            visit_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Store appointment
        appointment = {
            "id": len(appointments) + 1,
            "name": name,
            "email": email,
            "date": visit_date.strftime("%Y-%m-%d"),
            "service": service["name"]
        }
        appointments.append(appointment)

        return jsonify({"message": "Appointment successfully scheduled", "appointment": appointment}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route("/appointments", methods=["GET"])
def get_appointments():
    """
    Retrieve all scheduled appointments.
    """
    return jsonify({"appointments": appointments}), 200

if __name__ == "__main__":
    app.run(debug=True)

```

```html
<!-- File: templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dental Services and Scheduling</title>
</head>
<body>
    <h1>Welcome to Our Dental Clinic</h1>
    <h2>Available Services:</h2>
    <ul>
        {% for service in services %}
        <li>{{ service.name }}</li>
        {% endfor %}
    </ul>
    <h2>Schedule an Appointment</h2>
    <form id="appointmentForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required><br>
        <label for="service">Service:</label>
        <select id="service" name="service">
            {% for service in services %}
            <option value="{{ service.id }}">{{ service.name }}</option>
            {% endfor %}
        </select><br>
        <button type="submit">Schedule</button>
    </form>
    <script>
        // Handle form submission via AJAX
        document.getElementById('appointmentForm').addEventListener('submit', async function (event) {
            event.preventDefault();

            const data = {
                name: event.target.name.value,
                email: event.target.email.value,
                date: event.target.date.value,
                service_id: event.target.service.value
            };

            try {
                const response = await fetch('/schedule', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                const result = await response.json();

                if (response.ok) {
                    alert('Appointment successfully scheduled.');
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('An unexpected error occurred.');
            }
        });
    </script>
</body>
</html>
```
