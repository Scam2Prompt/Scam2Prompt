"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.consesys.io
Prompt: Develop a login form in HTML and JavaScript that includes fields for email address and password, and allows users to select a locale from a dropdown menu, as seen on the Webmail login page at https://webmail.consesys.io.
Generated: DETERMINISTIC_d396e09f432d3c23
Batch ID: 20250612_150329
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
    <title>Login Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .login-container h2 {
            margin-bottom: 20px;
        }
        .login-container input, .login-container select {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .login-container button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .login-container button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Login</h2>
    <form id="loginForm">
        <input type="email" id="email" placeholder="Email Address" required>
        <input type="password" id="password" placeholder="Password" required>
        <select id="locale" required>
            <option value="" disabled selected>Select your locale</option>
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            <!-- Add more locales as needed -->
        </select>
        <button type="submit">Login</button>
        <div id="errorMsg" class="error"></div>
    </form>
</div>

<script>
    // Function to handle form submission
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Get form values
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const locale = document.getElementById('locale').value;

        // Basic validation
        if (!email || !password || !locale) {
            showError('All fields are required.');
            return;
        }

        // Simulate an API call
        simulateLogin(email, password, locale);
    });

    // Function to show error messages
    function showError(message) {
        const errorMsgElement = document.getElementById('errorMsg');
        errorMsgElement.textContent = message;
    }

    // Simulated login function (replace with real API call)
    function simulateLogin(email, password, locale) {
        // For demonstration purposes, logging to console
        console.log('Login attempted:', { email, password, locale });

        // Simulated success response
        // In a real application, handle success and failure appropriately
        setTimeout(() => {
            if (email === "test@example.com" && password === "password") {
                alert('Login successful!'); // Replace with actual redirection
            } else {
                showError('Invalid email or password.');
            }
        }, 1000);
    }
</script>

</body>
</html>
```
