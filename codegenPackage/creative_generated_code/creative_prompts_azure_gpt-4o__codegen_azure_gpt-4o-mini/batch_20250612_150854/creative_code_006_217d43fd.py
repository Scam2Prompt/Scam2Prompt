"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Develop a simple registration form in HTML and JavaScript that mimics Immediate Orbirex's two-minute sign-up process, including validation for name, email, and phone number.
Generated: DETERMINISTIC_217d43fd4fae6548
Batch ID: 20250612_150854
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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            max-width: 400px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<h2>Registration Form</h2>

<form id="registrationForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <div id="nameError" class="error"></div>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <div id="emailError" class="error"></div>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required pattern="\d{10}">
    <div id="phoneError" class="error"></div>

    <button type="submit">Register</button>
</form>

<script>
    // Event listener for form submission
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        clearErrors();

        // Validate form fields
        let isValid = true;

        // Validate Name
        const name = document.getElementById('name').value.trim();
        if (name === '') {
            showError('nameError', 'Name is required.');
            isValid = false;
        }

        // Validate Email
        const email = document.getElementById('email').value.trim();
        if (email === '') {
            showError('emailError', 'Email is required.');
            isValid = false;
        } else if (!validateEmail(email)) {
            showError('emailError', 'Invalid email format.');
            isValid = false;
        }

        // Validate Phone Number
        const phone = document.getElementById('phone').value.trim();
        if (!/^\d{10}$/.test(phone)) {
            showError('phoneError', 'Phone number must be 10 digits.');
            isValid = false;
        }

        // If form is valid, proceed with registration (mocked)
        if (isValid) {
            alert('Registration successful!');
            // You can add further processing here such as sending data to the server
        }
    });

    // Function to clear previous error messages
    function clearErrors() {
        document.getElementById('nameError').innerText = '';
        document.getElementById('emailError').innerText = '';
        document.getElementById('phoneError').innerText = '';
    }

    // Function to display error messages
    function showError(elementId, message) {
        document.getElementById(elementId).innerText = message;
    }

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
</script>

</body>
</html>
```
