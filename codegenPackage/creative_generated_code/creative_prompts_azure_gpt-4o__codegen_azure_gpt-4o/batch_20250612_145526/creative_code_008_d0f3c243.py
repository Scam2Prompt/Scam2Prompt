"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Generate code to implement a custom login form for Outlook that validates user input and ensures browser compatibility with cookies and scripts.
Generated: DETERMINISTIC_d0f3c2430d1a524f
Batch ID: 20250612_145526
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
    <title>Custom Outlook Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .login-container h2 {
            margin: 0 0 15px;
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-size: 14px;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }

        .form-group input:focus {
            border-color: #0078D4;
            outline: none;
        }

        .error {
            color: red;
            font-size: 12px;
            margin-top: 5px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #0078D4;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #005A9E;
        }
    </style>
    <script>
        // Check if cookies are enabled
        function areCookiesEnabled() {
            document.cookie = "test_cookie=1";
            const cookiesEnabled = document.cookie.indexOf("test_cookie=") !== -1;
            if (cookiesEnabled) {
                // Delete the test cookie
                document.cookie = "test_cookie=; max-age=0";
            }
            return cookiesEnabled;
        }

        // Validate email format
        function isValidEmail(email) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }

        // Validate form input and display any errors
        function validateForm(event) {
            event.preventDefault();

            const emailInput = document.getElementById('email');
            const passwordInput = document.getElementById('password');
            const emailError = document.getElementById('emailError');
            const passwordError = document.getElementById('passwordError');
            const cookieError = document.getElementById('cookieError');

            let isValid = true;

            // Clear previous errors
            emailError.textContent = '';
            passwordError.textContent = '';
            cookieError.textContent = '';

            // Validate email
            if (!isValidEmail(emailInput.value)) {
                emailError.textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate password
            if (passwordInput.value.trim().length < 6) {
                passwordError.textContent = 'Password must be at least 6 characters.';
                isValid = false;
            }

            // Check cookies
            if (!areCookiesEnabled()) {
                cookieError.textContent = 'Cookies are required to log in. Please enable cookies in your browser.';
                isValid = false;
            }

            // Submit form if valid
            if (isValid) {
                alert('Form submitted successfully!');
                // In production, you would send the data to the server here
            }
        }

        // Ensure JavaScript is enabled
        function checkJavaScriptEnabled() {
            document.getElementById('jsError').style.display = 'none';
        }
    </script>
</head>
<body onload="checkJavaScriptEnabled()">
    <div class="login-container">
        <h2>Outlook Login</h2>
        <noscript>
            <p id="jsError" style="color: red; text-align: center;">JavaScript is required to use this form. Please enable JavaScript in your browser.</p>
        </noscript>
        <form onsubmit="validateForm(event)">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="text" id="email" name="email" placeholder="Enter your email" required>
                <div class="error" id="emailError"></div>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                <div class="error" id="passwordError"></div>
            </div>
            <div class="error" id="cookieError"></div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
```
