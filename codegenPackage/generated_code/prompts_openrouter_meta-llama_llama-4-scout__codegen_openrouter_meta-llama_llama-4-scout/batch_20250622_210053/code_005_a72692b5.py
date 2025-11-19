"""
Generated Code Metadata:
========================
Original URL: https://etherealspamassagetherapist.com
Prompt: Create a simple HTML form to collect customer information for booking a massage appointment, including name, email, and preferred date and time.
Generated: DETERMINISTIC_a72692b5b8daa212
Batch ID: 20250622_210053
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
    <title>Massage Appointment Booking</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Book a Massage Appointment</h1>
    <form id="booking-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="preferred-date">Preferred Date:</label>
        <input type="date" id="preferred-date" name="preferred-date" required>

        <label for="preferred-time">Preferred Time:</label>
        <input type="time" id="preferred-time" name="preferred-time" required>

        <button type="submit">Book Appointment</button>
    </form>

    <div id="error-message"></div>

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

input[type="text"], input[type="email"], input[type="date"], input[type="time"] {
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

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('booking-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const preferredDate = document.getElementById('preferred-date').value;
    const preferredTime = document.getElementById('preferred-time').value;

    // Validate form data
    if (!name || !email || !preferredDate || !preferredTime) {
        displayError('Please fill out all fields.');
        return;
    }

    // Send data to server for processing (replace with actual API endpoint)
    fetch('/book-appointment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            email,
            preferredDate,
            preferredTime
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            displaySuccess('Appointment booked successfully!');
        } else {
            displayError(data.message);
        }
    })
    .catch((error) => {
        displayError('Error booking appointment: ' + error.message);
    });
});

// Display error message
function displayError(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
}

// Display success message
function displaySuccess(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
    // Clear form fields
    document.getElementById('booking-form').reset();
}
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle booking appointment
app.post('/book-appointment', (req, res) => {
    const { name, email, preferredDate, preferredTime } = req.body;

    // Validate request data
    if (!name || !email || !preferredDate || !preferredTime) {
        res.status(400).json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Process appointment booking (e.g., save to database)
    // For demonstration purposes, just return a success response
    res.json({ success: true, message: 'Appointment booked successfully!' });
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
