"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Generate code to create a contact form for a personal blog using HTML, CSS, and JavaScript, ensuring it includes fields for name, email, and message.
Generated: DETERMINISTIC_86e83f9cd0285bf2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
    <div class="contact-container">
        <h1>Contact Us</h1>
        <form id="contactForm" onsubmit="return handleSubmit(event)">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse" class="response-message"></div>
    </div>

    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Basic reset */
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

.contact-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.response-message {
    margin-top: 20px;
    text-align: center;
}
```

```javascript
// script.js

/**
 * Handles the form submission by collecting data and displaying a response message.
 * @param {Event} event - The event object representing the form submission.
 * @returns {boolean} - Returns false to prevent the default form submission.
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const formResponse = document.getElementById('formResponse');

    // Simple validation (more can be added as needed)
    if (!name || !email || !message) {
        formResponse.textContent = 'Please fill in all fields.';
        formResponse.style.color = 'red';
        return false;
    }

    // Simulating an API call
    try {
        // Here you would typically send the data to your server
        // For example: await fetch('/api/contact', { method: 'POST', body: JSON.stringify({ name, email, message }) });
        
        // Display a success message (simulating success)
        formResponse.textContent = 'Your message has been sent successfully!';
        formResponse.style.color = 'green';

        // Reset form fields
        document.getElementById('contactForm').reset();
    } catch (error) {
        console.error('Error while sending message:', error);
        formResponse.textContent = 'There was an error sending your message. Please try again later.';
        formResponse.style.color = 'red';
    }

    return false; // Prevent default form submission
}
```
