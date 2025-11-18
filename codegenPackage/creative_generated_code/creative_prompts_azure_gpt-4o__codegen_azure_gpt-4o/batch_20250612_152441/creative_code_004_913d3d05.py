"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.dexodoor.com
Prompt: Provide code to create a custom login form for cPanel, including fields for username, password, and locale selection.
Generated: DETERMINISTIC_913d3d054ebb132c
Batch ID: 20250612_152441
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
    <title>Custom cPanel Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        .login-form h2 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        .form-group input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }

        .form-group input[type="submit"]:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: #ff0000;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <form class="login-form" id="cPanelLoginForm" action="/login" method="POST">
        <!-- Form title -->
        <h2>cPanel Login</h2>

        <!-- Username field -->
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <div class="error-message" id="usernameError"></div>
        </div>

        <!-- Password field -->
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <div class="error-message" id="passwordError"></div>
        </div>

        <!-- Locale selection -->
        <div class="form-group">
            <label for="locale">Locale:</label>
            <select id="locale" name="locale" required>
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <!-- Add more locales as needed -->
            </select>
        </div>

        <!-- Submit button -->
        <div class="form-group">
            <input type="submit" value="Login">
        </div>
    </form>

    <script>
        // JavaScript for client-side validation
        document.getElementById('cPanelLoginForm').addEventListener('submit', function(event) {
            // Reset error messages
            document.getElementById('usernameError').textContent = '';
            document.getElementById('passwordError').textContent = '';

            let isValid = true;

            // Validate username field
            const username = document.getElementById('username').value.trim();
            if (!username) {
                document.getElementById('usernameError').textContent = 'Username is required.';
                isValid = false;
            }

            // Validate password field
            const password = document.getElementById('password').value.trim();
            if (!password) {
                document.getElementById('passwordError').textContent = 'Password is required.';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
