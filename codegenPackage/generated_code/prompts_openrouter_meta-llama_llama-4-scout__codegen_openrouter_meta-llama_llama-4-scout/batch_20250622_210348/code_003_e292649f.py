"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: "Create a simple web form using HTML and JavaScript to collect patient information and medical orders for laboratory tests at Laboratorio Savaz."
Generated: DETERMINISTIC_e292649f26f376ea
Batch ID: 20250622_210348
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
    <title>Laboratorio Savaz - Patient Information and Medical Orders</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Laboratorio Savaz</h1>
    <form id="patient-form">
        <section>
            <h2>Patient Information</h2>
            <label for="patient-name">Patient Name:</label>
            <input type="text" id="patient-name" name="patientName" required>

            <label for="patient-date-of-birth">Date of Birth:</label>
            <input type="date" id="patient-date-of-birth" name="dateOfBirth" required>

            <label for="patient-medical-record">Medical Record:</label>
            <input type="text" id="patient-medical-record" name="medicalRecord" required>
        </section>

        <section>
            <h2>Medical Orders</h2>
            <label for="medical-order">Select Laboratory Tests:</label>
            <select id="medical-order" name="medicalOrder" multiple required>
                <option value="Complete Blood Count (CBC)">CBC</option>
                <option value="Blood Chemistry">Blood Chemistry</option>
                <option value="Urinalysis">Urinalysis</option>
                <option value="Other (please specify)">Other</option>
            </select>

            <label for="medical-order-other">Other (please specify):</label>
            <input type="text" id="medical-order-other" name="medicalOrderOther">
        </section>

        <button type="submit">Submit</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
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

**script.js**
```javascript
// Get the form element
const form = document.getElementById('patient-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get patient information
    const patientName = document.getElementById('patient-name').value;
    const dateOfBirth = document.getElementById('patient-date-of-birth').value;
    const medicalRecord = document.getElementById('patient-medical-record').value;

    // Get medical orders
    const medicalOrder = Array.from(document.getElementById('medical-order').selectedOptions).map(option => option.value);
    const medicalOrderOther = document.getElementById('medical-order-other').value;

    // Validate form data
    if (!patientName || !dateOfBirth || !medicalRecord || medicalOrder.length === 0) {
        alert('Please fill in all required fields.');
        return;
    }

    // Create a JSON object to store form data
    const formData = {
        patientInformation: {
            name: patientName,
            dateOfBirth: dateOfBirth,
            medicalRecord: medicalRecord
        },
        medicalOrders: {
            laboratoryTests: medicalOrder,
            other: medicalOrderOther
        }
    };

    // Send form data to server (replace with your server-side endpoint)
    fetch('/api/patient-info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

    // Clear form fields
    form.reset();
});
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to receive patient information
app.post('/api/patient-info', (req, res) => {
    try {
        const formData = req.body;
        console.log('Received patient information:', formData);

        // Save form data to database or perform other server-side logic here

        res.json({ message: 'Patient information received successfully.' });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
