"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aniarticles.com
Prompt: Describe how to create a user registration form for Ani Articles using HTML and JavaScript, ensuring it meets their submission requirements.
Generated: DETERMINISTIC_3b1e97c88ae73e73
Batch ID: 20250612_164145
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
    <title>User Registration - Ani Articles</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .container {
            max-width: 500px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, button {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input:focus {
            border-color: #007BFF;
            outline: none;
        }

        button {
            background-color: #007BFF;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            border: none;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: #d9534f;
            font-size: 14px;
        }

        .success {
            color: #5cb85c;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>User Registration</h1>
        <form id="registrationForm">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <span class="error" id="usernameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <span class="error" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="8">
                <span class="error" id="passwordError"></span>
            </div>
            <button type="submit">Register</button>
            <div id="formMessage"></div>
        </form>
    </div>
    <script>
        // Access the form and its elements
        const form = document.getElementById('registrationForm');
        const usernameInput = document.getElementById('username');
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const usernameError = document.getElementById('usernameError');
        const emailError = document.getElementById('emailError');
        const passwordError = document.getElementById('passwordError');
        const formMessage = document.getElementById('formMessage');

        // Handle form submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Clear previous error messages
            usernameError.textContent = '';
            emailError.textContent = '';
            passwordError.textContent = '';
            formMessage.textContent = '';

            let isValid = true;

            // Validate username
            if (usernameInput.value.trim() === '') {
                isValid = false;
                usernameError.textContent = 'Username is required.';
            }

            // Validate email
            if (!emailInput.value.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
                isValid = false;
                emailError.textContent = 'Please enter a valid email address.';
            }

            // Validate password
            if (passwordInput.value.length < 8) {
                isValid = false;
                passwordError.textContent = 'Password must be at least 8 characters long.';
            }

            // If all validations pass, show success message
            if (isValid) {
                formMessage.textContent = 'Registration successful!';
                formMessage.className = 'success';

                // Optionally, send data to a server (example placeholder)
                // fetch('/register', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/json'
                //     },
                //     body: JSON.stringify({
                //         username: usernameInput.value,
                //         email: emailInput.value,
                //         password: passwordInput.value
                //     })
                // }).then(response => response.json())
                //   .then(data => console.log(data))
                //   .catch(error => console.error(error));
            } else {
                formMessage.textContent = 'Please fix the errors and try again.';
                formMessage.className = 'error';
            }
        });
    </script>
</body>
</html>
```
