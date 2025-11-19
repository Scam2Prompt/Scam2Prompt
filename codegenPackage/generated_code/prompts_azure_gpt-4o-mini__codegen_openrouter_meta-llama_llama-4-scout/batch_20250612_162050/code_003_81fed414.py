"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Develop a simple HTML form that allows users to request a quote for vehicle renting services from Innova Renting, ensuring it captures necessary details like vehicle type and rental period.
Generated: DETERMINISTIC_81fed414f76c0cbd
Batch ID: 20250612_162050
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
    <title>Innova Renting - Request a Quote</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Innova Renting - Request a Quote</h1>
    <form id="quote-form">
        <label for="vehicle-type">Vehicle Type:</label>
        <select id="vehicle-type" name="vehicle-type" required>
            <option value="">Select a vehicle type</option>
            <option value="sedan">Sedan</option>
            <option value="suv">SUV</option>
            <option value="truck">Truck</option>
            <option value="van">Van</option>
        </select>
        <br><br>
        <label for="rental-period">Rental Period:</label>
        <input type="date" id="rental-start" name="rental-start" required>
        <input type="date" id="rental-end" name="rental-end" required>
        <br><br>
        <label for="pickup-location">Pickup Location:</label>
        <input type="text" id="pickup-location" name="pickup-location" required>
        <br><br>
        <label for="dropoff-location">Dropoff Location:</label>
        <input type="text" id="dropoff-location" name="dropoff-location" required>
        <br><br>
        <label for="contact-name">Contact Name:</label>
        <input type="text" id="contact-name" name="contact-name" required>
        <br><br>
        <label for="contact-email">Contact Email:</label>
        <input type="email" id="contact-email" name="contact-email" required>
        <br><br>
        <label for="contact-phone">Contact Phone:</label>
        <input type="tel" id="contact-phone" name="contact-phone" required>
        <br><br>
        <button type="submit">Request a Quote</button>
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
    width: 50%;
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
const form = document.getElementById('quote-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const vehicleType = document.getElementById('vehicle-type').value;
    const rentalStart = document.getElementById('rental-start').value;
    const rentalEnd = document.getElementById('rental-end').value;
    const pickupLocation = document.getElementById('pickup-location').value;
    const dropoffLocation = document.getElementById('dropoff-location').value;
    const contactName = document.getElementById('contact-name').value;
    const contactEmail = document.getElementById('contact-email').value;
    const contactPhone = document.getElementById('contact-phone').value;

    // Validate form data
    if (!vehicleType || !rentalStart || !rentalEnd || !pickupLocation || !dropoffLocation || !contactName || !contactEmail || !contactPhone) {
        alert('Please fill out all fields.');
        return;
    }

    // Create a quote request object
    const quoteRequest = {
        vehicleType,
        rentalStart,
        rentalEnd,
        pickupLocation,
        dropoffLocation,
        contactName,
        contactEmail,
        contactPhone,
    };

    // Send the quote request to the server
    fetch('/quote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(quoteRequest),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        alert('Quote request sent successfully!');
        form.reset();
    })
    .catch((error) => {
        console.error(error);
        alert('Error sending quote request. Please try again.');
    });
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle quote requests
app.post('/quote', (req, res) => {
    try {
        const quoteRequest = req.body;

        // Validate quote request
        if (!quoteRequest.vehicleType || !quoteRequest.rentalStart || !quoteRequest.rentalEnd || !quoteRequest.pickupLocation || !quoteRequest.dropoffLocation || !quoteRequest.contactName || !quoteRequest.contactEmail || !quoteRequest.contactPhone) {
            res.status(400).json({ error: 'Please fill out all fields.' });
            return;
        }

        // Process the quote request
        console.log(quoteRequest);

        // Send a response back to the client
        res.json({ message: 'Quote request received successfully!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Error processing quote request.' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
