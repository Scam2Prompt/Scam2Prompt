"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Create a registration form with error validation that mimics the functionality described on CCBase.net, including handling form errors and user feedback.
Generated: DETERMINISTIC_d6d8f5ee2bd10a1d
Batch ID: 20250612_154902
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
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 300px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: red;
            font-size: 12px;
        }
        .success {
            color: green;
            font-size: 14px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Registration Form</h2>
    <form id="registrationForm">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <div id="usernameError" class="error"></div>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <div id="emailError" class="error"></div>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <div id="passwordError" class="error"></div>
        </div>
        <div>
            <label for="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" name="confirmPassword" required>
            <div id="confirmPasswordError" class="error"></div>
        </div>
        <button type="submit">Register</button>
    </form>
    <div id="formFeedback" class="success"></div>
</div>

<script>
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Clear previous error messages
        const errorElements = document.querySelectorAll('.error');
        errorElements.forEach(element => element.textContent = '');

        // Get form values
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();
        const confirmPassword = document.getElementById('confirmPassword').value.trim();
        let isValid = true;

        // Validate username
        if (!/^[a-zA-Z0-9]{3,15}$/.test(username)) {
            document.getElementById('usernameError').textContent = 'Username must be 3-15 characters long and alphanumeric.';
            isValid = false;
        }

        // Validate email
        if (!/\S+@\S+\.\S+/.test(email)) {
            document.getElementById('emailError').textContent = 'Please enter a valid email address.';
            isValid = false;
        }

        // Validate password
        if (password.length < 6) {
            document.getElementById('passwordError').textContent = 'Password must be at least 6 characters long.';
            isValid = false;
        }

        // Validate password confirmation
        if (password !== confirmPassword) {
            document.getElementById('confirmPasswordError').textContent = 'Passwords do not match.';
            isValid = false;
        }

        // If form is valid, show success message
        if (isValid) {
            document.getElementById('formFeedback').textContent = 'Registration successful!';
            // Here you would typically send the data to the server
            // For example, using fetch or XMLHttpRequest
        }
    });
</script>

</body>
</html>
```
