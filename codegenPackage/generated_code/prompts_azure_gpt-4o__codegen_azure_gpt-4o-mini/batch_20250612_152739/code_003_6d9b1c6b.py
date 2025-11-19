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

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section id="contact" class="contact-section">
        <h2>Get in Touch</h2>
        <form id="contactForm" class="contact-form" novalidate>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                <span class="error-message" id="nameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <span class="error-message" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
                <span class="error-message" id="messageError"></span>
            </div>
            <button type="submit">Send Message</button>
            <div class="success-message" id="successMessage"></div>
        </form>
    </section>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.contact-section {
    padding: 20px;
    background-color: #fff;
    max-width: 600px;
    margin: 20px auto;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.error-message {
    color: red;
    font-size: 0.9em;
}

.success-message {
    color: green;
    text-align: center;
    margin-top: 10px;
}
```

```javascript
// script.js

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Function to handle form submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Clear previous error messages
    document.getElementById('nameError').textContent = '';
    document.getElementById('emailError').textContent = '';
    document.getElementById('messageError').textContent = '';
    document.getElementById('successMessage').textContent = '';

    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Validate form fields
    let isValid = true;

    if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
    }

    if (email === '' || !validateEmail(email)) {
        document.getElementById('emailError').textContent = 'Valid email is required.';
        isValid = false;
    }

    if (message === '') {
        document.getElementById('messageError').textContent = 'Message is required.';
        isValid = false;
    }

    // If form is valid, simulate sending data
    if (isValid) {
        // Simulate a successful submission
        document.getElementById('successMessage').textContent = 'Message sent successfully!';
        // Here you would typically send the data to a server
        // For example, using fetch() or XMLHttpRequest
    }
});
```
