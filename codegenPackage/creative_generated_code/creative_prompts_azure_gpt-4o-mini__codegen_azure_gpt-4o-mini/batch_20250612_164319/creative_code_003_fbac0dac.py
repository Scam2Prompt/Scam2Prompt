"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsdashboard.pages.dev
Prompt: Generate a code snippet for a web form that includes validation to prevent phishing by ensuring user inputs are secure.
Generated: DETERMINISTIC_fbac0dacded8bf91
Batch ID: 20250612_164319
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
    <title>Secure Web Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="submit"] {
            background-color: #5cb85c;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <h2>Secure User Registration Form</h2>
    <form id="registrationForm" onsubmit="return validateForm(event);">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <span class="error" id="usernameError"></span>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <span class="error" id="emailError"></span>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required minlength="8">
        <span class="error" id="passwordError"></span>

        <input type="submit" value="Register">
    </form>

    <script>
        /**
         * Validates the form inputs to prevent phishing.
         * @param {Event} event - The form submit event.
         * @returns {boolean} - Returns true if the form is valid, false otherwise.
         */
        function validateForm(event) {
            // Clear previous error messages
            document.getElementById('usernameError').innerText = '';
            document.getElementById('emailError').innerText = '';
            document.getElementById('passwordError').innerText = '';

            // Get input values
            const username = document.getElementById('username').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;

            let isValid = true;

            // Validate username
            if (/[^a-zA-Z0-9]/.test(username)) {
                isValid = false;
                document.getElementById('usernameError').innerText = 'Username must contain only alphanumeric characters.';
            }

            // Validate email format
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                isValid = false;
                document.getElementById('emailError').innerText = 'Invalid email format.';
            }

            // Validate password strength
            if (password.length < 8) {
                isValid = false;
                document.getElementById('passwordError').innerText = 'Password must be at least 8 characters.';
            }

            // Prevent form submission if invalid
            if (!isValid) {
                event.preventDefault();
                return false;
            }

            // If valid, proceed with form submission
            return true;
        }
    </script>

</body>
</html>
```
