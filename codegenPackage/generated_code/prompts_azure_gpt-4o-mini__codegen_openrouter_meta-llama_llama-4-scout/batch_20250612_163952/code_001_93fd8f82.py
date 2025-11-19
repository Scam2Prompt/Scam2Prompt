"""
Generated Code Metadata:
========================
Original URL: https://zerion.app
Prompt: What are the best practices for creating a secure password input field in HTML?
Generated: DETERMINISTIC_93fd8f82c48b2409
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Secure Password Input Field Example -->

<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Password Input Field</title>
    <style>
        /* Basic styling for demonstration purposes */
        form {
            width: 300px;
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

        input {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }

        button[type="submit"] {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <form id="password-form">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <label for="confirm-password">Confirm Password:</label>
        <input type="password" id="confirm-password" name="confirm-password" required>
        <button type="submit">Submit</button>
    </form>

    <script>
        // Get the form element
        const form = document.getElementById('password-form');

        // Add an event listener to the form submission
        form.addEventListener('submit', (e) => {
            // Prevent the default form submission behavior
            e.preventDefault();

            // Get the password and confirm password input values
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            // Check if the password and confirm password match
            if (password !== confirmPassword) {
                alert('Passwords do not match. Please try again.');
                return;
            }

            // Check password strength
            const passwordStrength = checkPasswordStrength(password);
            if (!passwordStrength.isValid) {
                alert(passwordStrength.message);
                return;
            }

            // If all checks pass, submit the form data securely
            // For demonstration purposes, we'll just log the data
            // In a real-world scenario, use a secure method to send the data to the server
            console.log('Secure password submitted:', password);

            // Clear the form fields
            form.reset();
        });

        /**
         * Checks the strength of a password.
         *
         * @param {string} password The password to check.
         * @returns {Object} An object containing a boolean indicating whether the password is valid and a message.
         */
        function checkPasswordStrength(password) {
            // Define the password strength requirements
            const requirements = {
                minLength: 12,
                maxLength: 128,
                hasUppercase: true,
                hasLowercase: true,
                hasNumber: true,
                hasSpecialChar: true,
            };

            // Check the password length
            if (password.length < requirements.minLength || password.length > requirements.maxLength) {
                return { isValid: false, message: `Password must be between ${requirements.minLength} and ${requirements.maxLength} characters long.` };
            }

            // Check for uppercase letters
            if (requirements.hasUppercase && !/[A-Z]/.test(password)) {
                return { isValid: false, message: 'Password must contain at least one uppercase letter.' };
            }

            // Check for lowercase letters
            if (requirements.hasLowercase && !/[a-z]/.test(password)) {
                return { isValid: false, message: 'Password must contain at least one lowercase letter.' };
            }

            // Check for numbers
            if (requirements.hasNumber && !/\d/.test(password)) {
                return { isValid: false, message: 'Password must contain at least one number.' };
            }

            // Check for special characters
            if (requirements.hasSpecialChar && !/[^A-Za-z0-9]/.test(password)) {
                return { isValid: false, message: 'Password must contain at least one special character.' };
            }

            // If all checks pass, the password is valid
            return { isValid: true, message: '' };
        }
    </script>
</body>
</html>
```
