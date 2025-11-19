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
    <title>Login Page</title>
    <style>
        /* Basic styling for the login page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        .login-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        .login-container h1 {
            font-size: 24px;
            margin-bottom: 20px;
            text-align: center;
            color: #333333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            font-size: 14px;
            margin-bottom: 5px;
            color: #555555;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .form-group input:focus {
            border-color: #007bff;
            outline: none;
        }

        .next-button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .next-button:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: red;
            font-size: 12px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form id="loginForm">
            <!-- Username field -->
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
                <div class="error-message" id="usernameError"></div>
            </div>

            <!-- Password field -->
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
                <div class="error-message" id="passwordError"></div>
            </div>

            <!-- Next button -->
            <button type="submit" class="next-button">Next</button>
        </form>
    </div>

    <script>
        // JavaScript for form validation
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission

            // Clear previous error messages
            document.getElementById('usernameError').textContent = '';
            document.getElementById('passwordError').textContent = '';

            // Get form values
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();

            let isValid = true;

            // Validate username
            if (username === '') {
                document.getElementById('usernameError').textContent = 'Username is required.';
                isValid = false;
            }

            // Validate password
            if (password === '') {
                document.getElementById('passwordError').textContent = 'Password is required.';
                isValid = false;
            }

            // If valid, proceed (e.g., send data to server)
            if (isValid) {
                alert('Form submitted successfully!');
                // Add logic to handle form submission (e.g., API call)
            }
        });
    </script>
</body>
</html>
```
