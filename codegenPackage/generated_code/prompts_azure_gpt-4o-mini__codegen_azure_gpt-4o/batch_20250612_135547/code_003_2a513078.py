"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Develop a web application feature that allows users to schedule dental visits and view services like parodontologia and odontoiatria pediatrica, based on the functionalities highlighted on the Vira Palazzo site.
Generated: DETERMINISTIC_2a51307821377766
Batch ID: 20250612_135547
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
from datetime import datetime

app = Flask(__name__)

# Mock data for services
SERVICES = [
    {"id": 1, "name": "Parodontologia", "description": "Treatment for gum diseases."},
    {"id": 2, "name": "Odontoiatria Pediatrica", "description": "Dental care for children."}
]

# Mock data for scheduled visits
scheduled_visits = []

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve available dental services.
    """
    return jsonify({"services": SERVICES}), 200

@app.route('/schedule', methods=['POST'])
def schedule_visit():
    """
    Endpoint to schedule a dental visit.
    Expects JSON payload with 'name', 'email', 'service_id', and 'date'.
    """
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ['name', 'email', 'service_id', 'date']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Check if service exists
        service = next((s for s in SERVICES if s['id'] == data['service_id']), None)
        if not service:
            return jsonify({"error": "Invalid service ID"}), 400
        
        # Validate date format
        try:
            visit_date = datetime.strptime(data['date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
        
        # Create visit record
        visit = {
            "id": len(scheduled_visits) + 1,
            "name": data['name'],
            "email": data['email'],
            "service": service['name'],
            "date": visit_date.strftime('%Y-%m-%d')
        }
        scheduled_visits.append(visit)
        
        return jsonify({"message": "Visit scheduled successfully", "visit": visit}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/visits', methods=['GET'])
def get_scheduled_visits():
    """
    Endpoint to retrieve all scheduled visits.
    """
    return jsonify({"scheduled_visits": scheduled_visits}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dental Services</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .service, .visit {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Dental Services</h1>
    <div id="services"></div>

    <h2>Schedule a Visit</h2>
    <form id="scheduleForm">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="service">Service:</label><br>
        <select id="service" name="service" required></select><br><br>
        <label for="date">Date:</label><br>
        <input type="date" id="date" name="date" required><br><br>
        <button type="submit">Schedule</button>
    </form>

    <h2>Scheduled Visits</h2>
    <div id="visits"></div>

    <script>
        const servicesDiv = document.getElementById('services');
        const visitsDiv = document.getElementById('visits');
        const serviceSelect = document.getElementById('service');
        const scheduleForm = document.getElementById('scheduleForm');

        // Fetch services
        fetch('/services')
            .then(response => response.json())
            .then(data => {
                data.services.forEach(service => {
                    const serviceElement = document.createElement('div');
                    serviceElement.className = 'service';
                    serviceElement.innerHTML = `<h3>${service.name}</h3><p>${service.description}</p>`;
                    servicesDiv.appendChild(serviceElement);

                    const option = document.createElement('option');
                    option.value = service.id;
                    option.textContent = service.name;
                    serviceSelect.appendChild(option);
                });
            });

        // Fetch scheduled visits
        function loadVisits() {
            fetch('/visits')
                .then(response => response.json())
                .then(data => {
                    visitsDiv.innerHTML = '';
                    data.scheduled_visits.forEach(visit => {
                        const visitElement = document.createElement('div');
                        visitElement.className = 'visit';
                        visitElement.innerHTML = `<h3>${visit.name}</h3><p>Email: ${visit.email}</p><p>Service: ${visit.service}</p><p>Date: ${visit.date}</p>`;
                        visitsDiv.appendChild(visitElement);
                    });
                });
        }
        loadVisits();

        // Handle form submission
        scheduleForm.addEventListener('submit', event => {
            event.preventDefault();
            const formData = new FormData(scheduleForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                service_id: parseInt(formData.get('service')),
                date: formData.get('date')
            };

            fetch('/schedule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(result => {
                    if (result.message) {
                        alert(result.message);
                        loadVisits();
                        scheduleForm.reset();
                    } else if (result.error) {
                        alert(result.error);
                    }
                });
        });
    </script>
</body>
</html>
```
