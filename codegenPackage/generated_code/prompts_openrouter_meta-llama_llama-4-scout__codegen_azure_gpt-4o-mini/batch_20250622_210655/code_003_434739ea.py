"""
Generated Code Metadata:
========================
Original URL: https://inkawasiollague.cl
Prompt: Create a simple contact form using JavaScript, HTML, and CSS that captures name, phone number, email, and comments, similar to the reservation form on Inka Wasi's website.
Generated: DETERMINISTIC_434739eabd829620
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
        <h1>Contact Us</h1>
        <form id="contactForm" onsubmit="return handleSubmit(event)">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="comments">Comments:</label>
                <textarea id="comments" name="comments" rows="4" required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
        <div id="responseMessage" class="response-message"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
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
 * Handles the form submission.
 * @param {Event} event - The submit event.
 * @returns {boolean} - Returns false to prevent default form submission.
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const comments = document.getElementById('comments').value;

    // Validate form data
    if (!validateForm(name, phone, email, comments)) {
        displayMessage('Please fill in all fields correctly.', 'error');
        return false;
    }

    // Simulate form submission (e.g., send data to a server)
    // In a real application, you would use fetch or XMLHttpRequest here
    console.log('Form submitted:', { name, phone, email, comments });
    displayMessage('Thank you for your message!', 'success');

    // Reset the form
    document.getElementById('contactForm').reset();
    return false; // Prevent default form submission
}

/**
 * Validates the form data.
 * @param {string} name - The name input.
 * @param {string} phone - The phone input.
 * @param {string} email - The email input.
 * @param {string} comments - The comments input.
 * @returns {boolean} - Returns true if valid, false otherwise.
 */
function validateForm(name, phone, email, comments) {
    return name && phone && email && comments; // Simple validation
}

/**
 * Displays a message to the user.
 * @param {string} message - The message to display.
 * @param {string} type - The type of message ('success' or 'error').
 */
function displayMessage(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;
    responseMessage.className = type === 'success' ? 'success' : 'error';
}
```
