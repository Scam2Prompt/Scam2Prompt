"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Generate code for a simple blog contact form using HTML, CSS, and JavaScript, inspired by the design on Rupak Parajuli's website.
Generated: DETERMINISTIC_5ea63a5516346b39
Batch ID: 20250622_210655
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
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-form">
        <h2>Get in Touch</h2>
        <form id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.contact-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-form h2 {
    text-align: center;
    margin-bottom: 20px;
}

.contact-form label {
    display: block;
    margin-bottom: 10px;
}

.contact-form input, .contact-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

.contact-form button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.contact-form button[type="submit"]:hover {
    background-color: #3e8e41;
}

#form-response {
    margin-top: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.success {
    color: #4CAF50;
}

.error {
    color: #f44336;
}
```

**script.js**
```javascript
// Get the form and response elements
const form = document.getElementById('contact-form');
const responseElement = document.getElementById('form-response');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Create a JSON payload
    const payload = {
        name,
        email,
        message
    };

    // Send a POST request to the server
    fetch('/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.success) {
            // Display success message
            responseElement.classList.remove('error');
            responseElement.classList.add('success');
            responseElement.innerText = 'Message sent successfully!';
            // Clear form fields
            form.reset();
        } else {
            // Display error message
            responseElement.classList.remove('success');
            responseElement.classList.add('error');
            responseElement.innerText = data.message;
        }
    })
    .catch((error) => {
        console.error(error);
        responseElement.classList.remove('success');
        responseElement.classList.add('error');
        responseElement.innerText = 'An error occurred. Please try again.';
    });
});
```

**server.js (Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Contact form submission handler
app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;

    // Validate form data
    if (!name || !email || !message) {
        res.json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Send email using a library like Nodemailer
    // For demonstration purposes, just log the message
    console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);

    res.json({ success: true });
});

// Serve static files
app.use(express.static('public'));

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
