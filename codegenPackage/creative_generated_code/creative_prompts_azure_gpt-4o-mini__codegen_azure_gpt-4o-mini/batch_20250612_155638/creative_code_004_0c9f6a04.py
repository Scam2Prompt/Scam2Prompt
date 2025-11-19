"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Create a registration form in HTML and JavaScript that includes fields for fullname, email, and password, similar to the one used by Signalrextrack.
Generated: DETERMINISTIC_0c9f6a0433bf6bc7
Batch ID: 20250612_155638
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
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <div class="container">
        <h1>Registration Form</h1>
        <form id="registrationForm">
            <div class="form-group">
                <label for="fullname">Full Name:</label>
                <input type="text" id="fullname" name="fullname" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="6">
            </div>
            <button type="submit">Register</button>
        </form>
        <div id="message" class="message"></div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the container */
.container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

/* Styling for form groups */
.form-group {
    margin-bottom: 15px;
}

/* Styling for buttons */
button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

/* Message styling */
.message {
    margin-top: 20px;
    font-weight: bold;
}
```

```javascript
// script.js

/**
 * Initializes the registration form validation and submission
 */
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve form values
    const fullname = document.getElementById('fullname').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    // Validate input fields
    if (!validateEmail(email)) {
        displayMessage('Please enter a valid email address.', 'error');
        return;
    }

    // Optionally, you can handle password strength checks here

    // Simulate form submission (this would typically be an API call)
    console.log('Form submitted:', { fullname, email, password });
    displayMessage('Registration successful!', 'success');
});

/**
 * Validates the email format using a regular expression
 * @param {string} email - The email to be validated
 * @returns {boolean} - True if the email is valid, otherwise false
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Displays a message to the user
 * @param {string} message - The message to display
 * @param {string} type - The type of message (success/error)
 */
function displayMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;

    // Change message color based on type
    messageDiv.style.color = type === 'success' ? 'green' : 'red';
}
```
