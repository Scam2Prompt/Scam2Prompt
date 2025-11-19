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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HVAC Service Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>HVAC Service Request Form</h1>
    <form id="serviceRequestForm" action="/submit-request" method="POST">
        <!-- Customer Contact Information -->
        <fieldset>
            <legend>Contact Information</legend>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
        </fieldset>

        <!-- Service Type Selection -->
        <fieldset>
            <legend>Service Type</legend>
            <label for="serviceType">Select Service:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="">--Please choose an option--</option>
                <option value="air_conditioning_repair">Air Conditioning Repair</option>
                <option value="duct_cleaning">Duct Cleaning</option>
                <option value="furnace_repair">Furnace Repair</option>
                <option value="tune_up">Tune-Up</option>
            </select>
        </fieldset>

        <!-- Preferred Appointment Time -->
        <fieldset>
            <legend>Preferred Appointment Time</legend>
            <label for="appointmentDate">Date:</label>
            <input type="date" id="appointmentDate" name="appointmentDate" required>
            
            <label for="appointmentTime">Time:</label>
            <input type="time" id="appointmentTime" name="appointmentTime" required>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Validate form data (basic validation)
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const serviceType = document.getElementById('serviceType').value;
            const appointmentDate = document.getElementById('appointmentDate').value;
            const appointmentTime = document.getElementById('appointmentTime').value;

            if (!name || !email || !phone || !serviceType || !appointmentDate || !appointmentTime) {
                alert('Please fill in all fields.');
                return;
            }

            // Prepare data for submission
            const formData = {
                name,
                email,
                phone,
                serviceType,
                appointmentDate,
                appointmentTime
            };

            // Send data to the server
            fetch('/submit-request', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Service request submitted successfully!');
                // Optionally reset the form
                document.getElementById('serviceRequestForm').reset();
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your request. Please try again later.');
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

fieldset {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
