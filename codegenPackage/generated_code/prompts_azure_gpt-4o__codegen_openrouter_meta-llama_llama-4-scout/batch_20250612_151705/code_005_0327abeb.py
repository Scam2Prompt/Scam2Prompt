"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Create a web form using HTML and JavaScript for course registration, including fields for selecting sales training programs like those provided by Debridge Advisory.
Generated: DETERMINISTIC_0327abebd24e406b
Batch ID: 20250612_151705
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
    <title>Course Registration Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Course Registration Form</h1>
    <form id="registration-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="program">Select Sales Training Program:</label>
        <select id="program" name="program" required>
            <option value="">Select a program</option>
            <option value="debridge-advisory-sales-training">Debridge Advisory Sales Training</option>
            <option value="debridge-advisory-leadership-training">Debridge Advisory Leadership Training</option>
            <option value="debridge-advisory-marketing-training">Debridge Advisory Marketing Training</option>
        </select>

        <label for="start-date">Preferred Start Date:</label>
        <input type="date" id="start-date" name="start-date" required>

        <button type="submit">Register</button>
        <button type="reset">Reset</button>
    </form>

    <div id="error-message"></div>
    <div id="success-message"></div>

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

button[type="reset"] {
    background-color: #ccc;
    color: #333;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#error-message {
    color: red;
}

#success-message {
    color: green;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('registration-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const program = document.getElementById('program').value;
    const startDate = document.getElementById('start-date').value;

    // Validate form data
    if (name === '' || email === '' || program === '' || startDate === '') {
        displayError('Please fill out all fields.');
        return;
    }

    // Send data to server for processing
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            email,
            program,
            startDate
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            displaySuccess('Registration successful!');
            form.reset();
        } else {
            displayError(data.message);
        }
    })
    .catch((error) => {
        console.error(error);
        displayError('An error occurred. Please try again.');
    });
});

// Display error message
function displayError(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
    setTimeout(() => {
        errorElement.textContent = '';
    }, 5000);
}

// Display success message
function displaySuccess(message) {
    const successElement = document.getElementById('success-message');
    successElement.textContent = message;
    setTimeout(() => {
        successElement.textContent = '';
    }, 5000);
}
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle registration
app.post('/register', (req, res) => {
    const { name, email, program, startDate } = req.body;

    // Validate data
    if (!name || !email || !program || !startDate) {
        res.json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Process registration data
    // ...

    // Send response
    res.json({ success: true });
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
