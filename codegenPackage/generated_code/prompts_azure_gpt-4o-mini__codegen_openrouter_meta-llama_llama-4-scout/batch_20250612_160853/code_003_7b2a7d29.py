"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Develop a simple HTML form for users to book a spot in the "Patente d'impresa" course, including dropdowns for event selection and user type.
Generated: DETERMINISTIC_7b2a7d29abb8e3df
Batch ID: 20250612_160853
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
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patente d'impresa Course Booking</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Patente d'impresa Course Booking</h1>
    <form id="booking-form">
        <!-- Event selection dropdown -->
        <label for="event">Select Event:</label>
        <select id="event" name="event" required>
            <option value="">Select an event</option>
            <option value="patente-impresa-course-1">Patente d'impresa Course 1</option>
            <option value="patente-impresa-course-2">Patente d'impresa Course 2</option>
            <!-- Add more options as needed -->
        </select>

        <!-- User type dropdown -->
        <label for="user-type">Select User Type:</label>
        <select id="user-type" name="user-type" required>
            <option value="">Select a user type</option>
            <option value="student">Student</option>
            <option value="professional">Professional</option>
            <option value="other">Other</option>
        </select>

        <!-- User information fields -->
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <!-- Booking submit button -->
        <button type="submit">Book a Spot</button>
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

select, input[type="text"], input[type="email"], input[type="tel"] {
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
const form = document.getElementById('booking-form');
const errorMessageDiv = document.getElementById('error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const event = formData.get('event');
    const userType = formData.get('user-type');
    const name = formData.get('name');
    const email = formData.get('email');
    const phone = formData.get('phone');

    try {
        const response = await fetch('/book', {
            method: 'POST',
            body: JSON.stringify({
                event,
                userType,
                name,
                email,
                phone,
            }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        alert('Booking successful!');
        form.reset();
    } catch (error) {
        console.error('Error:', error);
        errorMessageDiv.textContent = 'Error: ' + error.message;
    }
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/book', (req, res) => {
    const { event, userType, name, email, phone } = req.body;

    // Validate input data
    if (!event || !userType || !name || !email || !phone) {
        res.status(400).json({ error: 'Please fill in all fields' });
        return;
    }

    // Save booking to database or send confirmation email
    // For demonstration purposes, just return a success response
    res.json({ message: 'Booking successful!' });
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
