"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: How can I design a user-friendly interface for booking appointments online for a counseling service, based on the features of That Counseling Place?
Generated: DETERMINISTIC_e87e65f05a1413ca
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation using Flask for the backend and HTML/CSS/JavaScript for the frontend. This code provides a user-friendly interface for booking appointments online for a counseling service.

### Backend (Flask)

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock database for available counselors and appointments
counselors = [
    {"id": 1, "name": "Dr. Smith", "specialty": "Anxiety"},
    {"id": 2, "name": "Dr. Johnson", "specialty": "Depression"},
    {"id": 3, "name": "Dr. Lee", "specialty": "Relationship Issues"}
]

appointments = []  # Store booked appointments

@app.route('/')
def home():
    """Render the homepage with the booking interface."""
    return render_template('index.html', counselors=counselors)

@app.route('/book', methods=['POST'])
def book_appointment():
    """Handle appointment booking."""
    try:
        # Extract data from the request
        data = request.json
        counselor_id = data.get('counselor_id')
        client_name = data.get('client_name')
        appointment_date = data.get('appointment_date')

        # Validate input
        if not counselor_id or not client_name or not appointment_date:
            return jsonify({"error": "All fields are required"}), 400

        # Check if the date is valid
        try:
            appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Save the appointment
        appointment = {
            "counselor_id": counselor_id,
            "client_name": client_name,
            "appointment_date": appointment_date.strftime('%Y-%m-%d')
        }
        appointments.append(appointment)

        return jsonify({"message": "Appointment booked successfully", "appointment": appointment}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Retrieve all booked appointments."""
    return jsonify(appointments), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (HTML/CSS/JavaScript)

#### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Booking</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <div class="container">
        <h1>Book an Appointment</h1>
        <form id="bookingForm">
            <label for="counselor">Select Counselor:</label>
            <select id="counselor" name="counselor" required>
                <!-- Dynamically populate counselors -->
                {% for counselor in counselors %}
                <option value="{{ counselor.id }}">{{ counselor.name }} - {{ counselor.specialty }}</option>
                {% endfor %}
            </select>

            <label for="clientName">Your Name:</label>
            <input type="text" id="clientName" name="clientName" required>

            <label for="appointmentDate">Appointment Date:</label>
            <input type="date" id="appointmentDate" name="appointmentDate" required>

            <button type="submit">Book Appointment</button>
        </form>
        <div id="responseMessage"></div>
    </div>
    <script src="/static/scripts.js"></script>
</body>
</html>
```

#### `static/styles.css`

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-top: 10px;
    font-weight: bold;
}

input, select, button {
    margin-top: 5px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    cursor: pointer;
    margin-top: 20px;
}

button:hover {
    background-color: #0056b3;
}

#responseMessage {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
}
```

#### `static/scripts.js`

```javascript
document.getElementById('bookingForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const counselorId = document.getElementById('counselor').value;
    const clientName = document.getElementById('clientName').value;
    const appointmentDate = document.getElementById('appointmentDate').value;

    const responseMessage = document.getElementById('responseMessage');

    try {
        const response = await fetch('/book', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                counselor_id: counselorId,
                client_name: clientName,
                appointment_date: appointmentDate
            })
        });

        const data = await response.json();

        if (response.ok) {
            responseMessage.textContent = data.message;
            responseMessage.style.color = 'green';
        } else {
            responseMessage.textContent = data.error;
            responseMessage.style.color = 'red';
        }
    } catch (error) {
        responseMessage.textContent = 'An error occurred while booking the appointment.';
        responseMessage.style.color = 'red';
    }
});
```

This code provides a complete solution for booking appointments online, including a backend API, frontend interface, and styling.
