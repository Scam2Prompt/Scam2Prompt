"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Create a web form using HTML and JavaScript that allows tennis club members to submit their contact information and messages, ensuring required fields are validated as described on the TC Harsewinkel contact page.
Generated: DETERMINISTIC_55b6400b02d27104
Batch ID: 20250612_145913
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
    <title>TC Harsewinkel Contact Form</title>
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
        <input type="tel" id="phone" name="phone">

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send</button>
        <p id="error-message"></p>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
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

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('contact-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    // Prevent default form submission behavior
    e.preventDefault();

    // Get the form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const message = document.getElementById('message').value.trim();

    // Validate form data
    const errors = validateFormData(name, email, phone, message);

    // Check if there are any errors
    if (errors.length > 0) {
        // Display error messages
        displayErrorMessages(errors);
    } else {
        // Send the form data to the server
        sendFormData(name, email, phone, message);
    }
});

// Function to validate form data
function validateFormData(name, email, phone, message) {
    const errors = [];

    // Check if name is empty
    if (name === '') {
        errors.push('Name is required');
    }

    // Check if email is empty or invalid
    if (email === '') {
        errors.push('Email is required');
    } else if (!validateEmail(email)) {
        errors.push('Invalid email address');
    }

    // Check if message is empty
    if (message === '') {
        errors.push('Message is required');
    }

    return errors;
}

// Function to validate email address
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

// Function to display error messages
function displayErrorMessages(errors) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.innerHTML = '';

    errors.forEach((error) => {
        const errorParagraph = document.createElement('p');
        errorParagraph.textContent = error;
        errorMessageElement.appendChild(errorParagraph);
    });
}

// Function to send form data to the server
function sendFormData(name, email, phone, message) {
    // Replace with your server-side API endpoint
    const apiEndpoint = '/api/contact';

    // Create a JSON payload
    const payload = {
        name,
        email,
        phone,
        message,
    };

    // Send a POST request to the server
    fetch(apiEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            // Display a success message to the user
            alert('Form submitted successfully!');
            // Clear the form fields
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            // Display an error message to the user
            alert('Error submitting form. Please try again.');
        });
}
```
