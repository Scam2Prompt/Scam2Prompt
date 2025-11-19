"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Provide code examples for integrating a contact form into a web design project using HTML5, CSS3, and JavaScript, similar to the "Get in Touch" section on dionlineaja.id.
Generated: DETERMINISTIC_6d9b1c6b47be0ea6
Batch ID: 20250612_152739
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
    <title>Get in Touch</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section id="contact" class="container mt-5">
        <h2 class="text-center">Get in Touch</h2>
        <form id="contact-form">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea class="form-control" id="message" name="message" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send Message</button>
        </form>
        <div id="form-response"></div>
    </section>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
#contact {
    padding: 50px 0;
}

#contact h2 {
    margin-bottom: 20px;
}

#contact-form {
    margin-top: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.btn-primary {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn-primary:hover {
    background-color: #0069d9;
}

#form-response {
    margin-top: 20px;
}

.success {
    color: #008000;
}

.error {
    color: #ff0000;
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
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Display success message
            formResponse.classList.remove('error');
            formResponse.classList.add('success');
            formResponse.innerText = 'Message sent successfully!';
            // Reset the form
            contactForm.reset();
        } else {
            // Display error message
            formResponse.classList.remove('success');
            formResponse.classList.add('error');
            formResponse.innerText = 'Error sending message: ' + data.message;
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.classList.remove('success');
        formResponse.classList.add('error');
        formResponse.innerText = 'Error sending message: ' + error.message;
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
app.use(express.urlencoded({ extended: true }));

// Contact form endpoint
app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;

    // Validate the form data
    if (!name || !email || !message) {
        res.json({ success: false, message: 'Please fill out all fields' });
        return;
    }

    // Send the email
    const transporter = nodemailer.createTransport({
        host: 'your-email-host',
        port: 587,
        secure: false, // or 'STARTTLS'
        auth: {
            user: 'your-email-username',
            pass: 'your-email-password',
        },
    });

    const mailOptions = {
        from: email,
        to: 'your-email-username',
        subject: 'New Message from ' + name,
        text: message,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.json({ success: false, message: 'Error sending message' });
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
