"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Create a responsive contact form in HTML5 and CSS for a personal portfolio website, similar to the one described on EMFresh2o Digital Resume.
Generated: DETERMINISTIC_329f81154d95a4a0
Batch ID: 20250612_152240
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
    <div class="container">
        <h1>Contact Me</h1>
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
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
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
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Responsive design */
@media only screen and (max-width: 768px) {
    .container {
        margin: 20px auto;
        padding: 10px;
    }
}

@media only screen and (max-width: 480px) {
    h1 {
        font-size: 24px;
    }

    label {
        font-size: 16px;
    }

    input, textarea {
        padding: 5px;
        font-size: 16px;
    }

    button[type="submit"] {
        padding: 5px 10px;
        font-size: 16px;
    }
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
    const formData = new FormData(form);

    // Send form data to server using fetch API
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Display success message
            responseElement.innerHTML = '<p class="success">Message sent successfully!</p>';
            form.reset();
        } else {
            // Display error message
            responseElement.innerHTML = '<p class="error">Error sending message: ' + data.message + '</p>';
        }
    })
    .catch((error) => {
        console.error(error);
        responseElement.innerHTML = '<p class="error">Error sending message: ' + error.message + '</p>';
    });
});
```

**server.js (Node.js example)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));

// Contact form submission handler
app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;

    // Validate form data
    if (!name || !email || !message) {
        res.json({ success: false, message: 'Please fill out all fields.' });
        return;
    }

    // Send email using nodemailer (example)
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
        to: 'your-email@example.com',
        subject: 'Contact Form Submission',
        text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`,
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

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
