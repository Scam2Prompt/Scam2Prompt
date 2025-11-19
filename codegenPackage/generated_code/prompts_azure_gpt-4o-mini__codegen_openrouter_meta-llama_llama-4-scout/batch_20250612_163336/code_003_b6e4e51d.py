"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: How can I implement a contact form using HTML and JavaScript for a computer hardware store's website, inspired by the contact details provided by StarTec?
Generated: DETERMINISTIC_b6e4e51dfb38d398
Batch ID: 20250612_163336
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
    <title>StarTec Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Contact Us</h1>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Message</button>
    </form>

    <div id="form-response"></div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

#contact-form {
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
    text-align: center;
    margin-top: 20px;
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
// Get the contact form and response elements
const contactForm = document.getElementById('contact-form');
const formResponse = document.getElementById('form-response');

// Add event listener to the contact form
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(contactForm);

    // Send the form data to the server
    fetch('/api/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Display success message
            formResponse.textContent = 'Message sent successfully!';
            formResponse.classList.add('success');
            formResponse.classList.remove('error');

            // Reset the form
            contactForm.reset();
        } else {
            // Display error message
            formResponse.textContent = 'Error sending message: ' + data.message;
            formResponse.classList.add('error');
            formResponse.classList.remove('success');
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.textContent = 'Error sending message: ' + error.message;
        formResponse.classList.add('error');
        formResponse.classList.remove('success');
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
app.use(express.urlencoded({ extended: true }));

// Contact form API endpoint
app.post('/api/contact', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Validate the form data
    if (!name || !email || !phone || !message) {
        res.json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Send the email using a library like Nodemailer
    const nodemailer = require('nodemailer');
    const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        auth: {
            user: 'username',
            pass: 'password',
        },
    });

    const mailOptions = {
        from: email,
        to: 'recipient@example.com',
        subject: 'Contact Form Message',
        text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nMessage: ${message}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.json({ success: false, message: 'Error sending email.' });
        } else {
            res.json({ success: true });
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
