"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Design a user interface component (using HTML, CSS, and JavaScript) for a tire and wheel services website that allows users to select services (e.g., tire change, balancing, repair) and book appointments.
Generated: DETERMINISTIC_80a9457fe36204ea
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire and Wheel Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Tire and Wheel Services</h1>
        <form id="service-form">
            <label for="services">Select Services:</label>
            <div class="services">
                <div class="service">
                    <input type="checkbox" id="tire-change" name="services[]" value="Tire Change">
                    <label for="tire-change">Tire Change</label>
                </div>
                <div class="service">
                    <input type="checkbox" id="balancing" name="services[]" value="Balancing">
                    <label for="balancing">Balancing</label>
                </div>
                <div class="service">
                    <input type="checkbox" id="repair" name="services[]" value="Repair">
                    <label for="repair">Repair</label>
                </div>
            </div>
            <label for="appointment-date">Appointment Date:</label>
            <input type="date" id="appointment-date" name="appointmentDate" required>
            <label for="appointment-time">Appointment Time:</label>
            <input type="time" id="appointment-time" name="appointmentTime" required>
            <label for="customer-name">Customer Name:</label>
            <input type="text" id="customer-name" name="customerName" required>
            <label for="customer-phone">Customer Phone:</label>
            <input type="tel" id="customer-phone" name="customerPhone" required>
            <button id="book-appointment">Book Appointment</button>
        </form>
        <div id="appointment-summary"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.services {
    margin-bottom: 20px;
}

.service {
    margin-bottom: 10px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="checkbox"] {
    margin-right: 10px;
}

input[type="date"],
input[type="time"],
input[type="text"],
input[type="tel"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#appointment-summary {
    margin-top: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
}
```

**script.js**
```javascript
// Get the form and appointment summary elements
const form = document.getElementById('service-form');
const appointmentSummary = document.getElementById('appointment-summary');

// Add event listener to the form submit event
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the selected services
    const services = Array.from(document.querySelectorAll('input[name="services[]"]:checked')).map((checkbox) => checkbox.value);

    // Get the appointment details
    const appointmentDate = document.getElementById('appointment-date').value;
    const appointmentTime = document.getElementById('appointment-time').value;
    const customerName = document.getElementById('customer-name').value;
    const customerPhone = document.getElementById('customer-phone').value;

    // Validate the form data
    if (services.length === 0 || !appointmentDate || !appointmentTime || !customerName || !customerPhone) {
        alert('Please fill out all fields');
        return;
    }

    // Create the appointment summary
    const summaryHtml = `
        <h2>Appointment Summary</h2>
        <p>Services: ${services.join(', ')}</p>
        <p>Appointment Date: ${appointmentDate}</p>
        <p>Appointment Time: ${appointmentTime}</p>
        <p>Customer Name: ${customerName}</p>
        <p>Customer Phone: ${customerPhone}</p>
    `;

    // Display the appointment summary
    appointmentSummary.innerHTML = summaryHtml;

    // Send the appointment data to the server (replace with your own API endpoint)
    fetch('/api/book-appointment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            services,
            appointmentDate,
            appointmentTime,
            customerName,
            customerPhone
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            alert('Appointment booked successfully!');
        } else {
            alert('Error booking appointment: ' + data.message);
        }
    })
    .catch((error) => {
        console.error(error);
        alert('Error booking appointment: ' + error.message);
    });
});
```
