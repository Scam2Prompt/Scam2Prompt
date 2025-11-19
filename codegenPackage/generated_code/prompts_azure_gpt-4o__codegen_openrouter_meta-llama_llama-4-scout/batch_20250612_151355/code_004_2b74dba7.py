"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Generate HTML and CSS code for a responsive contact form, including fields for name, email, phone number, and message, inspired by the contact section on Ayoft's website.
Generated: DETERMINISTIC_2b74dba734fc706d
Batch ID: 20250612_151355
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
    <title>Responsive Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-form-container">
        <h2>Get in Touch</h2>
        <form id="contact-form">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
            </div>
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
    margin: 0;
    padding: 0;
}

.contact-form-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-form-container h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input, .form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.form-group textarea {
    resize: vertical;
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

/* Responsive Design */

@media only screen and (max-width: 768px) {
    .contact-form-container {
        margin: 20px auto;
        padding: 10px;
    }
}

@media only screen and (max-width: 480px) {
    .contact-form-container {
        margin: 10px auto;
        padding: 5px;
    }
    .form-group input, .form-group textarea {
        padding: 5px;
    }
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
            formResponse.innerHTML = '<p>Message sent successfully!</p>';
            form.reset();
        } else {
            formResponse.innerHTML = '<p>Error sending message. Please try again.</p>';
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.innerHTML = '<p>Error sending message. Please try again.</p>';
    });
});
```
