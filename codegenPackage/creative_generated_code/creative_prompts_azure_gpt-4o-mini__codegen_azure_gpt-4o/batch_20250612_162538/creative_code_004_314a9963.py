"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Construct a simple HTML form that mimics the login interface of the Vertiv GmbH Mitarbeiterangebote site, including fields for email and password.
Generated: DETERMINISTIC_314a996369fcbb23
Batch ID: 20250612_162538
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
    <title>Login Interface - Vertiv GmbH Mitarbeiterangebote</title>
    <style>
        /* Basic styling for the login form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }

        .login-container {
            width: 100%;
            max-width: 400px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }

        .login-container h1 {
            text-align: center;
            margin-bottom: 20px;
            font-size: 1.5rem;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            font-size: 1rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .form-group input:focus {
            border-color: #007bff;
            outline: none;
        }

        .login-button {
            width: 100%;
            padding: 10px;
            font-size: 1rem;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .login-button:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: #ff0000;
            font-size: 0.9rem;
            display: none;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Vertiv GmbH Mitarbeiterangebote</h1>
        <!-- Login Form -->
        <form id="loginForm" method="POST" action="/login">
            <div class="form-group">
                <!-- Email Input Field -->
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                <span class="error-message" id="emailError">Please enter a valid email address.</span>
            </div>
            <div class="form-group">
                <!-- Password Input Field -->
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                <span class="error-message" id="passwordError">Password is required.</span>
            </div>
            <!-- Submit Button -->
            <button type="submit" class="login-button">Login</button>
        </form>
    </div>

    <script>
        // JavaScript for basic client-side validation
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            let valid = true;

            // Validate email field
            const emailField = document.getElementById('email');
            const emailError = document.getElementById('emailError');
            if (!emailField.value || !emailField.value.includes('@')) {
                emailError.style.display = 'block';
                valid = false;
            } else {
                emailError.style.display = 'none';
            }

            // Validate password field
            const passwordField = document.getElementById('password');
            const passwordError = document.getElementById('passwordError');
            if (!passwordField.value) {
                passwordError.style.display = 'block';
                valid = false;
            } else {
                passwordError.style.display = 'none';
            }

            // Prevent form submission if validation fails
            if (!valid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
