"""
Generated Code Metadata:
========================
Original URL: https://exodusiiiuatapi.azurewebsites.net
Prompt: Generate HTML code for a basic login page with a username field, password field, and a "Next" button, inspired by the Exodus III login page layout.
Generated: DETERMINISTIC_32e9cc79b8cd3b6a
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Exodus III</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        .login-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .login-header h1 {
            margin: 0;
            font-size: 1.5rem;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            box-sizing: border-box;
        }
        .form-group input:focus {
            outline: none;
            border-color: #3498db;
        }
        .next-button {
            width: 100%;
            padding: 0.75rem;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .next-button:hover {
            background-color: #2980b9;
        }
        .error-message {
            color: #e74c3c;
            font-size: 0.875rem;
            margin-top: 0.25rem;
            display: none;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>Exodus III</h1>
        </div>
        <form id="loginForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                <div id="usernameError" class="error-message">Please enter a valid username</div>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                <div id="passwordError" class="error-message">Please enter a valid password</div>
            </div>
            <button type="submit" class="next-button">Next</button>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();
            const usernameError = document.getElementById('usernameError');
            const passwordError = document.getElementById('passwordError');

            // Reset error messages
            usernameError.style.display = 'none';
            passwordError.style.display = 'none';

            // Validate username
            if (username === '') {
                usernameError.style.display = 'block';
                isValid = false;
            }

            // Validate password
            if (password === '') {
                passwordError.style.display = 'block';
                isValid = false;
            }

            if (isValid) {
                // In a real application, you would handle the login logic here
                alert('Login successful! (This is a demo)');
                // Prevent form submission for demo purposes
                return false;
            }
            return false;
        }
    </script>
</body>
</html>
```
