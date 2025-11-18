"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Create a web form using HTML and JavaScript that allows tennis club members to submit their contact information and messages, ensuring required fields are validated as described on the TC Harsewinkel contact page.
Generated: DETERMINISTIC_55b6400b02d27104
Batch ID: 20250612_145913
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
    <title>Tennis Club Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .success {
            color: green;
            font-size: 1em;
        }
    </style>
</head>
<body>

<h2>Contact Us</h2>
<form id="contactForm">
    <label for="name">Name (required):</label><br>
    <input type="text" id="name" name="name" required><br>
    <span class="error" id="nameError"></span><br>

    <label for="email">Email (required):</label><br>
    <input type="email" id="email" name="email" required><br>
    <span class="error" id="emailError"></span><br>

    <label for="message">Message (required):</label><br>
    <textarea id="message" name="message" required></textarea><br>
    <span class="error" id="messageError"></span><br>

    <button type="submit">Submit</button>
</form>

<div class="success" id="successMessage"></div>

<script>
// Function to validate the form inputs
function validateForm(event) {
    event.preventDefault(); // Prevent form submission

    // Clear previous error messages
    document.getElementById('nameError').innerText = '';
    document.getElementById('emailError').innerText = '';
    document.getElementById('messageError').innerText = '';
    document.getElementById('successMessage').innerText = '';

    // Get input values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    let valid = true; // Flag to check overall validity

    // Validate name
    if (name === '') {
        document.getElementById('nameError').innerText = 'Name is required.';
        valid = false;
    }

    // Validate email
    if (email === '') {
        document.getElementById('emailError').innerText = 'Email is required.';
        valid = false;
    } else if (!validateEmail(email)) {
        document.getElementById('emailError').innerText = 'Please enter a valid email address.';
        valid = false;
    }

    // Validate message
    if (message === '') {
        document.getElementById('messageError').innerText = 'Message is required.';
        valid = false;
    }

    // If all fields are valid, show success message
    if (valid) {
        document.getElementById('successMessage').innerText = 'Thank you for your message!';
    }
}

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
    return re.test(email);
}

// Set up event listener for form submission
document.getElementById('contactForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
