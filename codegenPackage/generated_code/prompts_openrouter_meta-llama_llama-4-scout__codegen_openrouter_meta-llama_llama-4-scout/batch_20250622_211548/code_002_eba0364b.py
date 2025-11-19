"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Generate HTML/CSS code for a simple contact form like the one on the Central Seed & Chemical website.
Generated: DETERMINISTIC_eba0364ba42cb289
Batch ID: 20250622_211548
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
    <title>Simple Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-form-container">
        <h2>Contact Us</h2>
        <form id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone">

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
    background-color: #f2f2f2;
}

.contact-form-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-form-container h2 {
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
    border-radius: 5px;
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
const form = document.getElementById('contact-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            formResponse.classList.remove('error');
            formResponse.classList.add('success');
            formResponse.textContent = 'Message sent successfully!';
            form.reset();
        } else {
            formResponse.classList.remove('success');
            formResponse.classList.add('error');
            formResponse.textContent = 'Error sending message: ' + data.message;
        }
    })
    .catch((error) => {
        formResponse.classList.remove('success');
        formResponse.classList.add('error');
        formResponse.textContent = 'Error sending message: ' + error.message;
    });
});
```

**server.js (Node.js example)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/contact', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Replace with your email sending logic
    console.log('Message received:');
    console.log(`Name: ${name}`);
    console.log(`Email: ${email}`);
    console.log(`Phone: ${phone}`);
    console.log(`Message: ${message}`);

    res.json({ success: true, message: 'Message sent successfully!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
