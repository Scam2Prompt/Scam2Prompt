"""
Generated Code Metadata:
========================
Original URL: https://sergiupopa.com
Prompt: Generate a code snippet for a contact form, similar to the one on sergiupopa.com, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_fc0d46ef4c50644e
Batch ID: 20250622_211721
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
            <div id="form-response"></div>
        </form>
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

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
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

#form-response {
    margin-top: 10px;
    color: #666;
}

.success {
    color: #2ecc71;
}

.error {
    color: #e74c3c;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('contact-form');

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
    fetch('/api/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then((response) => response.json())
    .then((data) => {
        // Display form response
        const formResponse = document.getElementById('form-response');
        if (data.success) {
            formResponse.classList.remove('error');
            formResponse.classList.add('success');
            formResponse.textContent = 'Message sent successfully!';
            // Clear form fields
            form.reset();
        } else {
            formResponse.classList.remove('success');
            formResponse.classList.add('error');
            formResponse.textContent = data.message;
        }
    })
    .catch((error) => {
        console.error(error);
        const formResponse = document.getElementById('form-response');
        formResponse.classList.remove('success');
        formResponse.classList.add('error');
        formResponse.textContent = 'An error occurred. Please try again.';
    });
});
```

**server.js (Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const nodemailer = require('nodemailer');

// Middleware to parse JSON bodies
app.use(express.json());

// Contact form API endpoint
app.post('/api/contact', (req, res) => {
    const { name, email, message } = req.body;

    // Validate form data
    if (!name || !email || !message) {
        res.json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Create a transporter for nodemailer
    const transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 587,
        secure: false, // or 'STARTTLS'
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-password'
        }
    });

    // Create a mail options object
    const mailOptions = {
        from: email,
        to: 'your-email@gmail.com',
        subject: `Message from ${name}`,
        text: message
    };

    // Send the email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.json({ success: false, message: 'An error occurred. Please try again.' });
        } else {
            res.json({ success: true });
        }
    });
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
