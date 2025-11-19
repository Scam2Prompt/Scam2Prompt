"""
Generated Code Metadata:
========================
Original URL: https://khaleeji.com
Prompt: Generate a code snippet for a web form that allows users to inquire about purchasing the domain KHALEEJI.COM.
Generated: DETERMINISTIC_a1c4a2ca005af216
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Domain Inquiry Form**
=======================

### HTML

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquire about KHALEEJI.COM</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Inquire about KHALEEJI.COM</h1>
        <form id="inquiry-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (in styles.css file)

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
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
    margin-top: 20px;
}
```

### JavaScript

```javascript
// script.js

const form = document.getElementById('inquiry-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('/inquiry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        formResponse.innerText = 'Inquiry sent successfully!';
        form.reset();
    } catch (error) {
        formResponse.innerText = 'Error sending inquiry. Please try again.';
        console.error('Error:', error);
    }
});
```

### Server-side (Node.js and Express)

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/inquiry', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Validate input data
    if (!name || !email || !phone || !message) {
        res.status(400).json({ error: 'Please fill out all fields.' });
        return;
    }

    // Send email or store inquiry (example using nodemailer)
    const nodemailer = require('nodemailer');
    const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        auth: {
            user: 'username',
            pass: 'password'
        }
    });

    const mailOptions = {
        from: email,
        to: 'your-email@example.com',
        subject: 'Inquiry about KHALEEJI.COM',
        text: `Name: ${name}\nPhone: ${phone}\n\n${message}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending email:', error);
            res.status(500).json({ error: 'Error sending inquiry. Please try again.' });
        } else {
            res.json({ message: 'Inquiry sent successfully!' });
        }
    });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
